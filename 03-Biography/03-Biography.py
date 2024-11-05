## Exercise 3 
#Creating a dictionary that contains my information
dictionary = {'Name' : 'Bernard Ian Santella', 'Age' : '18', 'Location' : 'Ilocos Norte, Philippines'}
print(dictionary)
#Using the input function to enter first and second name and hometown
name1 = input("Enter your first name: ")
name2 = input("Enter your second name: ")
hometown = input("Enter your hometown: ")
#Using the while loop function to enter age and confirm if it is valid 
while True: 
   age = input("Enter your age: ")
   if age.isdigit():
       age = int(age) 
       break
   else:
       print ("Please Enter a valid number for your age.")
#Inputting information in the dictionary
person_info = {
 'First Name' : name1,
 'Second Name' : name2,
 'Hometown' : hometown,
'Age' : age
}
#Running and printing the main function
for key, value in person_info.items():
      print (f"{key}: {value}")