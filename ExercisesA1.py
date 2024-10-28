## Exercise 1
word1 = "Coding"
word2 = "is"
word3 = "Cool"

print (word1 + " " + word2  + " " + word3)

## Exercise 2
print("a=8")
print("b=10")
a=8
b=10
sum = a+b
print("The sum of two numbers is", sum)

## Exercise 3 
dictionary = {'Name' : 'Bernard Ian Santella', 'Age' : '18', 'Location' : 'Ilocos Norte, Philippines'}
print(dictionary)

name1 = input("Enter your first name: ")
name2 = input("Enter your second name: ")
hometown = input("Enter your hometown: ")

while True: 
   age = input("Enter your age: ")
   if age.isdigit():
       age = int(age) 
       break
   else:
       print ("Please Enter a valid number for your age.")

person_info = {
 'First Name' : name1,
 'Second Name' : name2,
 'Hometown' : hometown,
'Age' : age
}

for key, value in person_info.items():
      print (f"{key}: {value}")

## Exercise 4 
