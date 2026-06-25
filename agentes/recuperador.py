from rag.retrieval import buscar_contexto


class RecuperadorAgent:

    def __init__(self):
        self.nome = "Recuperador"

    def recuperar(self, pergunta: str) -> str:
        """
        Busca os trechos mais relevantes
        na base vetorial.
        """

        contexto = buscar_contexto(
            query=pergunta,
            n_resultados=5
        )

        return contexto