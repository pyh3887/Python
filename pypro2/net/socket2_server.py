# echo server - client 요청을 계쏙 처리 

from socket import *
import sys

host = ''
port = 8888

# server 구축

serversock = socket(AF_INET,SOCK_STREAM) #(종류 ,유형)

try : 
    serversock.bind((host,port))
    print('서버 서비스 시작...')
    serversock.listen(5)
    
    while True :
        conn,addr = serversock.accept()
        print('client info : ' , addr[0], addr[1])
        print(conn.recv(1024).decode())   # client 메세지 수신 후 출력
        
        # to client 송신
        conn.send(('from server :' + str(addr[1]) + '너도 잘지내').encode('utf_8'))
        
        
        
        
except socket.error as err:
    print('err:' , err)
    sys.exit()
    
finally:
    serversock.close()
    
    
