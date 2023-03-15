# Nhập vào một số nguyên n. Kiểm tra và in ra n là số chẵn hay lẻ

n = int(input('Enter a number: '))

if n % 2 == 0:
    print('This number is even:', n)
else: # n % 2 != 0
    print('This number ist odd:', n)
