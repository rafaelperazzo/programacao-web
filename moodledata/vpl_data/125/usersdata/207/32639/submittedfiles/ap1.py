# -*- coding: utf-8 -*-
n1 = input('digite n1:')
n2 = input('digite n2:')
n3= input('digite n3:')
def maior ( ):
    if n1 > n2 and n3 and n1:
        print n1, 'é o maior número ! !'
    elif n2 > n1 and n3:
        print n2, 'é o maior número ! !'
    elif n3 > n1 and n2:
        print n3, ' é o maior número ! !'
    elif n1 == n2 and n1 and n2 > n3:
        print n1, 'é o maior ! !'
    elif n1 == n3 and n1 and n3 > n2:
        print n1, 'é o maior ! !'
    elif n2 == n3 and n2 and n3 > n1:
        print n2, 'é o maior ! !'
    elif n1 == n2 and n3:
        print 'todos os números são iguais'
def menor ( ):
    if n1 < n2 and n3 and n1:
        print n1, 'é o maior número ! !'
    elif n2 < n1 and n3:
        print n2, 'é o menor número ! !'
    elif n3 < n1 and n2:
        print n3, 'é o menor número ! !'
        