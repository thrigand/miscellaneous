#!/usr/bin/env python3
import sys
import os
import string
import argparse

# accept argument or multiple arguments and return the sum of integers
def add_digits(*content):
    sum = 0
    for line in content:
        for char in line:
            if char.isdigit():
                sum = sum + int(char)
    return(sum)


# accept argument or multiple arguments and return the sum of hexadecimal digits in decimal
def add_hex_digits(*content):
    sum = 0
    for line in content:
        for char in line:
            found = char in string.hexdigits
            if found == True:
                sum = sum + int(char, 16)
    return(sum)


# main program
def main():
    parser = argparse.ArgumentParser(description = 'Sum of digits')

    # by default, accept the input is from STDIN otherwise, it must be from an input file
    # -f switch to accept the path of the file

    parser.add_argument('-f', type=argparse.FileType('r'), default=(None if sys.stdin.isatty() else sys.stdin))

    # accept strings (or character) as hexadecimal when "-x" flag is specified

    parser.add_argument("-x", action = 'store_true', help="all input to be interpreted as hexadecimal")

    args = parser.parse_args()

    #print(args)

    #print(add_digits("123", "123"))
    #print(add_hex_digits("abc123", "abcdef1283"))


    if args.f is not None:
        # read the content into a variable
        # beware, make sure the input or input file is not too big to handle
        filecontent = args.f.read()
        if args.x is not None and args.x is True:
            #print("reading input as hexadecimal values")
            print(add_hex_digits(filecontent))
        else:
            #print("reading input as integer values")
            print(add_digits(filecontent))


if __name__ == "__main__":
   main()