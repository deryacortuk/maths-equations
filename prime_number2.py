a = int(input("is Prime number:"))
if (a < 0 or a == 1 ):
    print (" {} is not a prime number".format(a))
elif (a==2):
    print(" {} is a prime number".format(a))
else:
    for i in range(2,a):
        if (a % i ==0):

            print("not a prime number")
            break
        else:
            print(" prime number")
            break

