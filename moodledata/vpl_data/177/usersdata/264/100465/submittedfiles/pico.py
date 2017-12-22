# -*- coding: utf-8 -*-

def pico(lista):
   contcres=0
   contdecres=0
   for i in range (0,len(lista),1):
       if lista[i]<lista[i+1]:
           contcres= contcres+1
