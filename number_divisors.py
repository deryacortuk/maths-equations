number = int(input("number:"))
divisors = []

for i in range(1,number+1):
    if(number % i ==0):
        divisors.append(i)
print(divisors)

