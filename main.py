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








def paddle_b_up():
    y=paddle_b.ycor()
    if paddle_b.ycor() < 240:
        y+=50
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    if paddle_b.ycor() > -240:
        y-=50
    paddle_b.sety(y)

#Keyboard vinding 
win.listen()
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")








while True:
    win.update()
    # move the ball
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    y=paddle_a.ycor()
    if paddle_a.ycor() < 240:
        if ball.ycor()>paddle_a.ycor():
            y+=1
    paddle_a.sety(y)


    y=paddle_a.ycor()
    if paddle_a.ycor() > -240:
        if ball.ycor()<paddle_a.ycor():
            y-=1
    paddle_a.sety(y)

    # vertical border checking 
    if ball.ycor() > 290:
        winsound.PlaySound("up.wav",winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        winsound.PlaySound("up.wav",winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1
    # horzontal border checking
    if ball.xcor() > 390:
        score_a+=1
        winsound.PlaySound("endgame.wav",winsound.SND_ASYNC)
        ball.goto(0,0)
        pen.clear()
        pen.write(f"player A: {score_a}   player B: {score_b}",align="center" , font=("Courier",24,"normal"))
    if ball.xcor() < -390:
        score_b+=1
        winsound.PlaySound("endgame.wav",winsound.SND_ASYNC)
        ball.goto(0,0)
        pen.clear()
        pen.write(f"player A: {score_a}   player B: {score_b}",align="center" , font=("Courier",24,"normal"))

    # bounce 
    if ball.xcor() > 340 and ball.xcor()<350 and  (paddle_b.ycor() + 60 > ball.ycor()) and (paddle_b.ycor() - 60 < ball.ycor()):
        winsound.PlaySound("pad.wav",winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1
    
    if ball.xcor() < -340 and ball.xcor()> -350 and  (paddle_a.ycor() + 40 > ball.ycor()) and (paddle_a.ycor() - 40 < ball.ycor()):
        winsound.PlaySound("pad.wav",winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1
