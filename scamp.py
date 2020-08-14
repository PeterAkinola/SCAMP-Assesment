#A script that computes the first twenty fibonacci's number
fibonacci =[0,1]
print(fibonacci)
def f_b():
	"""A function that computes the first twenty fibonacci's number"""
	for i in range(2,20):
		fibonacci_numbers = fibonacci[-1] + fibonacci[-2]
		fibonacci.append(fibonacci_numbers)
		print(fibonacci)


f_b()
