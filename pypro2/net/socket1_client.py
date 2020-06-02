# client side

from socket import * 

clientsocket = socket(AF_INET,SOCK_STREAM)

clientsocket.connect(('192.168.0.80',9999)) # server 와 연결

clientsocket.sendall('안녕 반가워'.encode(encoding='utf_8',errors='strict'))

clientsocket.close()