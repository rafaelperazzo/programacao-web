# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
if a<b and a<c and a<d and a<e and b>a and b>c and b>d and b>e:
    print('o valor de a')
    print('o valor de b')
elif a<b and a<c and a<d and a<e and c>a and c>b and c>d and c>e:
    print('o valor de a')
    print('o valor de c')
elif a<b and a<c and a<d and a<e and d>a and d>b and d>c and d>e:
    print('o valor de a')
    print('o valor de d')
elif a<b and a<c and a<d and a<e and e>a and e>b and e>c and e>d:
    print('o valor de a')
    print('o valor de e')
else:
    if b<a and b<c and b<d and b<e and a<b and a<c and a<d and a<e:
        print('o valor de b')
        print('o valor de a')
    elif b<a and b<c and b<d and b<e and c>a and c>b and c>d and c>e:
        print('o valor de b')
        print('o valor de c')
    elif b<a and b<c and b<d and b<e and d>a and d>b and d>c and d>e:
        print('o valor de b')
        print('o valor de d')
    elif b<a and b<c and b<d and b<e and e>a and e>b and e>c and e>d:
        print('o valor de b')
        print('o valor de e')
    else:
        if c<a and c<b and c<d and c<e and a>b and a>c and a>d and a>e:
            print('o valor de c')
            print('o valor de a')
        elif c<a and c<b and c<d and c<e and b>a and b>c and b>d and b>e:
            print('o valor de c')
            print('o valor de b')
        elif c<a and c<b and c<d and c<e and d>a and d>b and d>c and d>e:
            print('o valor de c')
            print('o valor de d')
        elif c<a and c<b and c<d and c<e and e>a and e>b and e>c and e>d:
            print('o valor de c')
            print('o valor de e')
        else:
            if d<a and d<b and d<c and d<e and a>b and a>c and a>d and a>e:
                print('o valor de d')
                print('o valor de a')
            elif d<a and d<b and d<c and d<e and b>a and b>c and b>d and b>e:
                print('o valor de d')
                print('o valor de b')
            elif d<a and d<b and d<c and d<e and c>a and c>b and c>d and c>e:
                print('o valor de d')
                print('o valor de c')
            elif d<a and d<b and d<c and d<e and e>a and e>b and e>c and e>d:
                print('o valor de d')
                print('o valor de e')
            else:
                if e<a and e<b and e<c and e<d and a>b and a>c and a>d and a>e:
                    print('o valor de e')
                    print('o valor de a')
                elif e<a and e<b and e<c and e<d and b>a and b>c and b>d and b>e:
                    print('o valor de e')
                    print('o valor de b')
                elif e<a and e<b and e<c and e<d and c>a and c>b and c>d and c>e:
                    print('o valor de e')
                    print('o valor de c')
                elif e<a and e<b and e<c and e<d and d>a and d>b and d>c and d>e:
                    print('o valor de e')
                    print('o valor de d')