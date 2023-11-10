# import os
# import re
# from typing import List
# from langchain.chains import LLMChain
# from langchain.retrievers import WebResearchRetriever
# from langchain.schema import AgentAction, OutputParserException, AgentFinish
# from langchain.utilities.serpapi import SerpAPIWrapper
# from pydantic import BaseModel, Field
# from langchain.prompts import PromptTemplate
# from langchain.output_parsers.pydantic import PydanticOutputParser
# from langchain.chat_models import ChatOpenAI
# from dotenv import load_dotenv
# from langchain.utilities import GoogleSerperAPIWrapper
# from langchain.utilities import GoogleSerperAPIWrapper
# from langchain.llms.openai import OpenAI
# from langchain.agents import initialize_agent, Tool, LLMSingleActionAgent, AgentOutputParser, AgentExecutor
# from langchain.agents import AgentType
# from typing import List, Union
# import os
# from langchain.vectorstores import Chroma
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.chat_models.openai import ChatOpenAI
# from langchain.utilities import GoogleSearchAPIWrapper
#
#
# os.environ["SERPER_API_KEY"] = "75a942c11f85b7704d82228936586548460c8a54"
# os.environ["OPENAI_API_KEY"] = "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"
#
#
# search = GoogleSerperAPIWrapper()
# tools = [
#     Tool(
#         name="Intermediate Answer",
#         func=search.run,
#         description="useful for when you need to ask with search"
#     )
# ]
#
# # Vectorstore
# vectorstore = Chroma(
#     embedding_function=OpenAIEmbeddings(), persist_directory="./chroma_db_oai"
# )
#
# # LLM
#
# llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
#
# # Initialize
# web_research_retriever = WebResearchRetriever.from_llm(
#     vectorstore=vectorstore,
#     llm=llm,
#     search=search,
# )
#
#
# #
# # # Set up a prompt template
# # class CustomOutputParser(AgentOutputParser):
# #
# #     def parse(self, llm_output: str) -> Union[AgentAction, AgentFinish]:
# #         # Check if agent should finish
# #         if "Final Answer:" in llm_output:
# #             return AgentFinish(
# #                 # Return values is generally always a dictionary with a single `output` key
# #                 # It is not recommended to try anything else at the moment :)
# #                 return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
# #                 log=llm_output,
# #             )
# #         # Parse out the action and action input
# #         regex = r"Action\s*\d*\s*:(.*?)\nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
# #         match = re.search(regex, llm_output, re.DOTALL)
# #         if not match:
# #             raise OutputParserException(f"Could not parse LLM output: `{llm_output}`")
# #         action = match.group(1).strip()
# #         action_input = match.group(2)
# #         # Return the action and action input
# #         return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)
# #
# # # LLMChain
# # search_prompt = PromptTemplate(
# #     input_variables=["question"],
# #     template="""You are an assistant tasked with improving Google search
# #     results. Generate FIVE Google search queries that are similar to
# #     this question. The output should be a numbered list of questions and each
# #     should have a question mark at the end: {question}""",
# # )
# #
# #
# # class LineList(BaseModel):
# #     """List of questions."""
# #
# #     lines: List[str] = Field(description="Questions")
# #
# #
# # class QuestionListOutputParser(PydanticOutputParser):
# #     """Output parser for a list of numbered questions."""
# #
# #     def __init__(self) -> None:
# #         super().__init__(pydantic_object=LineList)
# #
# #     def parse(self, text: str) -> LineList:
# #         lines = re.findall(r"\d+\..*?\n", text)
# #         return LineList(lines=lines)
# #
# # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
# #
# # llm_chain = LLMChain(
# #     llm=llm,
# #     prompt=search_prompt,
# #     output_parser=QuestionListOutputParser(),
# # )
# # output_parser = CustomOutputParser()
# #
# # agent = LLMSingleActionAgent(
# #     llm_chain=llm_chain,
# #     output_parser=output_parser,
# #     stop=["\nObservation:"],
# # )
# #
# # agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
# # agent_executor.run("How many people live in canada as of 2023?")
import requests


print(requests.post(
    'http://127.0.0.1:8000/',
    json= {'query':"Who is Zahrizhal Ali?"}
    ).json()
)