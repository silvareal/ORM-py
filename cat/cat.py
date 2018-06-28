"""
    recreating the 'cat' command line
    $ cat file.txt ---read the file
    $ cat file.txt sometext.txt othertext.txt ---read from all the textfile
    $ cat file.txt sometext.txt othertext.txt > newtext.txt ---reads all file and copy to newtext.txt

    same as mine: 
    $ python cat.py file.txt ---read the file
    $ python cat.py sometext.txt othertext.txt ---read from all the textfile
    $ python cat.py sometext.txt othertext.txt > newtext.txt ---reads all file and copy to newtext.txt

    and it has an optional argument:
    -n --number
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("filename", metavar='F', type=str, nargs='+', help="get the filename")
parser.add_argument("-n", "--number", action="store_true", help="indicate it's a number")
args = parser.parse_args()

print(">>>Parser argument: ", args)

line_number = 1

for file in args.filename: #loops through all the file in list
    text = open(file)
    if args.number:
        for line in text.readlines():
            print(f'\t{line_number}\t{line}')
            line_number +=1
    else:
        print(text.read())


 
