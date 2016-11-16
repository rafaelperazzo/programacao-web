# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    #escreva o código da função crescente aqui
    for i in range(1,len(a),1):
        if a[i]<=a[i-1]:
            return 'N'
            break
        if i==len(a)-1:
            return 'S'
a=[1,2,3,9,5,6,7,8]
print(crescente(a))
            
        


#escreva as demais funções





#escreva o programa principal
