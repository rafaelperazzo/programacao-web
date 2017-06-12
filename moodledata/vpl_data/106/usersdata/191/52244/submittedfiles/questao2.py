# -*- coding: utf-8 -*-
ap1=int(input('digite o primeiro numero apostado:'))
ap2=int(input('digite o segundo numero apostado:'))
ap3=int(input('digite o terceiro numero apostado:'))
ap4=int(input('digite o quarto numero apostado:'))
ap5=int(input('digite o quinto numero apostado:'))
ap6=int(input('digite o sexto numero apostado:'))
s1=int(input('digite o primeiro numero sorteado:'))
s2=int(input('digite o segundo numero sorteado:'))
s3=int(input('digite o terceiro numero sorteado:'))
s4=int(input('digite o quarto numero sorteado:'))
s5=int(input('digite o quintonumero sorteado:'))
s6=int(input('digite o sexto numero sorteado:'))
cont=0
if ap1==s1 or ap1==s2 or ap1==s3 or ap1==s4 or ap1==s5 or ap1==s6:
    cont=cont+1
if ap2==s1 or ap2==s2 or ap2==s3 or ap2==s4 or ap2=s5 or ap2==s6:
    cont=cont+1
if ap3==s1 or ap3==s2 or ap3==s3 or ap3==s4 or ap3==s5 or ap3==s6:
    cont=cont+1
if ap4==s1 or ap4==s2 or ap4==s3 or ap4==s4 or ap4==s5 or ap4==s6:
    cont=cont+1
if ap5==s1 or ap5==s2 or ap5==s3 or ap5==s4 or ap5==s5 or ap5==s6:
    cont=cont+1
if ap6==s1 or ap6==s2 or ap6==s3 or ap6==s4 or ap6==s5 or ap6==s6:
    cont=cont+1
if cont==3:
    print('terno')
elif cont==4:
    print('quadra')
elif cont==5:
    print('quina')
elif cont==6:
    print('sena')
elif cont<3:
    print('azar')
    
