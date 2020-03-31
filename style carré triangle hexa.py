from random import randint
from turtle import *
import time
def carre (taille, couleur) :
    color(couleur)
    left(0)
    down()
    for c in range (0,4) :
        forward(taille)
        right(90)
    up()

def triangle(taille) :
    down()
    c=0
    while c<3 :
        forward(taille)
        right(120)
        c+=1
    up()
    return
def hexa(taille):
    down()
    c=0
    while c<6 :
        forward(taille)
        right(60)
        c+=1
    up()

def dessin(r) :

        while r<3 :
            N = randint (0, 6)
            carre (taille , couleur [N])
            forward(0)
            triangle(taille)
            forward(0)
            hexa(taille)
            forward(ecart)
            r+=1


up()
goto(50,-100)
speed(300)
width(2)
couleur = ["red", "green", "purple", "blue", "black", "pink", "orange"]
taille, ecart, r, a = 7, 15, 0, 55

for i in range(0, 12) :
    dessin(r)
    left(a)
    a= a-1
    taille = taille +5
    ecart = ecart +10



write ("Terminer")
time.sleep(60)
bye()