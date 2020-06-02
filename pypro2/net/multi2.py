#python 의 GIL 정책으로 인해 thread 작동이 제대로 안되는 경우가 발생.
# multiprocessing을 위한 클래스를 별도 제공



import os 
from multiprocessing import Process 


def func():
    
    print('연속적으로 진행하고자 하는 어떤 직업')
    

def doubler(number):
    result = number + 10 
    func()
    proc = os.getpid()
    
    print('number : {0} , result : {1} , proc : {2}'.format(number, result,proc))
    

if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    procs = []
    
    for index, number in enumerate(numbers) :
        proc = Process(target = doubler , args = (number, ))
        procs.append(proc) # process 에 join 을 추가하려고 
        proc.start()
    for proc in procs:
        proc.join()
    