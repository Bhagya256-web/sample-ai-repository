# import os
# import csv
with open("db.csv","r") as file:
    for line in file:
        data = line.strip().split(",")
        print("Dear ",data[1],", Your user ID is ",data[0])
        response=os.system("ping -c 1 "+data[3])

# with open("students.csv","w") as file:
#     file.write("name,age,grade\n")
#     file.write("Bhagya,28,A\n")
#     file.write("Kusuma,25,B\n")

# students=[
#     ["name","age","grade"],
#     ["Bhagya K",28,"A"],
#     ["Kusuma K",25,"B"]
# ]

# with open("new_student.csv","w",newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(students)

# with open("new_student.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)