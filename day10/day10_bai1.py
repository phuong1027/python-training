#Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension
#1
count_even = 0
count_odd = 0
for i in range(0, 1001):
    if i % 2 == 0:
        count_even += 1
    else: # i % 2 != 0
        count_odd += 1
print('There are', count_even, 'even numbers')
print('There are', count_odd, 'odd numbers')

#2 list comprehension
