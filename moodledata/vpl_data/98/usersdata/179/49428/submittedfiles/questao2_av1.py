# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n1=int(input('digite o valor de n1 :'))
n2=int(input('digite o valor de n2 :'))
n3=int(input('digite o valor de n3 :'))
n4=int(input('digite o valor de n4 :'))
n5=int(input('digite o valor de n5 :'))
n6=int(input('digite o valor de n6 :'))
s1=int(input('digite o valor de s1 :'))
s2=int(input('digite o valor de s2 :'))
s3=int(input('digite o valor de s3 :'))
s4=int(input('digite o valor de s4 :'))
s5=int(input('digite o valor de s5 :'))
s6=int(input('digite o valor de s6 :'))
cont=0
for i in range(1,100,1):
    if n1==s1 or s2 or s3 or s4 or s5 or s6:
        cont=cont+1
    if n2==s1 or s2 or s3 or s4 or s5 or s6:
        cont=cont+1
    if n3==s1 or s2 or s3 or s4 or s5 or s6:
        cont=cont+1
    if n4==s1 or s2 or s3 or s4 or s5 or s6:
        cont=cont+1
    if n5==s1 or s2 or s3 or s4 or s5 or s6:
        cont=cont+1
    if n6==s1 or s2 or s3 or s4 or s5 or s6:
        cont=cont+1
    if cont==3:
        print('terno')
    elif cont==4:
        print('quadra')
    elif cont==5:
        print('quina')
    elif cont==6:
        print('sena')
    else:
        print('azar')

        

