notas[]
n_notas=int(input('Quantas notas você quer ler? ')
for i in range(0,n_notas,1):
    notas+=float(input('Digite a nota %d: '%(i+1))
    
med=sum(notas)/n_notas

print(med)