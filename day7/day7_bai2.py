album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}

# Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
#1
album_name = album_info["album_name"]
print(f'Value of album name is:', album_name)
release_year = album_info["release_year"]
print(f'Release year of the album:', release_year)
#2
print(album_info.get("album_name"))
print(album_info.get("release_year"))

# Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info['release_year'] = 1971
print(album_info)

# Xóa phần tử với key là track_list (album_info.pop("track_list")
del album_info["track_list"]
print(album_info)

# Thêm một key mới là amount = 2000 bằng hai cách 
#1
album_info['amount'] = 2000
print(album_info)

#2
new_info = {'amount': '2000'}
album_info.update(new_info)
print(album_info)

# Làm trống dict: album_info
album_info.clear()
print(album_info)