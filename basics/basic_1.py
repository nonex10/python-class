#variable in python


#  #snake case is used so we follow
#  #is case sensitive, cannnot start with 1school
 # name="xenon saud"
# school_name="pkmc"


if True:
  if True:
    pass      #no block can leave space
  

# print(name)
# print(school_name)

# name = input("Enter any name:\n")
# school_name = input("Enter your college:\n")

# print(name)
# print(school_name)

#list in python

# student_name=["xenon","sanjiv"]

# for index,student in enumerate(student_name): #forloop
#   print(index,student)
  #task 1
  
student_name = []


for i in range(3):
  name = input("enter any name:")
  student_name.append(name)
  
  #dispaying
print("\nstudent names are: ")
for i in range(3):
  print(f"student {i + 1}: {student_name[i]}") #f string allows to insert variables.
  
