# 정규표현식

import re 


ss = '1234 abc 가나다ABC_555_6 a b 123 nbc'
print(ss)
print(re.findall(r'123',ss,)) #패턴을 줄시 r 빼지 말기
print(re.findall(r'[0-9]',ss))
print(re.findall(r'\d',ss))

print(re.findall(r'[0-9]+',ss))
print(re.findall(r'[0-9]{2}',ss))
print(re.findall(r'\d{2}',ss))
print(re.findall(r'[0-9]{2,3}',ss))

print('---' * 10)
print(re.findall(r'.bc',ss))
print(re.findall(r'^1+',ss)) # 첫글자가 1
print(re.findall(r'[^1]+',ss)) # 첫글자가 1 이 아님
print(re.findall(r'[^0-9]+',ss)) # 숫자아닌
print(re.findall(r'nbc$',ss))

a = re.match(r'123',ss)
print(a)
print(a.group())


