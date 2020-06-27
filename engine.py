import pygame
import os 
import random

# Logic for collison detection
# Logic for game points 


def load_image(image_name):
    return pygame.image.load(images_dir + image_name)

def load_music(music_name): 
    music_dir = os.getcwd() + "/Music/"
    return pygame.mixer.Sound(music_dir + music_name)

pygame.init()
screen_height = 600
screen_width = 575
window = pygame.display.set_mode((screen_height, screen_width))
clock = pygame.time.Clock()

black_color = (0, 0, 0)
white_color = (200, 200, 200)
# blue_color = (0, 0, 128)
images_dir = os.getcwd() + "/Images/"
grid = load_image("grid.jpg")
cube_block = load_image("cube-block.png")
i_block = load_image("i-block.png")
j_block = load_image("j-block.png")
l_block = load_image("L-block.png")
r_s_block = load_image("r-s-block.png")
s_block = load_image("s-block.png")
t_block = load_image("t-block.png")
score_board = load_image("score_board.jpg")
tetrominos = [cube_block, i_block, j_block, l_block, r_s_block, s_block, t_block]
GRIDSIZE = screen_height // 24
COLLAPSED_BLOCKS = []

x_pos =  100 #screen_height / 2 - screen_width / 2
y_pos =  0 #screen_height - screen_width 
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (x_pos, y_pos)
os.environ['SDL_VIDEO_CENTERED'] = '0'


""" BACKGROUND MUSIC """
kalinka = load_music("kalinka.ogg")
katyusha = load_music("katyusha.ogg")
korobushka = load_music("korobushka.ogg")
smuglianka = load_music("smuglianka.ogg")

background_music = random.choice([kalinka, katyusha, korobushka, smuglianka])

pygame.mixer.Channel(0).play(background_music, -1)

def render_collapsed_blocks():
    global COLLAPSED_BLOCKS
    if COLLAPSED_BLOCKS == []: 
        return
    else: 
        for block_dict in COLLAPSED_BLOCKS: 
            window.blit(block_dict["current_block"], (block_dict["x_coord"], block_dict["y_coord"]))

def generate_tetrominos(x_coord, y_coord, counter): 
    if counter == 0: 
        counter = random.randrange(0, 7)
        block = tetrominos[0] 
    else: 
        block = tetrominos[counter]
        
    window.blit(block, (x_coord, y_coord))

def render_grid():
    """ Draw horizontal and vertical lines on the entire game window.
        Space between the lines is GRIDSIZE.
    """
    for i in range(15):
        pygame.draw.line(window, black_color, (i * GRIDSIZE, 0), (i * GRIDSIZE, screen_height), 1)

    for i in range(24):
        pygame.draw.line(window, black_color, (0, i * GRIDSIZE), (GRIDSIZE * 24, i * GRIDSIZE), 1)

def render_score_board(): 
    window.blit(score_board, (375, 0))

def game_loop():
    global window, clock, grid
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

            if event.key == pygame.K_DOWN: 
                block_speed += 1

            if event.key == pygame.K_LEFT: 
                block_start_x_coord -= 2

            if event.key == pygame.K_RIGHT: 
                block_start_x_coord += 2

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_DOWN: 
                block_speed = 1

        window.blit(grid, (0, 0))
        render_grid()
        render_score_board()
        render_collapsed_blocks()
        generate_tetrominos(block_start_x_coord, block_start_y_coord, block_count)
        block_start_y_coord += block_speed
        
        if block_start_y_coord == 530:
            global COLLAPSED_BLOCKS
            block_dict = {"current_block": tetrominos[block_count], "x_coord": block_start_x_coord, "y_coord": block_start_y_coord} 
            COLLAPSED_BLOCKS.append(block_dict)
            block_count = random.randrange(0, 7)
            block_start_y_coord = -50
            block_start_x_coord = random.randrange(0, 200)
            

        pygame.display.update()
        clock.tick(60)
