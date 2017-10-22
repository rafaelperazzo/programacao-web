# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input())

def primo(n)   
contador = 0
for i in range (2,n,1):
    if n%i == 0:
           contador += 1
           break
    if contador == 0 :
       return true
    else:
       return false
import minha_bib
print(primo(8))