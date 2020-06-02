kor = 100

def abc():
    print('모듈의 멤버인 함수')
    
class My:
    kor = 90
    
    def abc(self):
        print('메소드')
        
    def show(self):
        #kor = 77 # 모듈의 kor 이 출력됌
        print(kor) 
        print(self.kor) 
        self.abc() # 클래스의 멤버함수 출력
        abc()  # 모듈 멤버 함수 호출

m = My()
m.show()

print('\n----------------------------------')

class Our():
    a = 1
     
o1 = Our()
print(o1.a)
o1.a = 2 
print(o1.a)

print()
o2 = Our()
print(o2.a)
o2.b = 10

print(o2.b) # no erro o2 객체변수에서 선언가능
#print(o1.b) # err o1.b 는 없음
print(Our.a)
#print(Our.b) #err  


print('\n----클래스는 새로운 type을 생성 --------------------------------------')
class Singer:
    titleSong = '파이팅 코리아'
    
    def sing(self):
        msg = '노래는'
        print(msg, self.titleSong,'라라라라')

psy = Singer()
psy.sing()

print()
redvelvet = Singer()
redvelvet.sing()
redvelvet.titleSong = '빨간맛'
redvelvet.sing()
redvelvet.co = 'SM'

print('소속사:' + redvelvet.co)
print()
psy.sing()
# print('소속사:' + psy.co)  err psy.co x  














