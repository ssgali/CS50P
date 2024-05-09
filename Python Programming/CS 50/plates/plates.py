def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = int(0)                                          #Variable to check if 0 is in first place
    if len(s) <= 6 and s.isalnum() and len(s) >= 2:     #Checking length of string and Punctuation marks etc
        p = s[0 : 2]                                    #For first two characters
        if 0 == p.isalpha():
            return False
        for c in s:                                     #Checking each character using for loop
            if c == "0" and i == 0:
                return False
            if 0 == c.isalpha():                        #checking digits and incrementing i by 1
                i += 1
                continue
            else:                                       #check if there is a character after a digit
                if i>0:
                    return False
        return True
    else:
        return False
main()