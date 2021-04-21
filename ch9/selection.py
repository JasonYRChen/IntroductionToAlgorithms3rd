from random import randrange


def partition(array, start, end):
    mid = randrange(start, end+1)
    array[mid], array[end] = array[end], array[mid]
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


def group_select(array, item_no, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = 0
    


if __name__ == '__main__':
    a = [randrange(10) for _ in range(11)]
    b = a.copy()
    b.sort()
    print(a)
    print(b)
    ith_item = random_select(a, 5)
    print(ith_item, b[5])
