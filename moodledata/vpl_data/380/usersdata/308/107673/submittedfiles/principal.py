def converterDecimal(valor):
    resultado = 0
    expoente = 0
    for i in valor:
        resultado = resultado + int(i)**expoente
        expoente = expoente + 1 
    return resultado

print(converterDecimal('1000101'))

