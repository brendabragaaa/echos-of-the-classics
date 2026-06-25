<p align="center">
  <img src="./cover.png" alt="Echoes of the Classics Banner" width="100%">
</p>

# Echoes of the Classics

> **Sistema Multiagente de Perspectivas Literárias com LLMs Locais**

O **Echoes of the Classics** é um sistema multiagente inteligente baseado em Modelos de Linguagem de grande porte (LLMs) executados localmente. O sistema é capaz de simular como grandes autores da literatura mundial — *William Shakespeare, Fiódor Dostoiévski, Clarice Lispector e Virginia Woolf* — responderiam a uma mesma pergunta, dilema ou reflexão trazida pelo usuário, fundamentando suas respostas em trechos reais de suas obras por meio de técnicas de RAG (Geração Aumentada por Recuperação).

---

## Integrantes

* **Brenda Braga de Lima**
* **Leticia de Fragas**
* **Mariane Schneider da Silva**

**Disciplina:** Inteligência Artificial  
**Professores:** Diego A. Lusa e Roberto Rabello  

---

## Tecnologias Utilizadas

Para o desenvolvimento e controle do ecossistema, o projeto faz uso das seguintes ferramentas:

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
  <img src="https://img.shields.io/badge/ChromaDB-007ACC?style=for-the-badge&logo=googlecloud&logoColor=white" alt="ChromaDB" />
  <img src="https://img.shields.io/badge/MCP-Protocol-9B51E0?style=for-the-badge&logo=json&logoColor=white" alt="Model Context Protocol" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
</p>

---

## Descrição do Problema

Acessar e compreender profundamente a visão de grandes autores da literatura mundial exige um denso conhecimento prévio de suas obras, contexts históricos e estilos literários. Quando pessoas buscam diferentes perspectivas para refletir sobre questões pessoais, emocionais ou filosóficas, essa barreira cultural pode dificultar o acesso a esses ricos insights.

### A Solução
Este projeto propõe um ecossistema multiagente que reduz essa barreira. A partir de uma base documental de obras selecionadas, o sistema recupera o contexto semântico ideal e gera respostas independentes e personalizadas que emulam fielmente os temas, o tom e a linguagem de quatro pilares da literatura clássica.

---

## Objetivo da Solução

* **Simular Perspectivas Distintas:** Gerar respostas independentes inspiradas no estilo de cada autor para o mesmo tema.
* **Fundamentação por RAG:** Utilizar busca vetorial para basear as respostas em trechos e pensamentos de obras reais.
* **Cooperação Multiagente:** Demonstrar a arquitetura estruturada de múltiplos agentes especialistas trabalhando em paralelo.
* **Privacidade e Autonomia:** Implementar e explorar modelos de linguagem e bancos de embeddings rodando 100% de forma local.

---

## Arquitetura Multiagente

O ecossistema utiliza uma arquitetura modular composta por **6 agentes especializados** que colaboram em um pipeline sequencial e paralelo:

```text
       ┌────────────────────────┐
       │     Entrada Usuário    │
       └───────────┬────────────┘
                   ▼
       ┌────────────────────────┐
       │   Agente Recuperador   │ ◄─── (ChromaDB + RAG)
       └───────────┬────────────┘
                   │
         ┌─────────┴─────────┬───────────────────┐
         ▼                   ▼                   ▼
    Shakespeare         Dostoiévski       Clarice Lispector     Virginia Woolf
  (Agente Poético)    (Agente Psicológico) (Agente Introspectivo) (Agente Modernista)
         │                   │                   │                   │
         └─────────┬─────────┴───────────────────┘                   │
                   ▼                                                 ▼
       ┌────────────────────────┐
       │    Agente Moderador    │
       └───────────┬────────────┘
                   ▼
       ┌────────────────────────┐
       │     Resposta Retrô     │
       └────────────────────────┘

```

### Fluxo de Execução

1. O usuário envia uma reflexão ou dilema através do console.
2. O **Agente Recuperador** varre o banco vetorial em busca dos trechos mais semelhantes ao tema.
3. O contexto validado é distribuído simultaneamente aos **Agentes Especialistas**.
4. Cada especialista gera seu texto focado em sua persona literária.
5. O **Agente Moderador** captura, organiza as saídas em blocos e renderiza o layout visual formatado em arte ASCII.

---

## Agentes Especializados e Bases Documentais

### Agente Recuperador (Retriever Agent)

* **Função:** Realiza a busca semântica na base vetorial por similaridade de cosseno.
* **Foco:** Extrair o contexto factual mais rico para mitigar alucinações dos demais modelos.

---

### Agente Shakespeare

Produz respostas focadas na beleza poética da linguagem elisabetana e nos paradoxos do coração humano.

* **Especialidade:** Tragédias, dilemas de poder, ambição, honra, destino cruel e paixões avassaladoras.
* **Obras Base:** *Hamlet*, *Romeu e Julieta*, *Otelo*.

---

### Agente Dostoiévski

Gera análises profundas sob a ótica do sofrimento existencial e da complexidade da psique humana.

* **Especialidade:** Filosofia existencialista, moralidade, culpa, redenção, livre-arbítrio e crise de fé.
* **Obras Base:** *Crime e Castigo*, *Noites Brancas*, *Memórias do Subsolo*.

---

### Agente Clarice Lispector

Respostas altamente introspectivas focadas na epifania do cotidiano e no fluxo de consciência interior.

* **Especialidade:** Identidade, subjetividade da alma, solidão e crise do "eu".
* **Obras Base:** *A Hora da Estrela*, *Perto do Coração Selvagem*, *Laços de Família*.

---

### Agente Virginia Woolf

Explora percepções fragmentadas do tempo psicológico através da prosa modernista refinada.

* **Especialidade:** Modernismo, fluxo de consciência contínuo, memória e o papel da perspectiva.
* **Obras Base:** *Ao Farol*, *Orlando*, *Um Teto Todo Seu*.

---

### Agente Moderador (Moderator Agent)

* **Função:** Receber as saídas geradas por cada autor, aplicar filtros estruturais e empacotar no layout visual do terminal.
* **Foco:** Garantir que o contraste entre as visões seja apresentado ao usuário de forma limpa e legível.

---

## Tools Disponíveis via MCP

O projeto adota o **Model Context Protocol (MCP)** para registrar de forma limpa e acoplável os recursos de sistema que os agentes podem invocar:

* **`retrieve_context`:** Realiza conexões diretas de leitura na instância ativa do ChromaDB.
* **`author_profile`:** Retorna um mapa estático contendo diretrizes estruturais de escrita de cada autor (tom, vocabulário e vícios de linguagem) para calibrar o prompt do LLM.
* **`validate_context`:** Camada de segurança que checa se os trechos retornados do banco condizem semanticamente com a pergunta para evitar ruídos de IA.
* **`format_response`:** Renderizador de strings responsável por desenhar as molduras e caixas em caracteres ASCII no terminal do usuário.

---

## Estratégia de RAG e Base de Conhecimento

A arquitetura de **Geração Aumentada por Recuperação (RAG)** garante que as respostas não dependam unicamente do conhecimento genérico pré-treinado do LLM local.

```text
knowledge_base/
├── shakespeare/   # Arquivos TXT/Markdown limpos das obras elisabetanas
├── dostoievski/   # Romances focados em psicologia existencial russa
├── lispector/     # Contos e romances brasileiros introspectivos
└── woolf/         # Ensaios e romances de fluxo de consciência modernista

```

Os textos são segmentados em blocos lógicos (*chunks*), processados por um modelo local de embeddings e indexados no **ChromaDB**.

---

## Estrutura do Projeto

```text
echoes-of-the-classics/
│
├── agentes/           # Configuração de prompts e chamadas de LLM dos agentes
├── database/          # Arquivos de persistência local do ChromaDB
├── knowledge_base/    # Documentos textuais de domínio público fracionados por autor
├── mcp_server/        # Infraestrutura do servidor MCP e hubs de comunicação
│   ├── server.py      # Ponto de entrada do protocolo via STDIO
│   └── tools.py       # Centralizador de registro das ferramentas
├── models/            # Scripts auxiliares para configuração do Ollama
├── rag/               # Lógica de embeddings, ingestão e busca vetorial
├── tools/             # Código modular das funções de suporte (ASCII, validação)
│
├── .gitignore         # Exclusão de ambientes virtuais e base de dados pesadas
├── LICENSE            # Licença padrão de uso acadêmico
├── main.py            # Inicializador geral do ecossistema e interface de usuário
├── README.md          # Documentação descritiva do projeto
└── requirements.txt   # Gerenciador de dependências pip do Python

```

---

## Instalação e Execução (Em Desenvolvimento)

### Pré-requisitos

Certifique-se de ter instalado em sua máquina o **Python 3.11+** e o ecossistema do **Ollama**.

1. **Clonar o Repositório:**

```bash
   git clone [https://github.com/brendabragaaa/echos-of-the-classics.git](https://github.com/brendabragaaa/echos-of-the-classics.git)
   cd echos-of-the-classics

```

2. **Configurar Ambiente Virtual:**

```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate

```

3. **Instalar Dependências:**

```bash
   pip install -r requirements.txt

```

4. **Execução:**
As diretivas de carregamento da base vetorial e execução do loop principal (`main.py`) serão detalhadas conforme o avanço das sprints de desenvolvimento.

---

## Exemplos de Uso

**Pergunta digitada no terminal:**

> *"Como lidar com a sensação de estar completamente perdido no mundo?"*

**Comportamento Esperado na Resposta Combinada:**

* **Shakespeare:** Retornará uma metáfora sobre o mundo ser um palco de sombras, onde o destino testa os homens, instigando o usuário a enfrentar a tragédia interna com altivez.
* **Dostoiévski:** Evidenciará que estar perdido é o primeiro passo para o despertar espiritual e moral, tratando o sofrimento do isolamento como um processo purificador da alma.
* **Clarice Lispector:** Validará o vazio não como um problema, mas como um mergulho visceral na própria liberdade e na busca silenciosa pela identidade.
* **Virginia Woolf:** Mostrará a percepção do tempo passando, transformando o sentimento em impressões sensoriais e fragmentos de memória sob o fluxo das marés da vida.

---

## Conclusão

**Echoes of the Classics** consolida conceitos avançados de inteligência artificial de ponta de forma autônoma. Através do acoplamento do **Model Context Protocol (MCP)** com arquitetura de múltiplos agentes independentes e sistemas de busca RAG locais, o projeto prova ser uma ferramenta potente e viável para simulação analítica, contextualização literária e interface interpretativa humanizada.