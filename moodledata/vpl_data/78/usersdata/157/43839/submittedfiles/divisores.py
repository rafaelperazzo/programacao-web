n=int(input('Informe a quantidade de multiplos:'))
a=int(input('Informe o primeiro numero:'))
b=int(input('Informe o segundo numero:'))
cont=0
i=1
while (cont<n):
    if (i%a==0) or (i%b==0):
        cont=cont+1
        print(i)
    i=i+1