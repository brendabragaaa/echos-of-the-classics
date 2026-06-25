from rag.vector_store import get_collection

def buscar_contexto(query: str, autor: str = None, n_resultados: int = 3) -> str:
    """
    Busca os pedaços de texto mais semelhantes à query no ChromaDB.
    Filtra por autor se especificado.
    """
    colecao = get_collection()
    
    filtro_metadados = None
    if autor and autor.lower() != "todos":
        filtro_metadados = {"autor": autor.lower()}
        print(f"[LOG INFO] Buscando por: '{query}' de {autor}")
    else:
        print(f"[LOG INFO] Buscando por: '{query}' em todos os autores")

    # Faz a busca vetorial por similaridade de cosseno
    resultados = colecao.query(
        query_texts=[query],
        n_results=n_resultados,
        where=filtro_metadados
    )
    
    # Formata a resposta estruturada para o prompt do LLM
    contexto_formatado = ""
    if resultados and resultados['documents'] and len(resultados['documents'][0]) > 0:
        print(f"[LOG INFO] {len(resultados['documents'][0])} fragmentos encontrados")
        for i, doc in enumerate(resultados['documents'][0]):
            meta = resultados['metadatas'][0][i]
            contexto_formatado += f"--- Trecho de {meta['autor'].capitalize()} (Fonte: {meta['fonte']}) ---\n"
            contexto_formatado += f"\"{doc}\"\n\n"
        return contexto_formatado.strip()
    
    print("[LOG INFO] Nenhum fragmento encontrado")
    return "Nenhum fragmento literário histórico foi encontrado para dar suporte a este tema."