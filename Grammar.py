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

d = [1, 4, 3]
print("기본리스트: d = ", d)

d.append(2)
print("삽입: d = ", d)

d.sort()
print("오름차순 정렬: d = ", d)

d.sort(reverse = True)
print("내림차순 정렬: d = ", d)

d.reverse()
print("원소 뒤집기: d = ", d)

d.insert(2, 3)
print("인덱스 2에 3 추가: d = ", d)

print("값이 3인 데이터 갯수: ", d.count(3))

d.remove(1)
print("값이 1인 데이터 삭제: ", d)

e = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in e if i not in remove_set]
print(result)

