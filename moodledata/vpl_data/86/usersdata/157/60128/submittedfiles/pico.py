def pmax(b):
    for j in range (0, len(b)-1, 1):
        if (b[j]>b[j+1]):
            return(j)
def pico(b):
    m=pmax(b)
    for j in range (m, len(b)-1, 1):
        if (b[j]<b[j+1]):
            return(False)
    return(True)
    
n=int(input('Digite os elementos da lista:'))
a=[]
for z in range (1, n+1, 1):
    valor=float(input('Digite os elementos da lista:'))
    a.append(valor)
if (pico(a)):
    print('S')
else:
    print('N')