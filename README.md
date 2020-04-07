# EN.540.635_Software_Carpentry-Lazor_Project
This Lazor Project is for EN.540.635_Software_Carpentry class.

The goal of the project:<br>
Write a program that will automatically find solutions to the “Lazors” game on Android and iPhone.

User instructions:<br>
Before starting:<br>
*You need to have python to use this solver.<br>
*You also need to have unsolved lazor game in .bff file format.<br>
Solving:<br>
*Open Solution_for_Game-Lazors.py<br>
*Scroll down to the last line of code, change the filename in '' to the filename which you want to solve<br>
*Run the code<br>
*Done! (the code will create a new solution_txt which contains the solution of the game)<br>

Sample solution:<br>
Before: <br>
GRID START<br>
o B x o o<br>
o o o o o<br>
o x o o o<br>
o x o o x<br>
o o x x o<br>
B o x o o<br>
GRID STOP<br>

A 8 (8 reflect blocks)<br>

L 4 1 1 1 (Lazor with position （4，1）, direction (1,1))<br>

P 6 9 (target point with position (6,9))<br>
P 9 2 (target point with position (9,2))<br>

After:<br>
o B x o o<br>
o A o o o<br>
A x o o A<br>
o x A o x<br>
A o x x A<br>
B A x A o<br>

Notations:<br>
  > o: vacant position<br>
  > x: no block allowed position<br>
  > A: reflect block<br>
  > B: opaque block<br>
  > C: refract block<br>
  > L: lazor position with direction<br>
  > P: target point<br>