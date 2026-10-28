def is_positive_column(column):
    """Процедура проверки: все элементы столбца строго > 0."""
    return all(x > 0 for x in column)

def get_positive_columns(matrix):
    """Возвращает номера (с 1) столбцов, содержащих только положительные элементы."""
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    result = []
    for j in range(cols):
        column = [matrix[i][j] for i in range(rows)]
        if is_positive_column(column):
            result.append(j + 1)
    return result