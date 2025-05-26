# Snake Game

A classic Snake game implemented in Python using Pygame. The player controls a snake that grows longer as it eats food, with the goal of achieving the highest score possible without colliding with walls or itself.

![Snake Game](https://github.com/mvn-bachhuynh-dn/snake-amazonq/raw/main/screenshot.png)

## Phát triển với Amazon Q

Dự án này được phát triển hoàn toàn với sự hỗ trợ của Amazon Q, một trợ lý AI được phát triển bởi AWS. Quá trình phát triển bao gồm các bước sau:

1. **Tạo mã nguồn game**: Amazon Q đã tạo toàn bộ mã nguồn cho game Snake, bao gồm các chức năng:
   - Thiết kế giao diện người dùng với Pygame
   - Xây dựng logic di chuyển của rắn
   - Tạo hệ thống tính điểm
   - Xử lý va chạm và kết thúc game
   - Tạo menu lựa chọn tốc độ

2. **Quản lý mã nguồn với Git**:
   - Khởi tạo repository
   - Commit mã nguồn ban đầu
   - Push lên GitHub

3. **Tạo tài liệu**:
   - Tạo file README.md với hướng dẫn cài đặt và sử dụng
   - Mô tả chi tiết các tính năng và cách tùy chỉnh game

Toàn bộ quá trình được thực hiện thông qua giao diện dòng lệnh (CLI) của Amazon Q, cho thấy khả năng hỗ trợ phát triển phần mềm toàn diện của công cụ này.

## Tính năng

- Giao diện đơn giản, dễ sử dụng
- Ba mức độ tốc độ: Chậm, Trung bình, Nhanh
- Hệ thống tính điểm
- Khả năng chơi lại sau khi thua

## Yêu cầu hệ thống

- Python 3.6 hoặc cao hơn
- Pygame

## Cài đặt

1. Đảm bảo bạn đã cài đặt Python 3.6 hoặc cao hơn. Bạn có thể tải Python tại [python.org](https://www.python.org/downloads/).

2. Cài đặt thư viện Pygame bằng pip:

```bash
pip install pygame
```

3. Clone repository này:

```bash
git clone https://github.com/mvn-bachhuynh-dn/snake-amazonq.git
cd snake-amazonq
```

4. Hoặc tải xuống mã nguồn dưới dạng file ZIP và giải nén.

## Cách chơi

1. Chạy game bằng lệnh:

```bash
python snake_game.py
```

2. Trong menu bắt đầu, chọn tốc độ mong muốn (Chậm, Trung bình, Nhanh) và nhấn nút "Chơi".

3. Sử dụng các phím mũi tên để điều khiển rắn:
   - ↑: Di chuyển lên
   - ↓: Di chuyển xuống
   - ←: Di chuyển sang trái
   - →: Di chuyển sang phải

4. Mục tiêu là ăn thức ăn (hình vuông màu đỏ) để tăng điểm và độ dài của rắn.

5. Trò chơi kết thúc khi rắn va chạm vào tường hoặc chính nó.

6. Sau khi thua, nhấn phím SPACE để chơi lại.

## Cấu trúc mã nguồn

- `snake_game.py`: File chính chứa toàn bộ mã nguồn của trò chơi

## Tùy chỉnh

Bạn có thể tùy chỉnh trò chơi bằng cách thay đổi các giá trị trong mã nguồn:

- `WIDTH` và `HEIGHT`: Kích thước cửa sổ trò chơi
- `SEGMENT_SIZE`: Kích thước của mỗi đoạn rắn và thức ăn
- `SLOW`, `MEDIUM`, `FAST`: Tốc độ di chuyển của rắn (giá trị càng nhỏ, tốc độ càng nhanh)
- Các màu sắc: `BLACK`, `GREEN`, `RED`, `WHITE`, v.v.

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng tạo issue hoặc pull request nếu bạn muốn cải thiện trò chơi.

## Giấy phép

[MIT License](LICENSE)
