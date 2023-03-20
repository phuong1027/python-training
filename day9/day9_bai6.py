# Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]
n = int(input('Enter a positive integer n: '))
count_even = 0
count_odd = 0
for i in range(0, n+1): # range don't count stop
    if i % 2 == 0:
        count_even += 1
    else: # i % 2 != 0
        count_odd += 1
print('There are', count_even, 'even numbers')
print('There are', count_odd, 'odd numbers')