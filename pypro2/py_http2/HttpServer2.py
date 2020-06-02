# SimpleHttpRequestHandler를 확장한 CGIHttpRequestHandler 사용
# py 문서 내에서 html tag 를 기술

from http.server import CGIHTTPRequestHandler ,HTTPServer



port = 8888

class Handler(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin']
    
    

serv = HTTPServer(('192.168.0.80',port),Handler)
print('웹 서비스 시작')
serv.serve_forever()