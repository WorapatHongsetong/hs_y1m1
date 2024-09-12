# Import library

import turtle

# Setting
turtle.width(10)
turtle.penup()
turtle.forward(-300)

# Unit
turtle.pendown()
turtle.left(90)

turtle.color("navy")
turtle.forward(100)
turtle.forward(-100)

turtle.left(-90)
turtle.penup()
turtle.forward(20)
#########################

# Unit
turtle.pendown()
turtle.left(90)

turtle.left(-45)
turtle.forward(141)
turtle.left(45)
turtle.penup()
turtle.forward(-100)
turtle.pendown()

turtle.left(45)
turtle.forward(141)
turtle.left(45 + 180)
turtle.penup()
turtle.forward(100)
turtle.left(-90)
turtle.forward(100)
turtle.pendown()

turtle.left(90)
turtle.penup()
turtle.forward(20)
#########################

# Unit
turtle.pendown()
turtle.left(90)

turtle.color("silver")
turtle.forward(200)
turtle.forward(-100)
turtle.left(-90)
turtle.forward(100)
turtle.left(-90)
turtle.forward(100)
turtle.left(90)
turtle.forward(-100)
turtle.forward(100)

turtle.penup()
turtle.forward(20)
#########################

# End
turtle.mainloop()