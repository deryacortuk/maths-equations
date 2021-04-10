def is_prime(x):
    i = 2
    while(x>i):
        if(x%i==0):
            return False
        i +=1
    return True
def generator():
    i =2
    while True:
        if(is_prime(i)):
            yield i
        i +=1

for number in generator():
    if(number>100):
        break
    print(number )