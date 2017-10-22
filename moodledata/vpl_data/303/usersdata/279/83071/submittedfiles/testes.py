# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def primo(n):
   contador=0
   for i in range(2,n,1):
       if n%i==0:
           contador += 1
           break
   if contador == 0 :
       return true
   else:
       return false
print(primo(8))       
print(primo(11))