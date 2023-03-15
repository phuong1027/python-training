# Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
if a == 0:
    if b == 0:
        print("The equation has many results.")
    else: # b != 0
        print("The equation has no results.")
else: # a != 0
    print("The result of the equation is:", -b/a)