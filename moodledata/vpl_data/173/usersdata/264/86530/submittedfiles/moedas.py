# -*- coding: utf-8 -*-
a= int(input('Digite a:'))
b= int(input('Digite b:'))
c= int(input('Digite c:'))
for i in range (0,c,1):
    if ((c-(i*a))%b)==0:
        print (i)
        ib= (c-(i*a))//b
        print (ib)
        break
    else:
        print ('N')
