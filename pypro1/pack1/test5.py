# 제어문
# if 
var = 10
if var >= 3:
    print('크구나')
    print('참일 때')
    if var > 5:
        print('5 초과')
else:
    print('거짓')

print('계속1')

jumsu = 80
#jumsu = int(input('점수: ')) ## 키보드로 값을 받는 방법
if jumsu >= 90:
    print('우수')
elif jumsu >= 70:
    print('보통')
else:
    print('부족')
    
if 90 <= jumsu <= 100:
    res = 'a'
elif 70 <= jumsu < 90:
    res = 'b'
else:
    res = 'c'
    
print(res)

names = ['홍길동', '신기해', '이기자']
if '고길동' in names:
    print('친구 이름')
else:
    print('누구야')
    
a = 'kbs'
b = 9 if a == 'kbs' else 11
print(b)

a = 11
b = 'mbc' if a == 9 else 'kbs'
print(b)

print()
a = 6
re = a * 2 if a > 5 else a + 2
print(re)

a = 7
print((a + 2 , a * 2 )[a > 5]) # a>5 가 참이기 때문에 0이아닌 1번째를 실행함

# while

a = 1

while a <= 5:
    print(a, end = ' ')
    a += 1


colors = ['r' , 'g' , 'b']

a = 0 
while a < len(colors):
    print(colors[a], end = ' ')
    a += 1

print()
while colors : 
    print(colors.pop(), end = ' ')
    
print()    

#===============================================================================
# 
# import time
# sw = input('폭탄 스위치를 누를까요(y/n)')
# if sw == 'Y' or sw == 'y':
#     count = 5
#     while 1 <= count:
#         print('%d초 남았습니다'%count)
#         time.sleep(1)
#         count -= 1
#     print('폭발 !!')
# elif sw == 'N' or 'n':
#     print('취소')
# else:
#     print('y 또는 n을 누르시오')
#===============================================================================
   
    
a = 0 
while a < 10:
    a += 1
    if a == 5 :continue
    if a == 7 :break
    print(a)
else:
    print('while 수행')   # while 문에 else를 붙힐수 있음
    

import random
num = random.randint(1,10)  # 1 부터 10 까지 난수 발생
#print(num)
#while True:
while 1:  #숫자 1 을 넣을시 true 이므로 무한루프
    print('1 ~ 10 사이의 컴이 가진 숫자를 입력하시오')
    guess = input()
    su = int(guess)
    if su == num:
        print('성공~~' * 5)
        break
    elif su < num :
        print('더 큰 수 입력 ')
    elif su > num :
        print('더 작은 수 입력')












    
    
 










