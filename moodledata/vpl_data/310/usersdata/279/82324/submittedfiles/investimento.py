# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i=1
CONT=0


INVESTIMENTO=-1
TAXA=200










while (INVESTIMENTO<0) :
  INVESTIMENTO=float(input())
while TAXA<0 or TAXA>1 :

   TAXA=float(input())




for i in range(1,11,1) :

      
      INVESTIMENTO=INVESTIMENTO+INVESTIMENTO*TAXA

      print("%.2f" %INVESTIMENTO)

