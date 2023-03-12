friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
#                0                  1                 2
#Cho biết chiều dài của friends
print(len(friends))

#Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
first_friend = friends[0]
print(type(first_friend))
middle_friend = friends[1]
print(type(middle_friend))
last_friend = friends[2]
print(type(last_friend))

#Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)
new_friend_name = input(f'Enter new friends name: ')
new_friend_gender = input(f'Enter new friends gender: ')
friends.append((new_friend_name, new_friend_gender))
print(friends)