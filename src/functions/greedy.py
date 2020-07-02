import numpy as np

"""def MinMatching(A, B):
    if len(A) > len(B):
        if len(B) == 1:
            return [(A, B[0])]
        else:
            temp = [(A[0], B[0])]
            A.remove(A[0])
            B.remove(B[0])
            temp = temp + MinMatching(A, B)
            return temp
    else:
        if len(A) == len(B):
          if len(A) == 1:
            return [(A[0], B[0])]
          else:
            temp = [(A[0], B[0])]
            A.remove(A[0])
            B.remove(B[0])
            temp = temp + MinMatching(A, B)
            return temp
        else:
          if len(A) == 1:
              return [(A[0], B)]
          else:
              temp = [(A[0], B[0])]
              A.remove(A[0])
              B.remove(B[0])
              temp = temp + MinMatching(A, B)
              return temp"""


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
        for i in match[0]:
            sum += i
        return sum / temp


def sum(vec):
    if len(vec) == 0:
        return 0
    result = 0
    for i in vec:
        result += peso(i)
    return result


def MatchMult3(A, B):
    result = []
    flip = True
    counter = 0
    for i in range((len(A) // 3) * 2):
        if flip:
            t = [counter * 3, counter * 3 + 1]
            a = list(np.array(B)[t])
            result.append((A[counter * 3], a))
            flip = False
        else:
            t = [counter * 3 + 1, counter * 3 + 2]
            a = list(np.array(A)[t])
            result.append((a, B[(counter * 3) + 2]))
            flip = True
            counter = counter + 1
    return result


def MatchMult31(A, B):
    result = []
    flip = True
    counter = 0
    for i in range((len(A) // 3 - 1) * 2):
        if flip:
            t = [counter * 3, counter * 3 + 1]
            a = list(np.array(B)[t])
            result.append((A[counter * 3], a))
            flip = False
        else:
            t = [counter * 3 + 1, counter * 3 + 2]
            a = list(np.array(A)[t])
            result.append((a, B[(counter * 3) + 2]))
            flip = True
            counter = counter + 1
    t = [counter * 3, counter * 3 + 1, counter * 3 + 2]
    a = list(np.array(B)[t])
    result.append((A[counter * 3], a))
    t = [counter * 3 + 1, counter * 3 + 2, counter * 3 + 3]
    a = list(np.array(A)[t])
    result.append((a, B[counter * 3 + 3]))
    return result


def MatchMult32(A, B):
    result = []
    flip = True
    counter = 0
    for i in range((len(A) // 3 - 1) * 2):
        if flip:
            t = [counter * 3, counter * 3 + 1]
            a = list(np.array(B)[t])
            result.append((A[counter * 3], a))
            flip = False
        else:
            t = [counter * 3 + 1, counter * 3 + 2]
            a = list(np.array(A)[t])
            result.append((a, B[(counter * 3) + 2]))
            flip = True
            counter = counter + 1
    t = [counter * 3, counter * 3 + 1, counter * 3 + 2, counter * 3 + 3]
    a = list(np.array(B)[t])
    result.append((A[counter * 3], a))
    t = [counter * 3 + 1, counter * 3 + 2, counter * 3 + 3, counter * 3 + 4]
    a = list(np.array(A)[t])
    result.append((a, B[counter * 3 + 4]))
    return result


def Min_Matching_Greedy(A, B):
    result = list()
    if len(A) == len(B):
        if len(A) % 3 == 0:
            result = MatchMult3(A, B)
        elif len(A) % 3 == 1:
            result = MatchMult31(A, B)
        else:
            result = MatchMult32(A, B)
    else:
        if len(A) > len(B):
            A1 = A[0:len(B) - 1]
            B1 = B[0:len(B) - 1]
            if len(A1) % 3 == 0:
                result = MatchMult3(A1, B1)
            elif len(A1) % 3 == 1:
                result = MatchMult31(A1, B1)
            else:
                result = MatchMult32(A1, B1)
            t = A[len(B) - 1:len(A)]
            result.append(((t), B[len(B) - 1]))
        else:
            A1 = A[0:len(A) - 1]
            B1 = B[0:len(A) - 1]
            if len(A1) % 3 == 0:
                result = MatchMult3(A1, B1)
            elif len(A1) % 3 == 1:
                result = MatchMult31(A1, B1)
            else:
                result = MatchMult32(A1, B1)
            t = B[len(A) - 1:len(B)]
            result.append((A[len(A) - 1], (t)))
    return [result, sum(result)]
