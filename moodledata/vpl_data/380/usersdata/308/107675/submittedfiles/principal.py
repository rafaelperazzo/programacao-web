def converterDecimal(valor):
    resultado = 0
    expoente = 0
    for i in valor:
        resultado = resultado + int(i)**(len(valor)-expoente)
        expoente = expoente + 1 
    return resultado

print(converterDecimal('10001011'))

