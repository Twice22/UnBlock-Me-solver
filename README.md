# unblockme-solver
Using Udacity Course I implemented a program able to solve the game UnBlockMe. UnBlock Me is a game
freely available on [android](https://play.google.com/store/apps/details?id=com.kiragames.unblockmefree&hl=fr)

## Usage
+ Open `unblockme.py`
+ Change the first line: `N = VER = 8` by putting the number of rows and columns of your game.
+ Create your puzzle using `grid()` function (see example at the end of the code)
+ Print the solution using `print(solve_parking_puzzle(yourPuzzleDefinition))`

## More information
+ `@` represent the exit
+ `*` represent your block (red block in UnBlock Me)
+ `letter` represent block that keeps you from reaching the exit

To create a _horizontal_ block you can pass a tuple of tuple to the `grid` function.
For example : `('B', locs(19, 3))` will create a **horizontal block** represented by *B* starting at position **19** and having length **3** (3 columns span)

To create a _vertical_ block you can write e.g: `('O', locs(41, 2, N))`. It will create a block of **length 2 vertically** starting at position **41**.

**Note**: The location is a single integer and it takes into consideration the border. So if you create a _8 X 8 game_, you will have 2 columns (rightmost and leftmost columns) and 2 rows (top and bottom rows) that will be used for the border of the game. So your game will be a _6 X 6_.
For example here is a 8 X 8 game:

```
|  |  |  |  |  |  |  |
|         B          |
|         B          @
|   *  *  B          |
|            P  P  P | 
|               O    | 
|   Y  Y  Y     O    |
|  |  |  |  |  |  |  |
```

and here is the corresponding position:
```
 0   1   2   3   4   5   6   7
 8   9  10  11  12  13  14  15
16  17  18  19  20  21  22  23
24  25  26  27  28  29  30  31
32  33  34  35  36  37  38  39
40  41  42  43  44  45  46  47
48  49  50  51  52  53  54  55
56  57  58  59  60  61  62  63
```

## Note
There are tons of ways to improve the efficient of the algorithm. It is a very simple solver.