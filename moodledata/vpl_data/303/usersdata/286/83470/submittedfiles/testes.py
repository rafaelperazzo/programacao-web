# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO


while (True):
    x = int(input("Digite um número positivo: "))
    if x >= 0:
        break
    f = 1
    for i in range(2,x+1,1):
        contador = contador +1
        f =* i
    print("%d! = %d" %(x,f))
