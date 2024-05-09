
#Getting User Input

x = input("Expression: ")

#Assigining Values to Different Values

x,y,z = x.split()
x = int(x)
z = int(z)
if(y == "+"):
    print(float(x + z))
elif(y == "-"):
    print(float(x - z))
elif(y == "*"):
    print(float(x * z))
elif(y == "/" and z != 0):
    print(float(x / z))
