# 클래스의 상속

class Animal:
    def __init__(self):
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')
        
class Dog(Animal): # java - extends
    def __init__(self):
        print('Dog 생성자')
        
    def my(self):
        print('나는 개')

dog1 = Dog()
dog1.my() # 자바와 다른점 부모 생성자는 생성되지 않는다. 따로 호출을 해야됌
dog1.move()

print('----------------------')
class Cat(Animal):
    pass

cat1 = Cat()
cat1.move()

print('\n--overriding---')
class Parent:
    def PrintData(self):
        pass

class Child1(Parent):
    def PrintData(self):
        print('child1에서 overriding')
        

class Child2(Parent):
    def PrintData(self):
        print('child2에서  재정의')
    
    def abc(self):
        print('child2에서  고유 메소드')
    

c1 = Child1()
c1.PrintData()


c2 = Child2()
c2.PrintData()


print('-----다형성-------')
kbs = c1
kbs.PrintData()
kbs = c2
kbs.PrintData()
kbs.abc() #고유 메소드도 그냥 부르면 됌


print()
plist = [c1,c2]
for i  in plist:
    i.PrintData()







