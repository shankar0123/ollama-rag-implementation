import requests

def query_ollama(model_name, prompt):
    url = f"http://localhost:11434/api/models/{model_name}/generate"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": prompt}
    response = requests.post(url, json=data, headers=headers)
    return response.json()["response"]
