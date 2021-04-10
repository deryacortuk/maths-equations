
def isPrime(num):
    if(num==0 or num<0 or num==1):
        return False
    elif(num==2):
        return True
    else:
        for i in range(3,num+1):
            if(num%i ==0):
                return False

            return True
print(prime(7))

