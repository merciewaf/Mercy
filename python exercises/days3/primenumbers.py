import unittest
import primenumbers_test

def primenumbers(n):

	primelist=[2,3]

	current_no=4

	while True:
		for i in range(2,(current_no//2)+1):

			if current_no % i==0:
				break
		else:
			primelist.append(current_no)
		current_no+=1

		if len(primelist)==n:
			break
	return primelist

print(primenumbers(8))