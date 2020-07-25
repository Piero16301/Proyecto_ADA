def peso(match, u):
  if isinstance(match[0], int) and isinstance(match[1], int):
    return abs(match[0]/match[1] - u)
  elif isinstance(match[0], int):
    temp = match[0]
    sum = 0
    for i in match[1]:
      sum += i
    return abs(temp/sum - u)
  else:
    temp = match[1]
    sum = 0
    for i in match[0]:
      sum += i
    return abs(sum/temp - u)

def sumv(vec, u):
  if len(vec) == 0:
    return 0
  result = 0
  for i in vec:
    result += peso(i, u)
  return result

def minsum(vec, u):
  if len(vec) == 0:
    return None
  result = vec[0]
  for i in vec:
    if sumv(result, u) > sumv(i, u):
      result = i
  return result

def getvalues(match):
  if isinstance(match[0], int) and isinstance(match[1], int):
    return (1, 1)
  elif isinstance(match[0], int):
    return (1, len(match[1]))
  else:
    return (len(match[0]), 1)

from converter import converter
from match_converter import matchConverter

def it(A, B):
	min = None
	mem = {}
	u = sum(A)/sum(B)
	actual = []
	counters = [0]
	possible_values = [[]]
	i = len(A)-1
	j = len(B)-1
	while len(counters) > 0:
		if i > 0 and j > 0:
			if counters[len(counters)-1] == 0:
				if mem.get(i):
					if mem[i].get(j):
						new = mem[i][j] + actual
						# print(counters)
						if sumv(min, u) > sumv(new, u):
							min = new
						counters.pop()
						possible_values.pop()
						if len(actual) > 0:
							val = actual.pop(0)
							(v1, v2) = getvalues(val)
							i += v1
							j += v2
						continue
				# print(len(counters), len(actual))
				match = (A[i], B[j])
				actual.insert(0, match)
				(v1, v2) = getvalues(match)
				i -= v1
				j -= v2
				counters[len(counters)-1] += 1
				counters.append(0)
				possible_values[len(possible_values)-1].append(match)
				possible_values.append([])
			elif counters[len(counters)-1] <= i-1:
				nextnum = counters[len(counters)-1]
				match = ([A[i]], B[j])
				for it in range(1, nextnum+1):
					match[0].insert(0, A[i-it])
				actual.insert(0, match)
				(v1, v2) = getvalues(match)
				i -= v1
				j -= v2
				counters[len(counters)-1] += 1
				counters.append(0)
				possible_values[len(possible_values)-1].append(match)
				possible_values.append([])
			elif counters[len(counters)-1] > i-1 and counters[len(counters)-1] <= (i-1)+(j-1):
				nextnum = counters[len(counters)-1]-(i-1)
				match = (A[i], [B[j]])
				for it in range(1, nextnum+1):
					match[1].insert(0, B[j-it])
				actual.insert(0, match)
				(v1, v2) = getvalues(match)
				i -= v1
				j -= v2
				counters[len(counters)-1] += 1
				counters.append(0)
				possible_values[len(possible_values)-1].append(match)
				possible_values.append([])
			else:
				vals = []
				for it in possible_values[len(possible_values)-1]:
					(v1, v2) = getvalues(it)
					vals.append(mem[i-v1][j-v2] + [it])
				if mem.get(i):
					mem[i][j] = minsum(vals, u)
				else:
					mem[i] = {}
					mem[i][j] = minsum(vals, u)
				if len(actual) > 0:
					val = actual.pop(0)
					(v1, v2) = getvalues(val)
					i += v1
					j += v2
				possible_values.pop()
				counters.pop()
		else:
			counters.pop()
			possible_values.pop()
			match = None
			if i == 0 and j == 0:
				match = (A[i], B[j])
				actual.insert(0, match)
			elif i > 0:
				match = ([], B[j])
				for it in range(0, i+1):
					match[0].append(A[it])
				actual.insert(0, match)
			else:
				match = (A[i], [])
				for it in range(0, j+1):
					match[1].append(B[it])
				actual.insert(0, match)
			if mem.get(i):
				mem[i][j] = [match]
			else:
				mem[i] = {}
				mem[i][j] = [match]
			if min:
				if sumv(min, u) > sumv(actual, u):
					min = actual.copy()
			else:
				min = actual.copy()
			actual.pop(0)
			if len(actual) > 0:
				val = actual.pop(0)
				(v1, v2) = getvalues(val)
				i += v1
				j += v2
	return min

def Min_Transformation_DP_Mejorado(A, B):
	result = []
	for i in range(len(A)):
		A1 = converter(A[i])
		B1 = converter(B[i])
		MinMatch = it(A1, B1)
		result.append(matchConverter(MinMatch, A1, B1))
	return result
