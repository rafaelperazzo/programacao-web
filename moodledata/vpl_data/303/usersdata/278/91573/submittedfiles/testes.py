alunos = []
for i in range (0,50,1):
    alunos.append(float(input("Digite a nota do aluno%d: " %(i+1))))
media = 0
for i in range (0,50,1):
    media+=alunos[i]/5.0
print(alunos)
print(media)