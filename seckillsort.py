bookinfo=[('A',22.50,120),('B',65.10,89.80),('C',23.40,36.00),('C',22.50,128)]
bookinfo.sort(key=lambda x:(x[1],x[1]/x[2]))
print(bookinfo)