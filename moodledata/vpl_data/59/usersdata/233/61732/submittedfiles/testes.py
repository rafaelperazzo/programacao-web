# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
#Comentários sobre a função(calcula_pi)
# É sabido que na fórmula para calcular pi, cada fator do denominador varia dem duas unidades de termo para termo. 
#Exemplo: Se no segundo termo, temos(4/2*3*4), no terceiro, teremos(4/4*5*6). Para isso, chamaremos os fatores de a,b e c!
def calcula_pi(m):
    a=2
    b=3
    c=4
    soma=3
    for i in range(1,m+1,1):
        if i%2==0:
            soma=soma+4/(a*b*c)
        else:            
            soma=soma-4/(a*b*c)
        a=a+2
        b=b+2
        c=c+2
a=-8989
pi=calcula_valor_absoluto(a)
print(pi)
