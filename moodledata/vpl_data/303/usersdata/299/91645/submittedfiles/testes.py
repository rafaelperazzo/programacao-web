notas=[]
n=int(input('Quantas notas você quer ler? '))
for i in range(0,n,1):
    notas.append(float(input('Digite a nota %d: '%(i+1))))
med=sum(notas)/n
print(med)