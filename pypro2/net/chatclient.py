# 채팅 사용자

import socket
import threading
import sys

def Handle(socket):
    while True : 
        data = socket.recv(1024)
        if not data:continue  #데이터 없을시
        print(data.decode('utf-8'))
        

sys.stdout.flush()

name = input('채팅 아이디 입력:')
cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.connect(('192.168.0.80',7777))
cs.send(name.encode('utf-8')) #대화명 전송

th = threading.Thread(target = Handle, args = (cs,))
th.start()

while True : 
    msg = input(">")
    sys.stdout.flush()
    
    if not msg:continue  #데이터 없을시
    cs.send(msg.encode('utf-8'))

cs.close()