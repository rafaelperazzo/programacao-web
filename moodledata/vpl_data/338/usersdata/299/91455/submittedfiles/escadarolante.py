N=int(input(''))
cont=0
x=[]
for i in range(1,N,1):
    i=int(input(''))
    x+=[i]
    cont+=(x[i]-x[i-1])
print(cont+10)
    