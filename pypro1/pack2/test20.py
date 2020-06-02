# 추상클래스 

from abc import *  # import 를 해주어야함

class AbstractClass(metaclass=ABCMeta):
    # ABCMeta 클래스의 서브 클래스는 추상클래스
    
    @abstractclassmethod
    def abcMethod(self): #추상 메소드
        pass
    
    def normalMethod(self):
        print('AbstractClass 클래스의 일반 메소드')
        
    
        
        
#abs = AbstractClass() #TypeError: Can't instantiate abstract class AbstractClass with abstract methods abcMethod
#abs.normalMethod()

class Child1(AbstractClass):
    name = '난 child1'
    
    
    def abcMethod(self):
        print('추상 메소드를 오버라이딩')



c1 = Child1()

print(c1.name)
c1.abcMethod()
c1.normalMethod()


class Child2(AbstractClass):
    name = '난 child2'
    
    
    def abcMethod(self): #추상 : 오버라이딩 강요
        print('추상 메소드를 오브어 라이딩')
        
    def normalMethod(self): #오버라이딩 선택
        print('normalMethod도 오버라이딩 하였다') 

c2 = Child2()
print(c2.name)
c2.abcMethod()
c2.normalMethod()
print()

parent = AbstractClass
print(type(parent))

parent = c1
print(parent.name)


parent = c2
print(parent.name)

print()
imsi = c1
print(imsi.name)
imsi = c2
print(imsi.name) # 자바와는 다르게 부모의 변수에 주소객체를 주지않아도된다 (casting , promotion x )





