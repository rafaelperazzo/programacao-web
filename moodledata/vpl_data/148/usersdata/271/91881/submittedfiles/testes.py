# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO


#FUNÇÃOMG
def mg (a) :
    produto = 1
    for i in range (0,len(a),1) :
        produto = produto*a[i]
    mg = produto**(1/len(a))
    return(mg)
#ENTRADA
n = int(input('Digite a quantidade de elementos da lista : '))
a = []
    
#PROCESSAMENTO
for i in range (0,n,1) :
    valor = float(input('Digite o valor : '))
    a.append(valor)
#SAIDA
print('o valor da media é : %f' % mg(a))
        
    
    

