def factorial(x):
	if x==1:
	 	return 1
	else:
		return x*factorial(x-1)
v=int(input("Enter Number:"))
print(factorial(v))
