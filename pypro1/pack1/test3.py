# Tuple : 리스트와 유사 . 읽기전용
#t = ('a','b','c','a')

t = 'a','b','c','a'
print(t, ' ', t.count('a'), ' ', t.index('b'))
print(t[0])
#t[0] = 'm'
q = list(t)
q[0] = 'm'
t = tuple(q)
print(t)

t1 = (1,2)
print(t1)

a,b = t1
b,a = a,b 
t1 = a,b
print(t1)
kk = (1)
print(kk, type(kk))




print('--Set(순서x, 중복x)-----')
a = {1,2,3,1}
print(a)
b = {3,4}
print(a.union(b))
print(a.intersection(b))
print(a-b, a|b, a&b)
#print(a[0])
b.add(5)
print(b)
b.update({6,7})
b.update((8,9))
b.update([10,11])
print(b)

b.discard(7)
b.remove(6)
b.discard(7)
#b.remove(6)
print(b)
b.clear
print(b)

li = [1,2,1,2]
s = set(li)
li = list(s)
print(li)

print('-----------Dict(key:value) --------------') # key value (json용이)

mydic = dict(k1=1, k2='mbc' ,k3=1.2)
print(mydic)

dic = {'파이썬' : '뱀' , '자바':'커피','스프링':'용수철'}
print(dic,' ', len(dic))
print(dic['자바'])
#print(dic[0]) err

dic['오라클'] = '예언자'
print(dic)
del dic['오라클']
print(dic)
dic['자바'] = 'programing lan'
print(dic)
print(dic['자바'])
print(dic.keys())
print(dic.values())
print(dic.get('자바'))


print('d' ,)









