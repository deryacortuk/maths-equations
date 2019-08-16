def isTriange(a,b,c):
    if(a>0 and b>0 and c>0):
        if(a+b >c>abs(a-b)):
            return True
        elif(b+c>a>abs(b-c)):
            return True
        elif(c+a>b>abs(c-a)):
            return True
        else:
            return False
print(isTriange(6,5,7)) 