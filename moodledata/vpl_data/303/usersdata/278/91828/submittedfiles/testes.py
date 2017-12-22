a = [7.0, 3.5, 2.0]
a.append(0.0)
z = len(a)-1
print(len(a))
# 0.0 na posição 2
for i in range (1,z,1):
    x = a.pop(i)
    a.append(x)
print(a)