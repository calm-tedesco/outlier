import pygame
import random

# Initialize Pygame
pygame.init()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Set the width and height of each tile
TILE_SIZE = 100

# Set the margin between each tile
MARGIN = 5

# Set the size of the grid
GRID_SIZE = 3

# Set the size of the window
WINDOW_SIZE = GRID_SIZE * (TILE_SIZE + MARGIN) + MARGIN

# Create the window
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# Set the font for the tiles
FONT = pygame.font.SysFont("Arial", 36)

# Create a 2D list to represent the grid
grid = [[i + j * GRID_SIZE + 1 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

# Set the last tile to 0 to represent the empty tile
grid[GRID_SIZE - 1][GRID_SIZE - 1] = 0

# Create a variable to store the selected tile
selected_tile = None

# Create a variable to store the game state
game_started = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the click
            pos = pygame.mouse.get_pos()
            # Convert the position to grid coordinates
            col = pos[0] // (TILE_SIZE + MARGIN)
            row = pos[1] // (TILE_SIZE + MARGIN)

            # Check if the game has started
            if not game_started:
                # Check if the shuffle button was clicked
                if row == GRID_SIZE - 1 and col == GRID_SIZE - 1:
                    # Shuffle the grid
                    flat_list = [item for sublist in grid for item in sublist]
                    random.shuffle(flat_list)
                    grid = [flat_list[i:i + GRID_SIZE] for i in range(0, len(flat_list), GRID_SIZE)]
                    game_started = True
            else:
                # Check if a tile was clicked
                if grid[row][col] != 0:
                    if selected_tile is None:
                        # Select the tile
                        selected_tile = (row, col)
                    else:
                        # Get the position of the selected tile
                        sel_row, sel_col = selected_tile
                        # Check if the clicked tile is adjacent to the selected tile
                        if abs(sel_row - row) + abs(sel_col - col) == 1:
                            # Swap the tiles
                            grid[sel_row][sel_col], grid[row][col] = grid[row][col], grid[sel_row][sel_col]
                            # Check if the game is won
                            flat_list = [item for sublist in grid for item in sublist]
                            if flat_list == list(range(1, GRID_SIZE * GRID_SIZE)) + [0]:
                                print("Congratulations, you won!")
                                pygame.quit()
                                quit()
                        # Deselect the tile
                        selected_tile = None

    # Draw the grid
    WINDOW.fill(BLACK)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            # Draw the tile
            pygame.draw.rect(WINDOW, WHITE, (
                col * (TILE_SIZE + MARGIN) + MARGIN,
                row * (TILE_SIZE + MARGIN) + MARGIN,
                TILE_SIZE, TILE_SIZE))
            # Draw the number on the tile
            if grid[row][col] != 0:
                text = FONT.render(str(grid[row][col]), True, BLACK)
                text_rect = text.get_rect(center=(
                    col * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE // 2,
                    row * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE // 2))
                WINDOW.blit(text, text_rect)
            # Highlight the selected tile
            if (row, col) == selected_tile:
                pygame.draw.rect(WINDOW, YELLOW, (
                    col * (TILE_SIZE + MARGIN) + MARGIN,
                    row * (TILE_SIZE + MARGIN) + MARGIN,
                    TILE_SIZE, TILE_SIZE), 5)

    # Draw the shuffle button
    if not game_started:
        pygame.draw.rect(WINDOW, WHITE, (
            (GRID_SIZE - 1) * (TILE_SIZE + MARGIN) + MARGIN,
            (GRID_SIZE - 1) * (TILE_SIZE + MARGIN) + MARGIN,
            TILE_SIZE, TILE_SIZE))
        text = FONT.render("Shuffle", True, BLACK)
        text_rect = text.get_rect(center=(
            (GRID_SIZE - 1) * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE // 2,
            (GRID_SIZE - 1) * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE // 2))
        WINDOW.blit(text, text_rect)

    # Update the window
    pygame.display.update()
