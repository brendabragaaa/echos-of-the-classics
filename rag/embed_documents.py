import os
from rag.vector_store import get_collection

def carregar_e_fatiar_texto(caminho_arquivo, tamanho_chunk=500, overlap=100):
    """Lê o arquivo de texto e quebra em pedaços (palavras) com sobreposição."""
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        texto = f.read()
        
    palavras = texto.split()
    chunks = []
    
    # Cria os blocos deslizando o índice para manter o contexto entre as quebras
    for i in range(0, len(palavras), tamanho_chunk - overlap):
        chunk = " ".join(palavras[i:i + tamanho_chunk])
        if chunk.strip():
            chunks.append(chunk)
        
    return chunks

def indexar_base_conhecimento():
    base_dir = "./Knowledge_base"
    colecao = get_collection()
    
    if not os.path.exists(base_dir):
        print(f"[ERRO] A pasta {base_dir} não existe. Certifique-se de criá-la.")
        return

    print("[LOG INFO] Iniciando o processamento e geração de embeddings...")
    id_contador = 0
    
    # Varre as pastas de cada autor dentro de Knowledge_base/
    for autor in os.listdir(base_dir):
        autor_path = os.path.join(base_dir, autor)
        if os.path.isdir(autor_path):
            for arquivo_txt in os.listdir(autor_path):
                if arquivo_txt.endswith(".txt"):
                    caminho_completo = os.path.join(autor_path, arquivo_txt)
                    print(f"[LOG INFO] Processando: {autor} -> {arquivo_txt}")
                    
                    chunks = carregar_e_fatiar_texto(caminho_completo)
                    
                    documents = []
                    metadatas = []
                    ids = []
                    
                    for chunk in chunks:
                        documents.append(chunk)
                        metadatas.append({"autor": autor.lower(), "fonte": arquivo_txt})
                        ids.append(f"doc_{autor}_{id_contador}")
                        id_contador += 1
                    
                    # Salva o lote no banco vetorial
                    if documents:
                        colecao.add(documents=documents, metadatas=metadatas, ids=ids)

    print(f"[LOG INFO] Sucesso! {id_contador} fragmentos literários foram indexados no ChromaDB.")

if __name__ == "__main__":
    indexar_base_conhecimento()