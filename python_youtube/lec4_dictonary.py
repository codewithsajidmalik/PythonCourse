# info ={
#     "key" : "value",
#     "name" : "sajid",
#     "learning": "coding",
#     "age" : 35,
#     "is adult" : True,
#     "marks" : 45.6
# }
# print(info)

# info ={
#     "key" : "value",
#     "name" : "sajid",
#     "learning": "coding",
#     "subjects": ["python","pme"], # list datatypes
#     "topics": ("dic","set"),
#     "age" : 35,
#     "is adult" : True,
#     "marks" : 45.6
# }
# print(info)

#************nested dictonaries************
student = {
    "name" : "sajid",
    "subjects": {  # nested dictonaries
        "phy":34,
        "chem": 56,
        "math":78
    }
}


#*************methods of dictnaries************
print(student.keys())
print(student.values())
print(student.items()) # return the pair in the form of tuples