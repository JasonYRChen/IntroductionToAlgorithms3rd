from random import shuffle, randrange
from time import time


def insertion_sort(seq):
    for i in range(1, len(seq)):
        while i > 0 and seq[i] < seq[i-1]:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1


def merge_sort(seq, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        s1 = merge_sort(seq, start, mid)
        s2 = merge_sort(seq, mid, end)
        i = j = 0
        while i + j < len(s1) + len(s2):
            if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
                seq[start+i+j] = s1[i]
                i += 1
            else:
                seq[start+i+j] = s2[j]
                j += 1
    return seq[start:end]


def merge_sort_fast(seq, start, end, k=5):
    if end - start > k:
        mid = (start + end) // 2
        s1 = merge_sort(seq, start, mid)
        s2 = merge_sort(seq, mid, end)
        i = j = 0
        while i + j < len(s1) + len(s2):
            if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
                seq[start+i+j] = s1[i]
                i += 1
            else:
                seq[start+i+j] = s2[j]
                j += 1
    else:
        subseq = seq[start:end]
        insertion_sort(subseq)
        seq[start:end] = subseq
    return seq[start:end]


def speed(func, seq_len=10, repeat=30, **kwargs):
    start = time()
    for i in range(repeat):
        seq = [randrange(7) for _ in range(seq_len)]
        func(seq, **kwargs)
    elapse = time() - start
    avg = elapse / repeat
    print("average running time:", avg)


speed(insertion_sort, 40, 50)
speed(merge_sort, 40, 50, start=0, end=40)
speed(merge_sort_fast, 40, 50, start=0, end=40, k=10)
