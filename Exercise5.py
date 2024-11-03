## Exercise 5
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
month = int(input("Enter the number of the month (1-12): "))
if month in days_of_the_month: 
    if month == 2:
        leap_year = input("Is it a leap year? (yes or no): ").lower()
        if leap_year == "yes":
            days_of_the_month[2] = 29
    print(f"Month {month} has {days_of_the_month[month]} days.")
else: 
    print("Invalid month number. Please enter a number between 1 to 12")