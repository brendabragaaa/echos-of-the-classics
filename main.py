from rag.embed_documents import indexar_base_conhecimento
from rag.retrieval import buscar_contexto

from tools.retrieve_content import retrieve_content
from tools.author_profile import get_author_profile
from tools.validate_context import validate_context
from tools.format_response import format_response

from agentes.shakespeare import ShakespeareAgent
from agentes.dostoievski import DostoievskiAgent
from agentes.lispector import LispectorAgent
from agentes.woolf import WoolfAgent
from agentes.moderador import ModeradorAgent


def main():
    """
    Interface principal do Echos of the Classics.
    Integra busca vetorial, recuperação de contexto
    e respostas geradas pelos agentes literários.
    """

    print("[LOG INFO] Iniciando Echos of the Classics...")
    print("[LOG INFO] Carregando base de conhecimento literário...\n")

    # Indexa a base de conhecimento
    try:
        indexar_base_conhecimento()

    except Exception as e:
        print(f"[ERRO] Falha ao indexar base: {e}")
        return

    # Inicializa os agentes
    shakespeare = ShakespeareAgent()
    dostoievski = DostoievskiAgent()
    lispector = LispectorAgent()
    woolf = WoolfAgent()
    moderador = ModeradorAgent()

    print("\n" + "=" * 75)
    print("BEM-VINDO AO ECHOS OF THE CLASSICS")
    print("Um diálogo com os grandes mestres da literatura universal")
    print("=" * 75 + "\n")

    try:

        while True:

            query = input(
                "\n📖 Faça uma pergunta aos clássicos (ou 'sair' para encerrar): "
            ).strip()

            if query.lower() in {"sair", "exit", "quit"}:
                print("[LOG INFO] Encerrando aplicação...")
                break

            if not query:
                print("[LOG INFO] Por favor, digite uma pergunta válida.")
                continue

            print(f"\n[LOG INFO] Processando query: '{query}'")

            # Busca contexto no banco vetorial
            contexto = buscar_contexto(
                query=query,
                n_resultados=5
            )

            # Valida o contexto recuperado
            validacao = validate_context(
                query,
                contexto
            )

            if not validacao["valid"]:
                print(
                    f"[AVISO] Contexto pode ser irrelevante: "
                    f"{validacao['reason']}"
                )
                continue

            print("[LOG INFO] Contexto validado com sucesso")

            # Mantém compatibilidade com o código antigo
            conteudo_recuperado = retrieve_content(query)

            dados_autores = {}

            for item in conteudo_recuperado:

                autor = item.get("author", "Desconhecido")

                dados_autores[autor] = {
                    "livro": item.get("book", "Obra desconhecida"),
                    "trecho": item.get("content", ""),
                    "perfil": get_author_profile(autor)
                }

            print("[LOG INFO] Consultando os autores...")

            # Respostas dos agentes
            respostas_autores = {
                "Shakespeare": shakespeare.responder(
                    pergunta=query,
                    contexto=contexto
                ),

                "Dostoiévski": dostoievski.responder(
                    pergunta=query,
                    contexto=contexto
                ),

                "Clarice Lispector": lispector.responder(
                    pergunta=query,
                    contexto=contexto
                ),

                "Virginia Woolf": woolf.responder(
                    pergunta=query,
                    contexto=contexto
                )
            }

            # Moderador organiza a saída
            resposta_final = moderador.organizar(
                pergunta=query,
                respostas=respostas_autores
            )

            print("\n")
            print(resposta_final)

    except (KeyboardInterrupt, EOFError):

        print("\n[LOG INFO] Encerrando aplicação...")

    except Exception as e:

        print(f"[ERRO] Erro inesperado: {e}")


if __name__ == "__main__":
    main()