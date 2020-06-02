s1 = '자료 1'
s2 = "두번째 자료"


print('Content-Type:text/html;charset=utf-8\n')
print('''
<html><body>
<h2></h2>반가워요
자료출력 : {0} , {1} <br>
<img src = '../images/aaa.png' width = '60%' />
<br>
<a href = '../main.html'> 메인으로 </a>
</body></html>



'''.format(s1, s2))