set_a = set()

# Thêm 'Anna' vào set_a
set_a.add('Anna')
print(set_a)

# Thêm một tuple ('Kenny', 'Jen', 'Danny') / set.add() takes exactly one argument
set_a.update(['Kenny', 'Jen', 'Danny'])
print(set_a)

# In ra set_a và tính chiều dài của nó
print(set_a)
print('Lenght from set a:', len(set_a))
# Xóa 'Jen' ra khỏi set_a
set_a.remove('Jen')
print(set_a)

#Xóa tất cả các giá trị từ set_a
set_a.clear()
print(set_a)