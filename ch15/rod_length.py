# def optimal_cut(rod_length, cut_length, price_table, profit=0, temp=None, final=None):
#     if temp is None:
#         temp = [0 for _ in range(len(price_table))]
#     if final is None:
#         final = [0 for _ in range(len(price_table))]
#
#     max_cut = rod_length // cut_length
#     if cut_length == 1:
#         temp[cut_length] = max_cut
#         earn = sum(t*p for t, p in zip(temp, price_table))
#         if earn > profit:
#             profit = earn
#             final = temp.copy()
#     elif max_cut == 0:
#         temp[cut_length] = 0
#         profit, final = optimal_cut(rod_length, cut_length - 1, price_table, profit, temp, final)
#     else:
#         for cut in range(max_cut, -1, -1):
#             temp[cut_length] = cut
#             profit, final = optimal_cut(rod_length - cut * cut_length, cut_length-1, price_table, profit, temp, final)
#     return profit, final


def optimal_cut2(price_table, len_rod):
    revenue = [0 for _ in range(len_rod + 1)]
    for part in range(1, len_rod+1):
        profit = 0
        for cut in range(part):
            profit = max(profit, price_table[cut]+revenue[part-cut-1])

        revenue[part] = profit
        if part == len(price_table):
            price_table.append(profit)
    return revenue, price_table


def optimal_cut_with_solution(price_table, len_rod):
    revenue = [0 for _ in range(len_rod + 1)]
    solution = [0 for _ in range(len_rod)]
    for part in range(1, len_rod + 1):
        profit = 0
        for cut in range(part):
            if profit <= price_table[cut] + revenue[part - cut - 1]:
                profit = price_table[cut] + revenue[part - cut - 1]
                solution[part - 1] = cut

        revenue[part] = profit
        if part == len(price_table):
            price_table.append(profit)
    return revenue, solution, price_table


def optimal_cut_solution(price_table, len_rod):
    revenue, solution, price_table = optimal_cut_with_solution(price_table, len_rod)
    combinations = []
    while len_rod > 0:
        combinations.append(solution[len_rod-1]+1)
        len_rod -= solution[len_rod-1]+1
    return combinations


if __name__ == '__main__':
    price_table_original = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    price_table = price_table_original.copy()
    rod_length = 30
    # revenue, new_price_table = optimal_cut2(price_table, rod_length)
    revenue, solution, new_price_table = optimal_cut_with_solution(price_table, rod_length)
    combinations = optimal_cut_solution(price_table, rod_length)
    print('price table    :', price_table_original)
    print('new price table:', new_price_table)
    print('revenue        :', revenue)
    print('solution       :', solution)
    print('combination    :', combinations)
