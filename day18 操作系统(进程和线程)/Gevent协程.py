import gevent
import requests,time
start = time.time()

def f(url):
    print('GET:%s' %url)
    resp =requests.get(url)
    data = resp.text
    print('%d bytes received from %s' %(len(data),url))

gevent.joinall([
    gevent.spawn(f,'https://www.python.org'),
    gevent.spawn(f,'https://www.sina.com.cn')
])

print('cost time:',time.time()-start)