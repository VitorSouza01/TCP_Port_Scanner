# Bibliotecas
import argparse
import socket

# Título
print("[TCP Port Scanner]\n")

# Menu das ferramentas e argumentos
parser = argparse.ArgumentParser(description="Port scanner tcp")
parser.add_argument("-i", "--ip", help="Alvo IPv4", required=True)
parser.add_argument("-s", "--start", help="Starting port", type=int, required=True)
parser.add_argument("-e", "--end", help="Ending port", type=int, required=True)
args = parser.parse_args()

# Variáveis
target = args.ip
start_port = args.start
end_port = args.end

# Socket para conexão com a porta
for port in range(start_port, end_port+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    # Conexão com a porta
    try:
        s.connect((target, port))
        print(f"A porta [{port}] está aberta!")
        banner = s.recv(1024)

        # Verificação da porta
        if banner:
            print(f"Serviço: [{banner.decode().strip()}]")
        s.close()

    except:
        pass
