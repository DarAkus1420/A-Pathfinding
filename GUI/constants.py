
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600




GREY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (55, 55, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARKGREY = (150, 150, 150)
LIGHTGREY = (210, 210, 210)
UGLY_PINK = (255, 0, 255)
BROWN = (153, 76, 0)
GOLD = (153, 153, 0)
DARKGREEN = (0, 102, 0)
DARKORANGE = (255, 128, 0)
WHITE = (255, 255, 255)

MAPFILE = "map.txt"
TITLE = "Welcome to Tile World!"
FOOD_ENERGY = 10



MAP = [['m','m','m','m','m','m','m','m'],
       ['m','m','m','m','m','m','m','m'],
       ['m','m','m','m','m','m','m','m'],
       ['m','m','m','m','m','m','m','m'],
       ['m','m','m','m','m','m','m','m']
    ]

NUMBER_OF_BLOCKS_WIDE = len(MAP[0])
NUMBER_OF_BLOCKS_HIGH = len(MAP)

BLOCK_HEIGHT = round(SCREEN_HEIGHT/NUMBER_OF_BLOCKS_HIGH)
BLOCK_WIDTH = round(SCREEN_WIDTH/NUMBER_OF_BLOCKS_WIDE)