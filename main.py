import turtle
import winsound

win=turtle.Screen()
win.title("ping pong")
win.bgcolor("light green")
win.setup(width=800, height=600)
win.tracer(0)


# scre 
score_a=0
score_b=0







# paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
# paddle b
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)






ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("dark red")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5


# pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"player A: {score_a}   player B: {score_b}",align="center" , font=("Courier",24,"normal"))
