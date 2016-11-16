# -*- coding: utf-8 -*-
from __future__ import division

def crescente(a):
    #escreva o código da função crescente aqui
    for i in range(1,len(a),1):
        if a[i]<=a[i-1]:
            return False
            break
        if a[i]==len(a)-1:
            return True
a=[1,2,3,4,7,7,7,7]
print(crescente(a))
            
        


#escreva as demais funções





#escreva o programa principal
