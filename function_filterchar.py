def filterchar(string):
    '''功能：过滤危险字符，并将过滤的结果输出
    about：要过滤的字符串
    没有返回值'''

    import re
    pattern =r'(黑客)|(抓包)|(监听)|(Trojan)'
    sub=re.sub(pattern,'@_@',string)
    print(sub)
about='我是一个程序员，喜欢看黑客方面的书籍，想研究一下Trojan'
filterchar(about)
