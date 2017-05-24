# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
qm=int(input('Digite qm:'))
qh=int(input('Digite qh:'))

m=float(input('Digite m:'))
cont=0
mulhermaior=m
for i in range (2,qm+1,1):
    m=float(input('Digite m:'))
    cont=cont+m
    if m>=mulhermaior:
        mulhermaior=m
    else:
        mulhermenor=m

h=float(input('Digite h:'))
homemmaior=h
for i in range (2,qh+1,1):
    h=float(input('Digite h:'))
    if h>=homemmaior:
        homemmaior=h
    else:
        homemmenor=h
if homemmaior>=mulhermaior:
    print('O maior do grupo tem: %.2f' %homemmaior)
else:
    print('O maior do grupo tem: %.2f' %mulhermaior)
if homemmenor<=mulhermenor:
    print('O menor do grupo tem: %.2f' %homemmenor)
else:
    print('O menor do grupo tem: %.2f' %mulhermenor)

media=cont/qm
print('A media de altura entre as mulheres é: %.2f' %media)