
def somaimpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==1:
            soma=soma+lista[i]
    return soma
def somapar(lista):
    soma=0
    for i in range(0,len(lista,1):
        if lista[i]%2==0:
            soma=soma+lista[i]
    return soma
def qtdimpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==1:
            soma=soma+1
    return soma
def qtdpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+1
    return soma
a=[]
n=int(input('tamanho da lista:'))
for i in range(0,n,1):
    x=int(input('valor:'))
    a.append(x)
print(somaimpar(a))
print(somapar(a))
print(qtdimpar(a))
print(qtdpar(a))
print(a)