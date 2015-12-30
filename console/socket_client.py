#coding=utf-8

__author__ = 'John Wang'

import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 2345))

print(s.recv(1024).decode('utf-8'))

for data in [b'john', b'huahua', b'namei',b'john_2', b'huahua_2', b'namei_2']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
    time.sleep(2)

s.send(b'exit')
s.close()
