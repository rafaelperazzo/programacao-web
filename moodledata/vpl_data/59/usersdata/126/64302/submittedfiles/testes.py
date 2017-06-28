# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#criando uma função para transformar o número em uma lista#
def lista(numero):
    lista = []
    cont=0
    while numero>0:
        resto = numero%10
        cont = cont+1
        lista.insert(0,resto)
        numero = numero//10
    return (lista,cont)
#função para determinar se o número é feliz ou não#
def feliz(numero):
    b=[]
    while numero>1:
        soma = 0
        a = lista(numero)[0]
        for i in range(0,len(a),1):
            soma = soma+a[i]**2
        b.append(soma)
        if b[len(b)-1]==1:
            return(True,b)
        elif b[len(b)-1]==16:
            return (False,b)
        numero = soma
    
def contalgarismos(n):
    cont = 0
    b=[]
    a=lista(n)[0]
    for i in range(0,10,1):
        for j in range(0,len(a),1):
            if i == a[j]:
                cont=cont+1
                b.append(i)
                break
    return(b)
    
print(' Números felizes são números cujo a soma dos quadrados dos seus termos gera um novo número e, esse novo número deve satizfazer a afirmação anterior até que a soma dê o número "1".')
numero=int(input('Baseado na definição de número feliz, digite um número à ser testado:'))

if feliz(numero)[0]:
    print('SIM, o número testado é feliz! E estes são as somas dos quadrados dos seus algarismos, e por consequência, também são felizes:')
    print(feliz(numero)[1])
else:
    print('NÃO, o número testado não é feliz! E estes são algumas das somas dos quadrados dos seus algarismos, e por consequência, também não são felizes:')
    print(feliz(numero)[1])
    
r=lista(numero)[1]
p=10**(r-1)
q=(10**r)-1


print(contalgarismos(4599))
        
    
    
    
    
    
    
    
    
