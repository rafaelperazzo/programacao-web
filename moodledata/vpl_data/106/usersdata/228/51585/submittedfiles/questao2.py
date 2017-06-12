# -*- coding: utf-8 -*-
y1=int(input('numero apostado:'))
y2=int(input('numero apostado:'))
y3=int(input('numero apostado:'))
y4=int(input('numero apostado:'))
y5=int(input('numero apostado:'))
y6=int(input('numero apostado:'))

s1=int(input('número sorteado:'))
s2=int(input('número sorteado:'))
s3=int(input('número sorteado:'))
s4=int(input('número sorteado:'))
s5=int(input('número sorteado:'))
s6=int(input('número sorteado:'))
 
cont=0
for i in range (0,7,1):
    if y1==s1 or y1==s2 or y1==s3 or y1==s4 or y1==s5 or y1==s6:
        cont=cont+1
    if y2==s1 or y2==s2 or y2==s3 or y2==s4 or y2==s5 or y2==s6:
        cont=cont+1
    if y3==s1 or y3==s2 or y3==s3 or y3==s4 or y3==s5 or y3==s6:
        cont=cont+1
    if y4==s1 or y4==s2 or y4==s3 or y4==s4 or y4==s5 or y4==s6:
        cont=cont+1   
    if y5==s1 or y5==s2 or y5==s3 or y5==s4 or y5==s5 or y5==s6:
        cont=cont+1    
    if y6==s1 or y1==s2 or y6==s3 or y6==s4 or y6==s5 or y6==s6:
        cont=cont+1    
if cont==3:
    print('terno')
elif cont==4:
    print('quadra')
elif cont==5:
    print('quina')
elif cont==6:
    print('sena')
else:
    print('azar')
        
        
        
        
        
        
        
        
