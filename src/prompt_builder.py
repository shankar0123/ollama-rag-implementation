def construct_prompt(chunks, query):
    prompt = "You are an expert assistant. Answer the following query using the provided context.\n"
    for i, chunk in enumerate(chunks):
        prompt += f"Context {i+1}: {chunk['chunk']}\n"
    prompt += f"\nQuery: {query}\nAnswer:"
    return prompt
