#            0       1       2        3       4       5       6
friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
#            -7     -6       -5      -4      -3       -2      -1

#Lấy ra 4 người bạn đầu tiên trong friends
the_4_first_friends = friends[0:4]
print(the_4_first_friends)

#Lấy ra 4 người bạn cuối trong friends
the_4_last_friends = friends[3:]
print(the_4_last_friends)

#Đảo ngược danh sách friends
print(friends[::-1])

#Lấy ra những người bạn từ vị trí 1 đến hết
new_friendlist = friends[1:]
print(new_friendlist)

#Copy danh sách ban đầu thành một danh sách mới
new_friends = friends[:]
print(new_friends is friends)
print(new_friends == friends)

#Lấy ra những người bạn từ vị trí 2 đến sát cuối
another_friendlist = friends[2:-1]
print(another_friendlist)