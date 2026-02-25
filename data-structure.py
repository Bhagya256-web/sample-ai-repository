#Lists
students=["Bhagya","Kusuma","Anjali","Isha"]
numbers=[1,2,3,4,4,5]
mixed=[1,"Bhagya",25.4,True]

#print(students)
#students[1]="Akash"
#students.pop()
# print(students)
# #Length
# print("Lenght of students listy is ",len(students))
# #sum,min,mx
# print("Sum of all numbers in Numbers list is ",sum(numbers))
# print("min number in the numbers list is ",min(numbers))
# print("max number in the numbers list is ",max(numbers))
# #count
# print("Total number of occurences of number 4 is ",numbers.count(4))
# #find index
# print("The index of the List Item Kusuma is ",students.index("Kusuma"))
# #sort
# students.sort()
# print(students)
# #revese
# numbers.reverse()
# print(numbers)
# #Check Membership
# print("Kusuma"  in students)
# for name in students:
#     print(name)

# print(range(len(students)))

# for i in range(len(students)):
#     print(f"{i}: {students[i]}")

# print(enumerate(students))
# for k,v in enumerate(students):
#     print(f"{k}: {v}")

#squares = []
# for i in range(1,6):
#     squares.append(i ** 2)

# squares = [i ** 2 for i in range(1,6)]   
# print(squares)

#Tuples
coordinates=(10,20)
person = ("Anjali",25,"Davanagere")
#print(person[2])

name,age,district=person

#print(f"I am {name}, from {district}. I am {age} years old")

#Dictionaries
mathClass={}

student={
    "name":"Bhagya",
    "age":25,
    "grade":"A",
    "courses":["Math","Science","Social Science"]
}

#print(student["name"])
student["phone"]="5675675674"

#print(student.get("phone","User's Phone number doesn't exist"))

student['age']=26
#print(student)

#student.pop("grade")
#print(student)
# for key in student:
#     print(f"{key}: {student[key]}")

# for key,value in student.items():
#     print(f"{key}:{value}")

#Sets

# empty_set=set()
# numbers=[1,2,3,1,3,4,3,6,7,888,9,2,4,5,5,5,5,5,5]
# unique_numbers=set(numbers)
# print(numbers)
# print(unique_numbers)

# unique_numbers.discard(999)