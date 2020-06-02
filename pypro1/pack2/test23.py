# 우편번호 파일 읽기 : 동이름 입력 후 해당 자료 출력


try:
    
    dong = input('동이름 입력: ')    
    with open(r'zipcode.txt', mode='r' , encoding='euc-kr') as f :
        line = f.readline()
        #print(line)
        while line: 
            #print(line)
            #lines = line.split('\t')
            lines = line.split(chr(9)) # 9글자 자르기
            #print(lines[3])
            if lines[3].startswith(dong): # 서초로 시작하는 
                #print(lines)
                print('[' + lines[0] + ']' + lines[1] + '\t' + lines[2] + '\t' + lines[3])
            
            line = f.readline()
                       
            
    

except Exception as e:
    print('err :' + str(e))
        