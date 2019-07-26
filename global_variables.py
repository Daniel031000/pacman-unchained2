screensize = (1000, 500)
keys_pressed = []

game_over = False
lose = False
pixel_colour = []
level_pellets = []
current_level = 0
score = 0
strip_starting_point = []
screen = 0
LEVEL_PATHS = ["graphics/levels/level_1.png", "graphics/levels/level_2.png", "graphics/levels/level_3.png"]
ran_x = 0
ran_y = 0

directions = [[0, -1], [0, 1], [-1, 0], [1, 0], [0, 0]]

# the following variables are reassigned a type at a later point
pacman = 0
ghosts = []

GHOST_SOURCE_IMAGES = [
    ["graphics/ghosts/blue/ghost_left.png", "graphics/ghosts/blue/ghost_right.png",
     "graphics/ghosts/blue/ghost_up.png", "graphics/ghosts/blue/ghost_down.png"],
    ["graphics/ghosts/orange/ghost_left.png", "graphics/ghosts/orange/ghost_right.png",
     "graphics/ghosts/orange/ghost_up.png", "graphics/ghosts/orange/ghost_down.png"],
    ["graphics/ghosts/red/ghost_left.png", "graphics/ghosts/red/ghost_right.png",
     "graphics/ghosts/red/ghost_up.png", "graphics/ghosts/red/ghost_down.png"],
    ["graphics/ghosts/turquoise/ghost_left.png", "graphics/ghosts/turquoise/ghost_right.png",
     "graphics/ghosts/turquoise/ghost_up.png", "graphics/ghosts/turquoise/ghost_down.png"]
]
