# -*- coding: utf-8 -*-
Day01=int(input('Digite o Dia:'))
Month01=int(input('Digite o Mês:'))
Year01=int(input('Digite o Ano:'))
Day02=int(input('Digite o Dia:'))
Month02=int(input('Digite o Mês:'))
Year02=int(input('Digite o Ano:'))

if (Year01>Year02):
   print('DATA 1')
elif (Year02>Year01):
   print('DATA 2')
else:
    
 if (Month01>Month02):
   print('DATA 1')
 elif (Month02>Month01):
   print('DATA 2')
 else:
  if (Day01>Day02):
   print ('DATA 1')
  elif (Day02>Day01):
   print ('DATA 2')
  else:
    