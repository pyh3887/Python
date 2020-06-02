# 파일 i/o

import os # os import

try :
    print(os.getcwd())
    
    print('파일 읽기 ')
    #f1 = open(r'C:\work\py_sou\pypro1\pack2\ftest.txt', mode='r', encoding='utf-8')
    f1 = open(r'ftest.txt', mode='r', encoding='utf-8') # mode r :파일 읽기모드
    print(f1)
    print(f1.read())
    f1.close()
    
    print('파일 저장 -----')
    f2 = open('ftest2.txt', mode = 'w' , encoding = 'utf-8') #mode w : 파일을 읽기 및 쓰기모드
    f2.write('kbs\n')
    f2.write('월요일 아침\n')
    f2.close()
    print('저장 성공')
    
    print('파일 추가----')
    f3 = open('ftest2.txt', mode = 'a' , encoding = 'utf-8') # mode a : 파일을 쓰기 모드로 염
    f3.write('sbs\n')
    f3.write('홍길동')
    f3.close()
    print('추가 성공')
    
    print()
    f4 = open('ftest2.txt', mode='r', encoding='utf-8')
    #print(f4.read()) # 모든 파일 읽기
    print('--------------------------')
    #print(f4.readline()) 한행씩 읽기
    print(f4.readlines()) # list type 으로 전체 읽기
    f4.close()

except Exception as e:
    print(e)

print('**' * 20 )
print('with 블럭 사용 -------------')

try:
    #파일 저장
    with open('ftest3.txt', mode='w', encoding = 'utf-8') as ff1:
        ff1.write('파이썬으로 문서 저장\n')
        ff1.write('with 블럭 사용\n')
        ff1.write('close()문을 사용하지 않는다\n')
        
    print()
    #파일 읽기
    
    with open('ftest3.txt', mode = 'r' , encoding = 'utf-8') as ff2:
        print(ff2.read())  
    
        
        
except Exception as err:
    print(err)
    
print('**' * 20)
print('복합 객체(pickle) 저장 및 읽기-------------')   

import pickle

try:
    dicdata = {'tom' : '111-1111' , '길동 ':'222-2222'}
    listdata = ['마우스', '키보드']
    tupledata = (dicdata,listdata) # 복합 개체
    
    with open('hi.dat','wb') as ff3:
        pickle.dump(tupledata,ff3) #picle.dump (타겟 , 파일 오브젝트)
        pickle.dump(listdata,ff3)
    
    print('읽기')
    with open('hi.dat', 'rb') as ff4: #별명주기
        a,b = pickle.load(ff4)
        print(a)
        print(b) 
        c = pickle.load(ff4)
        print(c)
    
    
except Exception as e:
    print(e)