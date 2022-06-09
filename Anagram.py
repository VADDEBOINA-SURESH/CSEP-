#Anagram
def Anagram(x,y):
	if sorted(x)==sorted(y):
		print("Anagram")
	else:	
		print("Not an Anagram")
s=input("Enter First String:")
c=input("Enter Second String:")
Anagram(s,c)
