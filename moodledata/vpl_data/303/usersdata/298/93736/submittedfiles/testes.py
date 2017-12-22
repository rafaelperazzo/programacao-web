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