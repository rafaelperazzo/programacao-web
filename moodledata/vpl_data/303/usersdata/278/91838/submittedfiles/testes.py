a = [7.0, 3.5, 2.0]
z = len(a)
a.append(0.0)
z1 = len(a)
print(len(a))
# 0.0 na posição 2
for i in range (1,z,1):
    x = del a[i]
    a.append(x)
print(a)