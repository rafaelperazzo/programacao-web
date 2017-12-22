# -*- coding: utf-8 -*-

def crescente (a):
    #escreva o código da função crescente aqui
    if (a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[4] or a[4]==a[5]):
        False
    else:
        if (a[0] < a[1] and a[1] < a[2] and a[2] < a[3] and a[3] < a[4] and a[4] < a[5]):
            print('S')
        else:
            print('N')
def crescente (b):
    #escreva o código da função crescente aqui
    if (b[0]==b[1] or b[1]==b[2] or b[2]==b[3] or b[3]==b[4] or b[4]==b[5]):
        False
    else:
        if (b[0] < b[1] and b[1] < b[2] and b[2] < b[3] and b[3] < b[4] and b[4] < b[5]):
            print('S')
        else:
            print('N')
def crescente (c):
    #escreva o código da função crescente aqui
    if (c[0]==c[1] or c[1]==c[2] or c[2]==c[3] or c[3]==c[4] or c[4]==c[5]):
        False
    else:
        if (c[0] < c[1] and c[1] < c[2] and c[2] < c[3] and c[3] < c[4] and c[4] < c[5]):
            print('S')
        else:
            print('N')

#escreva as demais funções
def descrescente (a):
    if (a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[4] or a[4]==a[5]):
        False
    else:
        if (a[0] > a[1] and a[1] > a[2] and a[2] > a[3] and a[3] > a[4] and a[4] > a[5]):
            print('S')
        else:
            print('N')

def descrescente (b):
    if (b[0]==b[1] or b[1]==b[2] or b[2]==b[3] or b[3]==b[4] or b[4]==b[5]):
        False
    else:
        if (b[0] > b[1] and b[1] > b[2] and b[2] > b[3] and b[3] > b[4] and b[4] > b[5]):
            print('S')
        else:
            print('N')
            
def descrescente (c):
    if (c[0]==c[1] or c[1]==c[2] or c[2]==c[3] or c[3]==c[4] or c[4]==c[5]):
        False
    else:
        if (c[0] > c[1] and c[1] > c[2] and c[2] > c[3] and c[3] > c[4] and c[4] > c[5]):
            print('S')
        else:
            print('N')

def el_iguais (a):
    if (a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[4] or a[4]==a[5]):
        print('S')
    else:
        print('N')

#escreva o programa principal
n= int(input('Digite quantidade de elementos da lista: '))
a=[1,2,3,4,5,6]
b=[7,6,5,4,3,2]
c=[9,8,8,8,9,1]

crescente(a)
descrescente(a)
el_iguais(a)

crescente(b)
descrescente(b)
el_iguais(b)

crescente(c)
descrescente(c)
el_iguais(c)

