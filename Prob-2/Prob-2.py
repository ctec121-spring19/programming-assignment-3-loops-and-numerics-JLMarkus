# Module 2
#   Programming Assignment 3
#     Prob-2.py

# Jason Markus

def example():
    print("\nExample Output")
   # section 1
    x = 5
    # print x and its type
    print("x", x, "is a", type(x))

    # section 2
    print()
    x = float(x)
    print("x", x, "is a", type(x))

def studentCode():
    print("\nStudent Output")
    # section 1
    x = 5
    y = 3.14
    z = "a string"

    # print the values for x, y, and z and their types each on a separate line
    print("x", x, "is a", type(x))
    print()
    print("y", y, "is a", type(y))
    print()
    print("z", z, "is a", type(z))
    print()
    # section 2
    # convert y to an int and print
    y = 9.99
    y = int(y)
    print("y =",y)
    print()
    # convert z to an int and print
    z = 12.34
    z = int(z)
    print("z =",z)
    print()
    # print z and its type
    print("z is a", type(z))
    print()
    # use eval() to convert z to a number and print its value and type
    z = "12.34"
    z = eval(z)
    print("z", z, "is a", type(z))
    print()

example()
studentCode()