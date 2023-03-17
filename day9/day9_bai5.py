# Nhập vào một số nguyên dương n tính tổng các chữ số của n.
# Ví dụ: n = 4312 => S = 4 + 3 + 1 + 2 = 10
#1
n = int(input("Enter a positive integer n: "))
sum = 0
for digit in str(n):
    sum += int(digit)
print("The sum of digits of positive n is:", sum)

#2
n = int(input('Enter a positive integer n: '))
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print("The sum of digits of positive n is:", sum)