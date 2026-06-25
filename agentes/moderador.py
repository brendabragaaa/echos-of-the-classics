from tools.format_response import format_response

class ModeradorAgent:

    def __init__(self):
        self.nome = "Moderador"

    def organizar(self, pergunta: str, respostas: dict) -> str:

        print("[LOG INFO] Enviando respostas para formatação final...")

        return format_response(pergunta, respostas)