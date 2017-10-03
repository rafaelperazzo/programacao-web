# -*- coding: utf-8 -*-
matricula = int(input('insira sua matricula:'))
n1 = float(input('insira sua primeira nota de avaliacao:'))
n2 = float(input('insira sua segunda nota de avaliacao:'))
n3 = float(input('insira sua terceira nota de avaliacao:'))
n4 = float(input('insira sua primeira nota de exercicio:'))
n5 = float(input('insira sua segunda nota de exercicio:'))
n6 = float(input('insira sua terceira nota de exercicio:'))
me = (n4 + n5 + n6)/3
ma = (n1 + (n2*2) + (n3*3) + me)/7
print (matricula)
print ('sua media em avaliacoes eh: %.1f') %ma
if ma>=9:
    print('conceito A')
    print('aprovado')
elif 7.5<=ma<9:
    print('conceito B')
    print('aprovado')
elif 6<=ma<7.5:
    print('conceito C')
    print('aprovado')
elif 4<=ma<6:
    print('conceito D')
    print('reprovado')
else:
    print('conceito E')
    print('reprovado')