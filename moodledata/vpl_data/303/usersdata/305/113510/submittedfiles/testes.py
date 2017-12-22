# -*- coding: utf-8 -*-
from minha_bib import *
#COMECE A PARTIR DAQUI!
'''
while(True):
    while(True):
        n = int(input('Digite um número inteiro positivo: '))
        if (n >= 0):
            break
    f = 1
    for i in range (2,n+1,1):
        f *= i
    print('%d! = %d' %(n,f))
    opt = input('Deseja continuar? [S ou N]')
    if (opt == 'N'):
        print('\n\nATÉ BREVE!')
        break

n = int(input('Digite o valor de n: '))
i = 2
contador = 0
while (i < (n-1)):
    if n%i == 0 :
        contador += 1
    i += 1
if contador > 0 :
    print('%d NAO EH primo!' %n)
else:
    print('%d EH PRIMO!' %n)

i = int(input('Digite o valor de i: '))
for i in range (0,101,6):
    print(i)
   
i = int(input('Digite o valor de i: '))
for i in range (0,100,2):
    if i == 0:
        continue
    print(i)

def raiz(x,n):
    resultado = x**(1/float(n))
    return resultado
print(raiz(729,3))    

def primo(n):
    contador = 0
    for i in range (2,n,1):
        if n%i == 0:
            contador += 1
            break
    if contador == 0:
        return True
    else:
        return False
print(primo(51))

def conta_digitos(n):
    contador = 1
    while (n//10>0):
        n = n//10
        contador += 1
    return contador
print(conta_digitos(3857679))
print(conta_digitos(6597956456))

b = 0
a = 100
for i in range (0,a,1):
    if a%(i + 1) != 0:
        b = b + 1
print(b) 

print(multiplicacao(2,multiplicacao(2,4)))

cronometro(100)

matriz = []
M = int(input('Digite o número de quadras na direção Norte-Sul: '))
while M < 2 or M > 1000:
    M = int(input('Digite o número de quadras na direção Norte-Sul: '))
N = int(input('Digite o número de quadras na direção Lste-Oeste: '))    
while N < 2 or N > 1000:
    N = int(input('Digite o número de quadras na direção Leste-Oeste: '))
for i in range (0,M,1):
    linha = []
    for j in range (0,N,1):
        linha.append(int(input('Digite o valor da respectiva Quadra: ')))
    matriz.append(linha)

menor = (100*M) + 1
for j in range (0,N,1):
    soma = 0
    for i in range (0,M,1):
        soma += matriz[i][j]
    if soma < menor:
        menor = soma
    
print(menor)

n = int(input('Digite um número inteiro: '))
i = 1
cont = 0
while(i < n):
    if i%2 == 1:
        cont += 1
    i += 1
print(cont)

n = int(input('Digite o valor de n: '))
for i in range (0,n+1,1):
    print('Hello world') 

notas = []
for i in range (0,5,1):
    notas.append(float(input('Digite a nota %d : ' %(i+1))))
media = 0 
for i in range (0,5,1):
    media += notas[i]/5.0
if media >= 7 and media <= 10:
    print('aprovado,boas ferias')
elif media >= 5 and media < 7:
    print('recuperação')
else:
    print('reprovado,estude mais')
   
a = []
for i in range (1,11,1):
    a.append(int(input('Digite o elemento %d : ' %i)))
for i in range (9,-1,-1):
    print(a[i])

linhas = 5
colunas = 3
turma = []
for i in range (0,linhas,1):
    for j in range (0,colunas,1):
        turma.append(float(input('Digite a nota %d do aluno %d : ' %((j+1),(i+1)))))
print(turma)        

n = int(input('Digite a ordem do tabuleiro: '))
tabuleiro = []
for i in range (0,n,1):
    tabuleiro_linha = []
    for j in range (0,n,1):
        tabuleiro_linha.append(int(input('Digite o valor (%d,%d) : ' %((i + 1),(j + 1)))))
    tabuleiro.append(tabuleiro_linha)
    
soma_linha = []
for i in range (0,n,1):
    cont1 = 0
    for j in  range (0,n,1):
        cont1 += tabuleiro[i][j]
    soma_linha.append(cont1)
    
soma_coluna = []
for j in range (0,n,1):
    cont2 = 0
    for i in range (0,n,1):
        cont2 += tabuleiro[i][j]
    soma_coluna.append(cont2)
    
peça = 0
for i in range (0,n,1):
    for j in range (0,n,1):
        if (soma_linha[i] + soma_coluna[j] - 2*tabuleiro[i][j]) > peça:
            peça = soma_linha[i] + soma_coluna[j] - 2*tabuleiro[i][j]
print(peça)            
'''
def modulo_diferença(x,y):
    dif = x - y
    if dif < 0:
        dif = dif*(-1)
        return(dif)
    else:
        return(dif)
        
lista = []
degrau = 0
n = int(input('Digite a quantidade de elentos da lista: '))
if n < 2:
    n = int(input('Digite a quantidade de elentos da lista: '))
    else:
        break
    
for i in range (0,n,1):
    lista.append(int(input('Digite o valor do %dº elemento  da lista: ' %(i+1))))
for i in range (0,n-1,1):
    if modulo_diferença(lista[i],lista[i+1]) > degrau:
        degrau = modulo_diferença(lista[i],lista[i+1])
print(degrau)        