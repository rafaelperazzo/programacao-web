# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
if a<b and a<=c and a<=d and a<=e and b>=a and b>=c and b>=d and b>=e:
    print('a')
    print('b')
elif a<=b and a<=c and a<=d and a<=e and c>=a and c>=b and c>=d and c>=e:
    print('a')
    print('c')
elif  a<=b and a<=c and a<=d and a<=e and d>=a and d>=b and d>=c and d>=e:
    print('a')
    print('d')
elif  a<=b and a<=c and a<=d and a<=e and e>=a and e>=b and e>=c and e>=d:
    print('a')
    print('e')
else:
    if b<=a and b<=c and b<=d and b<=e and a>=b and a>=c and a>=d and a>=e:
        print('b')
        print('a')
    elif  b<=a and b<=c and b<=d and b<=e and c>=a and c>=b and c>=d and c>=e:
        print('b')
        print('c')
    elif  b<=a and b<=c and b<=d and b<=e and d>=a and d>=b and d>=c and d>=e:
        print('b')
        print('d')
    elif  b<=a and b<=c and b<=d and b<=e and e>=a and e>=b and e>=c and e>=d:
        print('b')
        print('e')
    else:
        if  c<=a and c<=b and c<=d and c<=e and a>=b and a>=c and a>=d and a>=e:
            print('c')
            print('a')
        elif  c<=a and c<=b and c<=d and c<=e and b>=a and b>=c and b>=d and b>=e:
            print('c')
            print('b')
        elif c<=a and c<=b and c<=d and c<=e and d>=a and d>=b and d>=c and d>=e:
            print('c')
            print('d')
        elif c<=a and c<=b and c<=d and c<=e and e>=a and e>=b and e>=c and e>=d:
            print('c')
            print('e')
        else:
            if d<=a and d<=b and d<=c and d<=e and a>=b and a>=c and a>=d and a>=e:
                print('d')
                print('a')
            elif d<=a and d<=b and d<=c and d<=e and b>=a and b>=c and b>=d and b>=e:
                print('d')
                print('b')
            elif d<=a and d<=b and d<=c and d<=e and c>=a and c>=b and c>=d and c>=e:
                print('d')
                print('c')
            elif d<=a and d<=b and d<=c and d<=e and e>=a and e>=b and e>=c and e>=d:
                print('d')
                print('e')
            else:
                if e<=a and e<=b and e<=c and e<=d and a>=b and a>=c and a>=d and a>=e:
                    print('e')
                    print('a')
                elif e<=a and e<=b and e<=c and e<=d and b>=a and b>=c and b>=d and b>=e:
                    print('e')
                    print('b')
                elif e<=a and e<=b and e<=c and e<=d and c>=a and c>=b and c>=d and c>=e:
                    print('e')
                    print('c')
                elif e<=a and e<=b and e<=c and e<=d and d>=a and d>=b and d>=c and d>=e:
                    print('e')
                    print('d')