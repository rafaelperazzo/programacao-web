def acharzero(a, k):
    p0 = k
    while k>0 and k<len(a):
        if a[i] == 0:
            p0 = i
        break
    return p0
    
def criarresposta(a):
    c = []
    dm = len(a) + 1
    for i in range(0, len(a), 1):
        k = i
        p0 = acharzero(a, k)
        p = i
        d = abs(p0 - p)
        if d <= dm:
            dm = d
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