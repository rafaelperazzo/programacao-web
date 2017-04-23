# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

if a>b and a>c and a>d and a>e and b>c and b>d and b>e:
    print ('%f'%a)
    print ('%f'%b)
elif a>b and a>c and a>d and a>e and c>b and c>d and c>e:
    print ('%f'%a)
    print ('%f'%c)
elif a>b and a>c and a>d and a>e and d>b and d>c and d>e:
    print ('%f'%a)
    print ('%f'%d)
elif a>b and a>c and a>d and a>e and e>b and e>c and e>d:
    print ('%f'%a)
    print ('%f'%e)
elif b>a and b>c and b>d and b>e and a>c and a>d and a>e:
    print ('%f'%b)
    print ('%f'%a)
elif b>a and b>c and b>d and b>e and c>a and c>d and c>e:
    print ('%f'%b)
    print ('%f'%c)
elif b>a and b>c and b>d and b>e and d>a and d>c and d>e:
    print ('%f'%b)
    print ('%f'%d)
elif b>a and b>c and b>d and b>e and e>a and e>c and e>d:
    print ('%f'%b)
    print ('%f'%e)
elif c>a and c>b and c>d and c>e and a>b and a>d and a>e:
    print ('%f'%c)
    print ('%f'%a)
elif c>a and c>b and c>d and c>e and b>a and b>d and b>e:
    print ('%f'%c)
    print ('%f'%b)
elif c>a and c>b and c>d and c>e and d>a and d>b and d>e:
    print ('%f'%c)
    print ('%f'%d)
elif c>a and c>b and c>d and c>e and e>a and e>b and e>d:
    print ('%f'%c)
    print ('%f'%e)
elif d>a and d>b and d>c and d>e and a>b and a>c and a>e:
    print ('%f'%d)
    print ('%f'%a)
elif d>a and d>b and d>c and d>e and b>a and b>c and b>e:
    print ('%f'%d)
    print ('%f'%b)
elif d>a and d>b and d>c and d>e and c>a and c>b and c>e:
    print ('%f'%d)
    print ('%f'%c)
elif d>a and d>b and d>c and d>e and e>a and e>b and e>c:
    print ('%f'%d)
    print ('%f'%e)
elif e>a and e>b and e>c and e>d and a>b and a>c and a>d:
    print ('%f'%e)
    print ('%f'%a)
elif e>a and e>b and e>c and e>d and b>a and b>c and b>d:
    print ('%f'%e)
    print ('%f'%b)
elif e>a and e>b and e>c and e>d and c>a and c>b and c>d:
    print ('%f'%e)
    print ('%f'%c)
elif e>a and e>b and e>c and e>d and d>a and d>b and d>c:
    print ('%f'%e)
    print ('%f'%d)