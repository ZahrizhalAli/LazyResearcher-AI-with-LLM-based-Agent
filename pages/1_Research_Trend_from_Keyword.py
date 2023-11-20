import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def generate_research_trend(keyword):
    llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo", max_tokens=30)

    # Add prompt template
    prompt_template = PromptTemplate(
        input_variables=['keyword'],
        template="Given the keyword {keyword}, find a list of relevant research trend topic. always place the most significant one in a descendant order."
    )


    name_chain = LLMChain(llm=llm, prompt=prompt_template,
                          output_key='get_trend')

    response = name_chain({'keyword': keyword})
    return response

st.title("📝 Research Trend using Keyword")

topic = st.text_input('Input Keyword')
trend_button = st.button("Research Trend Recently.")
if trend_button and topic:
    result = generate_research_trend(topic)
    st.text(result['get_trend'])
