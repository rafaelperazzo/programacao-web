a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))
cont=0
quantidade_a=c//a
quantidade_b=0
while quantidade_a>=0:
    troco=c-quantidade_a*a
    if troco%b==0:
        quantidade_b=troco//b
        cont=cont+1
    else:
        qa=qa-1
if cont>0:
    print(quantidade_a)
    print(quantidade_b)
else:
    print('N')