from langchain.document_loaders import YoutubeLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()


def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    """
    load the youtube and convert them to transcripts
    this transcript will be converted into chunks of tokens and converted to embeddings
    this embeddings will be stored in vectorstore
    :param video_url:
    :return:
    """
    # Load youtube video from url
    loader = YoutubeLoader.from_youtube_url(video_url)

    # Transcribe the youtube
    transcript = loader.load()

    # Text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    embeddings = OpenAIEmbeddings()

    # Save the splitted text
    docs = text_splitter.split_documents(transcript)

    # Create db
    db = FAISS.from_documents(docs, embeddings)

    return db


# k = 4 documents . 1 document = 1000 token/chunks
def get_response_from_query(db, query, k=4):
    # text-davinci can handle 4097 tokens. 1 token is 4 characters.

    # Perform similarity search from db to specific documents only
    docs = db.similarity_search(query, k=k)

    # Join the documents
    docs_page_content = " ".join([d.page_content for d in docs])

    # build model
    llm = OpenAI(model="text-davinci-003")

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
           you are a helpful youtube assistant that can answer questions about videos based on the video's transcript

           Answer the following question: {question}
           By searching the following video transcript: {docs}

           Only use the factual information from the transcript to answer the question


           If you feel like you don't have enough information to answer the question, say "I dont know"

           Your answer should be detailed. 
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(question=query, docs=docs_page_content)

    response = response.replace("\n", "")
    return response, docs