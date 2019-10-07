from random import choice
from turtle import *
from UtilitiesUsedForGames import floor, vector

State = {'score': 0}
Path = Turtle(visible=False)
Writer = Turtle(visible=False)
Aim = vector(5, 0)
Pacman_ = vector(-40, -80)
Ghosts_ = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
Tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 0, 0, 1 , 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    #This will draw the square using Path with axis (x, y).
    Path.up()
    Path.goto(x, y)
    Path.down()
    Path.begin_fill()

    for count in range(4):
        Path.forward(20)
        Path.left(90)

    Path.end_fill()

def Offset(Point):
    #This will return the Offset of the Point in the Tiles in each of the occasions
    x = (floor(Point.x, 20) + 200) / 20
    y = (180 - floor(Point.y, 20)) / 20
    Index_ = int(x + y * 20)
    return Index_

def valid(Point):
    #Return True if the Point is valid in the Tiles in each occasion
    Index_ = Offset(Point)

    if Tiles[Index_] == 0:
        return False

    Index_ = Offset(Point + 19)

    if Tiles[Index_] == 0:
        return False

    return Point.x % 20 == 0 or Point.y % 20 == 0

def world():
    #Drawing the world using the Path
    bgcolor('black')
    Path.color('blue')

    for Index_ in range(len(Tiles)):
        tile = Tiles[Index_]

        if tile > 0:
            x = (Index_ % 20) * 20 - 200
            y = 180 - (Index_ // 20) * 20
            square(x, y)

            if tile == 1:
                Path.up()
                Path.goto(x + 10, y + 10)
                Path.dot(2, 'white')

def move():
    #To move Pacman_ and all Ghosts_.
    Writer.undo()
    Writer.write(State['score'])

    clear()

    if valid(Pacman_ + Aim):
        Pacman_.move(Aim)

    Index_ = Offset(Pacman_)

    if Tiles[Index_] == 1:
        Tiles[Index_] = 2
        State['score'] += 1
        x = (Index_ % 20) * 20 - 200
        y = 180 - (Index_ // 20) * 20
        square(x, y)

    up()
    goto(Pacman_.x + 10, Pacman_.y + 10)
    dot(20, 'yellow')

    for Point, course in Ghosts_:
        if valid(Point + course):
            Point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(Point.x + 10, Point.y + 10)
        dot(20, 'red')

    update()

    for Point, course in Ghosts_:
        if abs(Pacman_ - Point) < 20:
            return

    ontimer(move, 100)

def change(x, y):
    #Changes Pacman_ Aim if valid.
    if valid(Pacman_ + vector(x, y)):
        Aim.x = x
        Aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
Writer.goto(160, 160)
Writer.color('white')
Writer.write(State['score'])
listen()
#Keyboard
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
