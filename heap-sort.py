def heap(a):
	for i in range(len(a)-1, 0, -1):
		if i % 2 == 0:
			indexParent = int((i-2)/2)
			swap = min(a[indexParent], a[i], a[int((i-1)/2)])
			a[indexParent], swap = swap, a[indexParent]
			print(a[indexParent], a[i])
		else:
			indexParent = int((i-1)/2)
			swap = min(a[indexParent], a[i], a[int((i-2)/2)])
			a[indexParent], swap = swap, a[indexParent]
			print(a[indexParent], a[i])
	return a