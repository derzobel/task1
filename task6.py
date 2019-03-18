import random
n = int(input("Введите размер n матриц: "))
a = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]  # заполняем первую матрицу
b = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]  # заполняем вторую матрицу
c = [[x + y for x, y in zip(one, two)] for (one, two) in zip(a, b)]  # сложение двух матриц
print("Первая матрица: ", a)
print("Вторая матрица: ", b)
print("Результат суммы: ", c)