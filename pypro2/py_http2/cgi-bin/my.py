import cgi

form = cgi.FieldStorage() #get 방식 데이터를 받는다.request.getparameter

irum = form['name'].value
nai = form['age'].value


print('Content-Type:text/html;charset=utf-8\n')
print('''
<html><body>
<h2></h2>반가워요
이름은{0}, 나이는{1}
</body></html>

'''.format(irum, nai))