import socket
import pickle

HOST = '192.168.0.103'  # The server's hostname or IP address
PORT = 3000      # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

HEADERSIZE = 10
while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"Novo tamanho de mensagem: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg
        if len(full_msg) - HEADERSIZE == msglen:
            print("Recebemos uma nova mensagem")
            print(full_msg[HEADERSIZE:])
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            new_msg = True
            full_msg = b''

    print(full_msg)