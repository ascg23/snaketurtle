import turtle
import random
import time

# ================= MENU =================

start_screen = turtle.Screen()
start_screen.setup(800, 800)
start_screen.bgcolor("black")
start_screen.title("SnakeTurtle")

stt = turtle.Turtle()
stt.hideturtle()
stt.penup()
stt.color("lime")

title = turtle.Turtle()
title.hideturtle()
title.penup()
title.color("lime")
title.goto(0, 100)

title.write(
    "SNAKETURTLE",
    align="center",
    font=("Arial", 30, "normal")
)

texto = [
    "Pressione P para começar",
    "",
    "Controles:",
    "W - cima",
    "S - baixo",
    "A - esquerda",
    "D - direita"
]

y = 0

for linha in texto:

    stt.goto(0, y)

    stt.write(
        linha,
        align="center",
        font=("Arial", 18, "normal")
    )

    y -= 30

start = False


def enter():
    global start

    start = True

    stt.clear()
    title.clear()


start_screen.listen()
start_screen.onkeypress(enter, "p")

while not start:
    start_screen.update()

# ================= JOGO =================

screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("SnakeTurtle")
screen.tracer(0)

# ================= BORDA =================

borda = turtle.Turtle()
borda.speed(0)
borda.color("lime")
borda.pensize(8)
borda.penup()

borda.goto(-480, -380)

borda.pendown()

for _ in range(2):

    borda.forward(960)
    borda.left(90)

    borda.forward(760)
    borda.left(90)

borda.hideturtle()

# ================= GAME OVER =================

gm_over = turtle.Turtle()
gm_over.hideturtle()
gm_over.penup()
gm_over.color("white")

game_over = False

# ================= CABEÇA =================

t = turtle.Turtle()
t.shape("square")
t.color("lime")
t.penup()

t.direction = "stop"

# ================= FRUTA =================

f = turtle.Turtle()
f.shape("circle")
f.color("red")
f.penup()

f.goto(
    random.randint(-400, 400),
    random.randint(-300, 300)
)

# ================= SCORE =================

score = 0
highscore = 0

st = turtle.Turtle()
st.hideturtle()
st.penup()

st.goto(0, 350)
st.color("lime")


def atualizar_score():

    st.clear()

    st.write(
        f"Pontos: {score}   Highscore: {highscore}",
        align="center",
        font=("Arial", 20, "normal")
    )


atualizar_score()

# ================= CAUDA =================

cauda = []

# ================= MOVIMENTO =================


def up():

    global game_over

    if game_over:
        gm_over.clear()
        game_over = False

    if t.direction != "down":
        t.direction = "up"


def down():

    global game_over

    if game_over:
        gm_over.clear()
        game_over = False

    if t.direction != "up":
        t.direction = "down"


def left():

    global game_over

    if game_over:
        gm_over.clear()
        game_over = False

    if t.direction != "right":
        t.direction = "left"


def right():

    global game_over

    if game_over:
        gm_over.clear()
        game_over = False

    if t.direction != "left":
        t.direction = "right"


screen.listen()

screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")

# ================= MOVIMENTAÇÃO =================


def mover():

    if t.direction == "up":
        t.sety(t.ycor() + 20)

    if t.direction == "down":
        t.sety(t.ycor() - 20)

    if t.direction == "left":
        t.setx(t.xcor() - 20)

    if t.direction == "right":
        t.setx(t.xcor() + 20)

# ================= LOOP PRINCIPAL =================


while True:

    screen.update()

    # ================= COLISÃO BORDA =================

    if (
        t.xcor() > 470 or
        t.xcor() < -470 or
        t.ycor() > 370 or
        t.ycor() < -370
    ):

        game_over = True

        gm_over.clear()

        gm_over.write(
            "Fim de jogo! Movimente para continuar",
            align="center",
            font=("Arial", 20, "normal")
        )

        t.goto(0, 0)
        t.direction = "stop"

        for segmento in cauda:
            segmento.goto(1000, 1000)

        cauda.clear()

        if score > highscore:
            highscore = score

        score = 0

        atualizar_score()

    # ================= COLISÃO FRUTA =================

    if t.distance(f) < 20:

        x = random.randint(-450, 450)
        y = random.randint(-350, 350)

        f.goto(x, y)

        novo = turtle.Turtle()
        novo.shape("square")
        novo.color("lime")
        novo.penup()

        cauda.append(novo)

        score += 10

        if score > highscore:
            highscore = score

        atualizar_score()

    # ================= MOVIMENTO CAUDA =================

    for i in range(len(cauda) - 1, 0, -1):

        x = cauda[i - 1].xcor()
        y = cauda[i - 1].ycor()

        cauda[i].goto(x, y)

    if len(cauda) > 0:

        cauda[0].goto(
            t.xcor(),
            t.ycor()
        )

    mover()

    # ================= COLISÃO CONSIGO MESMO =================

    for segmento in cauda:

        if segmento.distance(t) < 20:

            game_over = True

            gm_over.clear()

            gm_over.write(
                "Fim de jogo! Movimente para continuar",
                align="center",
                font=("Arial", 20, "normal")
            )

            t.goto(0, 0)
            t.direction = "stop"

            for s in cauda:
                s.goto(1000, 1000)

            cauda.clear()

            if score > highscore:
                highscore = score

            score = 0

            atualizar_score()


    time.sleep(0.1)
