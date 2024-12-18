from chunking import preprocess_articles
from retrieval import retrieve_top_chunks
from prompt_builder import construct_prompt
from ollama_client import query_ollama

# Load example data
import json
with open("../data/example_articles.json", "r") as f:
    articles = json.load(f)

# Query
query = "What are the key benefits of using Ollama?"

# Preprocess articles
chunks = preprocess_articles(articles)

# Retrieve top chunks
top_chunks = retrieve_top_chunks(chunks, query)

# Build prompt
prompt = construct_prompt(top_chunks, query)

# Query Ollama
response = query_ollama("your_model_name", prompt)
print("Ollama's Response:", response)
