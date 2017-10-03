# -*- coding: utf-8 -*-

#ENTRADA
matricula= float(input('digitar numero de matricula:'))
nota1= float(input('digitar primeira nota:'))
nota2= float(input('digitar segunda nota:'))
nota3= float(input('digitar terceira nota:'))
me= float(input('digitar valor para me:'))

MA=(nota1+(nota2*2)+(nota3*3)+me)/7
print('%.2i' %MA)

if MA>=9:
    print('A')
    print('APROVADO')
else:
    if 7.5<=MA<9:
        print('B')
        print('APROVADO')
    if 6<=MA<7.5:
        print('C')
        print('APROVADO')
    if 4<=MA<6:
        print('D')
        print('REPROVADO')
    if MA<4:
        print('E')
        print('REPROVADO')
    

