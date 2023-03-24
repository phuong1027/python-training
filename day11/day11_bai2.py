#Định nghĩa một hàm được gọi là print_show_info nhận vào một tham số duy nhất đó là một dict, lúc gọi thì sử dụng dict như sau:
""" tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
} """

# Hàm nên in ra một chuỗi có định dạng như sau:
# Breaking Bad (2008) - 5 seasons

def print_show_info(tv_show):
    title = tv_show.get("title")
    season = tv_show.get("season")
    initial_release = tv_show.get("initial_release")
    print(f'{title} {season} {initial_release}')

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}
print(tv_show)