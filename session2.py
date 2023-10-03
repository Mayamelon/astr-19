#this program will print various sums, differences, and products of different data types


#this prints the sum of two floats and the resulting type
def SumFloats():
	a = 31.4
	b = 82.19
	c = a + b
	print(f"{a} + {b} = {c}, {type(c)}")


#this prints the difference of two ints and the resulting type
def DiffInts():
	a = 58
	b = 12
	c = a - b
	print(f"{a} - {b} = {c}, {type(c)}")


#this prints the product of a float and int and the resulting type
def ProdFloatInt():
	a = 17.5
	b = 8
	c = a * b
	print(f"{a} * {b} = {c}, {type(c)}")


#this defines our main() function for our program
def main():
	SumFloats()
	DiffInts()
	ProdFloatInt()


#When we run the program, this executes first
if __name__ == "__main__":
	main()