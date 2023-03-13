art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# All about 'join'
# Tìm những người bạn học cả vẽ lẫn toán
art_and_math_students = art_students.intersection(math_students)
print('Art and math students:', art_and_math_students)

# Tìm những người bạn học toán nhưng không học vẽ
just_study_math_students = math_students.difference(art_students)
print('Just study math students:', just_study_math_students)

# Tìm những người bạn học vẽ hay toán không phải cả hai
just_study_art_or_math_student = art_students.symmetric_difference(math_students)
print('Just study art or math student:', just_study_art_or_math_student)

# Tìm tất cả những người bạn
all_friends = art_students.union(math_students)
print(all_friends)