from .retrieval import buscar_contexto

pergunta = "O que os autores dizem sobre a solidão e o isolamento da mente?"
print(f"Pesquisando no banco por: '{pergunta}'...\n")

resultados = buscar_contexto (
    query=pergunta, 
    autor="Todos", 
    n_resultados=2
)

print("--- TRECHOS ENCONTRADOS ---")
print(resultados)