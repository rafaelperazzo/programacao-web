# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#!/usr/bin/python
#Para o início do programa é exigida a digitação dos dados de entrada especificados.
import math
FT=float(input("Digite o valor do fator de atrito inicial:"))
DH=float(input("Digite o valor da perda de carga distribuída mensurada em metros:"))
L=float(input("Digite o valor do comprimento da tubuação:"))
Q=float(input("Digite o valor da vazão em metros cúbicos por segundo:"))
g=float(input("Digite o valor da aceleração gravitacional em metros por segundo ao quadrado:"))
E=float(input("Digite o valor da rugosidade do Tubo em metros:"))
V=float(input("Digite o valor da viscosidade cinemática a uma temperatura fixa em [m/s²]:"))
#Depois, estimamos um erro incial maior que o exigido para possibilitar que o progrma execute o que lhe é exigido.
Erro=1
#Enquanto a diferença do valor posterior e o anterior for maior que 0.000001, o programa será executado a fim de se obter um valor confiável.
while Erro>0.000001:
#Ao iniciar o primeiro loop, os dados de entrada geram um valor para o diâmetro do tubo.
    D=((8*FT*L*(Q**2))/(((math.pi)**2)*g*DH))**(1/5)
#através dos dados de entrada e do diâmetro encontrado, é gerado um número de Reynolds.
    REY=(4*Q)/(D*V*math.pi)
#Com essas informações, o programa irá encontrar o fator de atrito atualizado.
    F=(((64/(REY)**8)+9.5*(math.log(E/(3.7*D)+5.74/(REY**0.9))-(2500/REY)**6)**(-16)))**(0.125)
#Após esse procedimento, o programa irá armazenar o fator de atrito anterior descrito em A.
    A=FT
#E o caractere FT que antes amrazenava o fator de atrito anterior, irá receber o fator de atrito atualizado durante o processo.
    FT=F
#A diferença do fator de atrito atualizado com o seu anterior irá gerar um erro e se este for sufucientemente pequeno o programa irá se encerrar,caso contrário o mesmo irá se repetir.
    Erro=FT-A
#Como o valor do fator de atrito anterior pode ser maior que o atualizado o programa ira fornecer um erro negativo, interrompendo o processo, como esse proceso é incoerente visto que o que se quer é uma apoximação satisfatória, então deve-se trabalhar somente com valores positivos.
    if Erro<0:
        Erro=Erro*(-1)
#Após os loops necessários, o programa chegará ao ponto em que não conseguirá mais satisfazer a condição inical, quando isso ocorrer, ele irá expressar os dados de saída desejados.
print("Desta forma,o fator de atrito será igual a %.6f" %F)
print("Desta forma, o diâmetro do tubo será igual a %.6f metros" %D)
print("Desta forma, o número de Reynolds será igual a %.6f" %REY)
#Por fim, a partir do número de Reynolds, o programa irá  classificar o escoamento como laminar ou turbulento em comparação com o valor 2000.
if REY<=2000:
    print("O escoamento é classificado como laminar")
else:
    print("O escoamento  é classificado como turbulento")
