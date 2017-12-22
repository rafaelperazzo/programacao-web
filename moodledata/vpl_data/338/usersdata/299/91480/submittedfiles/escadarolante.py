N=int(input(''))
cont=0
x=[]
for i in range(1,N+1,1):
    i=int(input(''))
    x+=[i]
    continue

# iniciais
cont+=x[1]-x[0]
#centrais
for i in range(2,N,1):
    if x[i]-x[i-1]<=10:
        cont+=x[i]-x[i-1]
    elif x[i]-x[i-1]>10:
        cont+=x[i]+10
    else:
        cont+=20
#finais
if (x[N]-x[N-1])<10:
    cont+=(x[N]-x[N-1])+10
elif (x[N]-x[N-1])>10:
    cont+=20
else:
    cont+=20
print(cont)