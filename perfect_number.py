print("perfect number calculator")

number = int(input("number:"))

if ( number < 0):
    print("please you enter positive number and number: {} is a negative number.".format(number))

else:
    i =1
    result = 0
    while(i<number):
        if(number %i ==0):
            result += i
        i +=1
    if(result ==number):
        print("{} is a perfect number".format(number))
    else:
        print("{} is not a perfect number".format(number))