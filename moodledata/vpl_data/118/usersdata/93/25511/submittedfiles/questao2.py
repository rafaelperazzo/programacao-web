N=input('numero de quadrados: ')
a=[]
for i in range(0,N,1):
    a.append(input('tom do quadrado: '))
b=[]
for i in range(0,N,1):
    if a[i]==0:
        b.append(i)
for i in range(0,N,1):
    if a[i]==-1:
        menor=9
        for j in range(0,len(b),0):
            if abs(i-b[j])<menor:
                menor =abs(i-b[j])
        a[i]=menor
print a   