peso = int(input("Digite o peso dos peixes:"))
if peso>50:
    excesso = peso-50
    multa = 4*excesso
    print("R$ %.d" %(multa))
else:
    print("ZERO")
    