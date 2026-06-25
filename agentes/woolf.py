from models.ollama_config import llm
from tools.author_profile import get_author_profile

class WoolfAgent:

    def __init__(self):
        self.nome = "Virginia Woolf"

    def responder(self, pergunta: str, contexto: str) -> str:

        profile = get_author_profile("virginia woolf")

        prompt = f"""
Você é Virginia Woolf.

Perfil do autor:
{profile}

IMPORTANTE:
- Baseie-se apenas no contexto fornecido.
- Não invente fatos.
- Responda como se fosse a própria Virginia Woolf.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}
"""
        resposta = llm.invoke(prompt)

        return resposta.content