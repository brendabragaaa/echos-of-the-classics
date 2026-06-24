from pathlib import Path
import json
from typing import List, Dict, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import argparse

"""
embed_documents.py

Script para carregar arquivos de texto, fragmentá-los, gerar embeddings e salvar um índice FAISS.
Use como base e adapte conforme os outros arquivos do seu projeto.
"""


# Dependências: sentence-transformers, faiss-cpu
# pip install sentence-transformers faiss-cpu

try:
except Exception as e:
    raise ImportError("Instale 'sentence-transformers' (pip install sentence-transformers)") from e

try:
except Exception as e:
    raise ImportError("Instale 'faiss-cpu' (pip install faiss-cpu)") from e


def load_text_files(folder: Path, extensions: Tuple[str, ...] = (".txt", ".md")) -> List[Dict]:
    """Carrega todos os arquivos de texto do diretório e retorna lista de dicts {'text','source'}."""
    docs = []
    for p in folder.rglob("*"):
        if p.is_file() and p.suffix.lower() in extensions:
            text = p.read_text(encoding="utf-8", errors="ignore")
            if text.strip():
                docs.append({"text": text, "source": str(p)})
    return docs


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """Fragmenta um texto em pedaços de tamanho aproximado chunk_size com sobreposição overlap."""
    if chunk_size <= 0:
        return [text]
    pieces = []
    start = 0
    length = len(text)
    while start < length:
        end = start + chunk_size
        piece = text[start:end]
        pieces.append(piece)
        start = max(end - overlap, end) if overlap < chunk_size else end
    return pieces


def prepare_documents(docs: List[Dict], chunk_size: int = 1000, overlap: int = 200) -> List[Dict]:
    """Converte documentos brutos em chunks com metadados."""
    prepared = []
    for doc in docs:
        chunks = chunk_text(doc["text"], chunk_size=chunk_size, overlap=overlap)
        for i, c in enumerate(chunks):
            prepared.append({
                "text": c,
                "source": doc["source"],
                "chunk_id": i
            })
    return prepared


def embed_texts(texts: List[str], model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> np.ndarray:
    """Gera embeddings usando SentenceTransformer. Retorna matriz (n, dim)."""
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)
    return embeddings.astype("float32")


def build_faiss_index(embeddings: np.ndarray) -> faiss.Index:
    """Cria um índice FAISS simples (IndexFlatL2) a partir dos embeddings."""
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def save_index_and_metadata(index: faiss.Index, metadata: List[Dict], out_dir: Path, index_name: str = "faiss_index"):
    """Salva o índice FAISS (.idx) e os metadados (.json) no diretório out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    index_path = out_dir / f"{index_name}.idx"
    faiss.write_index(index, str(index_path))
    meta_path = out_dir / f"{index_name}.meta.json"
    with meta_path.open("w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    return index_path, meta_path


def pipeline(input_folder: str, out_folder: str, chunk_size: int = 1000, overlap: int = 200, model_name: str = None):
    """Executa pipeline completa: leitura, chunk, embed, index, salvar."""
    folder = Path(input_folder)
    out = Path(out_folder)
    docs = load_text_files(folder)
    prepared = prepare_documents(docs, chunk_size=chunk_size, overlap=overlap)
    texts = [p["text"] for p in prepared]
    if not texts:
        raise SystemExit("Nenhum documento encontrado para processar.")
    embeddings = embed_texts(texts, model_name=model_name or "sentence-transformers/all-MiniLM-L6-v2")
    index = build_faiss_index(embeddings)
    save_index_and_metadata(index, prepared, out)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Criar embeddings e índice FAISS a partir de documentos de texto.")
    parser.add_argument("--input", "-i", required=True, help="Pasta com arquivos de texto")
    parser.add_argument("--output", "-o", required=True, help="Pasta para salvar índice e metadados")
    parser.add_argument("--chunk_size", type=int, default=1000)
    parser.add_argument("--overlap", type=int, default=200)
    parser.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    args = parser.parse_args()

    pipeline(args.input, args.output, chunk_size=args.chunk_size, overlap=args.overlap, model_name=args.model)