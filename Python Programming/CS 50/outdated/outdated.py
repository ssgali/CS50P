list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while(True):
        x = input("Date: ")
        if (True == check(x)):
            break
def check(x):
    if ("/" in x):      ##Checking for the 1st format
        x = x.strip()
        x = x.rsplit("/")
        if (x[0].isdigit() and x[1].isdigit() and x[2].isdigit()):
            if(0 < int(x[0]) < 13 and 0<int(x[1])<32):
                convert(x)
                return True
    elif ("," in x):   #Checking for the 2nd format
        x = x.strip()
        x = x.rsplit()
        if (x[0] not in list) or (len(x) != 3):
            return False
        x[1] = x[1].strip(",")
        if(x[1].isdigit() and 0 < int(x[1]) < 32) and (x[2].isdigit()):
            convert_1(x)
            return True
    return False
def convert_1(y):       #For the First Format
    z = int(0)
    for a in list:
        z +=1
        if(a == y[0]):
            break
    print(f"{y[2]}-{z:02}-{int(y[1]):02}")
def convert(y):         #For the 2nd Format
    print(f"{y[2]}-{int(y[0]):02}-{int(y[1]):02}")
main()




