# event handling variables
keys_pressed = []

# game logic variables
game_over = False
lose = False
current_level = 0
score = 0
ran_x = 0
ran_y = 0
directions = [[0, -1], [0, 1], [-1, 0], [1, 0], [0, 0]]

# the following variables are filled in main.py
pacman = 0
ghosts = []
level_pellets = []

# animation variables
screen = 0
screensize = (1000, 500)
LEVEL_PATHS = ["graphics/levels/level_1.png", "graphics/levels/level_2.png", "graphics/levels/level_3.png"]
GHOST_SOURCE_IMAGES = [
    # blue ghost
    ["graphics/ghosts/blue/ghost_left.png", "graphics/ghosts/blue/ghost_right.png",
     "graphics/ghosts/blue/ghost_up.png", "graphics/ghosts/blue/ghost_down.png"],
    # orange ghost
    ["graphics/ghosts/orange/ghost_left.png", "graphics/ghosts/orange/ghost_right.png",
     "graphics/ghosts/orange/ghost_up.png", "graphics/ghosts/orange/ghost_down.png"],
    # red ghost
    ["graphics/ghosts/red/ghost_left.png", "graphics/ghosts/red/ghost_right.png",
     "graphics/ghosts/red/ghost_up.png", "graphics/ghosts/red/ghost_down.png"],
    # turquoise ghost
    ["graphics/ghosts/turquoise/ghost_left.png", "graphics/ghosts/turquoise/ghost_right.png",
     "graphics/ghosts/turquoise/ghost_up.png", "graphics/ghosts/turquoise/ghost_down.png"]
]
PACMAN_SOURCE_IMAGES = [
    # up
    ["graphics/pacman/up/pacman0.png", "graphics/pacman/up/pacman1.png",
     "graphics/pacman/up/pacman2.png", "graphics/pacman/up/pacman3.png"],
    # down
    ["graphics/pacman/down/pacman0.png", "graphics/pacman/down/pacman1.png",
     "graphics/pacman/down/pacman2.png", "graphics/pacman/down/pacman3.png"],
    # left
    ["graphics/pacman/left/pacman0.png", "graphics/pacman/left/pacman1.png",
     "graphics/pacman/left/pacman2.png", "graphics/pacman/left/pacman3.png"],
    # right
    ["graphics/pacman/right/pacman0.png", "graphics/pacman/right/pacman1.png",
     "graphics/pacman/right/pacman2.png", "graphics/pacman/right/pacman3.png"]
]
pixel_colour = []
