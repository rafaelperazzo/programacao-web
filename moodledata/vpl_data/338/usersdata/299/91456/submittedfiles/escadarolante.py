N=int(input(''))
cont=0
x=[]
for i in range(1,N,1):
    i=int(input(''))
    x+=[i]
    cont+=(x[i+1]-x[i])
print(cont+10)
    