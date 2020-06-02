# 예외처리 try ~ except

def divide(a,b):
    return a / b

print('작업 후')


c = divide(5,2)
#c = divide(5,0)
print(c)

try:
    #c = divide(5,2)
    c = divide(5,0)

    aa = [1,2]
    print(aa[0])
    #print(aa[3])
    
    f = open('c:/work/abc.txt')

except ZeroDivisionError:
    print('두번째 숫자는 0을 주지 마시오')

except IndexError as e:
    print('참조 범위 오류 : ', e)
    
except Exception as err:
    print('기타에러' + str(err)) 

print('종료')