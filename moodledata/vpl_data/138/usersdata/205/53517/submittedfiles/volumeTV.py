 -*- coding: utf-8 -*-
 v=int(input('digite o volume:'))
 t=int(input('digite quantas vezes houve a troca:'))
 volume=v
 cont=0
 for i in range ( 1, t+1, 1):
     a=int(input('digite a modificação do volume:'))
     volume=volume+a
     if ( volume>100):
         volume=100
     if ( volume<0):
         volume=0
print ( volume)