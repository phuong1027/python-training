# Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số

a = float(input('Enter a number a: '))
b = float(input('Enter a number b: '))

if a > b:
    print(a, 'is the largest number.')
    print(b, 'ist the smallest number.')
else: # b>a
    print(a, 'is the smallest number.')
    print(b, 'is the largest number.')