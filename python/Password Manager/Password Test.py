import json

y = 1
password = "abc"
p_guess = 0
p_mguess = 3

Pass = {}
with open("Pass.json", "r") as data_file:
    Pass = json.load(data_file)
def new(key, value):
    if key not in Pass:
        Pass[key] = value
        print("The key: "+key+" has been added with the value, "+value)
    elif key in Pass:
        print(key+" is already present.")
def delete(key):
    if key in Pass:
        del Pass[key]
        print("The key: "+key+" has been deleted")
    elif key not in Pass:
        print(key+" doesn't exist.")

try:
    while p_guess < p_mguess:
        p_uguess = input("Please enter the password: ")
        if p_uguess == password:
            for key in Pass:
                print(key)
            while y == 1:
                x = input("Please select desired password or function: ")
                if x in Pass:
                    print(Pass[x])
                elif x == "end":
                    y = 0
                elif x == "delete":
                    c = str(input("Key: "))
                    delete(c)
                    for key in Pass:
                        print(key)
                elif x == "new":
                    a = str(input("Key: "))
                    b = str(input("Value: "))
                    new(a, b)
                    for key in Pass:
                        print(key)
                elif x == "clear":
                    Pass.clear()
                    print("All keys removed.")
                else:
                    print("Unrecognised")
            p_guess = 4
        else:
            p_guess = p_guess + 1
            remg = p_mguess - p_guess
            print("Incorrect, "+str(remg)+" guesses remaining.")
except:
    print(Pass)
    raise
finally:
    off = [z**2 for z in range(10)]

# I need to find out how to use files as dictionaries
# Dict inside dict
