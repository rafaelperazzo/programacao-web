# -*- coding: utf-8 -*-
num = int(input('Digite num: '))
if num < 10000000 or num > 99999999 :
    print('NAO SEI')
else:
    # 45321045
    d1 = num//(10**7)
    d2 = (num-(d1*(10**7)))//(10**6)
    d3 = (num-(d1*(10**7))-(d2*(10**6)))//(10**5)
    d4 = (num-(d1*(10**7))-(d2*(10**6))-(d3*(10**5)))//(10**4)
    print(d1)
    print(d2)
    print(d3)
    print(d4)