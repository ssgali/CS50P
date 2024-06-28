#Taking Input

x = input("What is the Answer to the Great Question of life, the Universe, and everything? ")

#Conversion into lowercase
x = x.casefold()
x = x.strip()

#Checking Condition
if(x == "42" or x == "forty-two" or x == "forty two"):
    print("Yes")

else:
    print("No")
