# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA

a = []
#PROCESSAMENTO

def mg (a) :
    produto = 1
    for i in range (0,len(a),1) :
        valor = float(input('Digite o valor :'))
        a.append(valor)
        produto = produto*a[i]
    mg = produto**(1/len(a))
        
    
    

