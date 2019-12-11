#Last Edit: 3:48pm Sunday 17th November 2019

######################### Basic arithmetic function ################################
def num(x,z,y):
    if z=="add" or z=="Add" or z=="+":
        print(x+y)
    elif z=="subtract" or z=="Subtract" or z=="-":
        print(x-y)
    elif z=="divide" or z=="Divide" or z=="/":
        print(x/y)
    elif z=="multiply" or z=="Multiply" or z=="x" or z=="*": 
        print(x*y)
    else:
        print("Invalid input, please try again.")
################################# Notice ###########################################
print("Please note, you must include spaces inbetween your entered numbers. Only 2 numbers can be entered at a time.")
############################# Input Handling #######################################
while True:
    f = input("Enter your calculation:\n")
    if f=="stop":
        break
    else:
        #Splitting the words in input f into a list to allow the program to refer to each word individually 
        e = f.split()
        #Type handling
        x = float(e[0]) #Term 1
        z = e[1] #Function
        y = float(e[2]) #Term 2
        num(x,z,y)

#Error handling??
#Nah bro