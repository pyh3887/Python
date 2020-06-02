# 사용자 정으 ㅣ모듈 연습

print('이런저런 작업을 하다가...')

print(dir)

import pack1.mymod1
print(dir(pack1.mymod1))

list1 = [1,2]
list2 = [3,4,5]

pack1.mymod1.ListHap(list1, list2)


# 여러 모듈 중 응용프로그램의 시작 모듈을 명시적으로 표시하기
if __name__ == '__main__':
        print('최상위 메인 모듈')
        

pack1.mymod1.kbs()

from pack1 import mymod1
mymod1.kbs()

from pack1.mymod1 import kbs,mbc,gvar
kbs()
mbc()
print(gvar)

print('-----------')
from etc.mymod2 import *
print(Hap(5,3))
print(Cha(5, 3))

print('----------')
import mymod3
print(mymod3.Gop(4, 3))

