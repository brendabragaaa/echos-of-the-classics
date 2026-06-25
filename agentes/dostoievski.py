from models.ollama_config import llm
from tools.author_profile import get_author_profile


class DostoievskiAgent:

    def __init__(self):
        self.nome = "Fiódor Dostoiévski"

    def responder(self, pergunta: str, contexto: str) -> str:

        profile = get_author_profile("dostoievski")

        prompt = f"""
Você é Fiódor Dostoiévski.

Perfil do autor:
{profile}

IMPORTANTE:
- Baseie-se apenas no contexto fornecido.
- Não invente fatos.
- Responda como se fosse o próprio Dostoiévski.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}
"""

        resposta = llm.invoke(prompt)

        return resposta.content