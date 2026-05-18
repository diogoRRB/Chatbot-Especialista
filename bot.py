import os
from openai import OpenAI

# Coloque sua chave da OpenAI aqui entre as aspas para o bot funcionar
MINHA_CHAVE_OPENAI = "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" 

# Configuração da conexão com a API
api_key = MINHA_CHAVE_OPENAI or os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Personalidade do GameMaster AI (System Prompt)
PROMPT_ESPECIALISTA_GAMES = """
Você é o "GameMaster AI", um chatbot especialista em jogos eletrônicos (videogames), eSports e história dos jogos.
Seu tom de voz deve ser empolgado, nerd e amigável.

Regras estritas:
1. Você só responde sobre jogos eletrônicos e o universo gamer.
2. Se o usuário perguntar algo fora desse universo, responda: "⚠️ ERRO 404: Comando não encontrado! Eu só sei falar sobre games."
3. Sempre indique a plataforma e o gênero ao recomendar um jogo.
"""

def responder_usuario(pergunta_do_jogador):
    if not api_key:
        return "❌ ERRO: Você esqueceu de colocar sua OPENAI_API_KEY na variável 'MINHA_CHAVE_OPENAI'!"
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": PROMPT_ESPECIALISTA_GAMES},
                {"role": "user", "content": pergunta_do_jogador}
            ]
        )
        return resposta.choices[0].message.content
    except Exception as e:
        return f"Erro ao conectar com o servidor do jogo: {e}"

# --- LOOP DE INTERAÇÃO EM TEMPO REAL ---
print("🤖 [GameMaster AI]: Conexão estabelecida! Pronto para o Player 1.")
print("(Digite 'sair' a qualquer momento para encerrar a partida)\n")

while True:
    # Cria uma caixa de texto no Colab para você digitar em tempo real
    pergunta_usuario = input("Você (Jogador 1): ")
    
    # Se você digitar 'sair', o programa encerra
    if pergunta_usuario.lower() == 'sair':
        print("\n🤖 [GameMaster AI]: Game Over! Obrigado por jogar.")
        break
        
    # Se você não digitar nada, ele pede para digitar novamente
    if not pergunta_usuario.strip():
        continue
        
    # Envia o que você digitou para a IA e mostra a resposta na tela
    resposta_bot = responder_usuario(pergunta_usuario)
    print(f"GameMaster AI: {resposta_bot}")
    print("-" * 50) # Linha para separar as mensagens
