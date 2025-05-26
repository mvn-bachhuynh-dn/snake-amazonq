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

### Các Prompt Sử Dụng

Dưới đây là các prompt chính đã được sử dụng trong quá trình phát triển game:

1. **Tạo game Snake với Pygame**:
   ```
   Tạo một game Snake đơn giản bằng Python và Pygame
   ```

2. **Quản lý mã nguồn với Git**:
   ```
   commit toàn bộ trong folder này
   push lên nhánh main giúp tôi
   ```

3. **Tạo tài liệu**:
   ```
   Tạo file README hướng dẫn cài đặt và sử dụng game này!
   ```

### Ví Dụ Tương Tác với Amazon Q

Dưới đây là một số ví dụ về cách Amazon Q phản hồi các yêu cầu trong quá trình phát triển:

#### 1. Khi yêu cầu tạo game Snake

```
User: Tạo một game Snake đơn giản bằng Python và Pygame

Amazon Q: Tôi sẽ giúp bạn tạo một game Snake đơn giản bằng Python và Pygame. Dưới đây là mã nguồn đầy đủ cho game:

[Mã nguồn game Snake với đầy đủ chức năng]

Game này có các tính năng:
- Di chuyển rắn bằng phím mũi tên
- Hệ thống tính điểm khi ăn thức ăn
- Phát hiện va chạm với tường và thân rắn
- Menu lựa chọn tốc độ (Chậm, Trung bình, Nhanh)
- Khả năng chơi lại sau khi thua

Bạn có thể chạy game bằng cách lưu mã nguồn vào file snake_game.py và chạy lệnh: python snake_game.py
```

#### 2. Khi yêu cầu commit code

```
User: commit toàn bộ trong folder này

Amazon Q: Tôi sẽ giúp bạn commit tất cả các thay đổi trong thư mục hiện tại.

[Kiểm tra trạng thái git]
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	snake_game.py

[Thêm tất cả các file vào staging area]
[Commit các thay đổi]
[main (root-commit) 6e8fafb] Initial commit of snake game
 1 file changed, 383 insertions(+)
 create mode 100644 snake_game.py

Đã commit thành công! Tất cả các thay đổi trong thư mục hiện tại đã được commit vào repository.
```

#### 3. Khi yêu cầu tạo README

```
User: Tạo file README hướng dẫn cài đặt và sử dụng game này!

Amazon Q: Tôi sẽ tạo một file README với hướng dẫn cài đặt và sử dụng game Snake.

[Tạo file README.md với nội dung đầy đủ]
[Commit file README.md]
[main c312460] Add README with installation and usage instructions
 1 file changed, 79 insertions(+)
 create mode 100644 README.md

Đã tạo file README.md với hướng dẫn cài đặt và sử dụng game rắn thành công!

File README.md bao gồm các thông tin:
1. Giới thiệu về trò chơi Snake
2. Tính năng chính của game
3. Yêu cầu hệ thống
4. Hướng dẫn cài đặt
5. Cách chơi game
...
```

### Ví Dụ Code Mẫu

Dưới đây là một số đoạn code mẫu quan trọng trong game:

#### 1. Khởi tạo game và thiết lập màn hình

```python
# Initialize pygame
pygame.init()

# Set up display dimensions
WIDTH = 600
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
LIGHT_GREEN = (100, 255, 100)
```

#### 2. Di chuyển rắn và kiểm tra ăn thức ăn

```python
def move_snake(segments, direction, food_position, segment_size=20):
    """
    Move the snake based on its current direction.
    
    Args:
        segments: List of [x,y] coordinates for each snake segment
        direction: Current direction of movement (UP, DOWN, LEFT, RIGHT)
        food_position: [x, y] coordinates of the food
        segment_size: Size of each snake segment
        
    Returns:
        Updated snake segments list, boolean indicating if food was eaten
    """
    # Get the current head position
    head_x, head_y = segments[-1]
    
    # Calculate the new head position based on direction
    if direction == UP:
        new_head = [head_x, head_y - segment_size]
    elif direction == DOWN:
        new_head = [head_x, head_y + segment_size]
    elif direction == LEFT:
        new_head = [head_x - segment_size, head_y]
    elif direction == RIGHT:
        new_head = [head_x + segment_size, head_y]
    
    # Add the new head to the snake
    segments.append(new_head)
    
    # Check if the snake ate the food
    food_eaten = new_head == food_position
    
    # Remove the tail segment only if the snake didn't eat food
    if not food_eaten:
        segments.pop(0)
    
    return segments, food_eaten
```

#### 3. Kiểm tra kết thúc game

```python
def check_game_over(snake_segments, width, height, segment_size):
    """
    Check if the game is over due to wall collision or self-collision.
    
    Args:
        snake_segments: List of [x,y] coordinates for each snake segment
        width: Width of the game window
        height: Height of the game window
        segment_size: Size of each snake segment
        
    Returns:
        Boolean indicating if the game is over
    """
    # Get the head position
    head_x, head_y = snake_segments[-1]
    
    # Check wall collision
    if (head_x < 0 or head_x >= width or 
        head_y < 0 or head_y >= height):
        return True
    
    # Check self-collision (head hitting any part of the body)
    # Skip the last element (the head itself)
    for segment in snake_segments[:-1]:
        if segment == snake_segments[-1]:
            return True
            
    return False
```

#### 4. Menu lựa chọn tốc độ

```python
def show_start_menu():
    """
    Display the start menu with speed selection options
    
    Returns:
        Selected speed (delay in milliseconds)
    """
    selected_speed = MEDIUM  # Default speed
    
    menu_running = True
    while menu_running:
        WINDOW.fill(BLACK)
        
        # Draw title
        title_font = pygame.font.SysFont('Arial', 50)
        title_text = title_font.render('Snake Game', True, GREEN)
        title_rect = title_text.get_rect(center=(WIDTH//2, 80))
        WINDOW.blit(title_text, title_rect)
        
        # Draw speed selection text
        speed_font = pygame.font.SysFont('Arial', 30)
        speed_text = speed_font.render('Chọn tốc độ:', True, WHITE)
        speed_rect = speed_text.get_rect(center=(WIDTH//2, 150))
        WINDOW.blit(speed_text, speed_rect)
        
        # Draw speed buttons
        button_width = 120
        button_height = 40
        button_y = 200
        spacing = 30
        
        # Calculate positions for 3 buttons centered horizontally
        total_width = 3 * button_width + 2 * spacing
        start_x = (WIDTH - total_width) // 2
        
        # Draw speed buttons
        slow_hover = draw_button(WINDOW, "Chậm", start_x, button_y, 
                                button_width, button_height, 
                                GRAY, LIGHT_GREEN, WHITE, 25)
        
        medium_hover = draw_button(WINDOW, "Trung bình", start_x + button_width + spacing, button_y, 
                                  button_width, button_height, 
                                  GRAY, LIGHT_GREEN, WHITE, 25)
        
        fast_hover = draw_button(WINDOW, "Nhanh", start_x + 2 * (button_width + spacing), button_y, 
                                button_width, button_height, 
                                GRAY, LIGHT_GREEN, WHITE, 25)
        
        # Highlight the currently selected speed
        if selected_speed == SLOW:
            pygame.draw.rect(WINDOW, GREEN, (start_x, button_y, button_width, button_height), 3)
        elif selected_speed == MEDIUM:
            pygame.draw.rect(WINDOW, GREEN, (start_x + button_width + spacing, button_y, button_width, button_height), 3)
        elif selected_speed == FAST:
            pygame.draw.rect(WINDOW, GREEN, (start_x + 2 * (button_width + spacing), button_y, button_width, button_height), 3)
        
        # Draw play button
        play_hover = draw_button(WINDOW, "Chơi", WIDTH//2 - 60, 280, 120, 50, GREEN, LIGHT_GREEN, BLACK, 30)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if slow_hover:
                        selected_speed = SLOW
                    elif medium_hover:
                        selected_speed = MEDIUM
                    elif fast_hover:
                        selected_speed = FAST
                    elif play_hover:
                        menu_running = False  # Exit menu and start game
        
        pygame.display.update()
    
    return selected_speed
```

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
python snake_game.py #sẽ báo lỗi thiếu môi trường
```
Vì thế hãy vào Amazon Q, bằng cách gõ `q` và nhấn enter
```
Chạy code
```

Amazon Q sẽ phát hiện và cài đặt các môi trường python cần thiết!

1. Trong menu bắt đầu, chọn tốc độ mong muốn (Chậm, Trung bình, Nhanh) và nhấn nút "Chơi".

2. Sử dụng các phím mũi tên để điều khiển rắn:
   - ↑: Di chuyển lên
   - ↓: Di chuyển xuống
   - ←: Di chuyển sang trái
   - →: Di chuyển sang phải

3. Mục tiêu là ăn thức ăn (hình vuông màu đỏ) để tăng điểm và độ dài của rắn.

4. Trò chơi kết thúc khi rắn va chạm vào tường hoặc chính nó.

5. Sau khi thua, nhấn phím SPACE để chơi lại.

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
