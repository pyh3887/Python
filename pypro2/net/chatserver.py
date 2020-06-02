# 멀티 채팅 서버 - Thread , socket

import socket 
import threading 

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(('192.168.0.80',7777))
ss.listen(5)

print('채팅 서버 서비스중 ...')

users = []

def ChatUser(conn):
    name = conn.recv(1024)
    data = '^^' + name.decode('utf-8') + '님 입장 ^^;'
    print(data)
    try:
        for p in users: 
            p.send(data.encode('utf-8'))
        
        while True:
            msg = conn.recv(1024)
            data = name.decode('utf-8') + '님 메세지:' + msg.decode('utf-8')
            print('서버도 메세지 보기 :', data)
            
            for p in users:
                    p.send(data.encode('utf-8'))
    except: 
        users.remove(conn)
        data = '~~ ' + name.decode('utf-8') + '님 퇴장~~'
        print('서버도 보기:' , data)
        if users:
            for p in users:
                    p.send(data.encode('utf-8'))
        else:
            print('서버 종료')
                   

while True:
    conn,addr = ss.accept();
    users.append(conn)
    th = threading.Thread(target=ChatUser,args = (conn,))
    th.start()