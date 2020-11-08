import socket
import ssl

s = ssl.wrap_socket(socket.socket())

s.connect(('146.56.228.227', 443))

secret = input("Secret : ")

send_str = 'CONNECT / HTTP/1.1\r\nHost: ustc.edu.cn.gztime.cc:8080\r\nConnection: keep-alive\r\nSecret: ' + secret + '\r\nContent-Length: 0\r\n\r\n'

print('sending...')
s.sendall(send_str.encode('utf-8'))

s.settimeout(0.5)

buffer = []

print('waiting...')

while True:
    try:
        print('.',end='')
        d = s.recv(1024)
        buffer.append(d)
        if d == '\r\n':
            break
    except:
        break

send_str = 'GET http://146.56.228.227:8080/ HTTP/1.1\r\nHost: ustc.edu.cn.gztime.cc:8080\r\nConnection: keep-alive\r\nReferer: 146.56.228.227\r\nSecret: ' + secret + '\r\nContent-Length: 0\r\n\r\n'

s.sendall(send_str.encode('utf-8'))

while True:
    try:
        d = s.recv(1024)
        buffer.append(d)
        if d == '' or d == '\r\n':
            break
    except:
        break

data = b''.join(buffer)

s.close()

print(data.decode('utf-8'))
