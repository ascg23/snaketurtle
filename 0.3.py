import turtle
import random
import time

#Menu

#Tela Menu Config
start_screen = turtle.Screen()
start_screen.screensize(0,0,'black')
sts = turtle.Turtle()
sts.up()
sts.ht()
sts.speed(0)


start = False

def inicio():
        global start
        if sts.heading() == 70:
            start = True
            print('ok')
        
def enter():
        sts.setheading(70)

start_screen.onkeypress(enter,'p')
start_screen.listen()
start_screen.update()


while start == False:

    #Turtle Menu Config
    stt = turtle.Turtle()
    stt.ht()
    stt.up()
    stt.speed(0)
    stt.color('white')
    stt.write('Pressione ENTER para começar','','center',['Retro Game',20,'normal'])


    #Cores
    col = ['violet', 'indigo', 'blue', 
       'green', 'yellow', 'orange', 'red']

    title = turtle.Turtle()
    title.ht()
    title.up()
    title.speed(0)
    title.goto(0,100)
    title.color('white')


    title.write('SNAKETURTLE','','center',['Retro Game',30,'normal'])


    

   

















if start:
    #configuration
    t = turtle.Turtle() 
    screen = turtle.Screen()
    delay = 0.1
    score = 0

    #tela
    screen.screensize(0,0,"green")
    screen.delay(0)

    #Interface
    st = turtle.Turtle()
    st.ht()
    st.up()
    st.speed(0)
    st.goto(300,350)
    st.write("Pontos: ",True,"center",['Retro Game',20,'normal'])
    st_2 = turtle.Turtle()
    st_2.speed(0)
    st_2.ht()
    st_2.up()
    st_2.goto(370,350)

    




    #cauda
    cauda = []

    #cabeça
    t.shape("square")
    t.speed(0)


    #fruta
    f=turtle.Turtle()
    f.shape('circle')
    f.color("red")
    f.teleport(random.randint(100,100),random.randint(100,100))

    #Movimentação Cabeça
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

    screen.onkeypress(right, "d")
    screen.onkeypress(up, "w")
    screen.onkeypress(left, "a")
    screen.onkeypress(down,"s")

    velocidade = 20
    vivo = True

    while vivo:
        t.up()
        direcao = t.heading()

        screen.update()
        screen.listen()

        #Colisão Fruta
        if t.distance(f)<20:

            fruta=f.teleport(random.randint(0,250),random.randint(0,250))
            delay -= 0.0001

            #Score
            score += 10
            st_2.clear()
            st_2.write(score,'','center',['Retro Game',20,'normal'])

            #Adição Nova Cauda
            cauda_nova = turtle.Turtle()
            cauda_nova.speed(0)
            cauda_nova.shape('square')
            cauda_nova.shapesize(1,1)
            cauda_nova.up()
            cauda.append(cauda_nova)

        #Controle de Crescimento Cauda
        for i in range((len(cauda)-1), 0, -1):
            j = i-1 

            x = cauda[j].xcor() 
            y = cauda[j].ycor() 

            cauda[i].goto(x, y)


        #Estruturacao da primeira Cauda
        if len(cauda)>0:

            x = t.xcor()
            y = t.ycor()
            cauda[0].goto(x, y)


        #Colisão Cauda



        #movimentacao
        t.forward(velocidade) 



        #Delay Set
        time.sleep(delay)








        #Colisão Borda
        if t.xcor()>=470 or t.ycor()>=370 or t.xcor()<=-470 or t.ycor()<=-370: 
            vivo=False

