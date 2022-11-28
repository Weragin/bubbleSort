from typing import List


def bubbleSort(arg: List[int or float]):
	len = len(arg) - 1
	
	for i in range(len):
		n_changed = True
		
		for j in range(0, len - i):
			if arg[j] > arg[j + 1]:
				arg[j], arg[j + 1] = arg[j + 1], arg[j]
				n_changed = False
		
		if n_changed:
			return
	
	return
