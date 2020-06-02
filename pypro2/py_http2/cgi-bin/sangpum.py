# MariaDb 의 테이블 출력

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
          
    cursor.execute('select * from sangdata')
    
    
    print('Content-Type:text/html;charset=utf-8\n')
    print('<html><body>* 상품자료 *<br>')
    print('<table border = "1">')
    print('<tr><th>코드</th><th>상품</th><th>수량</th><th>단가</th></tr>')
    datas = cursor.fetchall()
    for d in datas:
        print('''
        <tr>
        <td>{0}</td>
        <td>{1}</td>
        <td>{2}</td>
        <td>{3}</td>
                
        </tr>
    '''.format(str(d[0]), str(d[1]),  str(d[2]), str(d[3])))
        
    print('</table></body></html>')



except Exception as e :
    print('err:' , str(e))

finally:
    cursor.close()
    conn.close()

 