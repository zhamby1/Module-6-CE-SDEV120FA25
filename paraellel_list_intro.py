#this proigram will use students at a college to display related data
#we will relate a students age, name, and grade


#parellel lists/arrays utilize indexes to keep everything in order
#if you want to relate data they must be in the same position or index

student_names = ["Zach","Tim","Lisa"]
student_ages = [22,18,34]
student_grades = ["A","B","B"]

#to just print the data, make sure you are using the same position of the arrays/lists

print(student_names[0], "age is", student_ages[0], "and their grade is", student_grades[0])

#remember we can display multiple pieces of data using a loop.
#we can use a loop variable and iterate over all of these items
#we can do this by make sure we use the same index for each entry

#because we have to use a loop variable, we will us a for i in range loop
#because all arrays that are related must be the same size, we can just pick whatever list/array we want to grab the length of
for i in range(len(student_names)):
    print(student_names[i], "age is", student_ages[i], "and their grade is", student_grades[i])