import urllib.parse
import urllib.request

#将数据使用urlencode编码处理后，再使用encoding设置为utf-8编码
data=bytes(urllib.parse.urlencode({'word':'hello'}),encodings='utf8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
html=response.read()
print(html)