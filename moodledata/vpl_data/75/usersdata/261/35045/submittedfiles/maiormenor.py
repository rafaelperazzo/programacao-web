# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
maior = ""
menor = ""
if a>=b and a>=c and a>=d and a>=e:
    maior = a
elif b>=a and b>=c and b>=d and b>=e:
    maior = b
elif  c>=a and c>=b and c>=d and c>=e:
    maior = c
elif  d>=a and d>=b and d>=c and d>=e:
    maior = d
elif  e>=a and e>=b and e>=c and e>=d:
    maior = e

if a<=b and a<=c and a<=d and a<=e:
    menor = a
elif b<=a and b<=c and b<=d and b<=e:
    menor = b
elif c<=a and c<=b and c<=d and c<=e:
    menor = c
elif d<=a and d<=b and d<=c and d<=e:
    menor = d
elif e<=a and e<=b and e<=c and e<=d:
    menor = e

print maior
print menor



