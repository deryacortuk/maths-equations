def isPrime(n):
    if(n==0):
        return False
    elif(n==1):
        return False
    elif(n < 0):
        return False
    elif(n==2):
        return True
    else:
        for i in range(2,n):
            if (n%i==0):

                return False
            return True
print(isPrime(17))



