# -*- encoding: utf-8 -*-
'''
@File    :   3.1_tcp_server.py
@Time    :   2025/05/12 21:22:22
@Author  :   keevinzha
'''

import socket
import threading

# you use 2.1_tcp_client as client, just change ip and port to the same as below
IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5) # 5 is the maximum number of connections
    print(f'[*] Listening on {IP}:{PORT}')
    
    while True:
        client, address = server.accept() # wait for connection
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,)) # create a thread to handle connection
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()