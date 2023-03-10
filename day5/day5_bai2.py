"""
students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
Yêu cầu:
a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
b. Lấy ra tuổi của sinh viên thứ hai
c. Lấy ra thông tin hai sinh viên cuối cùng
d. Lấy ra id của sinh viên thứ ba
"""
#                      0                    1                         2
#               0       1    2        0       1       2       0       1      2
students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]

#Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
first_student = students[0]
print(first_student)
first_student_ID = first_student[0]
print('ID:', first_student_ID)
first_student_name = first_student[1]
print('Name: ', first_student_name)
first_student_age = first_student[2]
print('age: ', first_student_age)

#Lấy ra tuổi của sinh viên thứ hai
#1
second_student = students[1]
print(second_student)
second_student_age = second_student[2]
print('Age:', second_student_age)
#2
student_age = students[1][2]
print('Age: ', student_age)

#Lấy ra thông tin hai sinh viên cuối cùng
two_last_student = students[1:]
print('Student infos:' ,two_last_student)

#Lấy ra id của sinh viên thứ ba
student_ID = students[2][0]
print('ID: ', student_ID)