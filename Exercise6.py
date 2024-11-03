## Exercise 6 
correct_password = '12345'
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    entered_password = input("Enter the password: ")

    if entered_password == correct_password:
        print("You entered the correct password.")
        break
    else:
        attempts +=1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:   
            print(f"Incorrect password. You have {remaining_attempts} attempts remaining. Please Try again.")
        else:
            print("You have reached the maximum limit. Authorities have been alerted.")