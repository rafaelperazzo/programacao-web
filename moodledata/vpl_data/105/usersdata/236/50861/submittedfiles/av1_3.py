# -*- coding: utf-8 -*-
import math

n1= int(input('digite n1:'))
n2= int(input('digite n2:'))
n3= int(input('digite n3:'))
i=1
MMC= n1*i
while MMC%n1!=0 or MMC%n2!=0 or MMC%n3!=0:
    
    i=i+1
print (MMC)
