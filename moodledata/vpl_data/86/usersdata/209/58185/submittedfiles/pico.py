def pico(lista):
    for i in range (1,(len(lista)//2)+1,1):
        if lista[i]<lista[i-1]:
            return False
        else:
            for i in range ((len(lista)//2)+1,len(lista),1):
                if lista[i]>lista[i-1]:
                    return False
    return True

n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range (0,n,1):
    x=int(input('Digite um valor para a lista:'))
    a.append(x)
if pico(a):
    print('S')
else:
    print('N')