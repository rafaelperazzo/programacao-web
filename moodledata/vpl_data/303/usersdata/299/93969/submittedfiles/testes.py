n_valores=int(input('Digite quantos valores vamos analisar? '))

l=[]

for i in range(0,n_valores,1):
    l.append(float(input('Digite o valor %d: ' %(i+1))))

media=sum(l)/n_valores
 
x=[]
dist=[]
 
for i in range(0,n_valores,1):
    x.append((l[i]-media)**2)
    #DISTANCIA
    dist.append(l[i]-media)
    
tipo=input('Sua população é amostral?[S/N] ')

if tipo == 'S':
    
    desvio=(sum(x)/n_valores-1)**1/2
    
    print(desvio)
    

else:
    
    desvio=(sum(x)/n_valores)**1/2
    
    print(desvio)  
    
#FAZER DISTANCIA POSITIVA
for i in range(0,n_valores,1):
    if dist[i]>=0:
        dist[i]=dist[i]
    else:
        dist[i]=dist[i]*(-1)
    
cont1=0
cont2=0
cont3=0


print(dist)
print(desvio)

for j in range(0,len(dist),1):
    
    j=int(j)
    
    if (dist[j]<desvio[j]):
        cont1+=1
    elif dist[j]<2*(desvio[j]):
        cont2+=1
    elif dist[j]<3*(desvio[j]):
        cont3+=1
porcentagem_cont1=((cont1)/n_valores)*100
porcentagem_cont2=((cont2)/n_valores)*100
porcentagem_cont3=((cont3)/n_valores)*100

if porcentagem_cont1==68 and porcentagem_cont2==95 and porcentagem_cont3==99.7:
    
    print('É uma distribuição normal')
    
else:
    
    print('Não é uma dist normal')

 