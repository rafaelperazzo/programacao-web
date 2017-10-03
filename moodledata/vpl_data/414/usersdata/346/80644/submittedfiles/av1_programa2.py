# -*- coding: utf-8 -*-

Matricula= str(input('Digite a sua Matricula: '))
nota1= float(input('Digite a sua primeira nota: '))
nota2= float(input('Digite a sua segunda nota: '))
nota3= float(input('Digite a sua terceira nota: '))
ME= float(input('Digite a sua Media dos exercicios: '))

MA= (nota1+(nota2*2)+(nota3*3)+ME)/7

A= MA>=9
B= MA>=7.5 and MA<9
C= MA>=6 and MA<7.5
D= MA>=4 and MA<6
E= MA<4

print (Matricula)
print ('%.1f' % MA)

if MA>=9:
    print('A')
    
elif MA>=7.5 and MA<9:
    print('B')
    
elif MA>=6 and MA<7.5:
    print('C')
    
elif MA>=4 and MA<6:
    print('D')
    
else:
    print('E')

if (A our B our C, True):
    print('APROVADO')
else:
    print('REPROVADO')
                