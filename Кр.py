array = []
print('Введите пять строк через Enter: ')
for _ in range(5):
    array.append(input())

for i in range(5):
    if len(array[i]) <= 3:
        print(array[i], end = ', ')
    