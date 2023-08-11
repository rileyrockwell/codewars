def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n - 1)

for i in range(11):
	print(factorial(i))

print("testing")