from random import randrange


def partition(array, start, end, pivot=None):
    pivot = randrange(start, end+1) if pivot is None else pivot
    array[pivot], array[end] = array[end], array[pivot]
    left, right = start, end - 1
    while left <= right:
        while left < end and array[left] <= array[end]:
            left += 1
        while right >= start and array[right] > array[end]:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    array[left], array[end] = array[end], array[left]
    return left


def insertion_sort(array, start, end):
    for i in range(start+1, end+1):
        while i > start and array[i-1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
            i -= 1


def random_select(array, item_no, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    candidate = partition(array, start, end)
    if item_no == candidate:
        return array[candidate]
    if item_no > candidate:
        return random_select(array, item_no, candidate+1, end)
    else:
        return random_select(array, item_no, start, candidate-1)


def group_select(array, item_no, elements=5, start=None, end=None, level=0):
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    if len(array) == 1:
        return array[0][1]
    next_array = []
    for left in range(start, end+1, elements):
        right = min(left + elements, end + 1) - 1
        insertion_sort(array, left, right)
        next_idx = (left + right) // 2
        idx = next_idx if isinstance(array[next_idx], int) else array[next_idx][1]
        next_array.append((array[next_idx], idx))
    pivot = group_select(next_array, item_no, elements, level=level+1)
    if level > 0:
        return pivot

    candidate = partition(array, start, end, pivot)
    if item_no == candidate:
        return array[candidate]
    if item_no > candidate:
        return group_select(array, item_no, elements, candidate+1, end)
    return group_select(array, item_no, elements, start, candidate-1)


if __name__ == '__main__':
    a = [randrange(11, 90) for _ in range(23)]
    print(a)
    b = a.copy()
    b.sort()
    print(b)
    # ith_item = random_select(a, 5)
    # print(ith_item, b[5])

    ith_item = group_select(a, 11, elements=6)
    print(a)
    print(ith_item, b[11])

    # insertion_sort(a, 0, len(a)-1)
    # print(a)
