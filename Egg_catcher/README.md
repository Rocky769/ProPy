# Egg Catcher

This game will test your concentration and the speed of your reflexes. Don’t
crack under pressure—just catch as many eggs as you can to get a high
score. Challenge your friends to see who is the champion egg catcher!

--------------------------------------------------------------
Game terms
--------------------------------------------------------------

Move the catcher along the bottom of the screen to catch each egg before it touches the
ground. When you scoop up an egg you score points, but if you drop an egg you lose a life.
Beware: the more eggs you catch, the more frequently new eggs appear at the top of the
screen and the faster they fall. Lose all three lives and the game ends.

--------------------------------------------------------------
Additional Info
--------------------------------------------------------------

The program uses Tkinter to draw and move shapes, and the random
module to place them on the screen. Also pygame is used for music.

We can use an arc to represent the catcher. An arc is one part of a whole
circle. Tkinter draws circles inside an invisible box. The first two
catcher_start coordinates (x and y) plot where one corner of
the box should be. The second two coordinates (x2 and y2) plot the
position of the box’s opposite corner. The create_arc() function
has two parameters, both given in degrees (°), that say where in the
circle to draw the arc: start says where to start drawing, while
extent is how many degrees to draw before stopping.
Check arc.png for reference.
