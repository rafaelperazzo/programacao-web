# -*- coding: utf-8 -*-
n=int(input('Digite um número:'))
if n<9999999:
    print('NAO SEI')
elif n>99999999:
    print('NAO SEI')
else:
    print('8')
a=(n//10000000)+(n//1000000)+(n//100000)+(n//10000)+(n//1000)+(n//100)+(n//10)
print(a)
    
    

    
    

