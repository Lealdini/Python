import socket
import select
import sys
from thread import *

confirm = True
interPort = True
HEADERSIZE = 10

while confirm:
    localhost = input("""
        Olá
        Digite o Localhost, para saber o localhost digite ipconfig no teminal do Windows ou ifconfig em Linux.
        Localhost:""")
    while interPort:
        port = input("""
        Digite a porta: maior ou igual a 3000.
        porta: """)
        try:
            aux = int(port)
            port = aux
            interPort = False
        except ValueError as verr:
            print('\t\033[7;30mFormato errado, apenas numeros inteiros\033[m')
    answer = input("""
        Confirma esses valores:
        localhost {} 
        porta {}
        confirmar s/n: """.format(localhost, port))
    if answer == "s" or answer == "S":
        confirm = False
    else:
        confirm = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((localhost, port))
s.listen(5)
while True:
    clientSocket, address = s.accept()
    print(f"\tConexao com {address} foi estabelecido!")

    d = {1: "Oi", 2: "Pessoa"}
    msg = pickle.dumps(d)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientSocket.send(msg)