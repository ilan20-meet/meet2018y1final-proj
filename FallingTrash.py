import turtle
import random

turtle.register_shape("bottle.gif")


num_bottle=0
max_bottle=8
bottle_list=[]
def make_bottle():  
    for num_bottle in range(max_bottle):
        random_x=random.randint(-940,940)
        bottle=turtle.clone()
        bottle.penup()
        bottle.shape("bottle.gif")
        bottle.goto(random_x,450)
        bottle_list.append(bottle)
    
make_bottle()    
    
    
man=turtle.clone()
turtle.hideturtle()
SQUARE_SIZE = 10
turtle.register_shape("giphy.gif")
man.shape("giphy.gif")
turtle.setup(1900,1000)
man.penup()
man.goto(0,-150)
turtle.tracer(1,0)
LEFT_ARROW = "Left" 
RIGHT_ARROW = "Right" 
LEFT=1
RIGHT=3
UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300
direction = RIGHT
def left():
    global direction 
    direction=LEFT 
    move_snake()
    print("You pressed the left key!")
def right():
    global direction 
    direction=RIGHT 
    print("You pressed the right key!")    
    move_snake()
turtle.onkeypress(right,RIGHT_ARROW) # Create listener for up key
turtle.onkeypress(left, LEFT_ARROW) # Create listener for up key
turtle.listen()
def move_snake():
    my_pos = man.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        man.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        man.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")




































turtle.mainloop()
