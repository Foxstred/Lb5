from input_module import input_matrix
from processing import get_positive_columns
from output import print_result, print_final_message

def main():
    print("Лабораторная работа № 5. Командная работа.")
    print("Поиск столбцов, содержащих только положительные элементы.\n")
    
    matrix1 = input_matrix("A")
    matrix2 = input_matrix("B")
    
    result1 = get_positive_columns(matrix1)
    result2 = get_positive_columns(matrix2)
    
    print("\nРезультаты:")
    print_result("A", result1)
    print_result("B", result2)
    
    if not result1 and not result2:
        print_final_message()

if __name__ == "__main__":
    main()