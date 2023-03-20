""" 
In ra người già nhất
Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
In ra enumerate các key trong people dict
Sử dụng hàm dict để biến enumerate bên trên trở thành dict 
"""
people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}
#In ra người già nhất
#1
oldest_person = max(people.values())
print(oldest_person)

#2
max_person = [(value, key) for key, value in people.items()]
print(max(max_person))

# Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
new_age = {}
for name, age in people.items():
    new_age[name] = age * 2
print(new_age)

# In ra enumerate các key trong people dict
for i, k in enumerate(people):
    print(i, k)

#Sử dụng hàm dict để biến enumerate bên trên trở thành dict 
print(dict(enumerate(people)))