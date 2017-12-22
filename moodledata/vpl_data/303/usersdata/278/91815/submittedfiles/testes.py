a = [7.0, 3.5, 2.0]
a.append(0.0)
i = len(a)
# 0.0 na posição 2
for i in range (1,len(a),1):
    del a[i]
    a.append(a[i])
print(a)