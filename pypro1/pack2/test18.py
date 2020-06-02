# 상속
from builtins import type

class Person:
    say = '난 사람이야~~~'
    nai = 20
    __kbs = '공영방송' #private
    
    def __init__(self,nai):
        print('Person 생성자')
        self.nai = nai 
        
    def PrintInfo(self):
        print('나이:{},이야기:{}'.format(self.nai,self.say))
        
    def Hello(self):
        print('안녕')
        print(self.__kbs)
        
    @staticmethod
    def sbs(tel):
        print('tel:' , tel)
        #print(self.say)    
    
print(Person.say, ' ' , Person.nai)
print()
p = Person('22')
print(p.nai)
p.PrintInfo()
p.Hello()

print('***' * 20)
class Employee(Person):
    say = '일하는 동물'
    
    def __init__(self):
        print('Employee 생성자')
        
    def PrintInfo(self):
        print('Employee의 PrintInfo')
        
    def EprintInfo(self):
        print(self.say, ' ' , super().say) #처음부터 부모클래스로 감
        super().PrintInfo()
        self.Hello()
        #print(self.__kbs) err : private 이므로 
        
e = Employee()

print(e.say, ' ', e.nai)
e.EprintInfo()

print('~~~~' * 20)

class Worker(Person):
    def __init__(self,nai):
        print('Worker 생성자')
        super().__init__(nai) 
        
        def WprintInfo(self):
            self.PrintInfo()
            super().PrintInfo()

w = Worker('33')
print(w.say, ' ' , w.nai)

w.PrintInfo()

print('^^^' * 20)
class Programmer(Worker):
    def __init__(self,nai):
        print('programmer 생성자')
        #super().__init__(nai)
        Worker.__init__(self, nai) # UnBound Method call
        
    def WprintInfo(self):
        print('Programmer 에서 오버라이딩')

pr = Programmer(44)
print(pr.say, ' ' , pr.nai)
pr.WprintInfo()
pr.PrintInfo()


print('==========')
print(type(12.3))
print(type(pr))
print(type(w))
print(Person.__bases__)
print(Programmer.__bases__)
print()
pr.sbs('123-4567') #비권장
Person.sbs('222-3333')


















