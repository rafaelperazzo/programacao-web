
n= input ('digite a quantidade de divisores desejados: ')
a= int(input('digite o valor de a: '))
b= int(input('digite o valor de b:' ))
c= 1

while n>0:
    if c%a==0 or c%b==0:
        print c
        n= n-1
    c= c+ 1
