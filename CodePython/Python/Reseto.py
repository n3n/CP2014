n, k = raw_input().split()
n = int(n)
k = int(k)
data = range(2, n + 1)
strip = []

counter = 0

while True:
	prime = data[0]
	i = 0
	while i < len(data):
		if data[i] % prime == 0:
			tmp = data[i]
			del data[i]
			counter += 1
			if counter == k:
				print tmp
				exit()
		i += 1