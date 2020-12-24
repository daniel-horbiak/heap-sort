def heap(a):
	for i in range(len(a)-1, 0, -1):
		if i % 2 == 0:
			nParent = int((i-1)/2)
			print(a[nParent], a[i])
		else:
			nParent = int((i-1)/2)
			print(a[nParent], a[i])