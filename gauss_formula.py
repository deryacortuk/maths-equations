print("""The sequence of numbers (1, 2, 3, … ,n) is arithmetic and when we are looking 
for the sum of a sequence, we call it a series.""")


number =int(input("number:"))
if(number>0):
    result = (number*(number+1))*0.5
    print("sum of sequence:{}".format(result))
else:
    print("please you enter a positive number")

