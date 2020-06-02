# echo server - clinet 의 요청을 1회만 수행

from socket import * 

# server 구축
serversock = socket(AF_INET, SOCK_STREAM) # 종류 , 유형
serversock.bind(('192.168.0.80',9999))
serversock.listen(1) # 1 ~ 5
print('server start...')

conn, addr = serversock.accept() # 연결 대기
print('client addr:', addr)
print('from client msg : ', conn.recv(1024).decode())
conn.close()
serversock.close()