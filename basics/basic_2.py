# #dictionary is represented as dict
# #dictionay=ry declaration

# #mutable : mean changeable

# user = dict(
#   first_name="Xenon",
#   middle_name="",
#   last_name="Saud",
#   username = "xenonsaud"
# ) #func builtins

# #if there is curly braces use "" double quote
# address = {
#   "country": "",
#   "state": "",
#   "local_level": "",
#   "ward": "",
#   "street": "",
#   "house_no": "",
#   "zip": 0
# } # value init

# user.update(key = "") #takes keyword argument  (some key = value {kwargs meaning})

# #getting value of key in dictionary
# #throws exception / error if not key is present

# fname = user["first_name"] # there must exist a key
# print(fname)

# #just attempt to get some value for any key

# # uname = user.get(key="username", default ="no username")
# uname = user.get("username", "no username")

# print(uname)

# #setting value in dict key
# #this is safe
# # if there is no country key then it can make

# address["country"] = "Nepal"
# # address["state"] = "bagmati"
# address.update(
#   state = "Bagmati",
#   local_level= "xyz",
#   ward= "31",
#   street= "abc",
#   house_no= "301",
#   zip=93010,
# )

# print(address)

# #list
# student_1 = dict (name = "", address = "")
# student_2 = dict (name = "", address = "")
# student_3 = dict (name = "", address = "")

# students =list()
# student_1.update(name = "Xenon", address = "ktm")
# students.append(student_1)
# student_2.update(name = "Sanjiv", address = "Okhaldhunga")
# students.append(student_2)
# student_3.update(name = "Ruzon", address = "Kathmandu")
# students.append(student_3)
# print(students)


#tuples
Roles = (
  ("ADMIN", "admin"),
  ("USER", "user"),
  ("XENON", "xenon"),
)
nums= (1,2,3,4)

#sets

Integers = {1,2,3,3,2,4,5,6,5}
# print(Integers)

name_list = ["xenon", "ruzon", "sanjiv"]
breakpoint()