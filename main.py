import turtle
import random

screen = turtle.Screen()
screen.bgcolor("PaleGreen2")
screen.title("Catch The Turtle")
FONT = ('Arial', 30 , 'normal')
score = 0
game_over = False

x_cordinates = [-600,-450,-300,-150,0,150,300,450,600]
y_cordinates = [-300,-150,0,150,300]

TurtleList = []
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    top_height = screen.window_height()
    y = top_height * 0.55
    score_turtle.color("darkblue")
    score_turtle.penup()
    score_turtle.setpos(0,y)
    score_turtle.pendown()
    score_turtle.write(arg="Score: 0", move=False ,align="center",font=FONT)
    score_turtle.hideturtle()
def make_turtle(x,y):
    t =turtle.Turtle()
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)
        print(x,y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.goto(x,y)
    TurtleList.append(t)
def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x,y)
def hide_turtles():
    for t in TurtleList:
        t.hideturtle()
def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(TurtleList).showturtle()
        screen.ontimer(show_turtle_randomly, 500)
def countdown(time):
    global game_over

    countdown_turtle.hideturtle()
    top_height = screen.window_height()
    y = top_height * 0.55
    countdown_turtle.color("black")
    countdown_turtle.penup()
    countdown_turtle.setpos(0,y - 200)
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False ,align="center",font=FONT)
        screen.ontimer(lambda: countdown(time - 1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Time's Up!", move=False, align="center", font=FONT)
def starting_game():
    turtle.tracer(0)
    countdown(15)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtle_randomly()
    turtle.tracer(1)

starting_game()
turtle.mainloop()