import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector


pdf_file_name = "aidants_familiaux.pdf"
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_file_path = os.path.join(script_dir, pdf_file_name)

loader = PyPDFLoader(file_path=pdf_file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

connection = "postgresql+psycopg://myuser:mypassword@localhost:5432/mydb"
collection_name = "my_docs"
embeddings = OpenAIEmbeddings()

vectorstore = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)

vectorstore.create_collection()

i = 0
for doc in splits:
    doc.metadata = {"id": i}
    doc.page_content = doc.page_content.replace('\x00', '')
    i += 1

vectorstore.add_documents(splits, ids=[doc.metadata['id'] for doc in splits])
