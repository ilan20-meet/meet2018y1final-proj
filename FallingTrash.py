import turtle
import random
import time

turtle.bgpic("env.gif")
score = 0
scoreTurtle=turtle.clone()
scoreTurtle.hideturtle()
scoreTurtle.penup()
scoreTurtle.goto(480,450)
scoreTurtle.write(int(score),align="center",font=("times",33,"bold"))

game_over=turtle.clone()
game_over.hideturtle()
game_over.penup()
game_over.goto(0,0)



turtle.register_shape("bottle.gif")

SQUARE_SIZE = 20

man=turtle.clone()
turtle.hideturtle()

turtle.register_shape("man.gif")
man.shape("man.gif")
turtle.setup(1000,1000)
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
direction = LEFT 

fire=turtle.clone()
turtle.register_shape("fire.gif")
fire.shape("fire.gif")
fire.penup()
fire.showturtle()
fire.goto(0,-490)



gun1 = turtle.clone()
#gun2 = turtle.clone()

#gun3 = turtle.clone()
#gun4 = turtle.clone()
#gun5 = turtle.clone()
#gun6 = turtle.clone()
#gun7 = turtle.clone()
#gun8 = turtle.clone()
index = 0


gun_list = [gun1]

SPACE = "space"

def up():
    global index
    index+=1
    print('You shoot the gun!')
    gun1.speed(1)
    turtle.register_shape("recycle.gif")
    gun1.shape("recycle.gif")
    gun1.hideturtle()
    gun1.penup()
    gun1.setheading(90)
    #gun_list[index%len(gun_list)].left(90)
    # x = snake.pos()[0]
    
    #gun_list[index%len(gun_list)].goto(x,1000)
    gun1.goto(man.pos())
    gun1.showturtle()
    gun1.forward(1000)
    
z=0
difficulty=0.1
num_bottle=0
max_bottle=8
bottle_list=[]
def make_bottle():  #need to make a few at a time
    for num_bottle in range(max_bottle):
        random_x=random.randint(-470,470)
        bottle=turtle.clone()
        bottle.speed(0)
        bottle.hideturtle()
        bottle.penup()
        bottle.shape("bottle.gif")
        bottle.goto(random_x,480)
        bottle_list.append(bottle)
        bottle.showturtle()
        bottle.speed(10)
    
    
def move_bottle():
    random_bottle=random.randint(0,max_bottle-1)
    bottle=bottle_list[random_bottle]
    bottle.goto(bottle.pos()[0],bottle.pos()[1]- SQUARE_SIZE)
    time.sleep(difficulty)        

old_stamp="not set"


def move_man():
    my_pos = man.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    #global old_stamp
    if direction==RIGHT:
        man.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        man.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    #print(old_stamp)    
    #old_stamp.clearstamp()
    #old_stamp=man.stamp()
        

def left():
    global direction 
    direction=LEFT 
    print("You pressed the left key!")
    move_man()
def right():
    global direction 
    direction=RIGHT 
    print("You pressed the right key!")    
    move_man()
    

turtle.onkeypress(right,RIGHT_ARROW) # Create listener for up key
turtle.onkeypress(left,LEFT_ARROW) # Create listener for up key
turtle.listen()
make_bottle()
while True:
    
   
    turtle.onkeypress(up,SPACE)
    for bottle in bottle_list:
        if  bottle.pos()[1] < -410:
            game_over.write("Great Job ! You Recycle " + str(score) + " bottles",align="center",font=("times",33,"bold"))
            quit()
        if  gun1.pos()[0] < bottle.pos()[0] + 30 and gun1.pos()[0] > bottle.pos()[0] - 30 and gun1.pos()[1] > bottle.pos()[1] - 30:
            bottle_list.remove(bottle)
            bottle.hideturtle()
            score+=1
            scoreTurtle.clear()
            scoreTurtle.write(int(score),align="center",font=("times",33,"bold"))
        if len(bottle_list) < max_bottle:
            random_x=random.randint(-470,470)
            bottle=turtle.clone()
            bottle.speed(0)
            bottle.hideturtle()
            bottle.penup()
            bottle.shape("bottle.gif")
            bottle.goto(random_x,480)
            bottle_list.append(bottle)
            bottle.showturtle()
            bottle.speed(8)    
        if score - z >= 10:
            difficulty-=0.025
            z=z+10
        move_bottle()

turtle.mainloop()
