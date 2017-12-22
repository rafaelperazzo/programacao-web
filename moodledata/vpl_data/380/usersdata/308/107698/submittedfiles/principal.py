def converterDecimal(valor):
    resultado = 0
    expoente = 0
    for i in range (len(valor),-1, 1):
        resultado += int(valor[i])*(2**(expoente))
        expoente += 1
    return resultado

print(converterDecimal('1011'))

