"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Billy Davignon.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
fat_turtle = rg.SimpleTurtle('turtle')
fat_turtle.pen = rg.Pen('pink',15)
fat_turtle.speed=20
size = 100

fat_turtle.pen_up()
fat_turtle.right(135)
fat_turtle.forward(100)
fat_turtle.left(135)
fat_turtle.pen_down()

for k in range(16):
    fat_turtle.draw_square(size)
    fat_turtle.pen_up()
    fat_turtle.forward(150)
    fat_turtle.forward(15)
    fat_turtle.left(45)
    fat_turtle.pen_down()
    size = size - 1

another_turtle = rg.SimpleTurtle()
another_turtle.pen = rg.Pen('yellow',30)
another_turtle.speed=20
size=50

for k in range(8):
    another_turtle.draw_square(size)
    another_turtle.pen_up()
    another_turtle.forward(50)
    another_turtle.left(180)
    another_turtle.pen_down()



window.close_on_mouse_click()
