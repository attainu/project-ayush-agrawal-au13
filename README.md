MAZE SOLVER
-----------
Project description:
--------------------
Objective:-
-----------
A maze in the form of matrix will be given in the form of 1’s and 0’s, where 1 represents the open
path and 0 represents the blocked path.
-----------
​And the goal is to find the path between the source to the destination in the maze (if the path exists) otherwise just return/"-1" indicating no path exists between the source and destination.
-----------
​
Concepts used:-
---------

Backtracking
---------
​
File Handling
----------
​
Approach:-
----------
Given a maze, NxN matrix.we have to find a path from source to destination. 
​
----------
maze[0][0] (left top corner)is the source and maze[N-1][N-1](right bottom corner) is destination. 
------------
There are few cells which are blocked, means we cannot enter into those cells. we can move in two direction ( forward and down).
---------------
•Create a solution matrix of the same structure as maze.
-----------------
•Whenever we move to cell in a maze, mark that particular cell in solution matrix.
-------------
•At the end print the solution matrix, follow that 1’s from the top left corner, it will be that path.
--------------
Implementation/algorithms:-
-------------
​
•If  we reach at the destination
---------------
print the solution matrix.
-------------
•Else
-----------
•Print -1
-------------
• Form a recursive function, which will follow a path and check if the path reaches the destination or not. If the path does not reach the destination then backtrack and try other paths.
--------------

Folder structure:
------------------
1. main.py: It contains the main function and logic to read input from the file inputfile.txt
2. maze_logic: It contains a class maze_logic which contains methods to solve the maze.
3. I have imported maze_logic.py in main.py so that functions to solve the maze are available in main.py.
4. inputfile.txt: It contains size of the matrix and the input matrix.
5. outputfile.txt: It contains solution matrix or -1 depending on whether path exists or not. 

Taking Input:-
---------------
1. Input will be taken from the file inputfile.txt
2. In this file, first row will be n(size of matrix), we are taking nxn matrix.
3. The next n rows will contain value of columns, either 1 or 0 in the respective rows.
4. Each row will have n columns.
----------------​
Output:-
-------
1. The output will be written to the file outputfile.txt.
2. It will contain the path if path exists or -1 if the path doesn't exist.
3. If path exists, then output file will contain 1s in cells through which path is formed and 0s in all other cells.

Instructions to execute the file:-
----------------------------------
1. Clone the git repository.
2. Go inside the cloned repository using the terminal or command prompt.
3. Execute the code file by writing -: main.py -i inputfile.txt -o outputfile.txt.
4. In the input file, provide the input in the following order.
-----------------------------------
​•	give size of the matrix = n​
-----------
•	n (any integer which represents the size  of the matrix)
-------------
​
•	1 0 1 0 0 ..1 ( n binary digits with space separated)
----------
•	Type n rows as above (of binary digits)
---------
sample Input-:
"""
-----------
C:\Users\Desktop\python>main.py -i inputfile.txt -o outputfile.txt
----------
4 (size of matrix)
------------
​
1 1 0 0
----------
0 1 0 0
-----------
0 1 0 0
-----------
1 1 1 1
----------
"""
-----------
​
The output will be printed in "outputfile.txt" and not on terminal.
---------------
​
sample output in outputfile.txt-:
----------
1 1 0 0
----------
0 1 0 0
----------
0 1 0 0
----------
0 1 1 1
----------

