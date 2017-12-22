N=int(input(''))
cont=0
x=[]
for i in range(1,N,1):
    i=int(input(''))
    x+=[i]
    continue

print(x)
# iniciais
cont+=x[1]-x[0]
#centrais
for i in range(1,N,1):
    if x[i+1]-x[i]<=10:
        cont+=x[i+1]-x[i]
    elif x[i+1]-x[i]>10:
        cont+=x[i]+10
#finais
if x[N]-x[N-1]<10:
    cont+=x[N]-x[N-1]
elif x[N]-x[N-1]>10:
    cont+=x[N-1]+10
print(cont+10)