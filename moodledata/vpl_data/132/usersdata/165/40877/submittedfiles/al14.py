# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de pessoas:'))
media=0
for termo in range (1,n+1,1):
    x=int(input('digite a idade:'))
    media=(media+x)/n
print(media)    