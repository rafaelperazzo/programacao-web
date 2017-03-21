n=input('Digite n:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite a cor do quadrado:'))
cont0=0
for i in range(0,n,1):
    if a[i]==0:
        cont0=cont0+1
if cont0==1:
    cor=0
    for i in range(0,10,1):
        for j in range(0,n-2,1):
            if a[j]==cor and a[j]!=9:
                if a[j-1]==-1:
                    a[j-1]=cor+1
                if a[j+1]==-1:
                    a[j+1]=cor+1
        if cor<10:
            cor=cor+1
def menor(a):
    menor=10000
    for i in range(0,len(a)-1,1):
        if a[i]<a[i+1] and a[i]<menor:
            menor=a[i]
    if menor==10000:
        for i in range(0,len(a)-1,1):
            if a[i]==a[i+1]:
                menor=a[i]
            if a[i+1]<a[i]:
                menor=a[i+1]
    return menor
if cont0>1:
    for i in range(0,n,1):
        if a[i]==-1:
            dist=[]
            for j in range(0,n,1):
                if a[j]==0:
                    dist.append(abs(j-i)
            a[i]= menor(dist)
print a