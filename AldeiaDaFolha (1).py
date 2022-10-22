import turtle
from turtle import*
from random import randint
#Configurações de entradas.
aldeia = turtle.Screen()                                 #Criação da tela para o jogo.
aldeia.tracer(0)
aldeia.title('Naruto Shippuden')                         #Título da janela.
aldeia.setup(height=1280, width=860, starty= 10)         #Definição da janela.
aldeia.addshape('Naruto1.gif')                           #Adicionando os formatos a serem utilizados.
aldeia.addshape('ramen.gif')
aldeia.addshape('fundo.gif')
aldeia.addshape('shuriken.gif')
aldeia.addshape('kunai.gif')
#Configurações de objetos.
estrada = turtle.Turtle()                                #Criação do objeto que terá o formato da estrada.
estrada.penup()
estrada.shape('fundo.gif')                               #Definição do formato da estrada.
estrada.rt(90)
estrada2 = turtle.Turtle()
estrada2.penup()
estrada2.shape('fundo.gif')
estrada2.rt(90)
estrada2.hideturtle()
estrada2.goto(0, 600)

#Criação do jogador.
naruto = turtle.Turtle()                                 #Jogador adicionado.
naruto.up()                                              #Jogador operando sem deixar rastros.
naruto.goto(0, -300)                                     #Posição inicial do jogador.
naruto.shape('Naruto1.gif')                              #Adicionando o formato do personagem do jogador.

#Obstáculos.
obstaculo1 = turtle.Turtle()                              #Primeiro obstáculo.
obstaculo1.up()                                           #Não deixará rastros.
obstaculo1.shape('shuriken.gif')                          #Adicionando o formato.
obstaculo1.rt(90)
obstaculo1.goto(randint(-200, 150), 600)
obstaculo2 = turtle.Turtle()                              #Segundo obstáculo.
obstaculo2.up()                                           #Não deixará rastros.
obstaculo2.shape('kunai.gif')                             #Adicionando o formato.
obstaculo2.rt(90)
obstaculo2.goto(randint(-200, 150), 600)

#Combustível.
ramen = turtle.Turtle()                                 #Criando o combustível que gerará a pontuação.
ramen.shape('ramen.gif')                                #Definindo o formato do combustível.
ramen.up()                                              #Impedindo que o combustível deixe ratros.
ramen.speed(0)                                          #Definindo a velocidade do combustível.
ramen.rt(90)
ramen.goto(randint(-200, 150), 600)   #randint(min, max)


#Pontuação & Tanque de Combustível.
score = turtle.Turtle()
score.up
score.goto
score.hideturtle()

#Funções
def geracaoObs():


def direita():                                           #Definindo a primeira tecla de movimento e o espaço percorrido.
    naruto.fd(50)                                        #Quantidade de pixels que irá movimentar para a direita.

def esquerda():                                          #Definindo a segunda tecla de movimento e o espaço percorrido.
    naruto.bk(50)                                        #Quantidade de pixels percorridos para a esquerda.

def lacoPrincipal():                                     #Laço onde toda a "mágica" ocorre.
    #estrada.fd(3)                                        #Quantidade de pixels que a estrada irá movimentar.
    meiofio()                                            #Chamando a função que irá definir o limite da estrada.
    #if estrada.ycor() == -700:
        #estrada2.showturtle()
        #estrada2.fd(10)
    aldeia.update()
    aldeia.ontimer(lacoPrincipal, 60 // 1000)
def meiofio():                                           #Limite da estrada para que ocorra a pausa.
    if naruto.xcor() >= 200 or naruto.xcor() <= -250:        #Parâmetros dos limites.
        naruto.goto(0, -300)                             #Caso o jogador atinja o limite, ele retornará para a posição inicial.

#Condições
#if naruto.xcor >= 151:
    #naruto.goto(0, -250)

#Chamadas de teclas.
onkeypress(esquerda, 'Left')                                  #Definindo a entrada da tecla de movimento para a esquerda.
onkeypress(direita, 'Right')                                  #Definindo a entrada da tecla de movimento para a direita.
listen()                                                 #Dizendo ao programa para entender("escutar") quando uma das duas teclas forem pressionadas.

lacoPrincipal()
aldeia.mainloop()                                        #Girando o loop da tela.
