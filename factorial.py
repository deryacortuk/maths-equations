print("Factorial Calculator n!")

number =int(input("number:"))
if (number==0 or number==1):
    result =1
    print("result:{}".format(result))
else:
    result = 1
    for i in range(2,number+1):
        result *= i
    print("result: {}".format(result))




