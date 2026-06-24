# mcp_server/server.py
from mcp.server.fastmcp import FastMCP

# Importando as funções que você fez na pasta tools
from tools.retrieve_content import retrieve_content
from tools.author_profile import get_author_profile
from tools.validate_context import validate_context
from tools.format_response import format_response

# Inicializa o servidor FastMCP
mcp = FastMCP("Echoes-of-the-Classics-Server")

@mcp.tool()
def tool_retrieve_content(query: str) -> str:
    """
    Recupera trechos relevantes da base de conhecimento RAG 
    com base em um conceito filosófico ou pergunta do usuário.
    """
    results = retrieve_content(query)
    output = []
    for item in results:
        output.append(f"Autor: {item['author']} | Obra: {item['book']}\nTrecho: {item['content']}\n")
    return "\n---\n".join(output)

@mcp.tool()
def tool_author_profile(author_name: str) -> str:
    """
    Retorna a vertente filosófica, foco temático e estilo literário 
    de um determinado autor (Shakespeare, Dostoiévski, Clarice ou Virginia Woolf).
    """
    return get_author_profile(author_name)

@mcp.tool()
def tool_validate_context(query: str, context: str) -> str:
    """
    Analisa se os trechos recuperados são semanticamente válidos 
    e suficientes para responder à pergunta original do usuário.
    """
    res = validate_context(query, context)
    return f"Válido: {res['valid']} | Motivo: {res['reason']}"

@mcp.tool()
def tool_format_response(query: str, raw_responses: dict) -> str:
    """
    Pega as respostas individuais dos autores literários e gera a 
    moldura final formatada em ASCII art para exibição retrô no terminal.
    """
    return format_response(query, raw_responses)

if __name__ == "__main__":
    # Roda o servidor
    print("[SERVER LOG] Servidor MCP iniciado. Aguardando conexão via STDIO...")
    mcp.run(transport='stdio')