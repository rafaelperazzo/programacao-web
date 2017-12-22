# -*- coding: utf-8 -*-

def crescente ():
    #escreva o código da função crescente aqui
    if (a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[4] or a[4]==a[5]):
        False
    else:
        if (a[0] < a[1] and a[1] < a[2] and a[2] < a[3] and a[3] < a[4] and a[4] < a[5]):
            print('S')
        else:
            print('N')
    

#escreva as demais funções
def descrescente ():
    if (a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[4] or a[4]==a[5]):
        False
    else:
        if (a[0] > a[1] and a[1] > a[2] and a[2] > a[3] and a[3] > a[4] and a[4] > a[5]):
            print('S')
        else:
            print('N')

def el_iguais ():
    if (a[0]==a[1] or a[1]==a[2] or a[2]==a[3] or a[3]==a[4] or a[4]==a[5]):
        print('S')
    else:
        print('N')

#escreva o programa principal
a= [1,2,3,4,5,6]
b= [7,6,5,4,3,2]
c= [9,8,8,8,9,1]

print(crescente(a))
print(descrescente(a))
print(el_iguais(a))

print(crescente(b))
print(descrescente(b))
print(el_iguais(b))

print(crescente(c))
print(descrescente(c))
print(el_iguais(c))