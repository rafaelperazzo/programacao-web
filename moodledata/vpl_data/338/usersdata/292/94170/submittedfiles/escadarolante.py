# -*- coding: utf-8 -*-
n = int(input("Digite o número de pessoas que o sensor detectou: "))
k, temp_t, dt = [], 0, 0
for i in range(1, n+1):
    k.append(int(input("Digite o instante em que a %dº pessoa passou: "%i)))
del n

for i in range(0, len(k)-1):
    dt = k[i+1] - k[i]
    if dt > 10:
        dt = 10
        
    temp_t += dt
temp_t += 10
del k, dt
print(temp_t)