# Python
1
-

Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:

Ví dụ với user ``pymivn``, sử dụng dữ liệu ở JSON format tại
https://api.github.com/users/pymivn/repos

Câu lệnh của chương trình có dạng::

  python3 githubrepos.py username

Gợi ý:

Sử dụng các thư viện:

- requests
- sys or argparse

2
-

Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Dạng của câu lệnh::

  ketqua.py [NUMBER1] [NUMBER2] [...]

Các thư viện:

- requests
- requests_html hay beautifulsoup4 [tuỳ chọn]
- argparse hay sys.argv

Gợi ý:

- ``nargs`` https://docs.python.org/2/library/argparse.html

3
-

Viết script lấy top **N** câu hỏi được vote cao nhất của tag **LABEL** trên stackoverflow.com.
In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất

Link API: https://api.stackexchange.com/docs

Dạng của câu lệnh:

  python3 so.py N LABEL

4
-

Viết script tìm 50 quán bia / quán nhậu / quán bar / nhà hàng quanh toạ độ của lớp học (lên google map để lấy) với bán kính 2KM.
Ghi kết quả theo định dạng JSON vào file pymi_beer.geojson

Sử dụng Google Map API
https://developers.google.com/places/web-service/

Chú ý: phải tạo "token" để có thể truy cập API.

Chú ý: giữa mỗi trang kết quả phải đợi để lấy tiếp.

Chú ý: tránh đặt ngược lat/long

- Kết quả trả về lưu theo format JSON, với mỗi điểm là một GeoJSON point (https://leafletjs.com/examples/geojson/), up file này lên GitHub để xem bản đồ kết quả.

- Xem mẫu GEOJSON https://github.com/tung491/make_boba_map

5
-

Viết script dùng API tạo 1 Trello board với 2 list "Thứ 3", "Thứ 5",
và tạo 12 card ứng với 12 buổi học của lớp, có set due date ứng với các ngày
học.

Ví dụ kết quả: https://trello.com/b/yEskTV8S/h%E1%BB%8Dc-python-h%C3%A0-n%E1%BB%99i-pymivn-hn2006-timetable

API: https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/

https://developer.atlassian.com/cloud/trello/rest/#api-boards-post
https://developer.atlassian.com/cloud/trello/rest/#api-lists-post
https://developer.atlassian.com/cloud/trello/rest/#api-cards-post

