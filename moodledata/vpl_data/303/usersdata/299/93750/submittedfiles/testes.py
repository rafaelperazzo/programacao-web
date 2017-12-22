n_valores=int(input('Digite quantos valores vamos analisar? '))

l=[]

for i in range(0,n_valores,1):
    l.append(int(input('Digite o valor %d: ' %(i+1))))

media=sum(l)/n_valores
 
x=[]
dist=[]
 
for i in range(0,n_valores,1):
    x.append((l[i]-media)**2)
    dist.append(((l[i]-media)**2)**1/2)
    
tipo=input('Sua população é amostral?[S/N] ')

if tipo == 'S':
    desvio=(sum(x)/n_valores-1)**1/2
    print(desvio)
else:
    desvio=(sum(x)/n_valores)**1/2
    print(desvio)
print(dist)
    
 