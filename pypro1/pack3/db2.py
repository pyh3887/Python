import MySQLdb

config = {      #기본값

    'host':'127.0.0.1',

    'user':'root',

    'password':'123',

    'database':'test',

    'port':3306,

    'charset':'utf8',

    'use_unicode':True

}

try:
    conn = MySQLdb.connect(**config)
    #print(conn)
    cursor = conn.cursor() # SQL 문 수행을 위한 커서 객체 생성
    
     
    #부분자료 읽기
    code = input('부서번호를 입력하세요 :')
    i = 0
    
    sql = "select jikwon_no,jikwon_name,buser_num,jikwon_jik from jikwon where buser_num='{0}'".format(code)
    
    sql = '''
          select jikwon_no,jikwon_name,buser_num,jikwon_jik 
          from jikwon 
          where buser_num='{0}'
          '''.format(code)
    
    cursor.execute(sql)
    print('사번\t이름\t부서번호\t직급' )
    for data in cursor.fetchall():
        #print(data) 튜플형식
        print('%s\t%s\t%s\t%s' %data)
        i = i+1
    print('인원수 :' , i , '명')
        

except Exception as e :
    print('err:' , e)

finally:
    conn.close()