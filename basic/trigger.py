def Lee(x):
	trigger = 10
	while x:
		if x % 10 > trigger:
			return 0
		trigger = x % 10
		x /= 10
	return 1

print(Lee(654321))