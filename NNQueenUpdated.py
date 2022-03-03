
   
import math
import random
import copy
import sys
import time
gameSize = 10
class Board:
    def __init__(self,board, empty_spaces, filled_spaces, filled_count,bad_configurations, bad_configuration_length,nonempty_bad_colors):
        self.board = board
        self.empty_spaces = empty_spaces
        self.filled_spaces = filled_spaces # array sorted by number value
        self.filled_count = filled_count
        self.bad_configurations = bad_configurations # a double array - sorted by color, with bad pairs
        self.bad_configuration_length = bad_configuration_length
        self.nonempty_bad_colors = nonempty_bad_colors
    def isValid(self): # can make thing for just checking the one entry (maybe this can work better)
        S = [];
        for i in range(gameSize):
            for item1 in self.filled_spaces[i]:
                for item2 in self.filled_spaces[i]:
                    if item1 != item2:
                        if abs(item1[0] - item2[0]) == 0 or abs(item1[1] - item2[1]) == 0 or abs(item1[0]-item2[0]) == abs(item1[1] - item2[1]):
                            S.append([item1,item2])
        return S # we calculate the bad configurations as len(S)/2 + gameSize^2 - filled_count
    def UpdateConfigurations(self, Tile, color1=-1, color2=-1): # one color is added, one removed
        if color1 != -1: # this is what we change FROM
            for item in self.bad_configurations[color1]:
                if Tile in item:
                    self.bad_configurations[color1].remove(item)
                    self.bad_configuration_length-=1
            if len(self.bad_configurations[color1]) == 0 and color1 in self.nonempty_bad_colors:
                self.nonempty_bad_colors.remove(color1)
        if color2 != -1: # this is what we change TO
            for item in self.filled_spaces[color2]:
                if abs(Tile[0] - item[0]) == 0 or abs(Tile[1] - item[1]) == 0 or abs(Tile[0] - item[0]) == abs(Tile[1] - item[1]):
                    self.bad_configurations[color2].append([Tile,item])
                    self.bad_configuration_length+=1
            if len(self.bad_configurations[color2]) > 0 and color2 not in self.nonempty_bad_colors:
                self.nonempty_bad_colors.append(color2)
    def MakeChange(self, Tile, Entry): # -1 will indicate empty, so we will initialize as empty.
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
Set = [-1] + [*range(gameSize)] + [*range(gameSize)] # weighting more towards putting actual entries in
board = [[-1 for x in range(gameSize)] for y in range(gameSize)]
empty_spaces = [[x,y] for x in range(gameSize) for y in range(gameSize)]
filled_spaces = [[] for x in range(gameSize)]
filled_count = 0
bad_configurations = [[] for x in range(gameSize)]
bad_configuration_length = 0
game = Board(board, empty_spaces, filled_spaces, filled_count, bad_configurations, bad_configuration_length,[])
meaningfulIterations = 0
start_time = time.time()
iterations = 100000
for i in range(iterations): # 2, 6, 13, 25, 32, 44?
    if (i%1000 == 0):
        print(i)
    r = random.random()
    L = random.choice(Set)
    if (game.bad_configuration_length > 0): # wont work in the way I did it because I dont track which one is nonempty - O(n) to search
        #if (r < 0.95):
        #    if (L == -1):
        #        T = random.choice(game.bad_configurations[0]) # since isvalid returns invalid PAIRs of pairs of points
        #    else:
        #        T = random.choice(game.bad_configurations[L]) #print(T)
        #else:
        if (r < 0.5):
            if (L != -1):
                T = random.choice(game.bad_configurations[random.choice(game.nonempty_bad_colors)])[0]
            else:
                T1 = random.choice(range(gameSize))
                T2 = random.choice(range(gameSize))
                T = [T1, T2]
    else:
        T1 = random.choice(range(gameSize))
        T2 = random.choice(range(gameSize))
        T = [T1, T2]
    if (L != game.board[T[0]][T[1]]):
        meaningfulIterations+=1
        copiedGame = Board(copy.deepcopy(game.board), copy.deepcopy(game.empty_spaces), copy.deepcopy(game.filled_spaces), game.filled_count, copy.deepcopy(game.bad_configurations), game.bad_configuration_length, copy.deepcopy(game.nonempty_bad_colors)) #Board(numpy.copy(game.board), numpy.copy(game.empty_spaces), numpy.copy(game.filled_spaces), game.filled_count)#Board(copy.deepcopy(game.board), copy.deepcopy(game.empty_spaces), copy.deepcopy(game.filled_spaces), game.filled_count)
        copiedGame.MakeChange(T, L)
        if (copiedGame.bad_configuration_length + pow(gameSize,2)-copiedGame.filled_count <= game.bad_configuration_length + pow(gameSize,2) - game.filled_count):
            game.MakeChange(T,L)

    
game.printBoard()
print(str(game.filled_count) + " out of " + str(pow(gameSize,2)))
print(game.bad_configuration_length)
print("What this random simulation has attained is " + str(game.filled_count-game.bad_configuration_length) + " out of "+str(pow(gameSize,2)))
print("And the number of meaningful iterations was "+str(meaningfulIterations))
print("My program took " + str(time.time() - start_time)+ " to run")
