<<<<<<< HEAD
# ollama-rag-implementation
rag from scratch
=======
# Ollama Integration with Retrieval-Augmented Generation (RAG)

This project integrates advanced document retrieval and generation techniques to build a **Retrieval-Augmented Generation (RAG)** pipeline. It demonstrates how to use **RankBM25**, **SentenceTransformers**, and **Ollama** to process a collection of documents, identify relevant chunks, and generate context-aware answers to user queries.

---

## **What is Retrieval-Augmented Generation (RAG)?**

RAG combines traditional search techniques with language model generation:

1. **Retrieve**: Search for relevant document chunks using BM25 and cosine similarity.
2. **Generate**: Use a language model to generate a response based on the retrieved chunks.

This approach ensures:
- Accurate, **grounded responses** tied to the input documents.
- The ability to handle **domain-specific** or **dynamic datasets** effectively.

---

## **Libraries Used**
This project uses the following Python libraries:
- **`rank-bm25`**: For BM25 lexical search.
- **`sentence-transformers`**: For semantic similarity using embeddings.
- **`torch`**: Backend for efficient tensor computations.
- **`requests`**: To query the Ollama API.

---

## **How It Works**

### **1. Document Chunking**
The pipeline splits large articles into smaller chunks for better retrieval. Each chunk represents a semantically coherent part of the document, such as a sentence or paragraph.

### **2. Retrieval**
The system uses two retrieval methods:
- **Lexical Search**: BM25 identifies chunks with high overlap with the query.
- **Semantic Search**: Cosine similarity ranks chunks based on their meaning.

The scores from both methods are combined using **Reciprocal Rank Fusion**.

### **3. Querying the Language Model**
The top-ranked chunks are formatted into a prompt and sent to **Ollama**, which generates a response.

---

## **Example Workflow**

### **Dataset**
Suppose you have the following articles about Bitcoin:

```json
[
  {"text": "Bitcoin is a decentralized digital currency invented in 2008."},
  {"text": "Satoshi Nakamoto is the pseudonym used by the unknown person or group who created Bitcoin."},
  {"text": "Bitcoin uses blockchain technology for secure transactions."}
]
```

### **Query**
> Who is Satoshi Nakamoto?

### **Steps**
1. **Chunking**: The articles are split into smaller chunks:
   - Chunk 1: "Bitcoin is a decentralized digital currency invented in 2008."
   - Chunk 2: "Satoshi Nakamoto is the pseudonym used by the unknown person or group who created Bitcoin."
   - Chunk 3: "Bitcoin uses blockchain technology for secure transactions."

2. **Retrieval**:
   - **BM25** ranks chunks lexically:
     - Chunk 2: Highest rank (mentions "Satoshi Nakamoto").
   - **Cosine similarity** ranks chunks semantically:
     - Chunk 2: Highest score (discusses Satoshi Nakamoto conceptually).
   - **Final Ranking**: Scores from BM25 and cosine similarity are fused for the final ranking.

3. **Prompt Construction**:
   ```plaintext
   Context 1: Bitcoin is a decentralized digital currency invented in 2008.
   Context 2: Satoshi Nakamoto is the pseudonym used by the unknown person or group who created Bitcoin.
   Context 3: Bitcoin uses blockchain technology for secure transactions.

   Query: Who is Satoshi Nakamoto?
   Answer:
   ```

4. **Language Model Response**:
   - Ollama generates the answer: "Satoshi Nakamoto is the pseudonym of the person or group who invented Bitcoin in 2008."

---

## **Installation**

### **Requirements**
- Python 3.9+
- Libraries in `requirements.txt`

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ollama-integration.git
   cd ollama-integration
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

### **Prepare Your Data**
Add your articles as JSON objects in the `data/example_articles.json` file.

### **Run the Script**
Execute the main script:
```bash
python src/main.py
```

### **Modify the Query**
Change the `query` variable in `src/main.py` to your desired query:
```python
query = "Who is Satoshi Nakamoto?"
```

---

## **Technical Details**

### **1. Chunking**
Documents are tokenized into smaller chunks (e.g., sentences) for better semantic coherence.

### **2. BM25 Retrieval**
The `RankBM25` library ranks chunks based on keyword overlap with the query.

### **3. Semantic Similarity**
`SentenceTransformers` computes cosine similarity between the query and chunk embeddings.

### **4. Reciprocal Rank Fusion**
Scores are combined as:
```python
final_score = 0.4 * bm25_score + 0.6 * cosine_score
```

### **5. Ollama Integration**
The top-ranked chunks are passed to Ollama for answer generation.

---

## **API Integration**

### **Ollama Setup**
- Ensure the Ollama server is running locally at `localhost:11434`.
- Update the model name in `src/ollama_client.py` if necessary.

---

## **Contributing**
We welcome contributions! Feel free to open an issue or submit a pull request.

---

## **License**
This project is licensed under the MIT License.
>>>>>>> 5e63d90 (First commit)
