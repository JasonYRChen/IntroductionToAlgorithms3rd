from random import randrange


def inversion_nsquare(seq):
    count = 0
    for i in range(len(seq)-1):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                count += 1
                yield i, j


def inversion_nlogn(seq, start, end):
    ctotal = 0
    if end - start > 1:
        mid = (start + end) // 2
        s1, c1 = inversion_nlogn(seq, start, mid)
        s2, c2 = inversion_nlogn(seq, mid, end)
        ctotal = c1 + c2
        i = j = 0
        while i + j < len(s1) + len(s2):
            if j == len(s2) or (i < len(s1) and s1[i] > s2[j]):
                seq[start+i+j] = s1[i]
                i += 1
                if j < len(s2):
                    ctotal += len(s2) - j
            else:
                seq[start+i+j] = s2[j]
                j += 1
    return seq[start:end], ctotal


s = [randrange(6) for _ in range(10)]
s_copy = s.copy()
print(s)
print(len(list(inversion_nsquare(s))))
s_result, count = inversion_nlogn(s_copy, 0, len(s))
print(s_result, count)
