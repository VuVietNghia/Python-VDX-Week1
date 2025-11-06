doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

doubles = [x * 2 for x in range(1, 11)]
triplets = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triplets)
print(squares)

traiCays = [traiCay.upper() for traiCay in ["apple", "banana", "cherry"]]

print(traiCays)

traiCays = [traiCay[0] for traiCay in ["apple", "banana", "cherry"]]
print(traiCays)

numbers = [1, -2, 3, -4, -5, 6]
positive = [num for num in numbers if num > 0]
print(positive)

listNhan3s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listNhan3 = [num * 3 for num in listNhan3s if num % 2 == 0]
print(listNhan3)
