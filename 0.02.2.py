import turtle
import random
#configuration
t = turtle.Turtle()
screen = turtle.Screen()



#tela
screen.screensize(400, 300,"green")

#cauda
s = turtle.Turtle()
cauda = []
s.shape("circle")
#cabeça
t.shape("square")


#fruta    
f=turtle.Turtle()
f.shape('circle')
f.color("red")
f.teleport(random.randint(100,100),random.randint(100,100))

def right():
    global direcao
    if direcao != 180:
        t.setheading(0)
def left():
    global direcao 
    if direcao != 0:
        t.setheading(180)
def up():
    global direcao
    if direcao != 270:
        t.setheading(90)
def down():
    global direcao
    if direcao != 90:
        t.setheading(270)

velocidade = 1
vivo = True

while vivo:
    s.up()
    t.up()
    t.forward(velocidade)
    direcao = t.heading()
    
    screen.onkeypress(right, "d")
    screen.onkeypress(up, "w")
    screen.onkeypress(left, "a")
    screen.onkeypress(down,"s")
    posicao_da_cabeca = t.pos()
    if direcao == 0:
        s.goto(posicao_da_cabeca[0] - 20,posicao_da_cabeca[1])
    if direcao == 180:
        s.goto(posicao_da_cabeca[0] + 20,posicao_da_cabeca[1])
    if direcao == 90:
        s.goto(posicao_da_cabeca[0],posicao_da_cabeca[1]-20)
    if direcao == 270:
        s.goto(posicao_da_cabeca[0] ,posicao_da_cabeca[1]+20)
    

    turtle.update()
    screen.listen()


   

    #Colisão Fruta
    if t.distance(f)<20:
        fruta=f.teleport(random.randint(0,250),random.randint(0,250))
        
        velocidade += 0.1
        #Adição Nova Cauda
        cauda_nova = s.clone()
        cauda.append(cauda_nova)
        cauda_nova.up()

        
        
            

    #Colisão Borda
    if t.xcor()>=470 or t.ycor()>=370 or t.xcor()<=-470 or t.ycor()<=-370: 
        vivo=False
        

        
