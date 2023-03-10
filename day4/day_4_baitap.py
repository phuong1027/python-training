#Tạo một movies list chứa tên các bộ phim đã xem
#           0            1           2          3         4        5
films = ["Predator", "John Wick", "One Piece", "gió", "Avenger", "Dune"]

#Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
new_film = input(f"Enter a new film: ")

#Thêm bộ phim vừa nhập vào cuối của danh sách movies
films.append(new_film)
print(films)

#In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
#First
print(films[0])
#Last
print(films[-1])
#Middle
middle_film = len(films) // 2
print(films[middle_film])

#Tính tổng bộ phim có trong movies
print(len(films))

#Xóa bộ phim đầu và cuối trong movies
#First
films.remove("Predator") #remove chi thuc hien hanh dong, k can gan bien.
print(films)

#Last
films.remove("Demon Slayer") #remove chi thuc hien hanh dong, k can gan bien.
print(films)


#Lấy ra và xóa bộ phim cuối cùng trong movies
print(films.pop()) #chi in ra bo phim lay ra va xoa no.
print(films) # thieu 1 buoc in ra danh sach phim

#Chèn một bộ phim bất kỳ vào đầu danh sách movies
films.insert(0, "Inception") #remove chi thuc hien hanh dong, k can gan bien.
print(films)

#Đếm số bộ phim có tiêu đề là "One Piece"
amount_film = films.count("One Piece") #count phai gan bien
print(amount_film)

#Tìm vị trí của bộ phim có tên là "gió"
position_of_gio = films.index("gió")
print(position_of_gio)

#Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
new_favorite_films = ["AoT", "Loki"]
films.extend(new_favorite_films)
print(films)

#Xóa tất cả các bộ phim có trong danh sách
films.clear()
print(films)
