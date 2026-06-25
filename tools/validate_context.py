# tools/validate_context.py

def validate_context(query: str, context: str) -> dict:
    """
    Analisa se o contexto recuperado é relevante para responder à pergunta do usuário.
    (Mockado para simular uma validação semântica simples)
    """
    print(f"[LOG INFO] Validando relevância do contexto para a query: '{query}'")
    
    # Converte tudo para minúsculo para facilitar a busca por palavras-chave básicas
    query_lower = query.lower()
    context_lower = context.lower()
    
    # Lista de palavras comuns para testar correspondência mínima
    keywords = ["sofrimento", "dor", "solidão", "tempo", "morte", "amor", "vida", "ser", "identidade"]
    
    # Uma lógica simples de "mock" para decidir se o contexto é válido
    # Se houver alguma palavra em comum ou se o contexto for grande, consideramos válido
    has_keyword = any(word in query_lower and word in context_lower for word in keywords)
    
    if len(context) > 20 or has_keyword:
        return {
            "valid": True,
            "reason": "O contexto possui densidade textual suficiente ou palavras-chave compatíveis com a pergunta."
        }
    else:
        return {
            "valid": False,
            "reason": "O contexto recuperado parece muito curto ou irrelevante para a pergunta feita."
        }