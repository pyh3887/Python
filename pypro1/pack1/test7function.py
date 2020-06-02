# 함수 : 실행단위
# 내장함수


print(sum([3,5,7]))
print(int(1.7),float(4),str(5) + '오')
print(round(1.2),round(1.6))

import math
print(math.ceil(1.2),math.ceil(1.6)) # 정수 근사치 중 큰 수 올림
print(math.floor(1.2),math.floor(1.6)) # 정수 근사치 중 작은수 내림

x = [10,20,30]
y = ['a','b']

for i in zip(x,y): 
    print(i)

#...

# 사용자 정의 함수
def DoFunc1():
    print('DoFunc1')
    
DoFunc1()
print(DoFunc1)
kbs = DoFunc1
kbs()

def DoFunc2(a,b):
    print('Do2')
    result = DoFunc3(a,b)
    return result

def DoFunc3(m,n):
    imsi = m + n 
    return imsi

mbc = DoFunc3
print(mbc(5, 6))

print('현재 사용중인 객체 목록:' , globals())

print()
def isOdd(arg):
    return arg % 2 == 1

MyDict = {x:x * x for x in range(11) if isOdd(x)}
print(MyDict)

# 전역 , 지역 변수

player = '전국대표'

def FuncSoceer():
    name = '홍길동'  # local
    player = '지역대표'
    print(name,player)

FuncSoceer()
print(player)

print()

a = 10; b = 20; c = 30

def Good():
    a = 40
    b = 50 
    print('2)a:',a,',b:',b,',c:',c)    
    def Nice():
        
        global c # 전역함수 c가 됌
        nonlocal b #자기를 포함하고 있는 함수의 멤버 변수로 감
        print('3)a:',a,',b:',b,',c:',c)
        c = 60  # err local variable 'c' referenced before assignment
        b = 70
    Nice()
    print('4)a:',a,',b:',b,',c:',c)
Good()
print('n)a:',a,',b:',b,',c:',c)







    






