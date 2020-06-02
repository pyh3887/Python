# for target in object:
 
for i in [1, 2, 3, 4, 5]:  # 집합형 자료가 순서대로 빠져나옴
    print(i, end=' ')

print()

# colors = {'r', 'g' , 'b'}
# colors = ['r', 'g' , 'b']
colors = ('r', 'g' , 'b')
for c in colors:
    print(c, end=' ')

print()    

soft = {'java' : '웹용언어', 'python': '접착언어', 'c' : '시스템개발용'}

for i in soft.items():
    # print(i)
    print(i[0], ' ', i[1])  # key value 출력

print()

for k in soft.keys():
    # print(i)
    print(k)  # key값출력

print()

for k in soft.values():
    # print(i)
    print(k)  # value값 출력

print()

for n in [2, 3]:
    print('--{}단'.format(n))
    for i in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        print('{0}*{1}={2}'.format(n, i, n * i))  # 2, 3 단 찍기

print()

li = ['a', 'b', 'c']
for ind, d in enumerate(li):
    print(ind, ' ', d)

print()
datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 3 :
        # continue
        break
    print(i, end=' ')
else: 
    print('정상 종료일 때 처리')

print()

print('------------문자열 검색후 단어수 출력---------------------')

import re

ss = '''생활 속 거리 두기 첫날인 6일 신종 코로나바이러스 감염증(코로나19) 확진 환자가 4명 늘어 총 1만810명이 됐다. 최근 3일간 없었던 지역사회 감염 환자가 나흘 만에 나왔다.

질병관리본부 중앙방역대책본부(방대본)는 7일 오전 0시 기준 국내 코로나19 누적 확진자가 1만810명이라고 밝혔다. 확진자 가운데 사망자는 1명 늘어 총 256명, 격리 해제된 완치자는 86명 증가한 총 9419명이다.
생활 속 생활 속 생활 속 확진자 가운데 확진자 가운데 확진자 가운데
'''

print(ss)

ss2 = re.sub(r'[^가-힣\s]', '', ss)  # \s 
print(ss2) 

ss3 = ss2.split(' ')  # 공백 자르기
print(ss3)
print(len(ss3)) 
sdata = set(ss3)  # 중복 제거
print(len(sdata))

cou = {}  # 단어의 발생 횟수를 dict type 으로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1

print(cou)

print('-- dict 자료로 과일값 출력 ----')
price = {'사과':500, '수박':12000, '참외':600}

my = {'사과':2, '수박':1}
bill = sum(price[f] * my[f] for f in my)
print('총 구매 가격 : {}원'.format(bill))

print()
datas = [1,2,'a',True,3]
li = [i * i for i in datas if type(i) == int]
print(li)

datas = {1,1,2,2,3}
se = {i* i for i in datas}
print(se)

id_name = {1:'tom', 2 :'james'}
name_id = {val:key for key,val in id_name.items()} #key value 순서바꾸기
print(name_id)

print()
temp = [1,2,3]
for i in temp:
    print(i, end = ' ')
print()
print([i for i in temp])
print({i for i in temp})
#print((i for i in temp)) # 튜플은 오브젝출력
temp2 = list()
for i in temp:
    temp2.append(i)
print(temp2)

temp3 = [i+10 for i in temp]
print(temp3)

print()
aa = [(1,2),(3,4),(5,6)]
for a, b in aa:
    print(a+b)
    
    
print('--------------------')
print(list(range(1,6)))
print(tuple(range(1,6)))
print(set(range(1,6)))


for i in range(6):
    print(i,end = ' ')
    
print()
for i in range(2,10):
    for j in range(1,10):
        print('{} * {} = '.format(i,j,i*j), end= ' ')
        print()
    
    
    
    
    
    
    
    
    
    



    
    
    
    





