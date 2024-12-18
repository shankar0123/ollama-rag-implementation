from pyserini.search import SimpleSearcher
from sentence_transformers import SentenceTransformer, util
import numpy as np

def retrieve_top_chunks(chunks, query):
    searcher = SimpleSearcher("path_to_index")
    bm25_results = searcher.search(query, k=20)
    bm25_scores = np.array([result.score for result in bm25_results])

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode(query)
    chunk_embeddings = model.encode([chunk['chunk'] for chunk in chunks])
    cosine_scores = util.pytorch_cos_sim(query_embedding, chunk_embeddings).squeeze().numpy()

    final_scores = reciprocal_rank_fusion(bm25_scores, cosine_scores)
    top_indices = np.argsort(final_scores)[::-1][:7]
    return [chunks[i] for i in top_indices]

def reciprocal_rank_fusion(bm25_scores, cosine_scores, bm25_weight=0.4, cosine_weight=0.6):
    # Logic as discussed earlier
    ...
