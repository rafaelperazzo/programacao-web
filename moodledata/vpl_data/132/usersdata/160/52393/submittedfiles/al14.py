# -*- coding: utf-8 -*-

def soma(n):
    total=0
    for i in n:
        total+=i
    return total
def media(n):
    return (soma(n))
    
a=int(input('Digite a quantidade de pessoas:'))
if media>0:
    print('%.2f'%media)