# Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?

year = int(input('Enter a year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('The', year, 'is a leep year.')
else:
    print('The', year, 'ist not a leep year.')