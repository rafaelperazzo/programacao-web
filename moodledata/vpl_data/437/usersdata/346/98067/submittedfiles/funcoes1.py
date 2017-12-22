# -*- coding: utf-8 -*-
a=[1,2,3,4,5,6]
b=[7,6,5,4,3,2]
c=[9,8,8,8,9,1]

def crescente ():
    #escreva o código da função crescente aqui
    if ([0]==[1] or [1]==[2] or [2]==[3] or [3]==[4] or [4]==[5]):
        False
    else:
        if ([0] < [1] and [1] < [2] and [2] < [3] and [3] < [4] and [4] < [5]):
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

def el_iguais (a):
    if (a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[4] or a[4]==a[5]):
        print('S')
    else:
        print('N')
    return ()
    
#escreva o programa principal
n= int(input('Digite quantidade de elementos da lista: '))
a=[1,2,3,4,5,6]
b=[7,6,5,4,3,2]
c=[9,8,8,8,9,1]

crescente(a)
crescente(b)
crescente(c)

descrescente(a)
el_iguais(a)
