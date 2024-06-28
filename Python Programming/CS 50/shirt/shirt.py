from PIL import Image,ImageOps
from pathlib import ntpath

import sys

def main():
    check()
    try:
        with Image.open("shirt.png") as file:
            with Image.open(sys.argv[1]) as input:
                z = ImageOps.fit(input,file.size)
                z.paste(file,(0,0),file)
                z.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")







def check():


    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ((ntpath.splitext(sys.argv[1]))[1] == ''):
        sys.exit("Invalid input")
    elif ((ntpath.splitext(sys.argv[2]))[1] == ''):
        sys.exit("Invalid Output")
    elif (sys.argv[1][-4:] != sys.argv[2][-4:]):
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()