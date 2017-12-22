def converterDecimal(valor):
    resultado = 0
    for i in range (0, len(valor), 1):
        resultado += int(valor[i])*(2**(i))
    return resultado

print(converterDecimal('1011'))

