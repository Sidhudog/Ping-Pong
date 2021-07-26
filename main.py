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
