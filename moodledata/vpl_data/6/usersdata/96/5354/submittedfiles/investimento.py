# -*- coding: utf-8 -*-
from __future__ import division

# -*- coding: utf-8 -*-
from __future__ import division

ValorInvestimento = input('Digite o valor do investimento:')
Taxa = input('Digite o valor da taxa de crescimento:')

SaldoAno1 = ValorInvestimento + (ValorInvestimento*(Taxa/100))
SaldoAno2 = SaldoAno1 + (SaldoAno1*Taxa)
SaldoAno3 = SaldoAno2 + (SaldoAno2*Taxa)
SaldoAno4 = SaldoAno3 + (SaldoAno3*Taxa)
SaldoAno5 = SaldoAno4 + (SaldoAno4*Taxa)
SaldoAno6 = SaldoAno5 + (SaldoAno5*Taxa)
SaldoAno7 = SaldoAno6 + (SaldoAno6*Taxa)
SaldoAno8 = SaldoAno7 + (SaldoAno7*Taxa)
SaldoAno9 = SaldoAno8 + (SaldoAno8*Taxa)
SaldoAno10 = SaldoAno9 + (SaldoAno9*Taxa)

print('%.2f' %SaldoAno1)
print('%.2f' %SaldoAno2)
print('%.2f' %SaldoAno3)
print('%.2f' %SaldoAno4)
print('%.2f' %SaldoAno5)
print('%.2f' %SaldoAno6)
print('%.2f' %SaldoAno7)
print('%.2f' %SaldoAno8)
print('%.2f' %SaldoAno9)
print('%.2f' %SaldoAno10)