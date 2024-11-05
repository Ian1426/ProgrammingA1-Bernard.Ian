## Exercise 3 
#Creating a dictionary that contains my information
dictionary = {
    'Name' : 'Bernard Ian Santella',            #Inputing my full name
    'Age' : '18',                               #Inputing my age
    'Location' : 'Ilocos Norte, Philippines'    #Inputing my hometown
    }
print(dictionary)                               #Printing the variable to display the information
#Using the input function to enter first and second name and hometown
name1 = input("Enter your first name: ")        #Inputing the user's first name
name2 = input("Enter your second name: ")       #Inputing the user's second name
hometown = input("Enter your hometown: ")       #Inputing the user's hometown
#Using the while loop function to enter age and confirm if it is valid 
while True: 
   age = input("Enter your age: ")              #User inputs their age
   if age.isdigit():                            #Checking if it is valid
       age = int(age)                           #Once valid, will be convterted to integer
       break                                    #Exiting the loop once valid
   else:
       print ("Please Enter a valid number for your age.")   #If invalid, error messaged as shown will be printed
#Creating a dictionary that contains the user's information
person_info = {
 'First Name' : name1,                          #Storing the user's first name
 'Second Name' : name2,                         #Storing the user's second name
 'Hometown' : hometown,                         #Storing the user's hometown
'Age' : age                                     #Storing the user's age
}
#Checking through each person_info dictionary and printing them
for key, value in person_info.items():
      #Use string variable to print each key and value
      print (f"{key}: {value}")