# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
x1=n//1000
resto=n%1000
x2=resto//100
resto2=resto%100
x3=resto2//10
x4=resto2%10
if ((x1*10)+x2)*((x3*10)+x4)==n:
    print('vampiro')
elif ((x1*10)+x2)*((x4*10)+x3)==n:
    print('vampiro')
elif ((x2*10)+x1)*((x3*10)+x4)==n:
    print('vampiro')
elif ((x2*10)+x1)*((x4*10)+x3)==n:
    print('vampiro')
elif ((x1*10)+x3)*((x2*10)+x4)==n:
    print('vampiro')
elif ((x1*10)+x3)*((x4*10)+x2)==n:
    print('vampiro')
elif ((x3*10)+x1)*((x2*10)+x4)==n:
    print('vampiro')
elif ((x3*10)+x1)*((x4*10)+x2)==n:
    print('vampiro')
elif ((x1*10)+x4)*((x2*10)+x3)==n:
    print('vampiro')
elif ((x1*10)+x4)*((x3*10)+x2)==n:
    print('vampiro') 
elif ((x4*10)+x1)*((x2*10)+x3)==n:
    print('vampiro')
elif ((x4*10)+x1)*((x3*10)+x2)==n:
    print('vampiro') 
elif ((x2*10)+x3)*((x1*10)+x4)==n:
    print('vampiro')
elif ((x2*10)+x3)*((x4*10)+x1)==n:
    print('vampiro')
elif ((x3*10)+x2)*((x1*10)+x4)==n:
    print('vampiro')
elif ((x3*10)+x2)*((x4*10)+x1)==n:
    print('vampiro')
elif ((x2*10)+x4)*((x1*10)+x3)==n:
    print('vampiro')
elif ((x2*10)+x4)*((x3*10)+x1)==n:
    print('vampiro')
elif ((x4*10)+x2)*((x3*10)+x1)==n:
    print('vampiro')
elif ((x4*10)+x2)*((x1*10)+x3)==n:
    print('vampiro')
elif ((x4*10)+x2)*((x3*10)+x1)==n:
    print('vampiro')
elif ((x4*10)+x3)*((x2*10)+x1)==n:
    print('vampiro')
elif ((x4*10)+x3)*((x1*10)+x2)==n:
    print('vampiro')
elif ((x3*10)+x4)*((x1*10)+x2)==n:
    print('vampiro')
elif ((x3*10)+x4)*((x2*10)+x1)==n:
    print('vampiro')
else:
    print('nao é vampiro')
















    
    
    
    
    
    
    
    
    
    
    
