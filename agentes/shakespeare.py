from models.ollama_config import llm
from tools.author_profile import get_author_profile

class ShakespeareAgent:

    def __init__(self):
        self.nome = "William Shakespeare"

    def responder(self, pergunta: str, contexto: str) -> str:

        profile = get_author_profile("shakespeare")

        prompt = f"""
Você é William Shakespeare.

Perfil do autor:
{profile}

IMPORTANTE:
- Baseie-se apenas no contexto fornecido.
- Não invente fatos.
- Responda como se fosse o próprio Shakespeare.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}
"""
        resposta = llm.invoke(prompt)

        return resposta.content