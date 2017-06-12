# -*- coding: utf-8 -*-
i=0
while i<100:
    a = int(input('Digite o Primeiro número: ')
    b = int(input('Digite o Segundo numero: ')
    c = int(input('Digite o Terceiro número: ')
    d = int(input('Digite o Quarto número: ')
    e = int(input('Digite o Quinto número: ')
    f = int(input('Digite o Sexto número: ')
    ra = int(input('Digite o Primeiro resultado ')
    rb = int(input('Digite o Segundo resultado: ')
    rc = int(input('Digite o Terceiro resultado: ')
    rd = int(input('Digite o Quarto resultado: ')
    re = int(input('Digite o Quinto resultado: ')
    rf = int(input('Digite o Sexto resultado: ')
    if a==ra or a==rb or a==rc or a==rd or a==re or a==rf:
        s1=1
        else:
            s1=0
    elif b==ra or b==rb or b==rc or b==rd or b==re or b==rf:
        s2=1
        else:
            s2=0
    elif c==ra or c==rb or c==rc or c==rd or c==re or c==rf:
        s3=1
        else:
            s3=0
    elif d==ra or d==rb or d==rc or d==rd or d==re or d==rf:
        s4=1
        else:
            s4=0
    elif e==ra or e==rb or e==rc or e==rd or e==re or e==rf:
        s5=1
        else:
            s5=0
    elif f==ra or f==rb or f==rc or f==rd or f==re or f==rf:
        s6=1
        else:
            s6=0
    soma=s1+s2+s3+s4+s5+s6
    print(soma)
    if soma==3:
        print('Terno')
    elif soma==4:
        print('Quadra')
    elif soma==5:
        print('Quina')    
    elif soma==6:
        print('Sena')
    else:
        print('AZAR')
        
        