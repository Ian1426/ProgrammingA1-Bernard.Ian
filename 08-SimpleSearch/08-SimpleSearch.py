## Exercise 8
#Creating a list that contains the given names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#Using the input function to ask the user to enter a name in the list
search_term = input("Please enter the name you want to search in the list: ")
#Checking if the entered name in present in the list via search_term
if search_term in [name.lower() for name in names]:             #Using .lower function to disregard capitalization
    print(f"{search_term.lower()} is in the list")              #Printing a message that says the name is in the list
else: 
    print(f"{search_term.lower()} is not in the list")          #Printing a message that says the name is not in the list