# --- SOCKETS RESEAU : SERVEUR ---

# socket
#    bind (ip, port) 127.0.0.1 -> localhost
#    listen
#    accept -> socket / (ip, port)
#    close

import socket

MAX_DATA_SIZE = 1024

HOST_IP = "127.0.0.1"
HOST_PORT = 32000

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print("Attente de connexion sur {HOST_IP}, port {HOST_PORT}")
connection_socket, client_address = s.accept()
print(f"Connexion acceptée de {client_address}")

while True:
    texte_envoye = input("Vous :")
    connection_socket.sendall(texte_envoye.encode())
    data_recu =connection_socket.recv(MAX_DATA_SIZE)
    if not data_recu:
        break
    print("Message : ", data_recu.decode())


s.close()
connection_socket.close()