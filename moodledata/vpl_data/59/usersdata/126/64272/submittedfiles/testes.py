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
        elif b[len(b)-1]==9:
            return False
        numero = soma
    
def contalgarismos(n):
    cont = 0
    a=lista(n)[0]
    for i in range(0,10,1):
        for j in range(0,len(a),1):
            if i == a[j]:
                cont=cont+1
                break
    return(cont)
    
    
numero=int(input('Digite o número à ser testado se é feliz:'))
print(feliz(numero)[1])
if feliz(numero)[0]:
    print('SIM, o número testado é feliz')
else:
    print('NÃO, o número testado não é feliz')
    
r=lista(numero)[1]
p=10**(r-1)
q=(10**r)-1


        
    
    
    
    
    
    
    
    
