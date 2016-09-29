# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor a ser sacado:'))

n1=n//20
n2=(n%20)//10
n3=((n%20)%10)//5
n4=(((n%20)%10)%5)//2
n5=((((n%20)%10)%5)%2)//1

n1=print('%d'%n1)
n2=print('%d'%n2)
n3=print('%d'%n3)
n4=print('%d'%n4)
n5=print('%d'%n5)