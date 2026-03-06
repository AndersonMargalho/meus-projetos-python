# 📊 Conversor de Temperatura
# Autor: Anderson Dos Santos Margalho
# Data: Março 2026

print("=" * 50)
print("📊 CONVERSOR DE TEMPERATURA")
print("=" * 50)

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def celsius_para_kelvin(c):
    return c + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

while True:
    print("\n🔄 ESCOLHA A CONVERSÃO:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Sair")
    print("-" * 50)
    
    opcao = input("\nDigite a opção (1-5): ")
    
    if opcao == "5":
        print("\n👋 Obrigado por usar o Conversor! Até logo!")
        break
    
    try:
        temperatura = float(input("\n🌡️  Digite a temperatura: "))
        
        if opcao == "1":
            resultado = celsius_para_fahrenheit(temperatura)
            print(f"\n✅ {temperatura}°C = {resultado:.2f}°F")
        elif opcao == "2":
            resultado = fahrenheit_para_celsius(temperatura)
            print(f"\n✅ {temperatura}°F = {resultado:.2f}°C")
        elif opcao == "3":
            resultado = celsius_para_kelvin(temperatura)
            print(f"\n✅ {temperatura}°C = {resultado:.2f}K")
        elif opcao == "4":
            resultado = kelvin_para_celsius(temperatura)
            print(f"\n✅ {temperatura}K = {resultado:.2f}°C")
        else:
            print("\n❌ Opção inválida!")
            
    except ValueError:
        print("\n❌ ERRO: Digite apenas números!")