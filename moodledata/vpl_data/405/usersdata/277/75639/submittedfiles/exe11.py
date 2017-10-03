# -*- coding: utf-8 -*-
num = int(input('Digite num: '))
if (num%(10**7) != 0) :
    print('NAO SEI')
else:
    # 45321045
    d1 = num//(10**7)
    d2 = (num-(d1*(10**7)))//(10**6)
    print(d1)
    print(d2)