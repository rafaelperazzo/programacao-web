#entrada_da_fita_quadriculada

n = int(input('Digite o número de quadrados da fita'))
fita = []
for i in range (0,n,1):
    x = int (input('Digite a quadrícula %'))
    fita.append(x)

print (fita)

#programa_tons
cont = 0
for i in range (0,10,1):
    for j in range (0,n,1):
        if fita[j]==0:
            fita[j]=0
        if fita [j]==-1:
            if fita [j-1]==-1:
                fita [j-1] = cont+1
            if fita[j+1] ==-1:
                fita [j+1] = cont+1
print (fita)

