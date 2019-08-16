list_ = list()
result=0
for i in range(1,1000):

    if(i%3==0 or i % 5==0 ):
        list_.append(i)
mylist=list_.copy()
for j in mylist:
    result +=j
print(result)
























