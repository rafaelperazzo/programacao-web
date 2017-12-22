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

#-------------------------------------------------------------------------------------------------------------------------------------------------
def crescente(lista):
    k=0
    for i in range (0, len(lista)-2, 1):
        if lista[i]<lista[i+1]:
            k+=0
        if lista[i]>=lista[i+1]:
            k+=1
    if k==0:
        cresc=True
    if not k==0:
        cresc=False
    return cresc
    
n=int(input('Digite a quantidade de valores: '))

lista=[]
for i in range (0, n, 1):
    lista.append(int(input('Digite um valor para a lista: ')))

if crescente(lista)==True:
    print('S')
if crescente(lista)==False:
    print('N')