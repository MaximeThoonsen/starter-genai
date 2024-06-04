from pprint import pprint

from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector

connection = "postgresql+psycopg://myuser:mypassword@localhost:5432/mydb"
collection_name = "my_docs"
embeddings = OpenAIEmbeddings()

vectorstore = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)

docs = vectorstore.similarity_search('habits', k=2)
pprint(docs)
