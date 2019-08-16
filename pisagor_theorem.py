def pisagor(n):
    pisagor_list= list()
    for i in range(1,n+1):
        for j in range(1,n+1):
            k = (i**2 + j**2)**0.5
            if(k== int(k)):
                pisagor_list.append((i,j,int(k)))
    return pisagor_list

print(pisagor(17))
