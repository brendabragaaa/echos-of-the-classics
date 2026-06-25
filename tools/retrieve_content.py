# tools/retrieve_content.py

def retrieve_content(query: str) -> list:
    """
    Simula a busca de trechos de livros no banco vetorial.
    (Atualmente mockado até a Pessoa 1 terminar o banco real)
    """
    print(f"[LOG INFO] Buscando no banco vetorial por: '{query}'")
    
    # Dados fictícios para vocês conseguirem testar o fluxo completo
    mock_database = [
        {
            "author": "Clarice Lispector", 
            "book": "A Hora da Estrela",
            "content": "Sou uma pergunta olhando para outra pergunta."
        },
        {
            "author": "Dostoiévski", 
            "book": "Notas do Subsolo",
            "content": "O homem gosta de contar os seus problemas, mas não conta as suas alegrias."
        },
        {
            "author": "Virginia Woolf",
            "book": "Mrs Dalloway",
            "content": "As pessoas não deveriam dizer o que sentem."
        },
        {
            "author": "Shakespeare",
            "book": "Hamlet",
            "content": "Ser ou não ser, eis a questão."
        }
    ]
    
    return mock_database