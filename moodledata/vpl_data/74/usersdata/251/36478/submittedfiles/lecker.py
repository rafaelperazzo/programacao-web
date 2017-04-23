# -*- coding: utf-8 -*-
import math
n1 = int (input('Digite o valor 1: '))
n2 = int (input('Digite o valor 2: '))
n3 = int (input('Digite o valor 3: '))
n4 = int (input('Digite o valor 4: '))
decisao = 0

if a>b:
    decisao = decisao+1

if b>a and b>c:
    decisao = decisao+1
    
if c>b and c>d:
    decisao = decisao+1
    
if d>c:
    decisao = decisao+1
    
if decisao==1:
    print('S')
    
else:
    print('N')