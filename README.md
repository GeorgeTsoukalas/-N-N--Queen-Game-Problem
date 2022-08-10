# $N^2$-Queen Problem
For those who might stumble upon this page now - as it turns out this problem has been well studied. Indeed Polya noticed in 1918, in the regular n-Queen problem (along with the modular version), that if you have a $n \times n$ regular solution and an $m \times m$ modular solution, there is an $mn \times mn$ regular solutions. It has been long known that if $\text{gcd}(n,6) = 1$, then a perfect solution is possible. This is due to Laparewicz from 1912/1913. Vasquez in 2004 showed this condition was not necessary, and produced solutions for $n =  12, 14, 15, 16, 18, 20, 21, 22, 24, 28, 32$. It is still open as to whether this is a large N such that for $n \geq N$ you can always find a perfect solution. A survey on these results, on other variants on $N$-queen problems appears here (from 2009): https://www.sciencedirect.com/science/article/pii/S0012365X07010394. And if you stumble upon this problem, like I did, and find the perfect solution for $n = 5$ - you might be better served thinking of ways to generalize the regularity you see in your example - as indeed the 5 by 5 solution follows a very simple coloring scheme.

-------------------------------------
When I was in high school I was given the following puzzle: given a $6 \times 6$ grid, you must fill each slot with a value from $\{\text{Empty}, 1, \dots, 6\}$. You must ensure that no column, row, or diagonal has two of the same value (except in the case of Empty). Determine
$$ \max_{\text{Valid Configurations}} \#\{\text{Filled Spaces of Configurations}\} $$
You can notice that if a corner slot is filled with an integer, that integer can only appear at most $5$ times in the grid. Hence this maximum is at most 32, and constructing a suitable example establishes that the maximum is indeed $32$. What about for different grid sizes?

The current records are:
1: 1/1

2: 2/4

3: 6/9

4: 13/16

5: 25/25

6: 32/36

7: 49/49

8: 58/64 It is unknown whether or not this is best possible - though I would assume it isn't.

9: 74/81 It is unknown whether or not this is best possible - though I would assume it isn't.

10: 92/100 It is unknown whether or not this is best possible - though I would assume it isn't.

11: 112/121 This is not best possible - you can get a perfect solution!

12: 132/144 This is not best possible - you can get a perfect solution!

13: 160/169 This is not best possible - you can get a perfect solution!

14: 183/196 This is not best possible - you can get a perfect solution!

15: 212/225 This is not best possible - you can get a perfect solution!

16: 241/256 This is not best possible - you can get a perfect solution!

17: 272/289 This is not best possible - you can get a perfect solution!

18: 308/324 This is not best possible - you can get a perfect solution!

19: 342/361 This is not best possible - you can get a perfect solution!

20: 380/400 This is not best possible - you can get a perfect solution!

21: 419/441 This is not best possible - you can get a perfect solution!

The method in constructing examples here is not that inspired - there is far more structure going on then random choices of assigning squares will indicate. Further attempts to improve the ideas of Vasquez will help give extremal constructions for n = 8,9,10 - and may likely be generalized to showing that perfect solutions occur for sufficiently large n.
