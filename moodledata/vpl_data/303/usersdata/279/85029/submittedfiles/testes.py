# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO


while (True) :
 while(True) :
  n=int(input("digite um numero inteiro positivo"))
  if  (n>=0) :
     break
    f=1
    for i in range  (2,n+1,1) :
     
      f *= i
     
      print("%d!= %d"%(n,f))
      opt=input('deseja continuar?[s ou n]')
   if(opt=='n'):
     print('\n\nate breve')
     break





