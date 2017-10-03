# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
a1 = int(input('digite num1 da aposta'))
a2 = int(input('digite num2 da aposta'))
a3 = int(input('digite num3 da aposta'))
a4 = int(input('digite num4 da aposta'))
a5 = int(input('digite num5 da aposta'))
a6 = int(input('digite num6 da aposta'))

s1 = int(input('digite num1 do sorteio'))
s2 = int(input('digite num2 do sorteio'))
s3 = int(input('digite num3 do sorteio'))
s4 = int(input('digite num4 do sorteio'))
s5 = int(input('digite num5 do sorteio'))
s6 = int(input('digite num6 do sorteio'))

acertos = 0

if (a1 == s1) or (a1 == s2) or (a1 == s3) or (a1 == s4) or (a1 == s5) or (a1 == s6) :
    acertos += 1
    
if (a2 == s1) or (a2 == s2) or (a2 == s3) or (a2 == s4) or (a2 == s5) or (a2 == s6) :
    acertos += 1
    
if (a3 == s1) or (a3 == s2) or (a3 == s3) or (a3 == s4) or (a3 == s5) or (a3 == s6) :
    acertos += 1

if (a4 == s1) or (a4 == s2) or (a4 == s3) or (a4 == s4) or (a4 == s5) or (a4 == s6) :
    acertos += 1

if (a5 == s1) or (a5 == s2) or (a5 == s3) or (a5 == s4) or (a5 == s5) or (a5 == s6) :
    acertos += 1
    
if (a6 == s1) or (a6 == s2) or (a6 == s3) or (a6 == s4) or (a6 == s5) or (a6 == s6) :
    acertos += 1

if acertos == 6 :
    print('sena')
elif acertos == 5 :
    print('quina')
elif acertos == 4 :
    print('quadra')
elif acertos == 3 :
    print('terno')
else:
    print('azar')
