a = int(input("number1:"))
b = int(input("number2:"))
i = 1
ebob = 1
while (i<=a  and i<= b):
    if(not(a % i ) and not(b % i)):
        ebob = i
    i +=1
print(ebob)



