import pygame
import sys
import random

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

# Snake representation
SEGMENT_SIZE = 20  # Each segment is 20x20 pixels

# Direction constants
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

# Speed options
SLOW = 200    # 200ms delay - Chậm
MEDIUM = 150  # 150ms delay - Trung bình
FAST = 100    # 100ms delay - Nhanh

def draw_button(screen, text, x, y, width, height, normal_color, hover_color, text_color, font_size=30):
    """
    Draw a button and check if mouse is hovering over it
    
    Returns:
        Boolean indicating if mouse is hovering over button
    """
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)
    
    # Check if mouse is hovering over button
    hover = button_rect.collidepoint(mouse_pos)
    
    # Draw button with appropriate color
    pygame.draw.rect(screen, hover_color if hover else normal_color, button_rect)
    pygame.draw.rect(screen, WHITE, button_rect, 2)  # Button border
    
    # Draw button text
    font = pygame.font.SysFont('Arial', font_size)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=button_rect.center)
    screen.blit(text_surf, text_rect)
    
    return hover

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

def spawn_food(snake_segments, segment_size, width, height):
    """
    Spawn food at a random position aligned to the grid.
    
    Args:
        snake_segments: List of [x,y] coordinates for each snake segment
        segment_size: Size of each segment/food
        width: Width of the game window
        height: Height of the game window
        
    Returns:
        [x, y] coordinates for the food
    """
    # Calculate the number of possible positions in the grid
    grid_width = width // segment_size
    grid_height = height // segment_size
    
    while True:
        # Generate random grid position
        food_x = random.randint(0, grid_width - 1) * segment_size
        food_y = random.randint(0, grid_height - 1) * segment_size
        
        # Check if the food position overlaps with any snake segment
        food_position = [food_x, food_y]
        if food_position not in snake_segments:
            return food_position

def draw_food(screen, food_position, segment_size):
    """
    Draw the food on the screen.
    
    Args:
        screen: PyGame surface to draw on
        food_position: [x, y] coordinates of the food
        segment_size: Size of the food
    """
    # Draw food as a red rectangle
    pygame.draw.rect(screen, RED, [food_position[0], food_position[1], segment_size, segment_size])

def draw_snake(screen, snake_segments, segment_size):
    """
    Draw the snake on the screen.
    
    Args:
        screen: PyGame surface to draw on
        snake_segments: List of [x,y] coordinates for each snake segment
        segment_size: Size of each segment
    """
    for segment in snake_segments:
        # Draw each segment as a green rectangle
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], segment_size, segment_size])

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

def draw_score(screen, score):
    """
    Draw the score on the screen in the top-left corner.
    
    Args:
        screen: PyGame surface to draw on
        score: Current score (number of food eaten)
    """
    font = pygame.font.SysFont('Arial', 25)
    score_text = font.render(f'Điểm: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

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

# Main game function
def main():
    # Show start menu and get selected speed
    move_delay = show_start_menu()
    
    # Initialize snake
    snake_segments = [
        [WIDTH // 2 - SEGMENT_SIZE * 2, HEIGHT // 2],  # Tail segment
        [WIDTH // 2 - SEGMENT_SIZE, HEIGHT // 2],      # Middle segment
        [WIDTH // 2, HEIGHT // 2]                      # Head segment
    ]
    current_direction = RIGHT
    
    # Initialize food position and score
    food_position = spawn_food(snake_segments, SEGMENT_SIZE, WIDTH, HEIGHT)
    score = 0
    game_over = False
    
    clock = pygame.time.Clock()
    running = True
    
    # Timer for controlling snake movement speed
    move_timer = 0
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Restart game if it's over and player presses space
                if game_over and event.key == pygame.K_SPACE:
                    # Reset game state
                    snake_segments = [
                        [WIDTH // 2 - SEGMENT_SIZE * 2, HEIGHT // 2],
                        [WIDTH // 2 - SEGMENT_SIZE, HEIGHT // 2],
                        [WIDTH // 2, HEIGHT // 2]
                    ]
                    current_direction = RIGHT
                    food_position = spawn_food(snake_segments, SEGMENT_SIZE, WIDTH, HEIGHT)
                    score = 0
                    game_over = False
                # Change direction based on key press (only if game is not over)
                elif not game_over:
                    if event.key == pygame.K_UP and current_direction != DOWN:
                        current_direction = UP
                    elif event.key == pygame.K_DOWN and current_direction != UP:
                        current_direction = DOWN
                    elif event.key == pygame.K_LEFT and current_direction != RIGHT:
                        current_direction = LEFT
                    elif event.key == pygame.K_RIGHT and current_direction != LEFT:
                        current_direction = RIGHT
        
        # Fill the background
        WINDOW.fill(BLACK)
        
        # Only update game state if the game is not over
        if not game_over:
            # Get time passed since last frame
            dt = clock.tick(60)
            move_timer += dt
            
            # Move the snake when the timer exceeds the delay
            if move_timer >= move_delay:
                snake_segments, food_eaten = move_snake(snake_segments, current_direction, food_position, SEGMENT_SIZE)
                
                # Check for game over conditions
                if check_game_over(snake_segments, WIDTH, HEIGHT, SEGMENT_SIZE):
                    game_over = True
                
                # If food was eaten, spawn new food and increase score
                if food_eaten:
                    food_position = spawn_food(snake_segments, SEGMENT_SIZE, WIDTH, HEIGHT)
                    score += 1
                
                move_timer = 0  # Reset the timer
            
            # Draw the food
            draw_food(WINDOW, food_position, SEGMENT_SIZE)
            
            # Draw the snake
            draw_snake(WINDOW, snake_segments, SEGMENT_SIZE)
            
            # Draw the score in the top-left corner
            draw_score(WINDOW, score)
        else:
            # If game is over, display game over message with score
            game_over_font = pygame.font.SysFont('Arial', 50)
            score_font = pygame.font.SysFont('Arial', 30)
            
            game_over_text = game_over_font.render('Game Over!', True, WHITE)
            score_text = score_font.render(f'Điểm của bạn: {score}', True, WHITE)
            restart_text = score_font.render('Nhấn SPACE để chơi lại', True, WHITE)
            
            game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
            score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
            
            WINDOW.blit(game_over_text, game_over_rect)
            WINDOW.blit(score_text, score_rect)
            WINDOW.blit(restart_text, restart_rect)
        
        # Update the display
        pygame.display.update()
        
        # Control the frame rate
        if game_over:
            clock.tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
