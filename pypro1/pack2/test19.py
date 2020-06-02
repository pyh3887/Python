# 다중 상속

class Tiger:
    data = '호랑이 세계'
    
    def Cry(self):
        print('호랑이 어흥')
    
    def Eat(self):
        print('맹수는 고기를 좋아함')
        

class Lion:
    
    def Cry(self):
        print('사자 으르렁')
        
    def Hobby(self):
        print('백수의 왕은 낮잠을 즐겨함')


class Liger1(Tiger,Lion): # 다중상속
    pass

aa = Liger1()
aa.Cry()
aa.Eat()
aa.Hobby()
print(aa.data)
print()
class Liger2(Lion, Tiger): # 중복일 경우에는 먼저 적어준 클래스의 멤버가 우선시 됌
    data = '라이거 만세'
    
    def Play(self):
        self.Cry()
        super().Cry()
        print(self.data)
        print(super().data)
        
    def Hobby(self):
        print('라이거는 낮잠을 좋아함')



bb = Liger2()

bb.Play()
bb.Hobby()


