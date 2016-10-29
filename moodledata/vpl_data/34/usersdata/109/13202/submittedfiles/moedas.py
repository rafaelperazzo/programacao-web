# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')

if a>b:
    if a>b:
        if c%a==0:
            a1=c//a
            print a1
            print '0'
        elif c%b==0:
            a2=c//b
            print '0'
            print a2
        else:
            d=c//a
            r=c%a
            e=r//b
            if r%b==0:
                print d
                print e
            else:
                print ('N')
elif b>a or b==a:
    if b>a or b==a:
        if c%a==0:
            a1=a//c
            print a1
            print '0'
        elif c%b==0:
            a2=c//b
            print 0
            print a2
        else:
            d=c//b
            r=c%b
            e=r//a
            if r%a==0:
                print e
                print d
            else:
                print ('N')