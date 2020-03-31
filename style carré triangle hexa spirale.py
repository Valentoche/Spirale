from random import randint
from turtle import *
import time
def carre (taille, couleur) :                                                   #fonction carré
    color(couleur)
    left(0)
    down()
    for c in range (0,4) :
        forward(taille)
        right(90)
    up()

def triangle(taille) :                                                          #fonction triangle
    down()
    c=0
    while c<3 :
        forward(taille)
        right(120)
        c+=1
    up()
    return
def hexa(taille):                                                               #fonction héxagone
    down()
    c=0
    while c<6 :
        forward(taille)
        right(60)
        c+=1
    up()

def dessin(r) :                                                                 #fonction dessin

        while r<3 :
            N = randint (0, 6)
            carre (taille , couleur [N])
            forward(0)
            triangle(taille)
            forward(0)
            hexa(taille)
            forward(ecart)
            r+=1                                                                #ajoute un tour


up()
goto(50,-100)
speed(500)
width(2)
couleur = ["red", "green", "purple", "blue", "black", "pink", "orange"]
taille, ecart, r, a = 7, 15, 0, 55                                              #Défini variable taille, écart, distance, angle

for i in range(0, 12) :                                                         #Répétiton de déssin 12 fois avec angle modifié par -1 et écart qui augmente de 10
    dessin(r)
    left(a)
    a= a-1
    taille = taille +5
    ecart = ecart +10



write ("Terminer")
time.sleep(10)
bye()