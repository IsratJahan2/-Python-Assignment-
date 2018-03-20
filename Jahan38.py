#Jahan38.py
#A program that ask the user to enter a meal order with items separated by
#..commas. Then to confirm the order, print out each item on a separated line with
#.. a leading tab.

def main():
    order=input("Enter the meal order separated by commas  ")
    meals=order.split(",")
    print("So let me confirm your order: " )
    for food in meals:
        print("\t"+food)
main()
    
    
