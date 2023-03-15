# Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)

a = float(input('Enter a number a: '))
b = float(input('Enter a number b: '))
c = float(input('Enter a number c: '))
delta = b*b - 4*a*c

if delta < 0:
    print('The equation has no result.')
elif delta == 0:
    print('The equation has double result:', -b/(2*a))
else: # delta > 0
    print('The equation has two reslts:')
    import math #must import math, otherwise sqrt (square) is not defined.
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print('The first result:', x1)
    print('The second result:', x2)