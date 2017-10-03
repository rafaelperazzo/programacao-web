# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('Que horas são? [0-23]'))
if a<2 and a>23:
   print('Hora Inválida!')
else:
    if a>3 and a <12:   
        print('Bom dia!')
    elif a>=12 and a<18:  
        print('Boa tarde!')
    elif a>=18 and a<23:  
        print('Boa noite!')
c=input('Digite um caractere: ')
if (c== 'a' or c== 'e' or c== 'i' or c== 'o' or c== 'u'):
    print('É uma vogal!')
else:
    print('Não é uma vogal!')
