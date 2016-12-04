#ARQUIVO COM SUAS FUNCOES

#fat = caculo do fatorial

def fat(numero):
    fatorial = 1
    while numero > 0:
        fatorial = fatorial * numero
        numero = numero - 1
    return fatorial
    
#Pi = Calculando o valor de pi aproximadamente

def Pi(n_termos):
    pi = 3
    i = 1
    while i <= n_termos:
        k = i * 2.0
        a = (4.0 / (k*(k+1)*(k+2))) * ((-1)**(i+1)
        pi = pi + a
        i = i + 1
    return pi
    
#Cos: aqui calcula-se o cos(z)

def Cos(z, epsilon):
    cosx = 1.0
    j = 1
    i = 2
    while (z**i)/fat(i) >= epsilon:
        a = (-1)**j
        cosx = cosx+ a * ((z**i)/fat(i))
        j = j + 1
        i = i + 2
    return cosx
    
#RA: calculando a razão auréa

def RA(n, epsilon):
    pi_considerado = Pi(n) / 5
    aurea = 2 * Cos(pi_considerado,epsilon)
    return aurea