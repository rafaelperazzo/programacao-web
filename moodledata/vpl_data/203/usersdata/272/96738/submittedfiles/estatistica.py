# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio_padrao(lista):
    delta=0
    for j in range(0,len(lista),1):
        delta=delta+((a[j]-media(lista)))**2
    desvpad=((1/(n-1))*delta)**(1/2)
    return desvpad
    


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('Digite o número de elementos: '))
a=[]
b=[]
for k in range(0,n,1):
    a.append(float(input('Digite o valor (lista1): ')))
for l in range(0,n,1):
    b.append(float(input('Digite o valor (lista2): ')))
print(a)
print(b)
media1=media(a)
desvpad1=desvio_padrao(a)
media2=media(b)
desvpad2=desvio_padrao(b)

print('%.2f' %media1)
print('%.2f' %desvpad1)
print('%.2f' %media2)
print('%.2f' %desvpad2)



