import math
import random
import copy
import sys
import time

class Board:
    def __init__(self,board, empty_spaces, filled_spaces, filled_count,bad_configurations, bad_configuration_length,nonempty_bad_colors):
        self.board = board
        self.empty_spaces = empty_spaces
        self.filled_spaces = filled_spaces
        self.filled_count = filled_count
        self.bad_configurations = bad_configurations
        self.bad_configuration_length = bad_configuration_length
        self.nonempty_bad_colors = nonempty_bad_colors
    def UpdateConfigurations(self, Tile, color1=-1, color2=-1):
        if color1 != -1: 
            for item in self.bad_configurations[color1]:
                if Tile in item:
                    self.bad_configurations[color1].remove(item)
                    self.bad_configuration_length-=1
            if len(self.bad_configurations[color1]) == 0 and color1 in self.nonempty_bad_colors:
                self.nonempty_bad_colors.remove(color1)
        if color2 != -1:
            for item in self.filled_spaces[color2]:
                if abs(Tile[0] - item[0]) == 0 or abs(Tile[1] - item[1]) == 0 or abs(Tile[0] - item[0]) == abs(Tile[1] - item[1]):
                    self.bad_configurations[color2].append([Tile,item])
                    self.bad_configuration_length+=1
            if len(self.bad_configurations[color2]) > 0 and color2 not in self.nonempty_bad_colors:
                self.nonempty_bad_colors.append(color2)
    def MakeChange(self, Tile, Entry):
        if Entry == -1 and self.board[Tile[0]][Tile[1]] != -1:
            self.filled_count-=1
            self.empty_spaces.append(Tile)
            self.filled_spaces[self.board[Tile[0]][Tile[1]]].remove(Tile)
            self.UpdateConfigurations(Tile, self.board[Tile[0]][Tile[1]], Entry)
            self.board[Tile[0]][Tile[1]] = Entry
        elif Entry != self.board[Tile[0]][Tile[1]]:
            if self.board[Tile[0]][Tile[1]] == -1:
                self.filled_count+=1
                self.empty_spaces.remove(Tile)
                self.UpdateConfigurations(Tile, self.board[Tile[0]][Tile[1]], Entry)
                self.filled_spaces[Entry].append(Tile)
                self.board[Tile[0]][Tile[1]] = Entry
            else:
                self.UpdateConfigurations(Tile, self.board[Tile[0]][Tile[1]], Entry)
                self.filled_spaces[self.board[Tile[0]][Tile[1]]].remove(Tile)
                self.filled_spaces[Entry].append(Tile)
                self.board[Tile[0]][Tile[1]] = Entry
    def printBoard(self):
        for i in range(gameSize):
            for j in range(gameSize):
                sys.stdout.write(" " + str(self.board[i][j]) + " ")
            print("\n")

gameSize = 7
Set = [-1] + [*range(gameSize)]
board = [[-1 for x in range(gameSize)] for y in range(gameSize)]
empty_spaces = [[x,y] for x in range(gameSize) for y in range(gameSize)]
filled_spaces = [[] for x in range(gameSize)]
filled_count = 0
bad_configurations = [[] for x in range(gameSize)]
bad_configuration_length = 0
game = Board(board, empty_spaces, filled_spaces, filled_count, bad_configurations, bad_configuration_length,[])
meaningfulIterations = 0
iterations = 50000
start_time = time.time()

for i in range(iterations):
    if (i%10000 == 0):
        print(i)
    r = random.random()
    if (game.bad_configuration_length > 0): 
        if (r < 0.95):
            T = random.choice(game.bad_configurations[game.nonempty_bad_colors[0]][0]) # might want to consider shuffling game.bad_configurations
        else:
            T = [random.choice(range(gameSize)), random.choice(range(gameSize))]
    else:
        T = random.choice(game.empty_spaces)
    L = random.choice(Set)
    if (L != game.board[T[0]][T[1]]):
        copiedGame = Board(copy.deepcopy(game.board), copy.deepcopy(game.empty_spaces), copy.deepcopy(game.filled_spaces), game.filled_count, copy.deepcopy(game.bad_configurations), game.bad_configuration_length, copy.deepcopy(game.nonempty_bad_colors)) #Board(numpy.copy(game.board), numpy.copy(game.empty_spaces), numpy.copy(game.filled_spaces), game.filled_count)#Board(copy.deepcopy(game.board), copy.deepcopy(game.empty_spaces), copy.deepcopy(game.filled_spaces), game.filled_count)
        copiedGame.MakeChange(T, L)
        if (copiedGame.bad_configuration_length + pow(gameSize,2)-copiedGame.filled_count <= game.bad_configuration_length + pow(gameSize,2) - game.filled_count):
            meaningfulIterations+=1
            game.MakeChange(T,L)

    
game.printBoard()
print(str(game.filled_count) + " out of " + str(pow(gameSize,2)))
print(game.bad_configuration_length)
print("What this random simulation has attained is " + str(game.filled_count-game.bad_configuration_length) + " out of "+str(pow(gameSize,2)))
print("And the number of meaningful iterations was "+str(meaningfulIterations))
print("My program took " + str(time.time() - start_time)+ " to run")
