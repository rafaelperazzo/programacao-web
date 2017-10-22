# -*- coding: utf-8 -*-
numero = input("Informe o número: ")
if (len(numero)==8):
    try 
        soma=0
        for i in range (0,8):
            soma+=int(numero[i])
        print(soma)
    except
        print('tem uma letra, manezão')
else:
    print('NAO SEI')