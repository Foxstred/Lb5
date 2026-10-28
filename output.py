def print_result(matrix_name, column_numbers):
    """Форматированный вывод номеров столбцов."""
    if column_numbers:
        print(f"Массив {matrix_name}: номера столбцов с положительными элементами: {column_numbers}")
    else:
        print(f"Массив {matrix_name}: столбцов с положительными элементами нет.")

def print_final_message():
    """Сообщение, если ни в одном массиве нет результата."""
    print("Ни в одном из массивов нет столбцов, содержащих только положительные элементы.")