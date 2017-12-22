n=int(input('Digite a ordem da matriz n x n: '))

matriz=[]
for i in range (0, n, 1):
    linha=[]
    for i in range (0, n, 1):
        linha.append(int(input('Digite um elemento: ')))
    matriz.append(linha)

lista_somas=[]
for i in range (0, n, 1):
    s=sum(matriz[i])
    lista_somas.append(s)
    
for i in range (0,n,1):
    scol=0
    for j in range (0,n,1):
        scol+=matriz[j][i]
    lista_somas.append(scol)
    
contador=0
for i in range (0, len(lista_somas)-1, 1):
    if lista_somas[i]==lista_somas[i+1]:
        contador+=0
    if not lista_somas[i]==lista_somas[i+1]:
        contador+=1

if contador==0:
    print('S')
if not contador==0:
    print('N')


'''
Grupo: G, Hora: 4º grupo da segunda feira
'''



def modulo(h):
    if h>=0:
        h=h
    if h<0:
        h=(-1)*h
    return h

n=int(input('Digite a quantidade de valores: '))

lista=[]
for i in range (0, n, 1):
    lista.append(float(input('Digite um valor para a lista: ')))

media = sum(lista)/(float(n))

somat=0
for i in range (0, n, 1):
    somat+=((lista[i] - media)**2)

desvpad= float(((1/(n - 1))*somat)**(float(1/2)))
print(desvpad)

qntd68=0
for i in range (0, n, 1):
    if modulo(lista[i] - media)<desvpad:
        qntd68+=1
    if modulo(lista[i] - media)>=desvpad:
        qntd68+=0
        
qntd95=0
for i in range (0, n, 1):
    if modulo(lista[i] - media)<2*desvpad:
        qntd95+=1
    if modulo(lista[i] - media)>=2*desvpad:
        qntd95+=0

qntd997=0
for i in range (0, n, 1):
    if modulo(lista[i] - media)<3*desvpad:
        qntd997+=1
    if modulo(lista[i] - media)>=3*desvpad:
        qntd997+=0
        
if (float(qntd68/n)>=float(68/100)) and (float(qntd95/n)>=float(95/100)) and (float(qntd997/n)>=float(99.7/100)):
    print('Sim, a distruição é normal.')
if not (float(qntd68/n)>=float(68/100)) and (float(qntd95/n)>=float(95/100)) and (float(qntd997/n)>=float(99.7/100)):
    print('Não, a distruição não é normal.')