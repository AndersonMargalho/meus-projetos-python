import socket

def scan_portas(ip_alvo, portas):
    """Tenta se conectar a portas específicas de um IP para ver se estão abertas."""
    print(f"Escaneando o alvo: {ip_alvo}\n")
    
    for porta in portas:
        # Cria um objeto socket (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Tempo máximo de espera
        
        resultado = s.connect_ex((ip_alvo, porta))
        if resultado == 0:
            print(f"Porta {porta}: ABERTA ✅")
        s.close()

# Exemplo: Escanear portas comuns no próprio computador (localhost)
alvo = "127.0.0.1"
portas_comuns = [21, 22, 80, 443, 8080]
scan_portas(alvo, portas_comuns)