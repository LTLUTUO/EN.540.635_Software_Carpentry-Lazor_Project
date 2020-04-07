# EN.540.635_Software_Carpentry-Lazor_Project
This Lazor Project is for EN.540.635_Software_Carpentry class.

The goal of the project:
Write a program that will automatically find solutions to the “Lazors” game on Android and iPhone.

User instructions:
Before starting:
*You need to have python to use this solver.
*You also need to have unsolved lazor game in .bff file format
Solving:
*Open Solution_for_Game-Lazors.py
*Scroll down to the last line of code, change the filename in '' to the filename which you want to solve
*Run the code
*Done! (the code will create a new solution_txt which contains the solution of the game)

Sample solution:
Before: 
GRID START
o B x o o
o o o o o
o x o o o
o x o o x
o o x x o
B o x o o
GRID STOP

A 8 (8 reflect blocks)

L 4 1 1 1 (Lazor with position （4，1）, direction (1,1))

P 6 9 (target point with position (6,9))
P 9 2 (target point with position (9,2))

After:
o B x o o
o A o o o
A x o o A
o x A o x
A o x x A
B A x A o

Notations:
  > o: vacant position
  > x: no block allowed position
  > A: reflect block
  > B: opaque block
  > C: refract block
  > L: lazor position with direction
  > P: target point