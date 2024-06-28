# Getting Input From the User
def main() :
    x = input()
    x = convert(x)

# Processed Output

    print(x)

# Converting Program

def convert(y) :
    y = y.replace(":)","🙂")
    y = y.replace(":(","🙁")
    return y

main()