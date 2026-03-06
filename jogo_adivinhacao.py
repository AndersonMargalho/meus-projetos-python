# 🎲 Jogo de Adivinhar Número
# Autor: Anderson Dos Santos Margalho
# Data: Março 2026

import random

print("=" * 50)
print("🎲 JOGO DE ADIVINHAR O NÚMERO")
print("=" * 50)

print("\n📜 REGRAS DO JOGO:")
print("- Vou pensar em um número entre 1 e 100")
print("- Você tenta adivinhar qual é")
print("- Eu te digo se é MAIOR ou MENOR")
print("- Tente acertar em menos tentativas possível!")
print("=" * 50)

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("\n✅ Pronto! Já pensei em um número entre 1 e 100.")
print("\n" + "-" * 50)

while not acertou:
    try:
        palpite = int(input("\n🤔 Seu palpite: "))
        tentativas += 1
        
        if palpite < 1 or palpite > 100:
            print("⚠️  Digite um número entre 1 e 100!")
            tentativas -= 1
        elif palpite < numero_secreto:
            print("📈 MAIS ALTO! Tente um número maior.")
        elif palpite > numero_secreto:
            print("📉 MAIS BAIXO! Tente um número menor.")
        else:
            acertou = True
            print("\n" + "=" * 50)
            print(f"🎉 PARABÉNS! Você acertou!")
            print(f"📊 Número secreto: {numero_secreto}")
            print(f"📊 Tentativas: {tentativas}")
            
            if tentativas <= 5:
                print("🏆 Desempenho: EXCELENTE!")
            elif tentativas <= 10:
                print("🥇 Desempenho: MUITO BOM!")
            else:
                print("📚 Desempenho: PODE MELHORAR!")
            print("=" * 50)
            
    except ValueError:
        print("⚠️  Por favor, digite apenas números!")

print("\nObrigado por jogar! 🎮")