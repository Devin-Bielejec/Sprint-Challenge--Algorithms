#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) (Linear) confirmed with examples. Thought it was O(n cubed) at first, but it appears that the loop is O(n cubed) but then a is increasing by a factor of n squared.

Example:

```
n=2

a=0
while (a < 8):
    a = 0 + 4

while (a < 4):
    a = 4 + 4;

a = 0
n = 3
while (a < 27):
    a = 0 + 9

while (9 < 27):
    a = 9 + 9

while (18 < 27):
    a = 18 + 9
```

b) O(n Logn) - Linearithmic

First loop indicates O(n)
Second loop indicates 1 less action than prior loop and since it's being multiplied by a constant amount (O(Logn))

c) O(n) - linear

## Exercise II

Answer: O(log(n))
0
1
2
.
.
.
n

if floor > f:
egg breaks
else:
egg alive
Start at floor: currentFloor = n/2
If the egg breaks,
Try again but halfway between 0 and n//2
so current Floor is currentFloor//2

if the egg doesn't break,
try again but halfway between n/2 and n
so current Floor is n - currentFloor//2

```
def eggBreak(start=0, end, f):
    dist = end - start
    if dist == 1:
        #Base Case
        return start
    else:
        startTest = start + dist//2
        if startTest > f:
            eggBreak(start=0, startTest, f)
        else:
            eggBreak(start=startTest, end, f)
```
