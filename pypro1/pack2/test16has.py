class LottoMachine:

        
        
    
    def selectBalls(self):
        #섞기전 출력
        #for a in range(45):
        #    print(self.ballList[a].num, end = ' ')
     
        # 섞기 후 출력
        #for a in range(45):
        #    print(self.ballList[a].num, end = ' ')
        return self.ballList[0:6]
class LottoUser:
    def __init__(self):
        self.machine = LottoMachine() # 포함
        
    def playLotto(self):
        input('로또를 시작합니다')
        selectedBalls = self.machine.selectBalls()
    
if __name__ == '__main__' :
    LottoUser