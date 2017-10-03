# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
a=int(input(':'))
b=int(input(':'))
c=int(input(':'))
d=int(input(':'))
e=int(input(':'))
f=int(input(':'))
if a>0 and a<=13 and b>0 and b<=13 and c>0 and c<=13 and d>0 and d<=13 and e>0 and e<=13 and f>0 and f<=13:
    if a<b and b<c and c<d and d<e and e<f:
        print('C')
    elif a>b or b>c or c>d or d>e or e>f:
        print('D')
    else:
        print('N')
else:
    print('N')
