from pprint import pprint
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

response = llm.invoke("What is the meaning of life for a french person who like cheese and wine? How can AI help "
                      "achieve it?")

pprint(response.content)
