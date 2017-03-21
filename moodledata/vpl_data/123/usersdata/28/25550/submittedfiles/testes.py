def distanciamenor(p0, p):
    dmenor = 0
    d = abs(p0 - p)
    if d <= dmenor:
        dmenor = d
    return dmenor
    
def criarresposta(a):
    c = []
    for i in range(0, len(a), 1):
        zero = a[i]
        p = i
        if zero == 0:
            p0 = p
            dm = distanciamenor(p0, p)
            c.append(dm)
    return c
    
n = input('Digite o numero de quadrados da fita:')
print ('Agora prepare-se para digitar as cores de cada quadrado da fita, -1 para nao colorido com o tom 0 e 0 se estiver colorido com o tom 0')
a = []
for i in range(0, n, 1):
    num = i + 1
    a.append(int(input('Digite a cor do %d quadrado:' %num)))
print a
distm = []
distm = criarresposta(a)
print distm