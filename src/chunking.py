from nltk.tokenize import sent_tokenize

def preprocess_articles(articles):
    raw_chunks = [article["text"] for article in articles]
    adjusted_chunks = adjust_chunks(raw_chunks)
    expanded_chunks = add_context(adjusted_chunks, window=1)
    return expanded_chunks

def adjust_chunks(chunks, min_size=200, max_size=600):
    # Logic as discussed earlier
    ...

def add_context(chunks, window=1):
    # Logic as discussed earlier
    ...
