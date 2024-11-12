## Exercise 10
#Defining a function 'check_even_odd' that takes 'number'
def check_even_odd(number):
    #Checking if the number is even by using %
    if number % 2 == 0:
        #If the number is even, a string indicating it is an even will show
        return f"The number {number} is an even."
    else:
        #If the number is odd, a string indicating it is an odd will show
        return f" The number {number} is an odd"
#Defining the function that will execute the program structure
def main():
    try:
        #Asking the user to enter a number then converted to integer
        num = int(input("Enter a number:"))
        #Checking the function check_even_odd with the user's answer then storing the result
        result = check_even_odd(num)
#Printing the result 
        print(result)
    except ValueError:
        #If invalid integer is entered, it will print "Invalid! Please enter a number"
        print("Invalid! Please enter a number.")
#Checking if the script is being run directly
if __name__ == "__main__":
    main()
