#This program creates a table of sin(x) vs x where x goes between 0 and 2pi with 1000 entries

#Imports the math library
import math

#This generates the table using a for loop
def generateTable():
	print ("x, sin(x)\n----------")
	for i in range(1000):
		x = math.pi * 2 * (i/1000)
		print (x,math.sin(x))

#this defines the main function for my program
def main():
	generateTable()

#This executes first
if __name__ == "__main__":
	main()