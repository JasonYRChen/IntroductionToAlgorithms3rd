def optimal_matrix_multiplication(array):
    matrix_num = len(array) - 1
    min_product = [[0]*matrix_num for _ in range(matrix_num)]
    min_combination = [[0]*matrix_num for _ in range(matrix_num)]
    product = 1
    for num in array:
        product *= num

    for end in range(1, matrix_num):
        for start in range(matrix_num - end):
            mid = start + end
            new_product = product
            for k in range(start, mid):
                if new_product > min_product[start][k] + min_product[k+1][mid] + array[start]*array[k+1]*array[mid+1]:
                    new_product = min_product[start][k] + min_product[k+1][mid] + array[start]*array[k+1]*array[mid+1]
                    min_combination[start][mid] = k
                min_product[start][mid] = new_product
    return min_product, min_combination


def matrix_product_sequence(min_combination, start, end):
    if start == end:
        return f"A{start}"
    return f"({matrix_product_sequence(min_combination, start, min_combination[start][end])}" \
           f"{matrix_product_sequence(min_combination, min_combination[start][end]+1, end)})"


def matrix_product_suggestion(matrix_dims):
    dims_array = []
    for i, (row, col) in enumerate(matrix_dims):
        if i == 0:
            dims_array.append(row)
        elif row != dims_array[-1]:
            raise ValueError('Matrix dimensions are not fit.')
        dims_array.append(col)
    min_product, min_combination = optimal_matrix_multiplication(dims_array)
    suggestion = matrix_product_sequence(min_combination, 0, len(min_combination[0])-1)
    return min_product[0][-1], suggestion


a = [30, 35, 15, 5, 10, 20, 25]
dims = [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]]
product, combination = optimal_matrix_multiplication(a)
print(product)
print(combination)
print(matrix_product_suggestion(dims))
