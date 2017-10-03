# -*- coding: utf-8 -*-


#COMECE SEU CODIGO AQUI
valor = int(input('Digite o valor do dinheiro:'))
cedulas=0
atual=20
valorentregue=valor

while True:
    if atual<=valorentregue:
        valorentregue-=atual
        cedulas+=1
    else:
        print('%d'%cedulas)
        if valorentregue==0:
            break
        if atual==20:
            atual=10
        elif atual==10:
            atual=5
        elif atual==5:
            atual=2
        elif atual==2:
            atual=1
        cedulas=0