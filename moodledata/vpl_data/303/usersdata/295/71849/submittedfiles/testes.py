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


