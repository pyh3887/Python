# module : 코드의 재 사용을 가능하게 하며 , 하나의 이름 공간으로 별도 관리가 가능하다.
# module 은 package 내에서 작성해야 한다.


print('뭔가를 하다가...')
a = 10 
print(a)
def aa():
    pass

import sys # 표준 모듈 읽기
print(sys.path)
#sys.exit()
print('종료')

import math
print(math.pi)
print(math.sin(math.radians(30)))

print()
import calendar
calendar.setfirstweekday(6) #일요일 먼저
calendar.prmonth(2020,5)

print('--난수 출력---')
import random
print(random.random())
print(random.randrange(1,10)) 

from random import random,randrange # from 모둘명 import 멤버명
print(random())
print(randrange(1,10))

from random import *  #랜덤 모듈의 모든 멤버를 갖다씀

