# -*- coding: utf-8 -*-
a=int(input('Número: '))

if a<=9999999:
    print('NAO SEI')
    if a>99999999:
        print('NAO SEI')
    else:
    b=a//10000000
    c=(a-b*10000000)
    d=c//1000000
    e=(c-d*1000000)
    f=e//100000
    g=(e-f*100000)
    h=g//10000
    i=(g-h*10000)
    j=i//1000
    k=(i-j*1000)
    l=k//100
    m=(k-l*100)
    n=m//10
    o=(m-n*10)
    p=o//1
    q=(o-p*1)
    
    r=(b+d+f+h+j+l+n+p+q)
    
    print(r)
   