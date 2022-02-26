import math
import pygame
import random
gameSize = 6
class Board:
    def __init__(self,board, empty_spaces, filled_spaces, filled_count):
        this.board = board
        this.empty_spaces = empty_spaces
        this.filled_spaces = filled_spaces # array sorted by number value
        this.filled_count = filled_count
    def isValid(self):
        S=[];
        for i in range(gameSize):
            for j in range(len(filled_spaces[i])):
                for k in range(j, len(filled_spaces[i])):
                    if abs(filled_spaces[i][j][0] - filled_spaces[i][k][0]) == 0 or abs(filled_spaces[i][j][1] - filled_spaces[i][k][1]) == 0 or abs(filled_spaces[i][j][0] - filled_spaces[i][k][0]) == abs(filled_spaces[i][j][1] - filled_spaces[i][k][1]):
                        S.append([filled_spaces[i][j], filled_spaces[i][k]])
        if len(S) > 0:
            return S
        else:
            return True
    def MakeChange(self, Tile, Entry): # -1 will indicate empty, so we will initialize as empty.
        if Entry == -1 and board[Tile[0]][Tile[1]] != -1:
            filled_count-=1
            empty_spaces.append(Tile)
            filled_spaces[board[Tile[0]][Tile[1]]].remove(Tile)
            board[Tile[0]][Tile[1]] = Entry
        elif Entry != board[Tile[0]][Tile[1]]:
            filled_spaces[board[Tile[0]][Tile[1]]].remove(Tile)
            filled_spaces[Entry].append(Tile)
            board[Tile[0]][Tile[1]] = Entry
clicked = False
running = True
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 18)
line_width = 6
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('M-N-Queen Game')
board = [[-1 for x in range(gameSize)] for y in range(gameSize)]
empty_spaces = [(x,y) for x in range(gameSize) for y in range(gameSize)]
filled_spaces = [[] for x in range(gameSize)]
filled_count = 0
game = Board(board, empty_spaces, filled_spaces, filled_count)
def draw_grid():
    color = (50,220,50)
    screen.fill(color)
    pygame.draw.line(screen, black, (0, 500), (screen_width, 500), line_width)
    for x in range(1, gameSize):
        pygame.draw.line(screen, black, (0, x*(500/gameSize)), (screen_width, x*(500/gameSize)), line_width)
        pygame.draw.line(screen, black, (x*(500/gameSize), 0), ((500/gameSize)*50, screen_height-100), line_width)
def draw_markers():
    x_pos = 0
    for x in game.board:
        y_pos = 0
        for y in x:
            if y == -1:
                pygame.draw.circle(screen, white, (x_pos*(500/gameSize) + 25, y_pos*(500/gameSize) + 25), 20, 25) # might be advised to switch the order eventually since blakc goes first
            else:
                textsurface = myfront.render(str(y), False, (0,0,0))
                screen.blit(textsurface,(x_pos*(500/gameSize) + 25, y_pos*(500/gameSize) = 25))
            y_pos+=1
        x_pos+=1
while running:
    draw_grid()
    draw_markers()
    textsurface = myfont.render('Filled Spaces ' + str(game.filled_count), False, (0,0,0))
    screen.blit(textsurface, (0, 450))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
    pygame.display.flip()   
pygame.quit()
            
                                 
                                 
