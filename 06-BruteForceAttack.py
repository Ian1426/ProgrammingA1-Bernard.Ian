## Exercise 6 
#Declaring the correct password
correct_password = '12345'
#Declaring the maximum attempts
max_attempts = 5
attempts = 0
#Asking the user to enter the password
while attempts < max_attempts:
    entered_password = input("Enter the password: ")
#Checking if the password is correct
    if entered_password == correct_password:
        print("You entered the correct password.")
        break
    else:
        #Informing the user of the remaining attempts if the entered password is incorrect
        attempts +=1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:   
            print(f"Incorrect password. You have {remaining_attempts} attempts remaining. Please Try again.")
        else:
        #If maximum limit is reached, it will notify that the authorities have been alerted
            print("You have reached the maximum limit. Authorities have been alerted.")