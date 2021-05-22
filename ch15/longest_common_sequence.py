def lcs_matrix(s1, s2):
    matrix = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
    for row in range(len(s2)):
        for col in range(len(s1)):
            matrix[row + 1][col + 1] = 1 + matrix[row][col] if s1[col] == s2[row] else \
                max((matrix[row+1][col], matrix[row][col+1]))
    return matrix


def lcs(s1, s2):
    matrix = [[[0, []]] * (len(s1)+1)]
    for row in range(len(s2)):
        matrix.append([])
        matrix[-1].append([0, []])
        for col in range(len(s1)):
            matrix[-1].append([0, []])

            if s1[col] == s2[row]:
                matrix[row+1][col+1][0] = 1 + matrix[row][col][0]
                if matrix[row][col][1]:
                    for word in matrix[row][col][1]:
                        matrix[row+1][col+1][1].append(word + s1[col])
                else:
                    matrix[row+1][col+1][1].append(s1[col])
            elif matrix[row][col+1][0] == matrix[row+1][col][0]:
                matrix[row + 1][col + 1][0] = matrix[row+1][col][0]
                matrix[row + 1][col + 1][1].extend(matrix[row][col+1][1])
                matrix[row + 1][col + 1][1].extend(matrix[row+1][col][1])
            else:
                target = max((matrix[row][col+1], matrix[row+1][col]), key=lambda x: x[0])
                matrix[row+1][col+1][0] = target[0]
                matrix[row+1][col+1][1] = target[1]

    result = set(matrix[-1][-1][-1])
    return result


if __name__ == '__main__':
    # s1 = 'abc'
    # s2 = 'ac'
    # s1 = 'abcbdab'
    # s2 = 'bdcaba'
    s1 = 'accggtcgagtgcgcggaagccggccgaab'
    s2 = 'gtcgttcggaatgccgttgctctgtaaa'
    result = lcs(s1, s2)
    print(result)
