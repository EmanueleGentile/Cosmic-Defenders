import turtle
import random
import time
import tkinter
from tkinter import messagebox

win = turtle.Screen()
win.title("Cosmic Defenders")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

score_display = turtle.Turtle()

punteggio = 0

#definisco l'aggiornamento del punteggio
def aggiorna_punteggio():
    score_display.clear()
    score_display.write("PUNTEGGIO: {}".format(punteggio), align="center", font=("Courier", 12, "normal"))

score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-290, 260)
aggiorna_punteggio()



# Personaggio potentissimo (è una tartaruga armata)
player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)  


#Movimento del personaggio

player_speed = 20

bullet_speed = 5     



def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -290:
        x = 290
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 290:
        x = 290
    player.setx(x)


bullet_state = "ready"  # "ready" significa che il proiettile non è visibile 


def colpo():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.hideturtle()
        bullet.penup()
        bullet.showturtle()
        
        

#proiettile (e tutti zitti)
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.penup()
bullet.hideturtle()

#Definisco i tasti della tastiera


win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
win.onkeypress(colpo, "space")






#Definisco gli invasori (e tutti zitti)
num_invaders = 5
invaders = []


invader_speed = 2

for _ in range (num_invaders):
    
    invader = turtle.Turtle()
    invader.shape("circle")
    invader.color("red")
    invader.speed(0)
    invader.penup()
    x = random.randint (-290, 290)
    y = random.randint (100,250)
    invader.goto(x, y)
    invaders.append(invader)





#Definisco il movimento degli invasori (e tutti zitti)
def move_invaders():
    for invader in invaders:
       y = invader.ycor()
       y-= invader_speed
       invader.sety(y)
       if player.distance(invader) < 20:
           invader.hideturtle()
           player.hideturtle()
           messagebox.showerror("Game Over", "Hai perso!")
           win.bye() 
            
       if invader.ycor() < -290:
            invader.hideturtle()
            x = random.randint(-290, 290)
            y = random.randint(100, 250)
            invader.goto(x, y)
            invader.hideturtle()
            player.hideturtle()
            messagebox.showerror("Game Over", "Hai perso!")
            win.bye()
    win.update()
    win.ontimer(move_invaders, 100)  # Aggiorna la posizione degli invasori ogni 100 ms
move_invaders()
            








while True:
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
    #verifico se il proiettile ha colpito un invasore
    for invader in invaders:
        if bullet.distance(invader) < 15:
            bullet.hideturtle()
            bullet_state = "ready"
            invader.hideturtle()
            x = random.randint(-290, 290)
            y = random.randint(100, 250)
            invader.goto(x, y)
            punteggio += 10
            aggiorna_punteggio()
            invader.showturtle() 
    if y > 290:
        bullet.hideturtle()
        bullet_state = "ready"        



    
        
    win.update()