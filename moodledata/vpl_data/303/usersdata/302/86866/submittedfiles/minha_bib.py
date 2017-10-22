# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def primo (n):
    cont = 0
    for i in range (2,n,1):
    if n%i == 0:
        cont += 1
        break
    if cont > 0:
        return False
    else:
        return True