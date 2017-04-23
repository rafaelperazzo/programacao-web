# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite n:'))
d=1
num=2
i=1
termo=1
while i<=n:
    termo=termo*(num/d)
    if d<num:
        d=d+2
    else:
        num=num+2
    i=i+1
termo=termo*2
print('%.5f'%termo)
    
    
        
    
