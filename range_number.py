result=0
for i in range(101):
    #print(i,end='.0\n')
    result+=i
print(result)

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+"*"+str(i)+"="+str(i*j)+"\t",end=' ')
    print('')