# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desv(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    desvpad=(soma/(n-1))**(0.5)
    return desvpad
    


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
a=[]
b=[]
n=int(input('n:))
for in range(0,n,1):
    a.append(input('a:'))
for in range(0,n,1):
    b.append(input('b:'))
media_a=media(a)
media_b=media(b)
desv_a=desv(a)
desv_b=desv(b)
print('%.2f' % media_a)
print('%.2f' % desv_a)
print('%.2f' % media_b)
print('%.2f' % desv_b)

