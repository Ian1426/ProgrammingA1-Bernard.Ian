## Exercise 6 
#Declaring the correct password
correct_password = '12345'
#Declaring the maximum attempts
max_attempts = 5        #User has 5 attempts to enter the correct password
attempts = 0            #Initialize the counter to 0
#Using a loop that will allow the user to continue trying until maximum attempts is reached
while attempts < max_attempts:
    entered_password = input("Enter the password: ") #Asking the user to enter the password
#Checking if the password is correct
    if entered_password == correct_password:
        print("You entered the correct password.")   #Printing what is shown if correct password is entered
        break                                        #Ending the loop if the correct password is entered
    else:
#Increasing the attempt counter if the entered password is incorrect
        attempts +=1
        remaining_attempts = max_attempts - attempts        #Calculating the remaining attempts from max attempts until 0 
#Checking if there are remaining attempts
        if remaining_attempts > 0:   
            print(f"Incorrect password. You have {remaining_attempts} attempts remaining. Please Try again.")   #When incorrect password is entered, prints an error and the remaining attempt
        else:
        #If maximum limit is reached, it will notify that the authorities have been alerted
            print("Incorrect Password. You have reached the maximum limit. Authorities have been alerted.")