# EN.540.635_Software_Carpentry-Lazor_Project

This is a Project for EN.540.635_Software_Carpentry class.

## Goal of the Project
Write a program that will automatically find solutions to the “Lazors” game on Android and iPhone.

## User Instructions
### Before Starting
* You need to have python to use this solver.
* You also need to have unsolved lazor game in .bff file format that discribe the current situation of the game you are solving. See sample solution for more information.
### Solving:
* Place the Solution_for_Game-Lazors.py under the same folder as your .bff file.
* Open Solution_for_Game-Lazors.py in terminal or double click the code file.
* Type in your file name coated with "" and hit enter! For example: "yarn_5.bff"
* Done! (the code will create a new solution.txt which contains the solution of the game)

## Sample Solution
### Content of .bff File
#### Elements
* Grid message framed with "GRID START" and "GRID STOP"
* Type and number of blocks you need to put
* Lazors with posiiton and direction.
* Target positions.

### Sample .bff File

GRID START
o B x o o
o o o o o
o x o o o
o x o o x
o o x x o
B o x o o
GRID STOP

A 8
#8 reflection blocks

L 4 1 1 1 
#Lazor with position （4，1）, direction (1,1))

P 6 9
P 9 2
#target point with position (6,9) and (9,2)

### Sample Solution .txt file
o B x o o
o A o o o
A x o o A
o x A o x
A o x x A
B A x A o

### Notations
  > o: vacant position
  > x: no block allowed position
  > A: reflect block
  > B: opaque block
  > C: refract block
  > L: lazor position with direction
  > P: target point
