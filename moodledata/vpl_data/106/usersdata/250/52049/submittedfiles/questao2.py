# -*- coding: utf-8 -*-
a1=int(input('1° numero da aposta:'))
a2=int(input('2° numero da aposta:'))
a3=int(input('3° numero da aposta:'))
a4=int(input('4° numero da aposta:'))
a5=int(input('5° numero da aposta:'))
a6=int(input('6° numero da aposta:'))
b1=int(input('1° numero sorteado:'))
b2=int(input('2° numero sorteado:'))
b3=int(input('3° numero sorteado:'))
b4=int(input('4° numero sorteado:'))
b5=int(input('5° numero sorteado:'))
b6=int(input('6° numero sorteado:'))
cont=0
if a1==b1 or a1==b2 or a1==b3 or a1==b4 or a1==b5 or a1==b6:
    cont=cont+1
if a2==b1 or a2==b2 or a2==b3 or a2==b4 or a2==b5 or a2==b6:
    cont=cont+1
if a3==b1 or a3==b2 or a3==b3 or a3==b4 or a3==b5 or a3==b6: 
    cont=cont+1
if a4==b1 or a4==b2 or a4==b3 or a4==b4 or a4==b5 or a4==b6: 
    cont=cont+1    
if a5==b1 or a5==b2 or a5==b3 or a5==b4 or a5==b5 or a5==b6: 
    cont=cont+1    
if a6==b1 or a6==b2 or a6==b3 or a6==b4 or a6==b5 or a6==b6: 
    cont=cont+1  
if cont==3:
    print('terno')
elif cont==4:
    print('quadra')
elif cont==5:
    print('quina')
elif cont==6:
    print('sena')
    

 