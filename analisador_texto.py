# 📝 Analisador de Texto em Python
# Autor: Anderson Dos Santos Margalho
# Data: Março 2026

print("=" * 50)
print("📝 ANALISADOR DE TEXTO")
print("=" * 50)

texto = input("\n📄 Digite ou cole seu texto abaixo:\n\n")

print("\n" + "=" * 50)
print("📊 RESULTADOS DA ANÁLISE:")
print("=" * 50)

# Contagens básicas
caracteres = len(texto)
caracteres_sem_espaco = len(texto.replace(" ", ""))
palavras = len(texto.split())
frases = texto.count('.') + texto.count('!') + texto.count('?')
paragrafos = texto.count('\n') + 1

# Análise de letras
vogais = sum(1 for c in texto.lower() if c in 'aeiouáéíóúãõâêîôû')
consoantes = sum(1 for c in texto.lower() if c in 'bcdfghjklmnpqrstvwxyzç')

# Palavra mais longa
palavras_lista = texto.split()
if palavras_lista:
    palavra_mais_longa = max(palavras_lista, key=len)
else:
    palavra_mais_longa = "Nenhuma"

# Exibe resultados
print(f"""
📏 CARACTERES:
   • Total: {caracteres}
   • Sem espaços: {caracteres_sem_espaco}

📝 PALAVRAS:
   • Total: {palavras}
   • Mais longa: "{palavra_mais_longa}" ({len(palavra_mais_longa)} letras)

📄 ESTRUTURA:
   • Frases: {frases}
   • Parágrafo(s): {paragrafos}

🔤 LETRAS:
   • Vogais: {vogais}
   • Consoantes: {consoantes}
""")

print("=" * 50)