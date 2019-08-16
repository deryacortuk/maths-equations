print(""""***
Please choose operation
1.addition(+)
2.subtraction(-)
3. multiplication(*)
4.division(/)

****""""")
choice =int(input("choice:"))
x = int(input("1.number:"))
y = int(input("2.number:"))
if(choice==1 ):
    result = x+y
    print("result: {}".format(result))
elif(choice==2):
    result = x - y
    print("result:{}".format(result))
elif(choice==3):
    result = x*y
    print("result {}".format(result))
elif(choice==4):
    if(y==0):
        print("result: undefined")
    else:
        result = x/y
        print("result:{}".format(result))
else:
    
    print("invalid choice")


