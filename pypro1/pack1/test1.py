'''

여러줄 주석

'''
from builtins import isinstance, divmod
from future.backports.xmlrpc.client import boolean
from sqlalchemy.sql.expression import false

# 한줄 주석

var1 = '안녕'  # 오브젝트 
print(var1)
var1 = 5; print(var1);

var1 = '변수 선언시 type은 저장되는 자료에 의해 결정됨'
print(var1)

a = 10
b = 20.1
c = b
print(a, b, c)
print('주소출력 :', id(a), id(10), id(b), id(20.1), id(c))

print(a is b , a == b)  # is : 주소 비교, == 값비교
print(b is c , b == c) 

print()
A = 1; a = 2 
print(A, ' ', a)  # 변수 선언시 대소문자 구분

print()
import keyword
print('예약어 : ', keyword.kwlist)  # 키워드 리스트 변수로 선언 x

print('\n진법')
print(10, oct(10), hex(10), bin(10))  # 10 0o12 0xa 0b1010

print('자료형')
print(7, type(7))
print(7.1, type(7.1))
print(7 + 3j, type(7 + 3j))
print(True, type('kbs'))

print((1,), type((1,)))
print([1], type([1]))
print({1}, type({1}))
print({'k:1'}, type({'k':1}))

print(isinstance(a, int))
print(isinstance(a, float))

v1 = 2
v1 = v2 = v3 = 5
print(v2, v2, v3)
print(v1)
print(v2)
* v1, v2, v3 = 1, 2, 3, 4, 5, ;

print(v1)
print(v2)
print(v3)

print('-----연산자---------')

print(5 + 3, 5 - 3 , 5 * 3)

print(5 / 3, 5 // 3 , 5 % 3 , 5 ** 3)
print(divmod(5, 3))  # (1,2)
print()
print(3 + 4 * 5, (3 + 4) * 5)

print('관계연산:' , end=' ')
print(5 > 3, 5 == 3 , not(5 >= 3))
print('문자열 더하기' , end=' ')
print('한' + '국' +'만세')

print('한국' * 20)

print('누적')
a = 10 
a = a + 1
a += 1  # ++ x
print(a)
print(a * -1, -a, - -a)

print('bool 처리 :' , bool(0), bool(0.0), bool(1), bool(True), bool(False))
print('bool 처리 :' , bool(100), bool(-10), bool(None), bool(''), bool([]), bool({}))

print()
print('kbs\tbs')
print('kbs\nbc')
print(r'kbs\tbs')
print(r'kbs\nbc')

print('**' * 20)






      
