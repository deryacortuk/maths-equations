print("the series find self power")
number=int(input("number:"))
result = 0
if(number>0):

    for i in range(1,number+1):

        result += i**i


        print("calculator self power:{}".format(result) )
