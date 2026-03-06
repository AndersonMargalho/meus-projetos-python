# 🧮 Calculadora Simples em Python
# Autor: Anderson Dos Santos Margalho
# Data: Março 2026

print("=" * 40)
print("🧮 CALCULADORA SIMPLES EM PYTHON")
print("=" * 40)

# Pede os números ao usuário
numero1 = float(input("\nDigite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Mostra as opções de operação
print("\n" + "=" * 40)
print("ESCOLHA A OPERAÇÃO:")
print("=" * 40)
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (×)")
print("4. Divisão (÷)")
print("=" * 40)

operacao = input("\nDigite o número da operação (1-4): ")

# Realiza o cálculo
if operacao == "1":
    resultado = numero1 + numero2
    simbolo = "+"
elif operacao == "2":
    resultado = numero1 - numero2
    simbolo = "-"
elif operacao == "3":
    resultado = numero1 * numero2
    simbolo = "×"
elif operacao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        simbolo = "÷"
    else:
        print("\n❌ ERRO: Não é possível dividir por zero!")
        resultado = None
else:
    print("\n❌ ERRO: Operação inválida!")
    resultado = None

# Mostra o resultado
if resultado is not None:
    print("\n" + "=" * 40)
    print(f"RESULTADO: {numero1} {simbolo} {numero2} = {resultado}")
    print("=" * 40)