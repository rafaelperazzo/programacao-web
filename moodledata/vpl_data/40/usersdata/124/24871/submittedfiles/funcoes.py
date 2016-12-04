#ARQUIVO COM SUAS FUNCOES
def vabsol(x):
    if 0 > x:
        x = -1*x
    return x
    
def calculopi(m):
    pi = 3
    d = 2
    c = 0
    for i in range (0, m, 1):
        if i%2 != 0:
            c = c - (4/(d*(d+1)*(d+2)))
        elif i%2 == 0:
            c = c + (4/(d*(d+1)*(d+2)))
        d = d + 2
    
    return c
    
def cos(z, epsilon):
    cosz = 1
    v = 2
    fat = 1
    cont = 0
    
    for i in range (v, 0, -1):
        fat = fat*i
        
    d = (z**v)/fat
    
    if cont%2 != 0:
        cosz = cosz + d
    elif cont%2 == 0:
        cosz = cosz - d
       
    while True:
        if epsilon <= d:
            v = v + 2
            fat = 1
            cont = cont + 1
        else:
            break
    
    return cosz
    
def razaurea(m, epsilon):
    pi = calculopi(m)
    fi = 2*cos(pi/5, epsilon)
    return fi