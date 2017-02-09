#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.bind(('localhost', 1234))

mySocket.listen(5)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    url = str(random.randint(1, 1000000000))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body><p>Hola, <a href='" + url +
                    "'>Dame otra</a></p></body></html>" +
                    "\r\n", 'utf-8'))
    recvSocket.close()
