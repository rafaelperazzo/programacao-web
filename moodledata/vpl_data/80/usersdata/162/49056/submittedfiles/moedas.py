a=(input('Digite a:'))
b=(input('Digite b:'))
c=(input('Digite c:'))
cont=0
qa=c//a
qb=0
while qa>=0:
    troco=c-qa*a
    if troco%b==0:
        qb=troco//b
        cont=cont+1
    else:
        qa=qa-1
if cont>0:
    print(qa)
    print(qb)
else:
    print('N')