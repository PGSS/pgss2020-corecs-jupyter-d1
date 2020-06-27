
def choose_one():
	a = input("a = ")
	b = input("b = ")
	z = a

	if a > b:
		z = a
	elif a < b:
		z = b

	print( "\n" + str(z) )

choose_one()
