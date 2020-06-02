
from abc import *  # import 를 해주어야함

class Employee(metaclass=ABCMeta):
    # ABCMeta 클래스의 서브 클래스는 추상클래스
    def __init__(self,irum,nai):
        self.irum = irum
        self.nai = nai
    
    @abstractclassmethod
    def pay(self): #추상 메소드
        pass
    
    @abstractclassmethod
    def data_print(self): #추상 메소드
        pass
    
    def irumnai_print(self):
        print(self.irum , " " ,self.nai, ' ' ,end='')
        
        


class Temporary(Employee):
    irum = ''
    
    def __init__(self,irum,nai,ilsu,ildang):
        super().__init__(irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
                        
  
    
  
    def pay(self): #추상 메소드
        return self.ilsu * self.ildang
    
  
    def data_print(self): #추상 메소드
        super().irumnai_print() 
        print(self.pay())
        


class Regular(Employee):
    irum = ''
    
    def __init__(self,irum,nai,salery):
        super().__init__(irum, nai)
        self.salery = salery
      
                
       
  
    def pay(self): #추상 메소드
        return self.salery
    
  
    def data_print(self): #추상 메소드
        super().irumnai_print() 
        print(self.pay())
        
        
        
class Salesman(Regular):
    irum = ''
    
    def __init__(self,irum,nai,salery,sales,commission):
        super().__init__(irum,nai,salery)
        self.sales = sales
        self.commission = commission
        self.salery = salery
        
                
    def irumnai_print(self,irum,nai):
        print(irum,nai)
    
  
    def pay(self): #추상 메소드
        return self.salery + (self.commission*self.sales)
    
  
    def data_print(self): #추상 메소드
        super().irumnai_print() 
        print(self.pay())
         
 
        
        
        
a = Temporary('홍길동',23,3,30000)
b = Regular('삼길동',24,2500000)
c = Salesman('고길동',29,120000,500000,0.25)
a.data_print()
b.data_print()
c.data_print()






























    