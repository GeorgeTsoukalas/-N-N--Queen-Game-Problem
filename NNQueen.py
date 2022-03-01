import math
import random
import copy
import sys
gameSize = 20
class Board:
    def __init__(self,board, empty_spaces, filled_spaces, filled_count):
        self.board = board
        self.empty_spaces = empty_spaces
        self.filled_spaces = filled_spaces # array sorted by number value
        self.filled_count = filled_count
    def isValid(self): # can make thing for just checking the one entry (maybe this can work better)
        S = [];
        for i in range(gameSize):
            for item1 in self.filled_spaces[i]:
                for item2 in self.filled_spaces[i]:
                    if item1 != item2:
                        if abs(item1[0] - item2[0]) == 0 or abs(item1[1] - item2[1]) == 0 or abs(item1[0]-item2[0]) == abs(item1[1] - item2[1]):
                            S.append([item1,item2])
        return S # we calculate the bad configurations as len(S)/2 + gameSize^2 - filled_count
    def MakeChange(self, Tile, Entry): # -1 will indicate empty, so we will initialize as empty.
        if Entry == -1 and self.board[Tile[0]][Tile[1]] != -1:
            self.filled_count-=1
            self.empty_spaces.append(Tile)
            self.filled_spaces[self.board[Tile[0]][Tile[1]]].remove(Tile)
            self.board[Tile[0]][Tile[1]] = Entry
        elif Entry != self.board[Tile[0]][Tile[1]]:
            if self.board[Tile[0]][Tile[1]] == -1:
                self.filled_spaces[Entry].append(Tile)
                self.filled_count+=1
                self.empty_spaces.remove(Tile)
                self.board[Tile[0]][Tile[1]] = Entry
            else:
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
game = Board(board, empty_spaces, filled_spaces, filled_count)
meaningfulIterations = 0
for i in range(8000): # 2, 6, 13, 25, 32, 44?
    T1 = random.choice(range(gameSize))
    T2 = random.choice(range(gameSize))
    T = [T1, T2]
    L = random.choice(Set)
    if (L != game.board[T1][T2]):
        meaningfulIterations+=1
        copiedGame = Board(copy.deepcopy(game.board), copy.deepcopy(game.empty_spaces), copy.deepcopy(game.filled_spaces), game.filled_count)
        copiedGame.MakeChange(T, L)
        if (len(copiedGame.isValid())/2 + pow(gameSize,2)-copiedGame.filled_count <= len(game.isValid())/2 + pow(gameSize,2) - game.filled_count):
            game.MakeChange(T,L)
game.printBoard()
print(str(game.filled_count) + " out of " + str(pow(gameSize,2)))
print(game.isValid())
print("What this random simulation has attained is " + str(game.filled_count-len(game.isValid())/2) + " out of "+str(pow(gameSize,2)))
print("And the number of meaningful iterations was "+str(meaningfulIterations))
