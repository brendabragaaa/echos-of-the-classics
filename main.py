from rag.embed_documents import indexar_base_conhecimento
from rag.retrieval import buscar_contexto
from tools.retrieve_content import retrieve_content
from tools.author_profile import get_author_profile
from tools.validate_context import validate_context
from tools.format_response import format_response

def main():
    """
    Interface principal do Echos of the Classics.
    Integra busca vetorial, recuperação de contexto e formatação de respostas.
    """
    print("[LOG INFO] Iniciando Echos of the Classics...")
    print("[LOG INFO] Carregando base de conhecimento literário...\n")
    
    # Indexa a base de conhecimento (executa uma única vez ou quando necessário)
    try:
        indexar_base_conhecimento()
    except Exception as e:
        print(f"[ERRO] Falha ao indexar base: {e}")
        return
    
    print("\n" + "="*75)
    print("BEM-VINDO AO ECHOS OF THE CLASSICS")
    print("Um diálogo com os grandes mestres da literatura universal")
    print("="*75 + "\n")
    
    try:
        while True:
            # Recebe input do usuário
            query = input("\n📖 Faça uma pergunta aos clássicos (ou 'sair' para encerrar): ").strip()
            
            if query.lower() in {"sair", "exit", "quit"}:
                print("[LOG INFO] Encerrando aplicação...")
                break
            
            if not query:
                print("[LOG INFO] Por favor, digite uma pergunta válida.")
                continue
            
            print(f"\n[LOG INFO] Processando query: '{query}'")
            
            # Busca contexto no banco vetorial
            contexto = buscar_contexto(query, n_resultados=5)
            
            # Valida o contexto recuperado
            validacao = validate_context(query, contexto)
            
            if not validacao["valid"]:
                print(f"[AVISO] Contexto pode ser irrelevante: {validacao['reason']}")
                continue
            
            print("[LOG INFO] Contexto validado com sucesso")
            
            # Recupera conteúdo e perfis dos autores
            conteudo_recuperado = retrieve_content(query)
            
            # Monta respostas estruturadas por autor
            respostas_autores = {}
            for item in conteudo_recuperado:
                autor = item.get("author", "Desconhecido")
                livro = item.get("book", "Obra desconhecida")
                trecho = item.get("content", "")
                
                # Busca perfil do autor
                perfil = get_author_profile(autor)
                
                respostas_autores[autor] = f"[{livro}]\n{trecho}\n\n{perfil}"
            
            # Formata e exibe resposta final
            resposta_final = format_response(query, respostas_autores)
            print(resposta_final)
    
    except (KeyboardInterrupt, EOFError):
        print("\n[LOG INFO] Encerrando aplicação...")
    except Exception as e:
        print(f"[ERRO] Erro inesperado: {e}")


if __name__ == "__main__":
    main()
