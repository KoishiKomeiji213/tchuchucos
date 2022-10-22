from random import choice, randint
from threading import Timer
import time
from tkinter import Y
from tkinter.font import BOLD, ITALIC
import turtle
#janela

main = turtle.Screen() # Cria a janela
main.bgcolor('black') # muda a cor do fundo
main.setup(900,800) # muda o tamanho da janela
main.title('touhou embodiment of the FuP devil') # titulo do jogo, o jogo foi feito com a tematica de touhou

main.addshape('bc.gif')
main.addshape('sprite.gif') # sprite do personagem principal
main.addshape('faca.gif') # sprite do projetil

#variaveis
global fuel # combustivel 
global placar # score
global enemys # inimigo speed
global players # player speed


fps = 30 # define o fps do jogo


# tenho que checar o xcor passado para dizer que não pode ser gerado outra faca lá

def spawnobj():
    faca.showturtle()
    faca.setpos(x=randint(-100,100),y= 400)

# colisão

def colisao():
        if abs(faca.xcor() - kirisame.xcor()) <= 20 and abs(faca.ycor() - kirisame.ycor()) <= 20:
            faca.clear()
            spawnobj()

def mainloopupdate():
    main.update()
fundo = turtle.Turtle()
fundo.shape('bc.gif')
fundo.penup()
# definir personagem, inimigo e combustivel.

kirisame = turtle.Turtle()
kirisame.penup() # levanta a personagem para não deixar rastro
kirisame.goto(0,-200) # define a posição inicial da personagem
kirisame.shape("sprite.gif") # coloca o sprite da kirisame

# pontuação

pontuacao = turtle.Turtle() #pontuação
pontuacao.hideturtle()
pontuacao.penup()
pontuacao.color("white")
pontuacao.goto(290, 170)
pontuacao.write("pontuação:", font=("verdana", 15, BOLD))
# combustivel
textcombustivel = turtle.Turtle() #pontuação
textcombustivel.hideturtle()
textcombustivel.penup()
textcombustivel.color("white")
textcombustivel.goto(290, -100)
textcombustivel.write("combustivel:", font=("verdana", 15, BOLD))

combustivel = turtle.Turtle()
combustivel.penup()
combustivel.color("white")
combustivel.goto(290, -120)


# velocidade dos itens, cenario e inimigos

players = 30
enemys = 0.4

# obstaculos

faca = turtle.Turtle() # Cria o obstaculo
faca.shape('faca.gif') # define a forma do obstaculo
faca.penup() # levanta a turtle do fundo, basicamente remove o rastro




def colisaoborda():
    kirisame.goto(kirisame.xcor(), kirisame.ycor())

def Left():
    if kirisame.xcor() <= -250:
        colisaoborda()
    else:
        kirisame.goto(kirisame.xcor() - players, kirisame.ycor())
def Right():
    if kirisame.xcor() >= 210:
        colisaoborda()
    else:
        kirisame.goto(kirisame.xcor() + players, kirisame.ycor())
def movefaca():
    if faca.ycor() <= -200:
        spawnobj()
    else:
        faca.goto(faca.xcor(), faca.ycor() - enemys)


main.listen()
main.onkeypress(Left, 'Left')
main.onkeypress(Right, 'Right')
main.ontimer(colisaoborda, 1000//fps )

while True:
    colisao()
    main.ontimer(movefaca, 1000//fps)
    main.tracer(0,0)
    main.update()
