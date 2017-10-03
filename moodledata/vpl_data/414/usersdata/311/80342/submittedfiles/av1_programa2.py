# -*- coding: utf-8 -*-
matricula= int(input('Digite sua matricula:'))
nota1=float(input('Digite sua nota1:'))
nota2=float(input('Digite sua nota2:'))
nota3=float(input('Digite sua nota3:'))
me=float(input('Digite sua ME:'))
print (matricula)
ma=(nota1+(nota2*2)+(nota3*3)+me)/7
print ('%.1F' %ma)
if ma>=9:
    print ('A')
else:
    if 7.5<=ma<9:
        print ('B')
    else:
        if 6<=ma<7.5:
            print('C')
        else:
            if 4<=ma<6:
                print ('D')
            else:
                if ma<4:
                    print('E')
if (ma>=9) or (7.5<=ma<9) or (6<=ma<7.5):
    print ('APROVADO')
else:
    print ('REPROVADO')
