# client side

from socket import * 

clientsocket = socket(AF_INET,SOCK_STREAM)

clientsocket.connect(('192.168.0.24',8888)) # server 와 연결

clientsocket.sendall('안녕 반가워 하하'.encode(encoding='utf_8',errors='strict')) # 송신

re_msg = clientsocket.recv(1024).decode()
print('수신 자료 :' + re_msg)

clientsocket.close()