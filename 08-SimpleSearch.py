## Exercise 8
#Creating a dictionary that contains the given names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#Using the search term function asking the user to enter the name to be searched from the dictionary
search_term = input("Please enter the name you want to search for: ")
#Using the if else function to determine if the given name is in the list or not
if search_term in names: 
    print(f"{search_term} is in the list")
else: 
    print(f"{search_term} is not in the list")