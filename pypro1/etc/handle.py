# 다른 클래스에서 공유할 클래스


class PohamHandle:
    quantity = 0 
    
    def LeftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    
    def RightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'