## Exercise 10
#Declaring a function to determine if a number is an even or an odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is an even."
    else:
        return f" The number {number} is an odd"
#Asking the user to enter a number
def main():
    try:
        num = int(input("Enter a number"))
#Checking the entered number if odd or even to the function
        result = check_even_odd(num)
#Printing the result
        print(result)
#If invalid integer is entered, it will print "Invalid! Please enter a number"
    except ValueError:
        print("Invalid! Please enter a number.")
if __name__ == "__main__":
    main()
