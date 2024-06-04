# Introduction
In this starter you will find the basic elements to build a genai application.

Langchain is the most used framework to build GenAI application
Unstructured is a lib to get the data from various sources

An embedding is a way to represent a text in a vector space. It is a way to represent the meaning of a text.
A similarity search is a way to find the most similar text to a given text. (Fruit is similar to apple, banana, etc.)

## Installation
The project use poetry and pyenv to manage the dependencies and the python version.

Install with `poetry install` and activate the virtual environment with `poetry shell`

Export the openai api key with `export OPENAI_API_KEY=your_api_key`

Test it with : `python src/1_call_model.py`

## Semantic search - RAG

### Read data from files, create embeddings, Store them in postgresql

Test it with : `python src/2_create_vector_store.py`

### Make a similarity search with them

Test it with : `python src/3_search.py`

## GENAI TOOL - Function calling

### Create a tool - define a function

### Use a tool with OpenAI - send your function definition to openai

### Call the function with the answer of OpenAI

