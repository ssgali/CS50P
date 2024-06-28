dict = {}
def main():
    while(True):
        try:
            item = input()
            if (True == check(item)):
                dict[item] += 1
            else :
                dict[item] = 1

        except EOFError:
            print()     #For seperation
            display(dict)
            return 0
        except (ValueError,KeyError):
            continue
def check(q):
    if q in dict:
        return True     # For Repeated Items
    else:
        return False    # For First Entries

def display(dict):

    s_dict = sorted(dict)   #To sort the dictionary
    for a in s_dict:
        print(dict[a], a.upper())

main()