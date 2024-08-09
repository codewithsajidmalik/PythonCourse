# f = open("demo.txt","r")
# data = f.read()
# line1  = f.readline()
# print(line1)

# print(data)
# print(type(data))
# f.close()

# **************writing to a file***********

# f = open("demo.txt","w")
# f.write("i am student")

# ***********appnd data*********
# f = open("demo.txt","a")
# f.write("i am student from nsps")

# f.close()

# ***********create file*********
# f = open("demo2.txt","w") #file a new name daalo and file create kro
# f.close()

# ***********overwrite a file no truncate means delete*********
# f = open("demo.txt","r+")
# f.write("khan")
# print(f.read()) # overwrite se nai print hogi file
# f.close()

# ***********Truncate a file means delete the file data*********
# f = open("demo.txt","w+")
# print(f.read())
# f.write("abc")
# f.close()

# ***********with syntax same as the other file function********* 
# with open("demo.txt","r") as f:
#     data=f.read()
#     print(data)

    # ***********Deleting the file using os*********
import os

os.remove("demo2.txt")






