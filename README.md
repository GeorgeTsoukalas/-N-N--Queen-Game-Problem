# -N-N--Queen-Game-Problem

When I was in high school I was given a puzzle from a teacher - given a 6 by 6 grid with entries from {Empty, 1, ... , 6}, satisfying that no column, row, or diagonal has two of the same digit (empty spaces are ok), what is max(Filled Spaces)? After a lot of guess and check, I came up with an example of a grid with 32 filled spaces (out of 36). Indeed the maximum is at most 32, as one may notice that filling a corner square with integer i precludes you from placing 6 i's in the grid. I call this game the (N,N)-queen problem - a harder version of the better known N-queen problem. My goal is to implement some simple constraint satisfaction techniques to see if I can get some nice bounds on the problem for general n (n = 6 being the puzzle I was given in high school).

The current records are:
1: 1/1

2: 2/4

3: 6/9

4: 13/16

5: 25/25

6: 32/36

7: 44/49 ? Best possible ?

8: 58/64 ? Best possible ?

9: 74/81 ? Best possible ?

10: 92/100 ? Best possible ?

11: 112/121 ? best possible ?

12: 132/144 ? best possible ? 

13: 160/169 ? best possible ?

14: 183/196 ? best possible ? 

15: 212/225 ? best possible ?

16: 241/256 ? best possible ?

17: 272/289 ? best possible ?

18: 308/324 ? best possible ?

19: 342/361 ? best possible ?

20: 377/400 ? best possible ?

21: 416/441 ? best possible ?
In general the algorithm thus far is not too inspired - just trying to improve by random choices with no backtracking or arc consistency checks. Will be adding more in the future.
