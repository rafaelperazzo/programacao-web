import time
# inicializando matriz vazia de notas da turma
turma = []
# lendo três notas de cinco alunos
for i in range(0,5,1):
    notas = [] # inicializando lista vazia de notas
    print('notas['+str(i)+'] = ' notas)
    time.sleep(2)
    for j in range(0,3,1):
        notas.append(float(input('Digite a nota%d do aluno%d: ' % ((j+1),(i+1)))))
    print('notas['+str(i)+'] = ' notas)
    time.sleep(2)
    print('turma = ' turma)
    time.sleep(2)
    turma.append(notas) # inserindo lista de notas na matriz
    print('turma = ' turma)
    time.sleep(2)
# mostrando toda a matriz de notas
print(turma)