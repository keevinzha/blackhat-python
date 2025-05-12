# -*- encoding: utf-8 -*-
'''
@File    :   2.2_udp_client.py
@Time    :   2025/05/12 21:22:11
@Author  :   keevinzha
'''

import socket

target_host = "127.0.0.1"
target_port = 9997

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_DGRAM stand for UDP
# send some data
client.sendto(b"AAABBBCCC", (target_host, target_port))
# receive some data
data, addr = client.recvfrom(4096) # this script may stuck here, don't worry

print(data.decode())
client.close()