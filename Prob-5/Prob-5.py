# Module 2
#   Programming Assignment 3
#     Prob-5.py

# Jason Markus

def main():

    itemList = ["pizza", "Large Coke", "doughnut"]

    costList = [2.00, 1.50, 0.56]

    quantityList = [2, 1 ,2]

    subtotal = 0

    for i in range(3):
        print(itemList[i], "@", quantityList[i],"\t", costList[i])
        subtotal = subtotal + costList[i] * quantityList[i]
    
    print("----------------------")
    
    tax = subtotal * 0.084

    grandTotal = subtotal + tax

    print("Subtotal:\t",round(subtotal, 2))

    print("Tax:\t\t", round(tax, 2))

    print()

    print("Total:\t\t", round(grandTotal, 2 ))

    print()

    userNum = (float(input("Please enter an amount: ")))
    
    print("Tendered:\t", userNum)

    change = userNum - grandTotal
    
    print("Change:\t\t", round(change, 2))
    
main()