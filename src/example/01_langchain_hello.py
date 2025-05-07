import json
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph
from typing import TypedDict
from langchain_openai import ChatOpenAI
from src.utils import get_config


# 定义状态和链
class State(TypedDict):
    history: str
    response: str

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{history}\nUser: {input}")
])


api_key, base_url, model = get_config()
llm = ChatOpenAI(
            openai_api_key=api_key,
            openai_api_base=base_url,
            model_name=model
)

chain = LLMChain(llm=llm, prompt=prompt)

res = chain.invoke({"history": "", "input": "Hi!"})
print(res)
