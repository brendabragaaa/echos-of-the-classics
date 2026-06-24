# tools/format_response.py

def format_response(query: str, raw_responses: dict) -> str:
    """
    Formata as respostas dos agentes literários em um layout limpo 
    e elegante para exibição no terminal.
    """
    print("[LOG INFO] Formatando a resposta final unificada...")
    
    border = "=" * 50
    sub_border = "-" * 30
    
    formatted_output = []
    formatted_output.append(border)
    formatted_output.append(f"   LITMIND AI - DEBATE FILOSÓFICO")
    formatted_output.append(border)
    formatted_output.append(f"Pergunta do Usuário: '{query}'\n")
    
    # Passa por cada autor e organiza sua respectiva fala
    for author, text in raw_responses.items():
        formatted_output.append(f"👤 {author.upper()}:")
        formatted_output.append(sub_border)
        formatted_output.append(f"{text}\n")
        
    formatted_output.append(border)
    formatted_output.append("Fim do Debate Literário.")
    formatted_output.append(border)
    
    return "\n".join(formatted_output)