print('txt 파일을 읽어 dict로 저장')

#===============================================================================
# with open('mydict.txt','r') as ff:
#     aa = eval(ff.read()) #보안 취약
#     print(aa)
#     print(type(aa))
#===============================================================================
    


print()
import ast 
with open('mydict.txt','r') as ff:
    aa = ff.read()
    print(type(aa))
    bb = ast.literal_eval(aa) # 안전 보장
    print(bb)
    print(type(bb))
    