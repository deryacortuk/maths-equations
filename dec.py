def extra(func):
    def wrapper(nums):
        for number in range(1,nums+1):
            i = 1
            sum=0
            while(number>i):
                if(number%i==0):
                    sum +=i
                i+=1
            if(sum==number):
                print("perfect number:",number)
        func(nums)
    return wrapper

@extra
def prime(num):
    for number in range(2,num+1):
        i = 2
        nmbr = 0
        while(number>i):
            if(number%i==0):
                nmbr +=1
            i +=1
        if(nmbr==0):
            print(number)

prime(100)
