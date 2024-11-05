## Exercise 5
#Create a dictionary that contains the number of month and days of that month 
days_of_the_month = {   #The key is the month number and the value is the number of days in each month
  1: 31,        #January, 31 days
  2: 28,        #February, 28 days
  3: 31,        #March, 31 days
  4: 30,        #April, 30 days
  5: 31,        #May, 31 days
  6: 30,        #June, 30 days
  7: 31,        #July, 31 days
  8: 31,        #August, 31 days
  9: 30,        #September, 30 days
  10: 31,       #October, 31 days
  11: 30,       #November, 30 days
  12: 31,       #December, 31 days
}
#Asking the user to input the number of month ranging from 1-12
month = int(input("Enter the number of the month (1-12): "))    #Converting to integer
#Checking if the value is in the range of (1-12) based on the dictionary
if month in days_of_the_month: 
#If month is February, input will ask if it is a leap year to adjust the days
    if month == 2:          
        leap_year = input("Is it a leap year? (yes or no): ").lower() #Using .lower to disregard capitalization
        if leap_year == "yes":
            days_of_the_month[2] = 29                                 #Update February's days from 28-29, since it is a leap year
    print(f"Month {month} has {days_of_the_month[month]} days.")      #Print the number of days depending on which month the user inputs
else: 
#If invalid number is entered, it will show an error and ask the user to enter an integer from 1-12
    print("Invalid month number. Please enter a number between 1 to 12")