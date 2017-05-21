# -*- coding: utf-8 -*-
Q= int(input('Digite a quantidade de pessoas:'))
SOMA=0
i=1
while i<=Q:
    IDADE= int(input('Digite a idade:'))
    SOMA=SOMA+IDADE
    MEDIA=SOMA/Q
    i=i+1
print ('%.2f'%MEDIA)
    
    

