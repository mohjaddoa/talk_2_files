from langchain.document_loaders import PyPDFLoader
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

import os
os.environ["OPENAI_API_KEY"] = "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"
pdf_loader = PyPDFLoader('/Users/mohammedjaddoa/Desktop/Assessment2.pdf')
documents = pdf_loader.load()
# print(documents)
# this function combin text with promote 
chain = load_qa_chain(llm=ChatOpenAI(temperature=0,model_name='gpt-4-0613'),verbose=True)
# chain = load_qa_chain(llm=OpenAI(temperature=0.6,model_name='gpt-4-0613'),verbose=True)

query = 'how many marks for this assessment'
response = chain.run(input_documents=documents, question=query)
print(response) 






##### This example about using OPENAI with chainlit
# import openai
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from dotenv import load_dotenv
# from langchain_community.chat_models import ChatOpenAI
# import chainlit as cl
# import os

# load_dotenv()
# template = """Question: {question}

# Answer: Let's think step by step."""


# @cl.on_chat_start
# def main():
#     prompt = PromptTemplate(template=template, input_variables = ["question"])
#     llm_chain = LLMChain(prompt = prompt,llm=ChatOpenAI(temperature=0.6,model_name='gpt-4-0613'),verbose=True)
#     cl.user_session.set("llm_chain",llm_chain)

# @cl.on_message
# async def main(message : str):
#     llm_chain = cl.user_session.get("llm_chain")

#     res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])

#     await cl.Message(content=res["text"]).send()






