from utils.matchConverter import matchConverter
from utils.vectorConverter import vectorConverter


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

def getvalues(match):
  if isinstance(match[0], int) and isinstance(match[1], int):
    return (1, 1)
  elif isinstance(match[0], int):
    return (1, len(match[1]))
  else:
    return (len(match[0]), 1)

def dynamic_programming(A, B):
	min = None
	mem = {}
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
						if sum(min) > sum(new):
							min = new
						counters.pop()
						possible_values.pop()
						if len(actual) > 0:
							val = actual.pop(0)
							(v1, v2) = getvalues(val)
							i += v1
							j += v2
						continue
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
					mem[i][j] = minsum(vals)
				else:
					mem[i] = {}
					mem[i][j] = minsum(vals)
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
				if sum(min) > sum(actual):
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

def Min_Transformation_DP(A, B):
	result = []
	for i in range(len(A)):
		A1 = vectorConverter(A[i])
		B1 = vectorConverter(B[i])
		MinMatch = dynamic_programming(A1, B1)
		result.append(matchConverter(MinMatch, A[i], B[i]))
	return result
