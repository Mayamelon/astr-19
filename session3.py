#this program will print the result of a function and print "YAY!" if the result is bigger than 27

#this function tells the computer to return the result of x**3 + 8
def f(x):
	return ((x**3)+8)

#this defines the main function for my program
def main():
	y = f(9)
	print(y)
	if (y > 27):
		print("YAY!")

#This executes first
if __name__ == "__main__":
	main()