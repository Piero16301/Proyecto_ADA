import numpy as np
def peso(match):
    if isinstance(match[0], int) and isinstance(match[1], int):
        return match[0] / match[1]
    elif isinstance(match[0], int):
        temp = match[0]
        sum = 0
        for i in match[1]:
            sum += i
        return temp / sum
    else:
        temp = match[1]
        sum = 0
        for i in range(np.shape(match[0])[1]):
            sum += match[0][i]
        #for i in match[0]:
        #    sum += i
        return sum / temp


def sum(vec):
    if len(vec) == 0:
        return 0
    result = 0
    print(vec)
    print(np.shape(vec));
    for i in range(np.shape(vec)[1]):
        result += peso(vec[i])
    #for i in np.nditer(vec):
    #    result += peso(i)
    return result


def minsum(vec):
    if len(vec) == 0:
        return None
    result = vec[0]
    for i in vec:
        if sum(result) > sum(i):
            result = i
    return result


memoria = {}


def Min_Matching_Memorized(A, B):
    i = len(A) - 1
    j = len(B) - 1
    if i == 0 and j == 0:
        return [(A[i], B[j])]
    elif i == 0 or j == 0:
        if i == 0:
            match = (A[i], [])
            for it in range(j + 1):
                match[1].append(B[it])
            return [match]
        else:
            match = ([], B[j])
            for it in range(i + 1):
                match[0].append(A[it])
            return [match]
    else:
        if memoria.get(i):
            if memoria[i].get(j):
                return memoria[i][j].copy()
        pesos = []
        match = []
        match = Min_Matching_Memorized(A[:i], B[:j])
        match.append((A[i], B[j]))
        pesos.append(match)
        for it in range(1, i):
            matches = Min_Matching_Memorized(A[:it], B[:j])
            match = ([], B[j])
            for elm in range(it, i + 1):
                match[0].append(A[elm])
            matches.append(match)
            pesos.append(matches)
        for it in range(1, j):
            matches = Min_Matching_Memorized(A[:i], B[:it])
            match = (A[i], [])
            for elm in range(it, j + 1):
                match[1].append(B[elm])
            matches.append(match)
            pesos.append(matches)
        minp = minsum(pesos)
        if memoria.get(i):
            memoria[i][j] = minp
        else:
            memoria[i] = {}
            memoria[i][j] = minp
        return memoria[i][j].copy()


def CleanMemoria():
    memoria.clear()
