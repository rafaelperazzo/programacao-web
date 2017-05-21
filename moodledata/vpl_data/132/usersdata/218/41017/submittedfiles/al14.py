# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas:'))
i=0
termo=n
while n>0:
    id=int(input('digite a idade:'))
    i=i+id
    termo=termo-1
media=(i/n)
print(media)