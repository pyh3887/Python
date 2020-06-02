# 함수 계속
# 인수 키워드 매핑
from sympy.physics.units import amount
from builtins import filter


def ShowGugu(start, end = 5 ):
    for dan in range(start, end + 1 ):
        print(str(dan) + '단 출력')

ShowGugu(2,3)
print()
ShowGugu(3)
print()
ShowGugu(start=2, end=4)
print()        

print('\n가변 인수')
def func1(*ar): # 아규 먼트 갯수를 받을수있음 
    print(ar)
    for i in ar:
        print('음식:' + i)
func1('비빔밥','공기밥')

print()

def func3(a,b,*v1,**v2): # * 튜플 ** 딕셔너리
    print(a,b)
    print(v1)
    print(v2)
    
func3(1,2)
print()
func3(1,2,3,4,5)
print()
func3(1,2,3,4,5,m=6,n=7)
print('------------')


# closure (클로저)
def out():
    count = 0 
    def inn():
        nonlocal count
        count += 1 
        return count
    print(inn())
    
out()
out()

print()

def outer():
    count = 0 
    def inner():
        nonlocal count
        count += 1 
        return count
    return inner # 클로저

add1 = outer() 
print(add1())
print(add1())
print(add1())

add2 = outer()
print(add2())
print(add2())

print("수량 * 단가 *세금 걸과 출력-----------")
def outer2(tax):
    def inner2 (su,dan):
        amount = su *  dan * tax
        return amount
        return inner2
    


print('^^^ 일급함수 (함수 안에 함수 , 인자로 함수전달 , 변환값이 함수)^^^^')

def fun1(a,b):
    return a+ b 
fun2 = fun1
print(fun2(3, 4))

print()

def fun3(func):
    def fun4(): #함수 안에 함수
        print('난 내부 함수')
    fun4()
    return func # 반환값이 함수
mbc = fun3(fun1)
print(mbc(3,4))    
    
print('-- lamda 함수 -----------')     
def Hap(x,y):
    return x + y

print(Hap(1, 2))



print((lambda x,y : x + y)(1,2))

aa = lambda x , y : x + y
print(aa(1,2))
print(aa(3,4))

kbs = lambda a, su = 10: a + su
print(kbs(5))
print(kbs(5,6))

sbs = lambda a, *tu, **di:print(a,tu,di)
sbs(1,2,3,m=4,n=5)

li = [lambda a, b: a+b , lambda a,b:a*b]
print(li[0](3,4))
print(li[1](3,4))

# 다른 함수에서 람다 사용
print(list(filter(lambda a:a<5,range(10)))) # filter 내장함수에서 lambda 사용
print(list(filter(lambda a:a % 2, range(10))))

print('--함수 장식자------')

def make2(fn):
    return lambda: '안녕' + fn()

def make1(fn):
    return lambda: '반가워' + fn()

def hello():
    return '홍길동'

hi = make2(make1(hello))
print(hi())

print()
@make2
@make1
def hello2():
    return '신기해'
print(hello2())

print('---------')

hi2 = hello2()
print(hi2)
h13 = hello2
print(h13)

print('-- 재귀 함수(함수 자신을 호출 : 반복처리 효과적) ----')
def CountDown(n):
    if n == 0:
        print('완료')
    else:
        print(n, end = ' ')
        CountDown(n - 1) # <=== 자신을 부름

CountDown(5)

print()
def tot(n):
    if n == 1:
        print('탈출')
        return 1 
    return n + tot(n-1)
result = tot(10)
print('합은' + str(result))

print() # 5!
def fact(a):
    if a == 1: return 1
    print(a)
    return a * fact(a - 1)

result2 = fact(5)
print('5! : ' + str(result2))
print(5 * 4 * 3 * 2 * 1)












    
        







