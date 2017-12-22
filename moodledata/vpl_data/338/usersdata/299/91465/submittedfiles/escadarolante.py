N=int(input(''))
cont=0
x=[]
for i in range(1,N,1):
    i=int(input(''))
    x+=[i]
    continue

print(x)

for i in range(0,N,1):
    #iniciais
    if (x[i+1]-x[i])<10:
        cont+=(x[i]-x[i-1]+10)
    elif (x[i+1]-x[i])>10:
        cont+=(x[i+1]+10+x[i]+10)
    else:
        cont+=(x[i+1]+10+x[i])+10
    #finais
    for i in range(N,N+1,1):
        if x[i]-x[i+1]:
            cont+=(x[i]-x[i-1])+10
print(cont)