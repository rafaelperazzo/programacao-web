a = int(input("Quanto vc ganha por hora? "))
h = int(input("Quantas horas vc trabalha por mês? "))
b = a*h
print("Salário bruto é igual a %.d" %(b))
inss = b*0.08
print("valor pago ao inss é igual a %.d" %(inss))
sindicato = b*0.05
print("valor pago ao sindicato é igual a %.d" %(sindicato))
l = b*0.76
print("%.d" %(l))
    