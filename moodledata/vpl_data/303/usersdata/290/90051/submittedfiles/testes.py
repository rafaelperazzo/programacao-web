# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def misterio(x):
    cont=0
    for i in range(2,x,1):
        if x%i==0:
            cont=cont+1
            break
        if cont==0:
            return True
        else:
            return False
print(misterio(4))
