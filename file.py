def fibonacci():
    i = 1
    j= 1
    yield i
    yield j

    while True:

        i,j = j, i+j
        yield j

for number in fibonacci():
    if(number>100):
        break
    print(number)

        





      


         
    
     
     
      

