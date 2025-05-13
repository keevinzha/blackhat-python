import sys
import socket
import threading

HEX_FILTER = ''.join(
    # printable char length is 3, raplace unprintable char with '.'
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)]
)

def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode()

    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])
        printable = word.translate(HEX_FILTER) # replace unprintable char with '.'
        hexa = ' '.join([f'{ord(c):02X}' for c in word]) # convert words to hex
        hexwidth = length*3
        results.append(f'{i:04x} {hexa:>{hexwidth}} {printable}') # 0000  70 79 74 68 6F 6E 20 72 6F 63 6B 73 20 0A 20 61 python rocks . a
    if show:
        for line in results:
            print(line)
        else:
            return results

def receive_from(connection):
    buffer = b""
    connection.settimeout(5)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except Exception as e:
        pass
    return buffer

def request_handler(buffer):
    # perform packet modifications
    return buffer

def response_handler(buffer):
    # perform packet modifications
    return buffer

def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

    remote_buffer = response_handler(remote_buffer)
    if len(remote_buffer):
        print("[<==] Sending %d bytes to localhost." % len(remote_buffer))
        client_socket.send(remote_buffer)
    



if __name__ == '__main__':
   hexdump('python rocks \n and proxies roll\n')