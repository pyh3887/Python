# socket 통신 확인

import socket

print(socket.getservbyname('http', 'tcp'))
print(socket.getservbyname('telnet', 'tcp'))
print(socket.getservbyname('ftp', 'tcp'))


print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP)) # socket 서버 정상 작동

