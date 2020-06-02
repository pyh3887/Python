class Car:
    handle = 0 
    speed = 0
    gear = '' 
    def __init__(self,name,speed):
        self.speed = speed
        self.name = name
        
    def showData(self):
        km = '킬로미터'
        msg = '속도:' + str(self.speed) + km
        return msg
    
    def setgearName(self, str):   # setter 를 이용한 인수받기
        self.gear= str

print(Car.handle)
print(Car.speed) 

#print(Car.name) AttributeError: type object 'Car' has no attribute 'name'
print('\ntom  ------------')
car1 = Car('tom',10)
car1.setgearName('1단기어')
print(car1.handle, car1.name, car1.speed , car1.gear)
car1.color = '검정'
print('car1.color:' , car1.color)



print('\njames 꺼----------')
car2 = Car('james',20)
print(car2.handle, car2.name, car2.speed)
car2.color = '빨강'
print('car2.color:',car2.color )

print()
print(id(Car), ' ' , id(car1) , id(car2)) #세개 모두 객체주속 다르다 자바와의 차이점 . 

print()
print(car1.showData())
print(car2.showData())

car1.speed = 88
car2.speed = 100
print(car1.showData())
print(car2.showData())


Car.handle = 1 
print(car1.handle)
print(car2.handle)




        