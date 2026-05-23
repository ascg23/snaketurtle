import turtle
import random
import time


#Menu

#Tela Menu Config
start_screen = turtle.Screen()
start_screen.screensize(800,800,'black')

gm_over = turtle.Turtle()
gm_over.ht()
gm_over.up()

stt = turtle.Turtle()
stt.ht()
stt.up()
stt.speed(0)
stt.color('white')
stt.write('Pressione P para começar','','center',['Retro Game',20,'normal'])
stt.sety(stt.ycor()-30)
stt.write('Controles:','','center',['Retro Game',20,'normal'])
stt.sety(stt.ycor()-30)
stt.write('W para ir pra cima','','center',['Retro Game',15,'normal'])
stt.sety(stt.ycor()-30)
stt.write('S para ir pra baixo','','center',['Retro Game',15,'normal'])
stt.sety(stt.ycor()-30)
stt.write('A para ir pra esquerda','','center',['Retro Game',15,'normal'])
stt.sety(stt.ycor()-30)
stt.write('D para ir pra direita','','center',['Retro Game',15,'normal'])



title = turtle.Turtle()
title.ht()
title.up()
title.speed(0)
title.goto(0,100)
title.color('white')
title.write('SNAKETURTLE','','center',['Retro Game',30,'normal'])

start = False


def enter():
        global start
        
        start = True
        stt.clear()
        title.clear()
start_screen.onkeypress(enter,'p')
start_screen.listen()


#Cores
col = ['violet', 'indigo', 'blue', 
       'green', 'yellow', 'orange', 'red']

while not start:
    start_screen.update()
    
if start:
    #configuration
    t = turtle.Turtle() 
    screen = turtle.Screen()
    delay = 0.02
    score = 0
    highscore = 0
    #tela
    screen.screensize(800,800,"green")
    screen.delay(0)

    #Interface
    st = turtle.Turtle()
    hs = turtle.Turtle()
    hs.ht()
    hs.up()
    hs.speed(0)
    hs.goto(-300,350)
    st.ht()
    st.up()
    st.speed(0)
    st.goto(300,350)
    
    hs.write("Highscore: ",True,"center",['Retro Game',20,'normal'])
    st.write("Pontos: ",True,"center",['Retro Game',20,'normal'])
    
    st_2 = turtle.Turtle()
    st_2.speed(0)
    st_2.ht()
    st_2.up()
    st_2.goto(370,350)
    
    hs_2 = turtle.Turtle()
    hs_2.speed(0)
    hs_2.ht()
    hs_2.up()
    hs_2.goto(-200,350)

    #Borda
    bd = turtle.Turtle()
    bd.ht()
    bd.speed(0)
    bd.width(20)
    bd.left(90)
    bd.teleport(-470,-470)
    for bdr in range(4):
        bd.forward(470*2)
        bd.right(90)
        




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


    def nada():
        pass
    def sair():
        global vivo
        vivo = False
       

    def restart():
        global velocidade
        velocidade = 20
        global cauda
        cauda.clear()
        global gm_over
        gm_over.clear()
        global t
        t.goto(0,0)
        t.showturtle()
        screen.onkeypress(nada, "r")
        screen.onkeypress(nada, "e")
        
        
        
        
        
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
        for cd in range(2,len(cauda)):
           if t.distance(cauda[cd])<20:
                t.ht()
                t.goto(0,0)
                for i in cauda:
                    i.ht()
                    i.clear()
                if highscore < score:
                    hs_2.clear()
                    highscore = score
                score = 0
                hs_2.write(highscore,'','center',['Retro Game',20,'normal'])
                
                gm_over.write("Fim de jogo! R para continuar",'','center',['Retro Game',20,'normal'])
                screen.onkeypress(restart,"r")
                




        #movimentacao
        t.forward(velocidade) 



        #Delay Set
        time.sleep(delay)


        
        









        #Colisão Borda
        if t.xcor()>=470 or t.ycor()>=370 or t.xcor()<=-470 or t.ycor()<=-370:
            t.ht()
            t.goto(0,0)
            for i in cauda:
                i.ht()
                i.clear()
            if highscore < score:
                hs_2.clear()
                highscore = score
            score = 0
            hs_2.write(highscore,'','center',['Retro Game',20,'normal'])
            
            gm_over.write("Fim de jogo! R para continuar",'','center',['Retro Game',20,'normal'])
            screen.onkeypress(restart,"r")
            
            
            
            
   
    
    
