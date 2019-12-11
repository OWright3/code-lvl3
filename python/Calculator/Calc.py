y = 1
print("Select a calculator type:\nefficient[0]\ninefficient[1]\n ")
ctype = input("")
	
if ctype == "1":
	func = str(input("Please select a function: Multiply, Divide, Add or Subtract: "))
	while y == 1:
		n1 = int(input("Please select a first number: "))
		n2 = int(input("Please select a second number: "))
		def multiply(n1, n2):
			n3 = n1 * n2 
			print(n3)
		def divide(n1, n2):
			n3 = n1 / n2
			print(n3)
		def add(n1, n2):
			n3 = n1 + n2
			print(n3)
		def subtract(n1, n2):
			n3 = n1 - n2
			print(n3)
		if func == "Multiply" or "multiply":
			multiply(n1, n2)
		elif func == "Divide" or "divide":
			divide(n1, n2)
		elif func == "Add" or "add":
			add(n1, n2)
		elif func == "Subtract" or "subtract":
			subtract(n1, n2)
		elif func == "End" or "end":
			y = 0
		else:
			print("Response not recognised, please enter a valid function.")
elif ctype == "0":
	while y == 1:
		x = input("Input function\n")
		try:
			if x == "end":
				y = 0
			else:
				xans = eval(x)
				print(xans)
		except NameError or TypeError:
			print("Unrecognised")
#dev notes:	try to intergrate a loop function to allow multiple questions to be answered in the same instance
#		try to also add a memory function in the form of "ans"
#		create a smarter func variable where it detects the function desired based on the calculation given