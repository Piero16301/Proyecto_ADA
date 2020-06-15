def peso(match):
  if isinstance(match[0], int) and isinstance(match[1], int):
    return match[0]/match[1]
  elif isinstance(match[0], int):
    temp = match[0]
    sum = 0
    for i in match[1]:
      sum += i
    return temp/sum
  else:
    temp = match[1]
    sum = 0
    for i in match[0]:
      sum += i
    return sum/temp

def sum(vec):
  if len(vec) == 0:
    return 0
  result = 0
  for i in vec:
    result += peso(i)
  return result

def minsum(vec):
  if len(vec) == 0:
    return None
  result = vec[0]
  for i in vec:
    if sum(result) > sum(i):
      result = i
  return result

def Min_Matching(A, B, i = 0, j = 0):
  if i == len(A) and j == len(B):
    return []
  elif i == len(A) or j == len(B):
    return None
  elif i == len(A)-1 and j == len(B)-1:
    return [(A[i], B[i])]
  elif i == len(A)-1 or j == len(B)-1:
    if i == len(A)-1:
      this = (A[i], [])
      for it in range(j, len(B)):
        this[1].append(B[it])
      return [this]
    else:
      this = ([], B[j])
      for it in range(i, len(A)):
        this[0].append(A[it])
      return [this]
  else:
    pesos = []
    match = Min_Matching(A, B, i+1, j+1)
    if match is not None:
      match.insert(0, (A[i], B[j]))
      pesos.append(match)
    temp = i+1
    while temp < (len(A)-1):
      this = ([], B[j])
      for it in range(i, temp):
        this[0].append(A[it])
      temp2 = Min_Matching(A, B, temp, j+1)
      if temp2 is not None:
        temp2.insert(0, this)
        pesos.append(temp2)
      temp += 1
    temp = j+1
    while temp < (len(B)-1):
      this = (A[i], [])
      for it in range(j, temp):
        this[1].append(B[it])
      temp2 = Min_Matching(A, B, i+1, temp)
      if temp2 is not None:
        temp2.insert(0, this)
        pesos.append(temp2)
      temp += 1
    return minsum(pesos)
