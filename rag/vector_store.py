import os
import chromadb
from chromadb.utils import embedding_functions

# Diretório onde o banco de dados será persistido localmente
DB_PATH = "./database"
COLLECTION_NAME = "echoes_literarios"

# Inicializa o cliente persistente do ChromaDB
client = chromadb.PersistentClient(path=DB_PATH)

# Define a função de embedding usando um modelo leve e 100% local
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def get_collection():
    """Obtém ou cria a coleção para armazenar os vetores literários."""
    print(f"[LOG INFO] Conectando ao banco de dados ChromaDB em '{DB_PATH}'...")
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )