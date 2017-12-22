import numpy as np

n = int (input ('Digite a dimensão do quadrado mágico: '))

while n<3:
    n = int (input('Digite a dimensão do quadrado mágico: '))

matriz = np.zeros ((n,n))
for i in range (0,n,1):
    for j in range (0,n,1):
        matriz[i,j] = int (input ('Digite os elementos do quadrado mágico: '))

somalinha = 0
somacoluna = 0

a = []
b = []

for i in range (0,matriz.shape[0],1):
  for j in range (0,matriz.shape[1],1):
    somalinha = somalinha + matriz[i,j]
  a.append (somalinha)
  somalinha = 0

for j in range (0,matriz.shape[1],1):
  for i in range (0,matriz.shape[0],1):
    somacoluna = somacoluna + matriz[i,j]
  b.append (somacoluna)
  somacoluna = 0   

c = []
d = []
for j in range (0,len (a),1):
    if a[0] == a[j]:
        c.append (j)
    if a[0] != a[j]:
        d.append (j)
        
if len (c) > len (d):
    linha = d[0]
else:
    linha = c[0]
    
e = []
f = []
for j in range (0,len (b),1):
    if b[0] == b[j]:
        e.append (j)
    if b[0] != b[j]:
        f.append (j)
        
if len (e) > len (f):
    coluna = f[0]
else:
    coluna = e[0]
    
soma = 0
soma1 = 0

for j in range (0,matriz.shape[1],1):
    soma = soma + matriz[linha,j]    

if linha == 0:
    for j in range (0,matriz.shape[1],1):
        soma1 = soma1 + matriz[1,j]

elif linha!=0:
    for j in range (0,matriz.shape[1],1):
        soma1 = soma1 + matriz[linha-1,j]

sub = soma - soma1
resposta = matriz[linha,coluna] - sub

print ('%d' %resposta)
print ('%d' %matriz[linha,coluna])
