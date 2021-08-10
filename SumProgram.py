#!/usr/bin/env python3
import sys
import os
import string
from os import path

def main():
    print("in the main method")

    print("Arguments length is: ",len(sys.argv))
    print("Argument List:", str(sys.argv))
 
    if len(sys.argv) <= 1:
        sys.stderr.write("Arguments are missing")
    elif str (sys.argv[1]) == '-f' or str (sys.argv[1]) == '-F':
        print("Input is a File")
        if len(sys.argv) <= 2:
            sys.stderr.write("File Name does not present")
        else:
            print("file string exists and verifying the path")
            if str(path.exists(str (sys.argv[2]))) == "True":
                #print("File is present in the path")
                fileContent = open(str (sys.argv[2]), "r")
                sum = 0
                for line in fileContent:
                    for x in line:
                        if x.isdigit():
                            sum = sum + int(x)
                print("sum of all digits is: ", sum)

            else:
                sys.stderr.write("File does not exist")
    elif str (sys.argv[1]) == '-x' or str (sys.argv[1]) == '-X':
        print("input is hexa decimal")
        if len(sys.argv) <= 2:
            print("Hexa Decimal String does not exist")
        else:
            print("Here is the string",str (sys.argv[2]) )
            num_hex = str (sys.argv[2])
            sum = 0
            for c in num_hex:
                found = c in string.hexdigits
                if found == True:
                    sum = sum + int(c,16)
            print("sum of all hexa decimals is:", sum)  


    else:
        print("input is a string", str (sys.argv[1]))
        input_string = str (sys.argv[1])
        contains_digit = False
        sum = 0
        for char in input_string:
            if char.isdigit():
                #print("yes this is int")
                sum = sum + int(char)
        print("sum of all digits in a string:", sum)


if __name__ == "__main__":
    main()