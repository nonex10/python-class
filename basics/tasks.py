#task 1
  
# student_name = []


# for i in range(3):
#   name = input("enter any name:")
#   student_name.append(name)
  
#   #dispaying
# print("\nstudent names are: ")
# for i in range(3):
#   print(f"student {i + 1}: {student_name[i]}") #f string allows to insert variables.

  #task 2: from terminal ask 5 student name and append to list of student
  #hint for i in range
  #declare list variable
  #ask student name and address
  
   #list
# studentname = []
# student_address = []

# for i in range(5):
#   name = input ("Name:")
#   address = input ("Address:")
#   studentname.append(name)
#   student_address.append(address)
  
# print("\n Students name and address:")
# for i in range(5):
#   print(f"Student {i + 1}: {studentname[i], student_address[i]}")
  
# dict

students = []
for i in range (5):
  name = input("Name:")
  address=input("Address:")
  
  students = dict (
    names = name,
    addresses = address,
  )
  
  students.append(students)
  for i in students:
    print(i)