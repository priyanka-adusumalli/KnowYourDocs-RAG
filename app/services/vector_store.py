import faiss
import os
import numpy as np
from app.services.loader import load_text
from app.services.chunker import chunk_text
from app.services.embedder import embed

INDEX_PATH = "data/faiss_index/index.bin"
META_PATH = "data/faiss_index/meta.npy"

os.makedirs("data/faiss_index", exist_ok=True)

if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
    metadata = list(np.load(META_PATH, allow_pickle=True))
else:
    index = faiss.IndexFlatL2(384)
    metadata = []

def process_document(file_path: str):
    text = load_text(file_path)
    chunks = chunk_text(text)
    vectors = embed(chunks)

    index.add(np.array(vectors).astype("float32"))
    metadata.extend(chunks)

    faiss.write_index(index, INDEX_PATH)
    np.save(META_PATH, np.array(metadata, dtype=object))

def search(query: str, top_k: int):
    vector = embed([query])
    _, indices = index.search(
        np.array(vector).astype("float32"),
        top_k
    )
    return [metadata[i] for i in indices[0]]
