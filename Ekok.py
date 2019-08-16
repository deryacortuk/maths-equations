def ekok(number1,number2):
    i =2
    ekok = 1
    while True:
        if (number1 % i == 0 and number2 % i==0):
            ekok *=i
            number1 //=i
            number2 //=i
        elif(number1 %i==0 and number2 %i != 0):
            ekok *=i
            number1 //=i
        elif(number1 % i != 0 and number2 %i ==0):
            ekok *=i
            number2 //= i
        else:
            i +=1
        if(number1==1 and number2 ==1):
            break
    return ekok
print(ekok(6,12))

