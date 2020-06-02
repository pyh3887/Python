# 원격DB - MariaDb 연동

import MySQLdb 

#conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')

#print(conn)

#conn.close

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
    
    
    #자료 추가 
    '''
    sql = 'insert into sangdata(code,sang,su,dan) values(15,"상품1",3,1000)'
    cursor.execute(sql)
    conn.commit()
   
    sql = "insert into sangdata values(%s,%s,%s,%s)"
    #sql_data = ('14','신상2',5,2000) # 튜플로 줌
    sql_data = '14','신상2',5,2000
    cursor.execute(sql,sql_data)
    conn.commit()
    '''
    
    #자료 수정 
    
    '''
    sql = "update sangdata set sang=%s,su=%s,dan=%s where code=%s"
    sql_data = ('파이썬','7','7000','14')
    cursor.execute(sql,sql_data)
    conn.commit()
    '''
    
    
    #자료삭제 
    '''
    code = '14'
    #sql = "delete from sangdata where code = "  + code
    #sql = "delete from sangdata where code='{0}".format(code)
    sql = "delete from sangdata where code= %s" # 가장 많이 쓰이는 방법    
    cursor.execute(sql,(code,))  # 튜플 타입으로 줄것 
    conn.commit()
    '''
        
     
    
    
    #부분자료 읽기
    code = 3 
    #sql = "select * from sangdata where code=%s"
    #cursor.execute(sql,(code,))
    sql = "select * from sangdata where code='{0}'".format(code)
    cursor.execute(sql)
    for data in cursor.fetchall():
        #print(data) 튜플형식
        print(data)
    
    
    
    #전체 자료 읽기
    sql = 'select  * from sangdata'
    cursor.execute(sql) # select 의 결과를 cursor 가 가짐
    
    #출력1
    for data in cursor.fetchall():
        #print(data) 튜플형식
        print('%s %s %s %s' %data)
    
    #출력2
    for r in cursor : 
        #print(r)
        print(r[0],r[1],r[2],r[3])
        
    #출력 3
    for(code,sang,su,dan) in cursor:
        print(code,sang,su,dan)
    
    #출력 4
    for(a,b,c,단가) in cursor:
        print(a,b,c,단가)
    
    
except Exception as e :
    print('err:' , e)

finally:
    conn.close()