# -*- coding: utf-8 -*-
a=int(input('Número: '))

if a<=9999999:
    print('NAO SEI')
if a>99999999:
    print('NAO SEI')
Else:
    b=a//100000000
    c=(a-b*100000000)
    d=c//10000000
    e=(c-d*10000000)
    f=e//1000000
    g=(e-f*1000000)
    h=g//100000
    i=(g-h*100000)
    j=i//10000
    k=(i-j*10000)
    l=k//1000
    m=(k-l*1000)
    n=m//100
    o=(m-n*100)
    p=o//10
    q=(o-p*10)
    
    r=(b+d+f+h+j+l+n+p+q)
    
    print(r)
        
