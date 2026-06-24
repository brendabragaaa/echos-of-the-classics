# Echoes of the Classics

Sistema Multiagente de Perspectivas Literárias com LLMs Locais

## Integrantes

* Brenda Braga de Lima
* Leticia de Fragas
* Mariane Schneider da Silva

Disciplina: Inteligência Artificial

Professores: Diego A. Lusa e Roberto Rabello

---

## Descrição do Problema

Pessoas frequentemente buscam diferentes perspectivas para refletir sobre questões pessoais, emocionais, filosóficas ou literárias. Entretanto, acessar e compreender a visão de grandes autores da literatura exige conhecimento prévio de suas obras e estilos.

Este projeto propõe um sistema multiagente capaz de simular como diferentes escritores clássicos responderiam a uma mesma pergunta ou situação apresentada pelo usuário. A partir de uma base documental construída com obras de cada autor, o sistema recupera contexto relevante e gera respostas coerentes com os temas, linguagem e características presentes em seus trabalhos.

Dessa forma, o usuário pode explorar múltiplas interpretações de um mesmo assunto através das perspectivas de William Shakespeare, Fiódor Dostoiévski, Clarice Lispector e Virginia Woolf.

---

## Objetivo da Solução

Desenvolver um sistema multiagente baseado em LLMs locais capaz de receber perguntas, reflexões, situações pessoais ou temas livres e gerar respostas independentes inspiradas em diferentes autores da literatura mundial.

A solução busca:

* Simular perspectivas literárias distintas para um mesmo tema;
* Utilizar recuperação de contexto para fundamentar as respostas em obras reais;
* Demonstrar a cooperação entre múltiplos agentes especializados;
* Explorar diferenças de estilo, linguagem e visão de mundo entre autores clássicos;
* Aplicar técnicas de RAG, embeddings, MCP e modelos locais em um sistema funcional.

---

## Arquitetura Multiagente

O sistema utiliza uma arquitetura composta por seis agentes especializados que colaboram para gerar múltiplas perspectivas literárias sobre uma mesma entrada fornecida pelo usuário.

O fluxo de execução ocorre da seguinte forma:

1. O usuário envia uma pergunta, reflexão, situação pessoal ou tema livre através do terminal.
2. O Agente Recuperador consulta a base vetorial e recupera trechos relevantes relacionados aos autores e ao tema da consulta.
3. O contexto recuperado é disponibilizado aos agentes especialistas.
4. Cada agente especialista gera sua própria resposta inspirada no estilo, nos temas recorrentes e nas características literárias de seu respectivo autor.
5. O Agente Moderador recebe as respostas produzidas pelos especialistas, organiza o conteúdo e apresenta o resultado final ao usuário de forma estruturada.

Fluxo resumido:

```text
Usuário
   ↓
Recuperador (RAG + ChromaDB)
   ↓
├─ Shakespeare
├─ Dostoiévski
├─ Clarice Lispector
└─ Virginia Woolf
   ↓
Moderador
   ↓
Resposta Final
```

---

## Agentes Especializados

### Recuperador (Retriever Agent)

* Realiza busca semântica na base vetorial
* Recupera trechos relevantes das obras
* Fornece contexto para os demais agentes
* Implementa a estratégia RAG do sistema

### Shakespeare Agent

Produz respostas inspiradas na linguagem e nos temas presentes nas obras de William Shakespeare.
Enfatiza tragédia, destino, paixão, honra, poder e conflitos humanos.

Especialista em:

* Tragédias
* Comédias
* Sonetos
* Temas de poder, ambição, destino, paixão, honra e conflitos humanos.

Base documental:

* Hamlet
* Romeu e Julieta
* Otelo

---

### Dostoiévski Agent

Produz respostas inspiradas nas reflexões filosóficas e psicológicas de Dostoiévski.

Especialista em:

* Filosofia existencial
* Psicologia dos personagens
* Temas de  moralidade, livre-arbítrio, culpa, fé e sofrimento

Base documental:

* Crime e Castigo
* Noites Brancas
* Memórias do Subsolo

---

### Clarice Lispector Agent

Produz respostas introspectivas focadas na experiência interior e na construção da identidade.

Especialista em:

* Fluxo de consciência
* Existencialismo
* Identidade e subjetividade
* Interioridade humana 

Base documental:

* A Hora da Estrela
* Perto do Coração Selvagem
* Laços de Família

---

### Virginia Woolf Agent

Produz respostas influenciadas pelo modernismo e pelo fluxo de consciência.

Especialista em:

* Modernismo
* Fluxo de consciência
* Tempo psicológico
* Explora perspectivas narrativas, memória, tempo e subjetividade

Base documental:

* Ao Farol
* Orlando
* Um Teto Todo Seu

---

### Moderador (Moderator Agent)

* Recebe as respostas dos agentes especialistas
* Organiza e apresenta os resultados ao usuário
* Garante consistência no formato de saída
* Pode destacar semelhanças e diferenças entre as perspectivas apresentadas.

---

## Tools Disponíveis

### retrieve_context

Ferramenta utilizada pelo Agente Recuperador para realizar buscas semânticas na base vetorial.

**Fluxo de funcionamento:**

Pergunta do usuário  
↓  
Consulta ao ChromaDB  
↓  
Recuperação dos documentos mais relevantes  
↓  
Envio do contexto aos agentes especialistas

---

### author_profile

Ferramenta responsável por fornecer informações sobre um autor específico, auxiliando os agentes na construção de respostas coerentes com seu estilo literário.

**Informações recuperadas:**

- Temas recorrentes;
- Estilo de escrita;
- Tom emocional;
- Características narrativas.

**Exemplo de uso:**

`get_author_profile("clarice")`

**Resultado esperado:**

Informações relacionadas à escrita de Clarice Lispector, como introspecção, existencialismo, fluxo de consciência e reflexões sobre identidade.

---

### validate_context

Ferramenta utilizada para verificar se os trechos recuperados pertencem ao autor correto e são relevantes para a consulta realizada.

**Objetivos:**

- Garantir a consistência do contexto recuperado;
- Reduzir respostas incorretas ou fora do escopo;
- Aumentar a confiabilidade do sistema.

---

### format_response

Ferramenta utilizada pelo Agente Moderador para organizar e estruturar as respostas geradas pelos agentes especialistas.

**Entrada:**

- Resposta do agente Shakespeare;
- Resposta do agente Dostoiévski;
- Resposta do agente Clarice Lispector;
- Resposta do agente Virginia Woolf.

**Saída esperada:**

🎭 **Shakespeare**

> Resposta gerada pelo agente.

📖 **Dostoiévski**

> Resposta gerada pelo agente.

🪞 **Clarice Lispector**

> Resposta gerada pelo agente.

🌊 **Virginia Woolf**

> Resposta gerada pelo agente.
---

## Uso do MCP

O projeto utiliza MCP (Model Context Protocol) para padronizar a comunicação entre agentes e ferramentas.

O MCP atua como uma camada intermediária responsável por:

* Registrar ferramentas disponíveis;
* Encaminhar chamadas dos agentes;
* Padronizar entrada e saída de dados;
* Facilitar a integração entre componentes do sistema.

Arquivos relacionados:

* mcp_server/server.py
* mcp_server/tools.py

---

## Estratégia de RAG

A abordagem Retrieval-Augmented Generation é utilizada para reduzir alucinações e aumentar a precisão das respostas.

Fluxo:

1. Usuário realiza uma pergunta.
2. A consulta é transformada em embedding.
3. O ChromaDB realiza busca vetorial.
4. Os documentos mais relevantes são recuperados.
5. O contexto é enviado aos agentes.
6. Os agentes geram respostas fundamentadas nos documentos recuperados.

---

## Base de Conhecimento

A base documental foi construída a partir de obras literárias e materiais de domínio público relacionados aos autores estudados.

Estrutura:

knowledge_base/

* shakespeare/
* dostoievski/
* lispector/
* woolf/

Os documentos são utilizados exclusivamente para fins acadêmicos.

---

## Embeddings e Banco Vetorial

Tecnologia prevista:

* ChromaDB

O sistema utilizará embeddings para representar semanticamente os documentos da base de conhecimento, permitindo a recuperação de contexto relevante para os agentes especializados.

Funções:

* Indexação semântica dos documentos;
* Busca vetorial por similaridade;
* Recuperação contextual para suporte à geração das respostas.

**Observação:** O modelo de embeddings será definido durante a implementação do projeto.

---

## Modelo Local Utilizado

Framework previsto:

* Ollama

O sistema utilizará um modelo de linguagem executado localmente para garantir independência de APIs externas e maior controle sobre o ambiente de execução.

**Observação:** O modelo específico será definido durante a implementação e testes do projeto.

---

## Tecnologias Utilizadas

Tecnologias previstas para o desenvolvimento:

* Python 3.11+
* Ollama
* ChromaDB
* MCP (Model Context Protocol)
* Git
* GitHub

Outras bibliotecas poderão ser adicionadas conforme a evolução do projeto.

---

## Dependências

As dependências do projeto serão listadas no arquivo:

```bash
requirements.txt
```

A instalação poderá ser realizada através do comando:

```bash
pip install -r requirements.txt
```

A lista final de bibliotecas será definida conforme a implementação dos agentes, ferramentas, RAG e integração com o modelo local.

---

## Estrutura do Projeto

```text
Echoes of the Classics
│
├── agentes/
├── database/
├── knowledge_base/
├── mcp_server/
├── models/
├── rag/
├── tools/
│
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

---

## Instalação

O projeto encontra-se em desenvolvimento. As instruções completas de instalação e execução serão atualizadas conforme a implementação dos componentes do sistema.

Etapas previstas:

1. Clonar o repositório:

```bash
git clone <url-do-repositorio>
```

2. Entrar na pasta do projeto:

```bash
cd echoes-of-the-classics
```

3. Criar e ativar um ambiente virtual Python.

4. Instalar as dependências listadas em `requirements.txt`.

5. Configurar o modelo local através do Ollama.

6. Gerar a base vetorial e os embeddings dos documentos.

7. Executar a aplicação principal.

**Observação:** Os comandos específicos poderão ser alterados durante o desenvolvimento do projeto.

---

## Exemplos de Uso

O usuário pode enviar perguntas, reflexões, situações pessoais ou temas livres para receber respostas inspiradas nos diferentes autores.

Pergunta:

* Estou com medo de tomar uma decisão importante na minha vida.

Resultado esperado:

* Shakespeare responde enfatizando destino, ambição e consequências das escolhas.
* Dostoiévski responde explorando conflito moral, culpa e livre-arbítrio.
* Clarice Lispector responde por meio da introspecção e da busca pela identidade.
* Virginia Woolf responde a partir da subjetividade e das percepções internas.

Pergunta:

* O que significa amar alguém?

Resultado esperado: cada agente apresenta uma interpretação inspirada nos temas e estilos característicos de seu respectivo autor.

Pergunta:

* Como lidar com a sensação de estar perdido?

Resultado esperado: o sistema apresenta quatro perspectivas distintas fundamentadas na base documental e nas características literárias dos autores representados.

---

## Conclusão

O projeto demonstra a aplicação integrada de arquitetura multiagente, modelos locais, MCP, RAG, embeddings e recuperação vetorial para simular diferentes perspectivas literárias sobre um mesmo tema.

Por meio da cooperação entre agentes especializados em William Shakespeare, Fiódor Dostoiévski, Clarice Lispector e Virginia Woolf, o sistema permite ao usuário explorar interpretações distintas para perguntas, reflexões e situações diversas, utilizando contexto recuperado de uma base documental para produzir respostas mais coerentes e fundamentadas.