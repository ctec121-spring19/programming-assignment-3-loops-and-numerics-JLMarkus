# Module 2
#   Programming Assignment 3
#     Prob-4.py

# Jason Markus
from random import *
def main():
    print("\nStudent Output:")

    # write code that will sum the numbers between 15 and 30 inclusive
    # and print the sum
    sum = 0
    for i in [15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]:
        sum = sum + i
        print(sum)
    print()
    # sum the numbers in the sequence [2, 4, 7, 9, 12, 14, 17, 19]
    # and print the sum
    sum = 0
    for i in [2, 4, 7, 9, 12, 14, 17, 19]:
        sum = sum + i
        print(sum)
    print()
    # use the randrange() function to sum 5 randomly generated numbers 
    # between 1 and 99 inclusive.
    # Print each random number on a line. 
    # Print the sum on the last line
    sum = 0
    for i in range(5):
        num = randrange(1,100)
        print(num)
        sum = sum + num
    print("------")
    print(sum)

main()
