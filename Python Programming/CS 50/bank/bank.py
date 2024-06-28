#Getting input

x = input("Greetings: ")

#Processing

x = x.casefold()

#Checking The condition using "in"
if("h" in x):
    if("hello" in x):
        print("$0")
    elif(x.startswith("h")):
        print("$20")
    else:
        print("$100")
else:
    print("$100")