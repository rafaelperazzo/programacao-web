# -*- coding: utf-8 -*-
n=int(input('n:'))
taxa=float(input('taxa'))
for i in range(1,11,1):
    investimento=n+(n*taxa)
    n=investimento
    print('%.2f' %investimento)
        
    

