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

top is top
bottom is bottom

try:
if top = bottom
return top

    drop egg midway between top and bottom
    if egg breaks -> top = midway - 1
    else -> bottom = midway + 1
