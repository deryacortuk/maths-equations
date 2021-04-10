def extra_(func):
    def decorator(nums):
        
        for number in range(1,nums+1):
            i =1
            sum = 0
            while(number>i):
                if(number%i ==0):
                    sum +=i
                i +=1
            if(sum==number):
                print("perfect number:", number)
        func(nums)
        
    return decorator




@extra_
def prime_n(num):

     if(num==0 or num==1 or num<0):
         print("please enter valid number")
         return 
     else:
        
         for number in range(2,num+1):
             i = 2
             rise = 0
             while(i<number):
                 if(number%i ==0):
                     rise +=1
                 i+=1
             if(rise==0):
                 print(number)
prime_n(1000)
      


         
    
     
     
      

