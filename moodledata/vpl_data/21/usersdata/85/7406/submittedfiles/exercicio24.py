# -*- coding: utf-8 -*-
from __future__ import division
import math

a= int(input('Digite um número inteiro: '))
b= int(input('Digite um número inteiro: '))

i= 1
m= 0
if a>=b:
    while i<a:
        if a%i==0 and b%i==0:
            m= i
            
    i= i+1
            print m
if b>a:
    while i<b:
        if a%i==0 and b%i==0:
            m= i
        i= i+1
            print m