import pygame
import os 
import random
import math 
import time


# Logic for collison detection
# Logic for game points 
# WIP: move tetrominos in blocks

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
BLOCK_Y_COORDS = [x for x in range(531) if x % GRIDSIZE  == 0]
BLOCK_X_COORDS = [x for x in range(326) if x % GRIDSIZE == 0 ]



""" WIP : POSITION THE WINDOW AT THE CENTER """ 
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

# pygame.mixer.Channel(0).play(background_music, -1)

#---------------------------------------------------------------


def get_current_block(counter):
    if counter == 0 :
        return "cube"

    elif counter == 1:
        return "i_block"

    elif counter == 2: 
        return "j_block"

    elif counter == 3: 
        return "l_block"

    elif counter == 4: 
        return "r_s_block"

    elif counter == 5: 
        return "s_block"

    elif counter == 6: 
        return "t_block"

    else:  
        return None

def render_collapsed_blocks():
    global COLLAPSED_BLOCKS
    if COLLAPSED_BLOCKS == []: 
        return
    else: 
        for block_dict in COLLAPSED_BLOCKS: 
            window.blit(block_dict["current_block"], (block_dict["x_coord"], block_dict["y_coord"]))

def generate_tetrominos(x_coord, y_coord, counter): 
    global GRIDSIZE
    # if counter == 0: 
    block = tetrominos[0] 
    # else: 
    #     block = tetrominos[counter]

    window.blit(block, (x_coord, y_coord))
    return block


def render_grid():
    """ Draw horizontal and vertical lines on the entire game window.
        Space between the lines is GRIDSIZE.
        24 rows and 15 columns.
    """
    for i in range(15):
        pygame.draw.line(window, black_color, (i * GRIDSIZE, 0), (i * GRIDSIZE, screen_height), 1)

    for i in range(24):
        pygame.draw.line(window, black_color, (0, i * GRIDSIZE), (GRIDSIZE * 24, i * GRIDSIZE), 1)

def render_score_board(): 
    window.blit(score_board, (375, 0))

def check_collision_for_cube(current_row, current_column): 
    global COLLAPSED_BLOCKS

    #WIP Conditions
    # print(COLLAPSED_BLOCKS)
    """ SWAPPING CURRENT ROW AND CURRENT COLUMN BECAUSE WE MIGHT HAVE WRONG VALUES IN THESE VARS"""
    temp = 0
    temp = current_row 
    current_row = current_column
    current_column = temp

    # print((current_row, current_column))
    for block in COLLAPSED_BLOCKS: 
        # This is done just to make it more readable for myself
        condition_1 = (block["row"] == current_row and block["column"] == current_column) 
        condition_2 = (block["row"] == (current_row - 1) and block["column"] == (current_column - 1))
        # print((block["row"], block["column"]), "   --->   ", (current_row, current_column))

        print(type(current_row), type(current_column), type(block["row"]), type(block["column"]))
        if condition_2: # or condition_2: # or condition_3 or condition_4 or condition_5:
            print("TRUE")
            return True

        else: 
            pass

    return False

def block_collision_cases(current_block, row, column): 
    global tetrominos
    if current_block is not None: 
        if current_block == "cube":
            if check_collision_for_cube(row, column): 
                return True
                # current_block = tetrominos[0]
                # window.blit(current_block, (x_coord, y_coord))

    else: 
        pass

def check_for_collision(x_coord, y_coord, block_count): 
    global COLLAPSED_BLOCKS, tetrominos

    current_block  = get_current_block(block_count)
    
    current_row =  math.ceil(x_coord / GRIDSIZE) + 1
    current_column =  math.ceil(y_coord / GRIDSIZE) + 1
    return block_collision_cases(current_block, current_row, current_column)
    

def update_block_counter(counter):
    global BLOCK_Y_COORDS
    length = len(BLOCK_Y_COORDS) - 1
    if counter == length: 
        return 0

    elif counter < length:
        return counter + 1 

    elif counter > length:
        return 0

    else: 
        pass
        

def game_loop():
    global window, clock, grid, GRIDSIZE, BLOCK_Y_COORDS, BLOCK_X_COORDS, COLLAPSED_BLOCKS 
    block_counter = 0
    block_start_y_coord = -100
    block_start_x_coord = random.choice(BLOCK_X_COORDS)
    block_count = 0 
    block_x_counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: 
                pygame.quit()
                quit()

            if event.key == pygame.K_DOWN and block_start_y_coord <= 520: 
                block_counter += 1
                
            if event.key == pygame.K_LEFT and block_start_x_coord >= 10: 
                block_start_x_coord -= GRIDSIZE

            if event.key == pygame.K_RIGHT and block_start_x_coord <= 315:                 
                block_start_x_coord += GRIDSIZE

        # if event.type == pygame.KEYUP: 
        #     0
            # if event.key == pygame.K_DOWN: 
                # block_counter = 0

            # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                

        window.blit(grid, (0, 0))
        render_grid()
        render_score_board()
        render_collapsed_blocks()
        block = generate_tetrominos(block_start_x_coord, block_start_y_coord, block_count)
        
        block_counter = update_block_counter(block_counter)
        block_start_y_coord = BLOCK_Y_COORDS[block_counter]
        clock.tick(8)
        
        if check_for_collision(block_start_x_coord, block_start_y_coord, block_count):
            block_dict = {
                "current_block": tetrominos[block_count], 
                "x_coord": block_start_x_coord, 
                "y_coord": block_start_y_coord,
                "row": math.ceil(block_start_x_coord / GRIDSIZE) + 1,
                "column": math.ceil(block_start_y_coord / GRIDSIZE) + 1
                } 

            COLLAPSED_BLOCKS.append(block_dict)
            block_count = 0 #random.randrange(0, 7)
            block_start_y_coord = -100
            block_start_x_coord = random.choice([x for x in range(326) if x % GRIDSIZE == 0 ])
            # block_start_y_coord = -100
            # block_start_x_coord = random.choice([x for x in range(326) if x % GRIDSIZE == 0 ])
         
        
        if block_start_y_coord > 525: 
            block_start_y_coord = 525

        if block_start_y_coord == 525:            
            block_dict = {
                "current_block": tetrominos[block_count], 
                "x_coord": block_start_x_coord, 
                "y_coord": block_start_y_coord,
                "column": math.ceil(block_start_x_coord / GRIDSIZE) + 1,
                "row": math.ceil(block_start_y_coord / GRIDSIZE) + 1
                } 

            COLLAPSED_BLOCKS.append(block_dict)
            block_count = 0
            print(COLLAPSED_BLOCKS)
            block_start_y_coord = -100
            block_start_x_coord = random.choice([x for x in range(326) if x % GRIDSIZE == 0 ])
            
        pygame.display.update()
        clock.tick(60)
