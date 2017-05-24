# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
qm=int(input('Digite qm:'))
qh=int(input('Digite qh:'))

cont=0
mulhermaior=0
for i in range (1,qm+1,1):
    m=float(input('Digite m:'))
    cont=cont+m
    if m>=mulhermaior:
        mulhermaior=m
    else:
        mulhermenor=m

homemmaior=0
for i in range (1,qm+1,1):
    m=float(input('Digite m:'))
    if m>=homemmaior:
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