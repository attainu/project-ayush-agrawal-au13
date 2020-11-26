MAZE SOLVER
-----------

Project description
-----------
Instructions to execute the file
--------------------
​
Project description:
--------------------
​
Objective:-
-----------
A maze in the form of matrix will be given in the form of 1’s and 0’s, where 1 represents the open
path and 0 represents the blocked path.
-----------
​And the goal is to find the path between the source to the destination in the maze (if the path exists) otherwise just return/"-1" indicating no path exists between the source and destination.
​​
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
------------
​
•If none of the above solution works then BACKTRACK and mark the current cell as 0.
NOTE: It is important to check the previous direction in which the we have moved because if we will move in the opposite direction w.r.t its previous direction then we might end up in infinite loop.
------------
Taking Input:-
-------------
1. Input will be taken from the file inputfile.txt
2. In this file, first row will be n(size of matrix), we are taking nxn matrix.
3. The next n rows will contain value of columns, either 1 or 0 in the respective rows.
4. Each row will have 


----------------
​
Output:-
-------
•	Open a file, say outputfile.txt, in write mode
​
Instructions to execute the file:-
----------------------------------
 • open : Open the file m.py
----------------
•	Open the cmd and go to the folder where you save the python code .
-------------
•   Execute the code file by writting -: maze.py or maze.py -i inputfile.txt -o outputfile.txt
--------------
​
•	pass the arguments in the following order
------------
​
•	give size of the matrix = n
​
-----------
•	n (any integer which represents the order of the matrix)
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
--------------
​
•The output will be printed in "outputfile.txt" (which probably be created and found in the folder of the system where you save the code) 
and not on terminal.
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

