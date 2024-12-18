from nltk.tokenize import sent_tokenize

def preprocess_articles(articles):
    """
    Preprocesses a list of articles by splitting them into chunks, 
    adjusting their sizes, and expanding their context.
    
    Args:
        articles (list of dict): Each article should have a "text" key with its content.
    
    Returns:
        list of dict: List of chunk dictionaries with added context.
    """
    # Split articles into raw chunks (sentences in this case)
    raw_chunks = [sent for article in articles for sent in sent_tokenize(article["text"])]

    # Adjust the chunks to meet size constraints
    adjusted_chunks = adjust_chunks(raw_chunks, min_size=200, max_size=600)

    # Add context to each chunk
    expanded_chunks = add_context(adjusted_chunks, window=1)
    
    return expanded_chunks


def adjust_chunks(chunks, min_size=200, max_size=600):
    """
    Adjusts the sizes of text chunks by merging smaller ones and splitting larger ones.
    
    Args:
        chunks (list of str): List of text chunks.
        min_size (int): Minimum size (in characters) of a chunk.
        max_size (int): Maximum size (in characters) of a chunk.
    
    Returns:
        list of str: List of adjusted text chunks.
    """
    adjusted_chunks = []
    buffer = ""

    for chunk in chunks:
        if len(chunk) < min_size:
            # Accumulate smaller chunks into a buffer
            buffer += " " + chunk
        elif len(chunk) > max_size:
            # Split large chunks at sentence boundaries
            sentences = sent_tokenize(chunk)
            temp_chunk = ""
            for sentence in sentences:
                if len(temp_chunk) + len(sentence) > max_size:
                    adjusted_chunks.append(temp_chunk.strip())
                    temp_chunk = ""
                temp_chunk += " " + sentence
            if temp_chunk:
                adjusted_chunks.append(temp_chunk.strip())
        else:
            # Add buffer (if any) and current chunk to the final list
            if buffer:
                adjusted_chunks.append(buffer.strip())
                buffer = ""
            adjusted_chunks.append(chunk)

    # Add any leftover buffer
    if buffer:
        adjusted_chunks.append(buffer.strip())

    return adjusted_chunks


def add_context(chunks, window=1):
    """
    Adds context to each chunk by including surrounding chunks as metadata.
    
    Args:
        chunks (list of str): List of adjusted text chunks.
        window (int): Number of chunks before and after to include as context.
    
    Returns:
        list of dict: Each dictionary contains a "chunk" and its "context".
    """
    expanded_chunks = []
    for i, chunk in enumerate(chunks):
        # Get context before and after the current chunk
        context_before = " ".join(chunks[max(0, i - window):i])
        context_after = " ".join(chunks[i + 1:i + 1 + window])
        
        expanded_chunks.append({
            "chunk": chunk,
            "context": f"Before: {context_before}\nAfter: {context_after}"
        })
    
    return expanded_chunks
