# 클래스의 포함


import etc.handle
from etc.handle import PohamHandle

class PohamCar:
    turnShow = '정지'
    
    def __init__(self,ownerName):
        self.ownerName = ownerName
        #self.handle = etc.handle.PohamHandle() # 포함
        self.handle = PohamHandle()
        
    def TurnHandle(self,q):
        if q > 0:
            self.turnShow = self.handle.RightTurn(q)
        
        elif q < 0:            
            self.turnShow = self.handle.LeftTurn(q) 
        else:
            self.turnShow = '직진'
        

if __name__ == '__main__':
    tom = PohamCar('tom')
    tom.TurnHandle(10)
    print(tom.ownerName + '의 회전량은' + tom.turnShow + str(tom.handle.quantity))
        
    tom.TurnHandle(-15)
    print(tom.ownerName + '의 회전량은' + tom.turnShow + str(tom.handle.quantity))
    
    print()
    
    james = PohamCar('james')
    james.TurnHandle(0)
    print(james.ownerName + '의 회전량은' + james.turnShow + str(james.handle.quantity))

