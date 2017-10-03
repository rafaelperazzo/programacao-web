# -*- coding: utf-8 -*-
def mdc(num1,num2):
    max_div=1
    for i in range(1,num2 +1):
        if num1%i==0 and num2%i==0:
            max_div=i
        
        return max_div