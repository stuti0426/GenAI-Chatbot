# LANGCHAIN_API_KEY="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"
# LANGCHAIN_PROJECT="default"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# ##Environment variables call
# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

##Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"

##Creating chatbot
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please provide response to the user queries"),
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title("Language Demo With LLama2 API")
input_text=st.text_input("Search the topic you want")

#Open AI LLM call
llm=Ollama(model="llama2")
output_parser=StrOutputParser()

##Chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))