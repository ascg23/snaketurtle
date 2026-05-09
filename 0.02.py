import turtle
import random
#configuration
t = turtle.Turtle()
screen = turtle.Screen()



#tela
screen.screensize(400, 300,"green")

#cabeça
t.shape("square")


#fruta    
f=turtle.Turtle()
f.shape('circle')
f.color("red")
f.teleport(random.randint(100,100),random.randint(100,100))

def right():
    t.setheading(0)
def left():
    t.setheading(180)
def up():
    t.setheading(90)
def down():
    t.setheading(270)

velocidade = 1
vivo=True
while vivo:
    t.up()
    t.forward(velocidade)
    screen.onkeypress(right, "d")
    screen.onkeypress(up, "w")
    screen.onkeypress(left, "a")
    screen.onkeypress(down,"s")
    

    turtle.update()
    screen.listen()


   

    #Colisão Fruta
    if t.distance(f)<20:
        fruta=f.teleport(random.randint(0,250),random.randint(0,250))

        velocidade += 0.1

    #Colisão Borda
    if t.xcor()>=470 or t.ycor()>=370 or t.xcor()<=-470 or t.ycor()<=-370: 
        vivo=False
        

        


