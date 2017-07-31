import math
import os
a = [int(x) for x in input().split()]




def comp(num):
	i = 0
	result = []
	for x in num:
		if i == 0:
			result.append(num[i])
		else:
			result.append(result[i-1]+num[i]/math.log(i+1,2))
		i+=1
	print(result)
	return result

first = comp(a)
bestnum = [int(x) for x in input().split()]
i = 0
best = comp(bestnum)
i = 0
ratio = []
i = 0
for x in first:
	ratio.append(first[i]/best[i])
	i +=1
print(ratio)
