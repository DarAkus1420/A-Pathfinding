import pygame, sys
import GUI.constants

def get_tile_color(tile_contents):
    if tile_contents == 'm':
        tile_color = GUI.constants.WHITE
    if tile_contents == ".":
        tile_color = GUI.constants.WHITE
    if tile_contents == "s":
        tile_color = GUI.constants.RED
    if tile_contents == "e":
        tile_color = GUI.constants.GREEN
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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x,row in enumerate(allrects):
                    for y,item in enumerate(row):
                        rect=item[0]
                        color=item[1]
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
                            if color == GUI.constants.WHITE:
                                item[1] = GUI.constants.RED
                                item[2]="wall"
                            if color== GUI.constants.RED:
                                item[1] = GUI.constants.GOLD
                                item[2]="beginning"
                            if color== GUI.constants.GOLD:
                                item[1] = GUI.constants.BLACK
                                item[2]="ending"
                            if color== GUI.constants.BLACK:
                                item[1] = GUI.constants.WHITE 
                                item[2]="clear"
                            print("Estado actual:",item[2])
                #Se vuelve a dibujar todos los rects con los colores actualizados
                #Es la unica manera que encontre para que se actualizaran todos los rects
                            for row in allrects:
                                for item in row:
                                    rect,color,status=item
                                    pygame.draw.rect(surface,color,rect)  
        draw_grid(surface)
        pygame.display.update()

def initialize_game():
    pygame.init()
    surface = pygame.display.set_mode((GUI.constants.SCREEN_WIDTH, GUI.constants.SCREEN_HEIGHT)) #Main window
    pygame.display.set_caption(GUI.constants.TITLE)
    surface.fill(GUI.constants.UGLY_PINK)
    return surface

def read_map(mapfile):
    #with open(mapfile, 'r') as f:
    #    world_map = f.readlines()
    #world_map = [line.strip() for line in world_map]
    world_map=GUI.constants.MAP
    return (world_map)

def main():
    world_map = read_map(GUI.constants.MAPFILE)
    surface = initialize_game()
    game_loop(surface, world_map)

if __name__=="__main__":
    main()