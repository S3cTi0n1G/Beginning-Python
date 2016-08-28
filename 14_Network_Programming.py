#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('abc.xyz', 80))
# 参数是一个tuple

s.send('GET/HTTP/1.1\r\nHost:abc.xyz\r\nConnection:close\r\n\r\n')

buffer = []

while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

s.close()

header, html = data.split('\r\n\r\n', 1)

print header

with open('google.html', 'wb') as f:
    f.write(html)
'''

'''
import socket

s = socket.socket()

host = socket.gethostname()
port = 9999
# linux 系统中，需要admin 权限才能使用1024 以下的port
s.bind((host, port))

s.listen(5)
# 操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
print 'Waiting for connection...'

while True:
    c, addr = s.accept()
    t = threading.Thread(target = tcplinlk, args = (sock, addr))
    t.start()
    print 'Accept new connection from %s:%s...' % addr
    c.send('Thank you for Connecting')
    c.close()
'''
