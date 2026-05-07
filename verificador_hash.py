import hashlib

def gerar_hash_arquivo(caminho_arquivo):
    """Gera o hash SHA-256 de um arquivo para verificar sua integridade."""
    sha256_hash = hashlib.sha256()
    
    try:
        with open(caminho_arquivo, "rb") as f:
            # Lê o arquivo em pedaços (buffer) para não travar a memória
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "Arquivo não encontrado."

# Exemplo de uso
arquivo = input("Digite o nome/caminho do arquivo: ")
hash_resultado = gerar_hash_arquivo(arquivo)
print(f"O Hash SHA-256 do arquivo é: {hash_resultado}")
