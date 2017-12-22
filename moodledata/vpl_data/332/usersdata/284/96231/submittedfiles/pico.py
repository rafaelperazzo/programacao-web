lista=[]

def pico(lista):
    contcresc=0
    contdecresc=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            contcresc=contcresc+1
        else:
            break
    for i in range(contcresc,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            contdecresc=contdecresc+1
        else:
            break
    if(contcresc+contdecresc==len(lista)-1 and contcresc>0 and contdecresc>0):
        return ('S')
    else:
        return ('N')
        
n = (int(input('Digite a quantidade de elementos da lista: ')))
for i in range(0,n,1):
    lista.append(int(input('digite um valor%.d: ' %(i+1))))
print(pico(lista))   
