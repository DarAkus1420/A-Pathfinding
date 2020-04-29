import pygame, sys
import GUI.constants
from backend.algorithm import Algorithm

def get_tile_color(tile_contents):
    if tile_contents == 0:
        tile_color = GUI.constants.WHITE
    if tile_contents == 1:
        title_color = GUI.constants.RED
    return tile_color

def draw_map(surface, map_tiles):
    allrects=[]
    for j, tile in enumerate(map_tiles):
        row=[]
        for i, tile_contents in enumerate(tile):
            # print("{},{}: {}".format(i, j, tile_contents))
            myrect = pygame.Rect(i*GUI.constants.BLOCK_WIDTH, j*GUI.constants.BLOCK_HEIGHT, GUI.constants.BLOCK_WIDTH, GUI.constants.BLOCK_HEIGHT)
            pygame.draw.rect(surface, get_tile_color(tile_contents), myrect)
            status="clear"
            row.append([myrect,get_tile_color(tile_contents),status])
        allrects.append(row)
    return allrects

def draw_grid(surface):
    for i in range(GUI.constants.NUMBER_OF_BLOCKS_WIDE):
        new_height = round(i * GUI.constants.BLOCK_HEIGHT)
        new_width = round(i * GUI.constants.BLOCK_WIDTH)
        pygame.draw.line(surface, GUI.constants.BLACK, (0, new_height), (GUI.constants.SCREEN_WIDTH, new_height), 2)
        pygame.draw.line(surface, GUI.constants.BLACK, (new_width, 0), (new_width, GUI.constants.SCREEN_HEIGHT), 2)

def game_loop(surface, world_map):
    allrects=draw_map(surface, world_map)
    start = 0
    end = 0
    color = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_a:
                    color = GUI.constants.WHITE
                    print("white")
                if event.key == pygame.K_s:
                    color = GUI.constants.RED
                    print("red")
                if event.key == pygame.K_z:
                    color = GUI.constants.GOLD
                    print("gold")
                if event.key == pygame.K_x:
                    color = GUI.constants.BLACK
                    print("black")
                if event.key == pygame.K_SPACE:
                    path = Algorithm.astar(world_map, start, end)
                    print(path)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x,row in enumerate(allrects):
                    for y,item in enumerate(row):
                        rect=item[0]
                        status=item[2]
                        if rect.collidepoint(event.pos):
                            #Obtiene cuadro
                            print(rect)
                            #obtiene color
                            print(color)
                            #obtiene coordenada
                            print("{}, {}".format(x, y))
                            #obtiene estado
                            print("Estado anterior:",status)
                            if color == GUI.constants.RED:
                                item[1] = GUI.constants.RED
                                item[2]="wall"
                            if color== GUI.constants.GOLD:
                                item[1] = GUI.constants.GOLD
                                item[2]="beginning"
                            if color== GUI.constants.BLACK:
                                item[1] = GUI.constants.BLACK
                                item[2]="ending"
                            if color== GUI.constants.WHITE :
                                item[1] = GUI.constants.WHITE 
                                item[2]="clear"
                            print("Estado actual:",item[2])

                            if item[2] == 'wall':
                                world_map[x][y] = 1
                            elif item[2] == 'beginning':
                                start = (x, y)
                            elif item[2] == 'ending':
                                end = (x, y)

                            print(world_map[x][y], item[2])
                            print(start)
                            print(end)
                            #Se vuelve a dibujar todos los rects con los colores actualizados
                            #Es la unica manera que encontre para que se actualizaran todos los rects
                            for row in allrects:
                                for item in row:
                                    rect,color_item,status=item
                                    pygame.draw.rect(surface,color_item,rect)  
        draw_grid(surface)
        
        pygame.display.update()

def initialize_game():
    # Configuracion de pygame para el "juego"
    pygame.init()
    surface = pygame.display.set_mode((GUI.constants.SCREEN_WIDTH, GUI.constants.SCREEN_HEIGHT)) #Main window
    pygame.display.set_caption(GUI.constants.TITLE)
    surface.fill(GUI.constants.UGLY_PINK)
    return surface


def main():
    mapa = GUI.constants.MAP
    surface = initialize_game()
    game_loop(surface, mapa)

if __name__=="__main__":
    main()