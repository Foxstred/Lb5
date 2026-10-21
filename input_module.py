def input_matrix(name):
    """Ввод двумерного массива (до 10x10) с клавиатуры."""
    while True:
        try:
            rows = int(input(f"Введите количество строк массива {name} (1..10): "))
            cols = int(input(f"Введите количество столбцов массива {name} (1..10): "))
            if 1 <= rows <= 10 and 1 <= cols <= 10:
                break
            print("Ошибка: размеры должны быть от 1 до 10.")
        except ValueError:
            print("Ошибка: введите целое число.")
    
    matrix = []
    print(f"Введите элементы массива {name} ({rows}x{cols}), числа через пробел:")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"  Строка {i + 1}: ").split()))
                if len(row) == cols:
                    matrix.append(row)
                    break
                print(f"  Ошибка: нужно ввести ровно {cols} чисел.")
            except ValueError:
                print("  Ошибка: введите числа через пробел.")
    return matrix