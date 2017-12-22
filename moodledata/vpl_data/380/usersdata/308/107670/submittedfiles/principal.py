def converterDecimal(valor):
    resultado = 0
    expoente = 0
    for i in valor[::-1]:
        resultado = resultado + int(i)**expoente
        expoente = expoente + 1 
    return resultado

print(resultado('0101'))

