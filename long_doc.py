from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"

documents = []
for file in os.listdir('docs'):
    if file.endswith('.pdf'):
        pdf_path = 'docs/' + file
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())
    elif file.endswith('.docx') or file.endswith('.doc'):
        doc_path = 'docs/' + file
        loader = Docx2txtLoader(doc_path)
        documents.extend(loader.load())
    elif file.endswith('.txt'):
        text_path = 'docs/' + file
        loader = TextLoader(text_path)
        documents.extend(loader.load())



### loading pdf
# loader = PyPDFLoader('/Users/mohammedjaddoa/Desktop/Assessment2.pdf')
# doc = loader.load()
# print(doc)
text_spliter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
text_doc = text_spliter.split_documents(documents)
# print(text_doc)

vectors = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(), persist_directory="documents")


vectors.persist()

chaining = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0,model_name='gpt-4-0613'),
    retriever=vectors.as_retriever(search_kwargs={'k': 7}),
    return_source_documents=True
)
result = chaining({'query': 'please write marking ruburic ?'})
print(result['result'])