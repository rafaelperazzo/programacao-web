# -*- coding: utf-8 -*-
q=int(input('digite o total de pessoas :'))

soma=0
for i in range(0,q,1):
    idade=int(input('digite a idade da pessoa:'))
    soma=soma+idade
media=soma/q
print(media)
    