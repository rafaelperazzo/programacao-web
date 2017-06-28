# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#criando uma função para transformar o número em uma lista#
def lista(numero):
    lista=[]
    cont=0
    while numero>0:
        resto=numero%10
        cont=cont+1
        lista.insert(0,resto)
        numero = numero//10
    return (lista,cont)
#função para determinar se o número é feliz ou não#
def feliz(numero):
    while i>len(a):
        soma=0
        i=0
        a=lista(numero)[0]
        for i in range(0,len(a),1):
            soma=soma+a[i]**2
            numero=soma
    if soma==1:
        return True
    elif soma!=1:
        return False
        
def contalgarismos(n):
    cont=0
    a=lista(n)[0]
    for i in range(0,10,1):
        for j in range(0,len(a),1):
            if i==a[j]:
                cont=cont+1
                break
    return(cont)
    
    
numero=int(input('Digite o número à ser testado se é feliz:'))

if feliz(numero):
    print('SIM, o número testado é feliz')
else:
    print('NÃO, o número testado não é feliz')
    
r=lista(numero)[1]
p=10**(r-1)
q=(10**r)-1


        
    
    
    
    
    
    
    
    
