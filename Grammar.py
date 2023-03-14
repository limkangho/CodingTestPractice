a = list()
print("a =", a)

b = []
print("b =", b)

c = [0] * 10
print("c =", c)

print("c[1 : 4] =", c[1:4])

array1 = [i for i in range(20) if i%2 == 1]
print("array1 =", array1)

array2 = []
for i in range(20):
  if i%2 == 1:
    array2.append(i)
print("array2 =", array2)

array3 = [i * i for i in range(1, 10)]
print("array3 =", array3)

n = 3
m = 4
array4 = [[0] * m for _ in range(n)]
print("array4 =", array4)