from models.ollama_config import llm
from tools.author_profile import get_author_profile

class LispectorAgent:

    def __init__(self):
        self.nome = "Clarice Lispector"

    def responder(self, pergunta: str, contexto: str) -> str:

        profile = get_author_profile("clarice lispector")

        prompt = f"""
Você é Clarice Lispector.

Perfil do autor:
{profile}

IMPORTANTE:
- Baseie-se apenas no contexto fornecido.
- Não invente fatos.
- Responda como se fosse a própria Clarice Lispector.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}
"""
        resposta = llm.invoke(prompt)

        return resposta.content