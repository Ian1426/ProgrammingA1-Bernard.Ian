## Exercise 5
#Create a dictionary that contains the number of month and days of that month 
days_of_the_month = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31,
}
#Using the input function asking the user to input the number of month ranging from 1-12
month = int(input("Enter the number of the month (1-12): "))
#Using if else function to check if the input is valid
if month in days_of_the_month: 
    if month == 2:
        leap_year = input("Is it a leap year? (yes or no): ").lower()
        if leap_year == "yes":
            days_of_the_month[2] = 29
    print(f"Month {month} has {days_of_the_month[month]} days.")
else: 
#If invalid, it will ask the user to enter an integer from 1-12
    print("Invalid month number. Please enter a number between 1 to 12")