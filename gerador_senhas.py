# 🔐 Gerador de Senhas Seguras
# Autor: Anderson Dos Santos Margalho
# Data: Março 2026

import random
import string

print("=" * 50)
print("🔐 GERADOR DE SENHAS SEGURAS")
print("=" * 50)

def gerar_senha(tamanho, usar_letras=True, usar_numeros=True, usar_simbolos=True):
    """Gera uma senha aleatória segura"""
    
    caracteres = ""
    
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        return "Erro: Selecione pelo menos um tipo de caractere!"
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("\n⚙️  CONFIGURAÇÕES DA SENHA:")
print("-" * 50)

try:
    tamanho = int(input("\n📏 Tamanho da senha (8-50): "))
    
    if tamanho < 8:
        print("⚠️  Senhas menores que 8 caracteres são inseguras!")
        confirmacao = input("Deseja continuar mesmo assim? (s/n): ")
        if confirmacao.lower() != 's':
            tamanho = 12
            print(f"✅ Tamanho ajustado para {tamanho} caracteres.")
    elif tamanho > 50:
        tamanho = 50
        print("✅ Tamanho máximo é 50 caracteres.")
    
    print("\n🔤 TIPOS DE CARACTERES:")
    usar_letras = input("Incluir letras? (s/n): ").lower() == 's'
    usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
    usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
    
    print("\n" + "=" * 50)
    print("🔑 SUAS SENHAS GERADAS:")
    print("=" * 50)
    
    for i in range(3):
        senha = gerar_senha(tamanho, usar_letras, usar_numeros, usar_simbolos)
        print(f"\nOpção {i+1}: {senha}")
    
    print("\n" + "=" * 50)
    print("💡 DICA: Use uma senha diferente para cada serviço!")
    print("=" * 50)
    
except ValueError:
    print("❌ ERRO: Digite apenas números para o tamanho!")