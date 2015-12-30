#coding=utf-8

__author__ = 'John Wang'

import socket, threading, time

'''
socket 通信测试，服务器端
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1',2345))
s.listen(5)

print('Waiting for connection ...')

def tcplink(sock, addr):
    print('accept a new connection from %s:%s' % addr)
    print('current threading %s.' % threading.current_thread())

    sock.send(b'welcome')

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()



