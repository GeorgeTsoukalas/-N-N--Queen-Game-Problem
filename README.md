# -N-N--Queen-Game-Problem

When I was in high school I was given a puzzle from a teacher - given a 6 by 6 grid with entries from {Empty, 1, ... , 6}, satisfying that no column, row, or diagonal has two of the same digit (empty spaces are ok), what is max(Filled Spaces)? After a lot of guess and check, I came up with an example of a grid with 32 filled spaces (out of 36). Indeed the maximum is at most 32, as one may notice that filling a corner square with integer i precludes you from placing 6 i's in the grid. I call this game the (N,N)-queen problem - a harder version of the better known N-queen problem. My goal is to implement some simple constraint satisfaction techniques to see if I can get some nice bounds on the problem for general n (n = 6 being the puzzle I was given in high school).

The current records are:
1: 1/1

2: 2/4

3: 6/9

4: 13/16

5: 25/25

6: 32/36

7: 49/49 ? Best possible ?

  2  4  6  1  0  5  3 

 5  3  2  4  6  1  0 

 1  0  5  3  2  4  6 

 4  6  1  0  5  3  2 

 3  2  4  6  1  0  5 

 0  5  3  2  4  6  1 

 6  1  0  5  3  2  4 

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

20: 380/400 ? best possible ?

 10  7  14  4  17  1  6  3  16  19  8  11  13  9  2  5  12  15  18  0 

 1  15  16  6  12  0  19  2  5  17  7  18  3  14  13  10  8  11  -1  9 

 5  13  9  19  3  6  8  18  15  1  10  17  0  16  11  12  4  7  14  2 

 12  -1  8  11  14  4  10  19  17  7  0  1  9  3  6  2  5  18  13  16 

 11  17  10  -1  13  12  9  5  -1  15  4  2  6  1  -1  19  0  14  8  18 

 0  16  15  9  7  5  4  -1  18  3  6  14  11  19  12  13  10  -1  17  1 

 9  8  18  3  1  2  14  13  19  0  15  5  -1  6  7  4  17  12  16  10 

 13  6  1  2  18  3  11  17  8  -1  16  10  4  12  19  -1  14  9  7  15 

 17  11  0  10  -1  16  18  12  2  -1  1  9  5  8  3  7  15  6  4  14 

 14  10  6  12  19  9  -1  0  4  8  11  15  7  13  16  17  18  3  2  5 

 6  3  19  5  10  15  13  7  -1  16  -1  0  12  2  4  9  1  17  11  8 

 19  2  7  13  4  8  -1  15  10  11  17  -1  1  18  14  16  3  0  9  12 

 8  12  11  1  16  18  17  14  6  9  2  3  19  5  0  15  7  13  10  4 

 4  5  17  18  2  14  3  16  12  10  13  6  15  7  9  8  11  1  0  19 

 15  14  4  0  9  13  2  1  7  6  5  19  17  10  18  3  16  8  12  11 

 18  1  13  7  15  17  16  11  9  14  3  12  8  4  5  0  -1  2  19  6 

 7  9  12  17  -1  11  1  8  3  2  19  4  14  0  15  18  6  10  5  13 

 3  0  2  8  6  19  5  10  11  18  12  13  16  17  1  14  9  4  15  7 

 16  18  3  15  0  10  12  4  14  5  9  7  2  11  8  6  13  19  1  17 

 -1  19  5  14  11  7  0  9  13  12  18  8  10  15  17  1  2  16  6  3 

21: 419/441 ? best possible ?
In general the algorithm thus far is not too inspired - just trying to improve by random choices with no backtracking or arc consistency checks. Will be adding more in the future.
