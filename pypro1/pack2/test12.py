# 모듈의 멤버로 클래스

aa = 10 

def aa():
    pass

print(aa)

print()

class TestClass:
    kk = 1  # 멤버변수(전역) public
    
    def __init__(self):
        print('생성자')
    
    def __del__(self):
        print('소멸자')
        
    def printMsg(self): #메소드(public)
        name = '한국인' #지역변수
        print(name)
        print(self.kk)
        

test = TestClass() #생성자 호출. 
print(test.kk)
print(TestClass.kk) #prototype 클래스

print('-----------------')
test.printMsg()  # Boune Method call 객체변수의 이름으로 부를때 

#TestClass.printMsg() # printMsg() missing 1 required positional argument: 'self'
TestClass.printMsg(test) # UnBound Method call
print()
print(type(1))
print(type(test))
print(id(test))
print(id(TestClass))

# del test
# test.printMsg()
