turma=[]
for i in range(0,5,1):
    notas=[]
    for j in range(0,3,1):
        notas.append(float(input("Digite a nota%d do aluno%d: " %((j+1),(i+1)))))
    turma.append(notas)
print(turma)

    
        
        
    