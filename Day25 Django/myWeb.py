from wsgiref.simple_server import make_server

def application(envrion,start_respoonse):
    print(envrion)
    start_respoonse('200 ok', [('Content-Type', 'text/html')])
    print('path-->',envrion['PATH_INFO'])
    return [b'<h1>Hello World<h2>']

httpd = make_server('',8080,application)

print('serving Http on port 8080....')
httpd.serve_forever()