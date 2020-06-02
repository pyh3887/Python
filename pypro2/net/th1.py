# process : 실행 중인 응용프로그램으로 자신 만의 메모리를 확보해

# 다른 process와 메모리 공유를 하지 않는다 .

from subprocess import * 

#Popen("C:\\Windows\\System32\\calc.exe")
#Popen(['ping','www.google.co.kr'])


#call("C:\\Windows\\System32\\calc.exe")
#Popen("C:\\Windows\\System32\\calc.exe")

# thread : Light weight process 라고 할수 있다.
# process와 달리 같은 process 내에서 메소드/함수 자원을 공유 할수 있다.

import threading
import time

def run(id):
    for i in range(1,11):
        print('id:{} --> {}'.format(id, i))
        time.sleep(0.3)
        
# thread 를 사용하지 않는 경우 
#run('일')
#run('둘')

# thread 를 사용한 경우 :
'''
th1 = threading.Thread(target=run, args = ('일'))
th2 = threading.Thread(target=run, args = ('둘'))

th1.start()  
th2.start()

th1.join() # join thread 종료후 메인 메소드 실행 
th2.join() 
'''

# thread 를 사용한 경우 (반복문)
ths = []
for i in range(2) :
    th = threading.Thread(target=run, args=(i,))
    th.start()
    ths.append(th)
    
for th in ths:
    th.join()
    
        
print('프로그램 종료')




