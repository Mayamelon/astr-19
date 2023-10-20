#This program definies a class, animal, and creates an instance of the class called cat. It then describes the cat

#This defines the animal class
class Animal:
	armLength = 0.0
	legLength = 0.0
	numEyes = 0
	hasTail = False
	isFurry = False

	#this initializes an instance of the class
	def __init__(self, armLength, legLength, numEyes, hasTail, isFurry):
		self.armLength = armLength
		self.legLength = legLength
		self.numEyes = numEyes
		self.hasTail = hasTail
		self.isFurry = isFurry

	#this prints a description of an instance of the class
	def describe(self):
		print (f"I have {self.armLength}cm long arms.")
		print (f"I have {self.legLength}cm long legs.")
		print (f"I have {self.numEyes} eyes.")
		if (self.hasTail):
			print("I have a tail.")
		else:
			print("I do not have a tail.")
		if (self.isFurry):
			print("I am furry.")
		else:
			print("I am not furry.")


#this defines our main() function for our program
def main():
	cat = Animal(22.5, 23.5, 2, True, True)
	cat.describe()

#When we run the program, this executes first
if __name__=="__main__":
	main()
