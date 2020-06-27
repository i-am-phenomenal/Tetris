import pygame
import os 
import random

# Grid 
# Logic for creating tetromino 
# Logic for making them fall in the grid 
# Logic for collison detection
# Logic for game points 


def load_image(image_name):
    return pygame.image.load(images_dir + image_name)

pygame.init()
screen_height = 600
screen_width = 600
window = pygame.display.set_mode((screen_height, screen_width))
clock = pygame.time.Clock()

black_color = (0, 0, 0)
white_color = (200, 200, 200)
blue_color = (0, 0, 128)
images_dir = os.getcwd() + "/Images/"
grid = load_image("grid.jpg")
block_size = 25 #Set the size of the grid block
cube_block = load_image("cube-block.png")
i_block = load_image("i-block.png")
j_block = load_image("j-block.png")
l_block = load_image("L-block.png")
r_s_block = load_image("r-s-block.png")
s_block = load_image("s-block.png")
t_block = load_image("t-block.png")
tetrominos = [cube_block, i_block, j_block, l_block, r_s_block, s_block, t_block]


def render_window_in_center(): 
    x_pos =  screen_height / 2 - screen_width / 2
    y_pos =  screen_height - screen_width 
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (x_pos, y_pos)
    os.environ['SDL_VIDEO_CENTERED'] = '0'

def generate_tetrominos(x_coord, y_coord, counter): 
    if counter == 0: 
        block = tetrominos[0] 
    else: 
        block = random.choice(tetrominos)  
        
    window.blit(block, (x_coord, y_coord))

def render_grid():
    for x in range(0, 20):
        for y in range(int(screen_width / block_size)):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(window, white_color, rect, 1) # to render the border of the rectangle 


def game_loop():
    global window, clock, grid
    render_window_in_center()
    block_speed = 1
    block_start_y_coord = -50
    block_start_x_coord = random.randrange(0, 200)
    block_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    pygame.quit()
                    quit()

        window.blit(grid, (0, 0))
        render_grid()
        generate_tetrominos(block_start_x_coord, block_start_y_coord, block_count)
        block_start_y_coord += block_speed

        if block_start_y_coord > screen_height: 
            block_count = random.randrange(0, 7)


        pygame.display.update()
        clock.tick(60)
