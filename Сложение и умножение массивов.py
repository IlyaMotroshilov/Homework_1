import numpy



a = numpy.zeros((3, 3))
b = numpy.zeros((3,3))

print('Введите матрицу А: ')
for i in range(0, 3):
    for j in range(0, 3):
        a[i][j] = int(input("Ввод значения: "))

def matrix(a):
    for arr in a:
        for el in arr:
            print(el, end = ' ')
        print()
matrix(a)
print('Введите матрицу B: ')
for i in range(0, 3):
    for j in range(0, 3):
        b[i][j] = int(input("Ввод значения: "))
def matrix(b):
    for arr in b:
        for el in arr:
            print(el, end = ' ')
        print()
matrix(b)
print("Сумма матриц равна: ")
print(matrix(a)+matrix(b))

print("Произведение матриц равно: ")
print(matrix(a)*matrix(b))





