def fibonacci(n):

    if(n<0):
        print("n is not positive integer")
    elif n==0:
        return n
    elif n==1:
        return n
    else:
        a=0
        b=1
        for i in range(0,n):
            a,b = b, a+b
        return b

print(fibonacci(17))



