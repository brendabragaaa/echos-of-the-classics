# tools/format_response.py

def format_response(query: str, raw_responses: dict) -> str:
    """
    Formata as respostas dos agentes literários em um layout imersivo 
    utilizando molduras de caracteres ASCII sem elementos visuais modernos (emojis).
    """
    print("[LOG INFO] Formatando a resposta final unificada...")
    
    ascii_banner = """
    +---------------------------------------------------------+
    |  _     _ _   __  __ _           _    _____ _____        |
    | | |   (_) | |  \/  (_)_ __   __| |  |_   _|_   _|       |
    | | |   | | __| |\/| | | '_ \ / _` |    | |   | |         |
    | | |___| | |_| |  | | | | | | (_| |   _| |_ _| |_        |
    | |_____|_|\__|_|  |_|_|_| |_|\__,_|  |_____|_____|       |
    |                                                         |
    +---------------------------------------------------------+
    |                   DEBATE EXISTENCIAL                    |
    +---------------------------------------------------------+
    """
    
    # Linhas divisórias usando caracteres de caixa estilizados
    width = 75
    top_border    = "┌" + "─" * (width - 2) + "┐"
    bottom_border = "└" + "─" * (width - 2) + "┘"
    separator     = "├" + "─" * (width - 2) + "┤"
    dots_line     = "│ " + "." * (width - 4) + " │"
    
    formatted_output = []
    formatted_output.append(ascii_banner)
    
    # Caixa da pergunta
    formatted_output.append(top_border)
    formatted_output.append(f"│ QUESTIONAMENTO: {query.ljust(width - 19)} │")
    formatted_output.append(separator)
    
    # Inserção das respostas dos autores
    for author, text in raw_responses.items():
        author_header = f" AUTOR: {author.upper()} "
        formatted_output.append(f"│ {author_header.ljust(width - 4, '-')} │")
        formatted_output.append("│" + " " * (width - 2) + "│")
        
        # Quebra o texto em linhas para caber na moldura do terminal de forma alinhada
        words = text.split()
        current_line = []
        max_text_width = width - 6 # Margem interna
        
        for word in words:
            # Verifica se a palavra cabe na linha atual
            if len(" ".join(current_line + [word])) <= max_text_width:
                current_line.append(word)
            else:
                line_str = " ".join(current_line)
                formatted_output.append(f"│   {line_str.ljust(max_text_width)}   │")
                current_line = [word]
        if current_line:
            line_str = " ".join(current_line)
            formatted_output.append(f"│   {line_str.ljust(max_text_width)}   │")
            
        formatted_output.append("│" + " " * (width - 2) + "│")
        formatted_output.append(dots_line)
        
    # Rodapé do bloco
    formatted_output.append(separator)
    footer_text = " Fim da transmissao. O conhecimento permanece oculto. "
    formatted_output.append(f"│ {footer_text.center(width - 4, ' ')} │")
    formatted_output.append(bottom_border)
    
    return "\n".join(formatted_output)