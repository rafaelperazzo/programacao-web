 -*- coding: utf-8 -*-
 
 v=int(input('Digite o volume inicial:'))
 t=int(input('Digite as alterações feita no volume:'))
 i=0
 f=0
 for i in range(1,t,1):
     a=int(input('Digite a alteração feita no volume:'))
     if a>0:
         f=f+v+a
         
    else: 
        f=f+v-a
print(f)