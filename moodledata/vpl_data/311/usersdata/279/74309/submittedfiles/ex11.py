# -*- coding: utf-8 -*-

dia1=int(input('digite o dia'))

mes1=int(input('digite o mês'))

ano1=int(input('digite o ano'))

dia2=int(input('digite o dia'))

mes2=int(input('digite o mês'))

ano2=int(input('digite o ano'))

if ano1<ano2 :
  print('DATA 2')
  
elif ano2<ano1 :
  print('DATA 1')
  
elif mes1<mes2 :
  print('DATA 2')
  
elif mes2<mes1 :
  print('DATA 1')
  
elif dia1<dia2 :
  print('DATA2')
  
elif dia2<dia1 :
  print('DATA 1')
  
else:
  print('IGUAIS')











