N=int(input(''))
cont=0
x=[]
for i in range(1,N,1):
    i=int(input(''))
    x+=[i]
    if (x[i]-x[i-1])<10:
        cont+=(x[i]-x[i-1]+10)
    elif (x[i]-x[i-1])>10:
        cont+=(x[i]+10+x[i-1]+10)
    else:
        cont+=(x[i]-x[i-1]+10)
        
print(cont)
    