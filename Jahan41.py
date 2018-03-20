#Jahan41.py
#A program that ask the user to enter a sequence of amounts to debit or credit
#..to their account. The program continue to process their amounts as long as the
#..account have possitive balance. When the program finds negative balance it stops
#..with error message. If the program is able to process all the amounts, it prints
#..the final balance.

def main():
    
    amounts=input("Plase enter the amounts from your account separated by commas ")
    initialbalance = 1000
    amounts = amounts.split(",")
    print("Initial Balance: $1000" )
    print()

    for value in amounts:
        initialbalance=initialbalance+float(value)
        print("Amount: ", value)

        if initialbalance<0:
            print(" Your balance has dropped below 0!  Please contact the bank immediately!")
            break
        print("Current balance: ", "${:,.2f}".format(initialbalance))
    if initialbalance>0:
        print("\nYour final balance is: ", "${:,.2f}".format(initialbalance))

        
main()
