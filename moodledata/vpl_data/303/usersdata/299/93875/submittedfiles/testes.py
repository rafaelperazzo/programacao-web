n_valores=int(input('Digite quantos valores vamos analisar? '))

l=[]

for i in range(0,n_valores,1):
    l.append(float(input('Digite o valor %d: ' %(i+1))))

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
    
cont1=0
cont2=0
cont3=0

for i in range(0,n_valores,1):
    if dist[i]<desvio[i]:
        cont1+=1
    elif dist[i]<2*desvio[i]:
        cont2+=1
    elif dist[i]<3*desvio[i]:
        cont2+=1

porcentagem_cont1=((cont1)/n_valores)*100
porcentagem_cont2=((cont2)/n_valores)*100
porcentagem_cont3=((cont3)/n_valores)*100

if porcentagem_cont1==68 and porcentagem_cont2==95 and porcentagem_cont3==99.7:
    print('è uma distribuição normal')
else:
    print('ñ é uma dist normal')

 