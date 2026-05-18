 Chatbot-Especialista
 Projeto de criação de uma Inteligência artificial focada em uma função especifica
 
  🎮 GameMaster AI - Chatbot Especialista em Games

Este repositório contém o projeto de um Agente Conversacional Inteligente (Chatbot) focado no universo dos jogos eletrônicos, eSports e cultura pop gamer.

 📝 Contexto do Projeto
A indústria de jogos eletrônicos consolidou-se como um dos maiores mercados de entretenimento do mundo. Com milhares de lançamentos anuais espalhados por diversas plataformas (PC, PlayStation, Xbox, Nintendo Switch, Mobile), os jogadores frequentemente enfrentam o desafio da "paralisia de escolha" ou a dificuldade de encontrar informações consolidadas sobre história e curiosidades dos games. 

O GameMaster AI surge como uma solução para esse cenário: um consultor virtual de alta fidelidade que atua como um guia especializado para a comunidade gamer.

 🎯 Objetivo
O principal objetivo deste projeto é construir e documentar um chatbot especialista capaz de:
1. Fornecer recomendações precisas de jogos com base em gêneros e plataformas preferidas do usuário.
2. Responder a dúvidas sobre a história dos videogames, estúdios de desenvolvimento e cenários competitivos (eSports).
3. Manter o escopo estrito de atuação: Ignorar e bloquear de forma educada e temática qualquer tentativa do usuário de desviar o assunto para fora do universo dos jogos (fuga de escopo).

 🔍 Visão Geral da Solução
A aplicação consiste em um script estruturado em Python que se conecta aos modelos de linguagem de larga escala (LLM) da OpenAI (especificamente o modelo `gpt-4o-mini`). O grande diferencial do sistema está na camada de **Engenharia de Prompt** aplicada à função de sistema (*System Role*), que blinda o comportamento da inteligência artificial para que ela aja estritamente sob as regras de negócio definidas, garantindo uma experiência imersiva e focada.

 🏗️ Arquitetura da Solução e Funcionamento

O funcionamento do chatbot segue um fluxo de processamento lógico dividido em três etapas fundamentais: Entrada/Triagem, Processamento de Contexto via LLM e Saída Formatada.

 Fluxo de Funcionamento (Diagrama)

```mermaid
graph TD
    A[Usuário/Jogador] -->|Envia Mensagem| B(Interface do Chatbot)
    B --> C{Validação do Prompt de Sistema}
    C -->|Dentro do Escopo Gamer| D[Processamento na API OpenAI]
    C -->|Fora do Escopo Ex: Receitas| E[Geração Automática do Erro 404]
    D --> F[Resposta Customizada do GameMaster]
    E --> G[Mensagem de Bloqueio Temática]
    F --> H[Exibição na Tela do Usuário]
    G --> H
