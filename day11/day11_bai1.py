# Định nghĩa 4 hàm add, subtract, divide, multiply (+, -, /, *). Mỗi hàm nhận vào hai tham số thực hiện lần lượt các phép toán cộng, trừ, chia, nhân. Lưu ý hàm nên trả về thay vì in ra.
def add(value1, value2):
    return value1 + value2

def substract(value1, value2):
    return value1 - value2

def multiply(value1, value2):
    return value1 * value2

def divide(value1, value2):
    if value2 == 0:
        return "Error"
    return value1 / value2

a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))

total = add(a, b)
print('Add =', total)

sub = substract(a, b)
print('Substruct =', sub)

mul = multiply(a, b)
print('Multiply =', mul)

dev = divide(a, b)
print('Divide =', dev)