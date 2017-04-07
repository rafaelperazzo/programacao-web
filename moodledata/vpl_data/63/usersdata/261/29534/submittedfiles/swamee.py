# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
def exerc_6():
    pi = math.pi
    g = 9.81
    e = 0.000002
    f = float(input("Digite o valor de f"))
    l = float(input("Digite o valor de L"))
    q = float(input("Digite o valor de Q"))
    deltah = float(input("Digite o valor de DeltaH"))
    v = float(input("Digite o valor de v"))
    
    d = ((8*f*l*q*q)/(pi*pi*g*deltah))**(1/5)
    
    
    rey = (4*q)/(pi*d*v)
    
    k = 0.25/(math.log10((e/3.7*d)+(5.74/(rey**0.9))))**2
    
    print ("D =",str(d))
    print ("Rey =",str(rey))
    print ("k =",str(k))

exerc_6()