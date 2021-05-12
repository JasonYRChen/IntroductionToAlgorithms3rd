def optimal_cut(rod_length, cut_length, price_table, profit=0, temp=None, final=None):
    if temp is None:
        temp = [0 for _ in range(len(price_table))]
    if final is None:
        final = [0 for _ in range(len(price_table))]

    max_cut = rod_length // cut_length
    if cut_length == 1:
        temp[cut_length] = max_cut
        earn = sum(t*p for t, p in zip(temp, price_table))
        if earn > profit:
            profit = earn
            final = temp.copy()
    elif max_cut == 0:
        temp[cut_length] = 0
        profit, final = optimal_cut(rod_length, cut_length - 1, price_table, profit, temp, final)
    else:
        for cut in range(max_cut, -1, -1):
            temp[cut_length] = cut
            profit, final = optimal_cut(rod_length - cut * cut_length, cut_length-1, price_table, profit, temp, final)
    return profit, final


if __name__ == '__main__':
    price_table = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    rod_length = 10
    cut_length = len(price_table) - 1
    profit, segment = optimal_cut(rod_length, cut_length, price_table)
    print(profit)
    print(segment)
