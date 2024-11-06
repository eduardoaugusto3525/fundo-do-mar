import random
import time

print("🐠 Bem-vindo ao jogo 'No Fundo do Mar'! 🐟")
print("Seu objetivo é sobreviver e evitar os obstáculos.\n")

# Configuração inicial do jogo
vida = 3
pontuacao = 0

# Loop do jogo
while vida > 0:
    print("\nVocê está nadando no fundo do mar...")
    time.sleep(1)  # Pausa para criar suspense
    
    # Gera um evento aleatório: 1 = obstáculo, 2 = peixe menor para capturar, 3 = nada acontece
    evento = random.randint(1, 3)
    
    if evento == 1:
        print("Oh não! Um obstáculo apareceu à sua frente! 🌊")
        acao = input("Digite 'd' para desviar ou 'e' para enfrentar: ").lower()
        
        if acao == 'd':
            print("Você desviou com sucesso! 🏊‍♂️")
        elif acao == 'e':
            print("Você tentou enfrentar o obstáculo e perdeu uma vida.")
            vida -= 1
        else:
            print("Escolha inválida! Você hesitou e perdeu uma vida.")
            vida -= 1
    elif evento == 2:
        print("Você encontrou um peixe menor! 🐟")
        acao = input("Digite 'c' para capturar ou 'i' para ignorar: ").lower()
        
        if acao == 'c':
            print("Você capturou o peixe e ganhou pontos! 🎉")
            pontuacao += 10
        elif acao == 'i':
            print("Você ignorou o peixe e continuou nadando.")
        else:
            print("Escolha inválida! Você perdeu a chance de capturar o peixe.")
    else:
        print("Nada de especial aconteceu, continue nadando... 🌊")
    
    # Exibe a pontuação e a vida restantes
    print(f"\nPontuação: {pontuacao} | Vidas restantes: {vida}")
    time.sleep(1)

# Mensagem de fim de jogo
print("\nSuas vidas acabaram! O jogo terminou.")
print(f"Pontuação final: {pontuacao}")
