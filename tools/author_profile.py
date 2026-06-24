# tools/author_profile.py

def get_author_profile(author_name: str) -> str:
    """
    Retorna o perfil temático e o foco filosófico de um autor específico.
    """
    print(f"[LOG INFO] Buscando perfil do autor: '{author_name}'")
    
    # Padroniza o nome para evitar problemas de maiúsculas/minúsculas
    author = author_name.lower()
    
    profiles = {
        "shakespeare": (
            "Foco: Tragédia, destino, ambição humana e amor. "
            "Estilo: Poético, dramático, focado nas falhas trágicas dos personagens (como o orgulho ou a dúvida)."
        ),
        "dostoievski": (
            "Foco: Culpa, sofrimento, moralidade, redenção e fé. "
            "Estilo: Psicológico denso, existencialista, explorando os abismos da mente humana e crises espirituais."
        ),
        "clarice lispector": (
            "Foco: Introspecção, identidade, existência e fluxo de consciência. "
            "Estilo: Epifanias cotidianas, olhar voltado para o 'eu' interior e o estranhamento da realidade."
        ),
        "virginia woolf": (
            "Foco: Subjetividade, o impacto do tempo, memória e percepção. "
            "Estilo: Fluxo de consciência avançado, fragmentado, focado na experiência psicológica do tempo presente."
        )
    }
    
    # Tenta encontrar o autor na base, senão retorna um aviso
    for key in profiles:
        if key in author:
            return profiles[key]
            
    return f"Autor '{author_name}' não encontrado na base de perfis literários do LitMind AI."