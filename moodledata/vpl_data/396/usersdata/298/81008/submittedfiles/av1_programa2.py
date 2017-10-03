# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a1 = int(input('Apostado 1: '))
a2 = int(input('Apostado 2: '))
a3 = int(input('Apostado 3: '))
a4 = int(input('Apostado 4: '))
a5 = int(input('Apostado 5: '))
a6 = int(input('Apostado 6: '))

s1 = int(input('Sorteado 1: '))
s2 = int(input('Sorteado 2: '))
s3 = int(input('Sorteado 3: '))
s4 = int(input('Sorteado 4: '))
s5 = int(input('Sorteado 5: '))
s6 = int(input('Sorteado 6: '))

resultado1 = (a1==s1) or (a1==s2) or (a1==s3) or (a1==s4) or (a1==s5) or (a1==s6)
resultado2 = (a2==s1) or (a2==s2) or (a2==s3) or (a2==s4) or (a2==s5) or (a2==s6)
resultado3 = (a3==s1) or (a3==s2) or (a3==s3) or (a3==s4) or (a3==s5) or (a3==s6)
resultado4 = (a4==s1) or (a4==s2) or (a4==s3) or (a4==s4) or (a4==s5) or (a4==s6)
resultado5 = (a5==s1) or (a5==s2) or (a5==s3) or (a5==s4) or (a5==s5) or (a5==s6)
resultado6 = (a6==s1) or (a6==s2) or (a6==s3) or (a6==s4) or (a6==s5) or (a6==s6)

if resultado1==True:
    k1=1
else:
    k1=0
    
if resultado2==True:
    k2=1
else:
    k2=0
    
if resultado3==True:
    k3=1
else:
    k3=0
    
if resultado4==True:
    k4=1
else:
    k4=0
    
if resultado5==True:
    k5=1
else:
    k5=0
    
if resultado6==True:
    k6=1
else:
    k6=0
    
total=int(k1+k2+k3+k4+k5+k6)
if (total>=0) and (total<3):
    print('azar')
if total==3:
    print('terno')
if total==4:
    print('quadra')
if total==5:
    print('quina')
if total==6:
    print('sena')