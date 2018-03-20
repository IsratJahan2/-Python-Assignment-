#Jahan13.py
#A program that asksthe user for 15 letters and accumulates them into a single string
#Israt Jahan

def main():
    final_str=''
    for i in range(15):
       single_str=input("Please enter a letter: ")
       final_str=final_str+single_str
    print("The string is", final_str)
main()
                              
