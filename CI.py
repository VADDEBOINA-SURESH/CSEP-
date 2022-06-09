def compound_interest(prin,rate,year):
	if year<=0:
		return prin
	else:
		return compound_interest(prin+prin*rate/100,rate,year-1)
print(compound_interest(100000,12,3))
