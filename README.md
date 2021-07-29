# PathFinding

## Usage
work with python2 or python3

### [1] edit the numberList in the pathFinding_7x7.py
```
numberList = [  0, 0, 0, 0, 0, 0, 0, \
                0, 0, 0, 0, 0, 0, 0, \
                0, 2, 0, 0, 1, 0, 0, \
                0, 0, 0, 0, 0, 0, 0, \
                0, 1, 0, 0, 1, 0, 0, \
                0, 0, 0, 0, 1, 3, 0, \
                0, 0, 0, 0, 0, 0, 0  ]
Note:
the length of numberList must be 3x3=9, 4x4=16, 25, 36, 49 .....
1 = obstacle
2 = start point
3 = end ponit
```

### [2] python pathFinding_7x7.py
```
========================================
Need 9 moves to solve this puzzle: ('right', 'right', 'down', 'right', 'right', 'right', 'down', 'left', 'down')
========================================
-----------------
|               |
|               |
|   S     X     |
|               |
|   X     X     |
|         X G   |
|               |
-----------------
move#1: right
-----------------
|               |
|               |
|     S   X     |
|               |
|   X     X     |
|         X G   |
|               |
-----------------
move#2: right
-----------------
|               |
|               |
|       S X     |
|               |
|   X     X     |
|         X G   |
|               |
-----------------
move#3: down
-----------------
|               |
|               |
|         X     |
|       S       |
|   X     X     |
|         X G   |
|               |
-----------------
move#4: right
-----------------
|               |
|               |
|         X     |
|         S     |
|   X     X     |
|         X G   |
|               |
-----------------
move#5: right
-----------------
|               |
|               |
|         X     |
|           S   |
|   X     X     |
|         X G   |
|               |
-----------------
move#6: right
-----------------
|               |
|               |
|         X     |
|             S |
|   X     X     |
|         X G   |
|               |
-----------------
move#7: down
-----------------
|               |
|               |
|         X     |
|               |
|   X     X   S |
|         X G   |
|               |
-----------------
move#8: left
-----------------
|               |
|               |
|         X     |
|               |
|   X     X S   |
|         X G   |
|               |
-----------------
move#9: down
-----------------
|               |
|               |
|         X     |
|               |
|   X     X     |
|         X S   |
|               |
-----------------
```
## Reference
UC Berkeley CS188 Pacman AI projects

https://github.com/jinhoko/CS188

