matriz = []
m = int(input("Digite a quantidade de linhas :"))
while m<=2 or m>=1000:
    m = int(input("Digite a quantidade de linhas :"))
n = int(input("Digite a quantidade de colunas :"))
while n<=2 or n>=1000:
    n = int(input("Digite a quantidade de colunas :"))
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        matriz.append(linha)
menor = ((100*m)+1)
for j in range(0,n,1):
    soma = 0 
    for i in range(0,m,1):
        soma += matriz[i][j]
    if soma < menor:
        menor = soma
print(menor)








































n = int(input('Digite a quantidade de elementos: '))
e = []
for i in range(0,n,1):
    e.append(float(input("Digite um valor :")))

for i in range(0,n,1):
    media = sum(e)/n
print(media)
x = 0
for i in range(0,n,1):
    x += (e[i] - media)**2
des = ((1/(n-1)) * ((x)))**0.5
print(des)

print("----------------------------------------------------")



n = int(input('Digite a quantidade de elementos: '))
a = []
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))

for i in range(0,n,1):
    if a[i]% 2 ==0:
        print ([a[i]])

print("----------------------------------------------------")




n = int(input('Digite a quantidade de elementos: '))
a = []
for i in range(0,n,1):
    a.append(input('Digite um valor: '))

for i in range(0,n,1):
     if a[n - 1] %2 ==0:
         print (a[2])






lista1 = [1,2,3,8]
n = 2
for i in range (0,len(lista1),1):
    print(lista1[len(lista1)-1])   

print("----------------------------------------------------")




for i in range(1,11,1):
    a.append(float(input("Digite o elemento :")))
print(a)
print(sum(a))
print(len(a))
del a[1]
print(a)
print(len(a)) 
for i in range(9 , -1, -1):
    print(a[i])
    
print("----------------------------------------------------")

a = []
for i in range(1,11,1):
    a.append(input("Digite o elemento :"))
print(a)
for i in range(9 , -1, -1):
    print(a[i])





n = int(input("Digite o numero de notas :"))
while n<=1:
    n = int(input("Digite o numero de notas :"))
notas = []
for i in range(0,n,1):
    notas.append(float(input("Digite a nota%d[%d]: "% (i+1, i))))
media = 0 
for i in range(0,n,1):
    media += notas[i]/float(n)
print(notas)
print(media)






notas = []
for i in range(0,50,1):
    notas.append(float(input("Digite a nota%d[%d]: "% (i+1, i))))
media = 0 
for i in range(0,50,1):
    media += notas[i]/50.0
print(notas)
print(media)






n = int(input("Digite um número inteiro nao negativo :"))
i = 1
cont = 1
while i<=n:
    if n>0:
        cont = cont*i
        i = i + 1
print("%d! = %d" % (n,cont))



def primo(n):
    contador = 0
    for i in range(2,n,1):
        if n%i == 0:
            contador += 1
            break
    if contador == 0:
        return True 
    else: 
        return False 
print(primo(11))




def raiz(x,n):
    resultado = x**(1/float(n))
    return resultado 
print(raiz(8,3))





n = int(input("Digite o valor de n :"))
i = 1
cont = 0 
while i<n:
    if i%2==1:
        cont = cont + 1
    i = i + 1
print(cont)






a = float(input("Digite um numero :"))
b = a/15
print("%.4f" % b)




a = int(input("Digite um numero :"))
if a%2==0:
    print("par")
else:
    print("impar")




a = int(input("Digite um numero a:"))
b = int(input("Digite um numero b:"))
if (a + b) > 10:
    print(a)
if (a + b) > 10:
    print(b)

a = float(input("Digite um numero :"))
if a > 20:
    print(a)





p1 = float(input("Digite o peso 1 :"))
c1 = float(input("Digite o comprimento 1 :"))
p2 = float(input("Digite o peso 2 :"))
c2 = float(input("Digite o comprimento 2 :"))
if (p1*c1) == (p2*c2):
    print("0")
elif (p1*c1) > (p2*c2):
    print("-1")
else:
    print("1")



p = float(input("Digite o peso: "))
h = float(input("Digite a altura: "))
imc = p/(h**2)
if imc<20:
    print("ABAIXO")




#ENTRADA
a = int(input("que horas são? (0-23) "))
#PROCESSAMENTO E SAÍDA
if a >= 3 and a < 12:
    print("BOM DIA")
elif a >= 12 and a < 18:
    print("Boa tarde")
elif a < 3:
    print("Boa noite")
elif a >= 18:
    print("Boa noite")
else:
    print("hora invalida")

"""if a < 0 or a > 23:
    print("Hora invalida")
else:
    if a > 3 and a < 12:
        print("Bom dia")
    elif a >= 12 and a < 18:
        print("Boa tarde")
    else:
        print("Boa noite")"""
      






a= (5%2)!=0
print(a)








a = float(input("digite o ano:"))
b = float(input("é o mundial do palmeiras ou a cachaça? digite 1 ou 2 respectivamente:"))
c = float(input("se responder mundial ta falso"))





n1 = float(input("Digite n1:"))
n2 = float(input("Digite n2:"))
n3 = float(input("Digite n3:"))
total = (n1+n2+n3)
print(total)


a = (10//5)%3
print(a)

a = float(input("Digite a:"))
b = float(input("Digite b:"))
c = a+b/2
print(c)


a = 5.2
print("a=%.5f" % a)








unidade=float(input("digite uma medida em metros: "))
converte=(unidade*100)
print("o valor em cetimetros da unidade é %2.f" %converte)

















nota1=float(input("digite nota 1: "))
print(nota1)
nota2=float(input("digite nota 2: "))
print(nota2)
nota3=float(input("digite nota 3: "))
print(nota3)
nota4=float(input("digite nota 4: "))
print(nota4)
media=((nota1+nota2+nota3+nota4)/4)
print("----------------------------")
print("a media do aluno eh %2.f" % media)
print("----------------------------")


