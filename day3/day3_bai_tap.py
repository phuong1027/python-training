# 1: Nhập vào từ bàn phím hai số thực number1, number2. Hãy in ra tổng, hiệu, tích, thương, chia nguyên, chia lấy dư, lũy thừa của hai số đó.
num1 = 10
num2 = 5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)


# 2.Dự đoán kết quả của các biểu thức so sánh sau:

print('a' > 'b')  # ASCII a: 97, b: 98, output: False

print(3.0 > 3)  # 3.0 =3, output False

print('' <= ' ')  # '' thuoc ' ', output True

print(.5 > 1)  # 0.5 < 1, output: False


# 3. Dự đoán kết quả của các biểu thức logic sau:

print(0 and 1)  # 0 = False -> output: 0

print('' or 'none')  # '' = Falsy  output: none

print(3 and 4 or 0)
# and > or, and: 3 = true -> 4, (4 or 0) : 4 = True ->4
# -> output: 4

print('not' or 'none')  # not (non-empty string) = True, output: not

print(not 0)  # not 0 ist 1, output: True


# 4. Nhập vào số nguyên n. Hãy thực hiện các công việc sau:
# tăng n lên 10 đơn vị
# gấp 3 lần n
# giảm n đi 9 đơn vị
# Cuối cùng in ra n

n = 12

n = n + 10
print(n)

n = 3 * n
print(n)

n = n - 9
print(9)
