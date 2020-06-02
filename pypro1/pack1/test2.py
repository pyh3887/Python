# 집합 자료형 : String , List , Tuple , Set, Dict



# String : 문자열 취급 (순서형) , 변경 불가

s = 'sequence'
print(len(s))
print(s.count('e'))
print(s.find('e') , ' ' , s.find('e',3) , s.rfind('e')) 
print(s.startswith('s'))

ss = 'mbc'
print('mbc', id(ss))

ss = 'abc'
print('abc', id(ss))

# 슬라이싱

print(s[0], ' ', s[2:4], ' ', s[:3], ' ' , s[3:])
print(s[-1], ' ', s[-4:-1], ' ', s[-4:], ' ', s[::2]) # ::2 증가치가 2이다

#s[0] = 'k' # err

ss = 'kbs mbc'
ss2 = ss.split(sep= ' ')
print(ss2)
print(' ' .join(ss2))

print('\n---List(배열과 유사, 순서있다 , 변경가능 , 여러종류의 자료 ㅎ어용------------)')

a = [1 , 2 , 3]
b = [10, a , 12.3 , True ,'kbs']
print(a , ' ' , id(a))
print(b , ' ' , id(b))

print(b[0], ' ' , b[1] , ' ' , b[1][2])
b[0] = 'mbc'
print(b[0])
b.remove('kbs') # 값으로 삭제
print(b)
del b[3]       #순서로 삭제
print(b)

family = ['엄마' , '아빠' , '나']
family.append('동생')
print(family, len(family) , family[0])
family.remove('나')
family.insert(0,'할아버지')
family.extend(['삼촌','고모','이모'])
family += {'아주머니' , ' 아저씨'}
print(family,len(family), family[0])
print()
li = [[0,1,2],[3,4,5]]
print(li[0])
print(li[0][0])
print()

name = ['tom', 'james' , 'oscar']
name2 = name 
print(name, ' ' , name2)
name[0] = 'sujan'
name2[1] = 'john'
print(name, ' ', name2)

import copy
name3 = copy.deepcopy(name) # 새로운 객체의 주소 기억
print(name, ' ', name3)
name[0] = '길동'
print(name, ' ' , name3)

print('stack 과 queue ---------')
sbs = [1,2,3]
sbs.append(4)
print(sbs)
sbs.pop()
print(sbs)
sbs.pop()
print(sbs)




























