def analiseiguais(x,y):
    cont=0
    for i in range(0,n,1):
         for j in range(0,m,1):
            if listan[i]==listam[j]:
                cont+=1
            else:
                cont+=0
    return cont

listan=[]
listam=[]
n=int(input(''))
m=int(input(''))

for i in range(0,n,1):
    listan.append(int(input('')))
for i in range(0,m,1):
    listam.append(int(input('')))
    
print(analiseiguais(listan,listam))



