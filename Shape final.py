import tkinter as tk
from turtle import *
import os
import gtts
from playsound import playsound


##y = turtle
a = Turtle()
a.shapesize(0.1,0.1,0.1)
##turtle.bgcolor("cyan")
# Class----------------------------------------------------------------------------
class shapeAndColor():

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

##-------------------CIRCLE--------------------------------------------------------
    def circle():
      a.fillcolor('purple')
      a.begin_fill()
      l = 50
      a.circle(l)
      a.end_fill()
      tts = gtts.gTTS("purple circle",lang="en")
      tts.save("hello.mp3")
      ##playsound("hello.mp3")
      os.startfile('hello.mp3')

##-------------------SQUARE------------------------------------------------------
    def square():
        a.fillcolor('light green')
        a.begin_fill()
        a.right(90)
        a.forward(100)
        for i in range(3):
           a.right(90)
           a.forward(100)
        a.end_fill()
        tts = gtts.gTTS("light green square",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##-----------------TRIANGLE------------------------------------------------------
    def triangle():
        a.fillcolor('pink')
        a.begin_fill()
        a.right(120)
        a.backward(100)
        for i in range(2):
           a.right(120)
           a.backward(100)
        a.end_fill()
        tts = gtts.gTTS("pink triangle",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##-----------------RECTANGLE-----------------------------------------------------
    def rectangle():
        a.fillcolor('orange')
        a.begin_fill()
        for i in range(2):
           a.right(90)
           a.forward(100)
           a.right(90)
           a.forward(160)
        a.end_fill()
        tts = gtts.gTTS("orange rectangle",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##------------------STAR-----------------------------------------------------------
    def star():
        a.fillcolor('yellow')
        a.begin_fill()
        a.right(105)
        a.backward(100)
        for i in range(4):
            a.right(144)
            a.backward(100)
        a.end_fill()
        tts = gtts.gTTS("yellow star",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##-------------------------OVAL-------------------------------------------
    def oval():
        a.fillcolor('blue')
        a.begin_fill()
        def draw(rad):
            for i in range(2):
               a.circle(rad,90)
               a.circle(rad//3,90)
        a.seth(-45)
        draw(100)
        a.end_fill()
        tts = gtts.gTTS("blue oval",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##-------------------------PENTAGON----------------------------------------------------
    def pentagon():
        a.fillcolor('violet')
        a.begin_fill()
        for i in range(5):
           a.left(72)
           a.forward(100)
        a.end_fill()
        tts = gtts.gTTS("violet pentagon",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##-----------------------KITE------------------------------------------------
    def kite():
        a.fillcolor('brown')
        a.begin_fill()
        a.forward(40)
        a.left(120)
        a.forward(40)
        a.left(120)
        a.forward(40)
        a.right(100)
        for i in range(4):
           a.forward(150)
           a.right(90)
        a.right(45)
        a.forward(210)
        a.right(45)
        a.end_fill()
        tts = gtts.gTTS("brown kite",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##-------------------------HEXAGON------------------------------------------
    def hexagon():
        a.fillcolor('white')
        a.begin_fill()
        for i in range(6):
           a.forward(90)
           a.left(300)
        a.end_fill()
        tts = gtts.gTTS("white hexagon",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')
        
##-----------------------HEART------------------------------------------------
    def heart():
        a.fillcolor('red')
        a.begin_fill()
        def curve():
           for i in range(200):
               a.right(1)
               a.forward(1)
        def pen():
            a.left(140)
            a.forward(113)
            curve()
            a.left(120)
            curve()
            a.forward(112)
        pen()
        a.end_fill()
        tts = gtts.gTTS("red heart",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##-----------------------HEPTAGON------------------------------------------------------
    def heptagon():
        a.fillcolor('lime')
        a.begin_fill()
        for i in range(7):
           a.right(51)
           a.forward(100)
        a.end_fill()
        tts = gtts.gTTS("lime heptagon",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##------------------------LINE------------------------------------------------
    def line():
        a.fillcolor('black')
        a.begin_fill()
        a.forward(300)
        a.left(180)
        a.end_fill()
        tts = gtts.gTTS("black line",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##-------------------------OCTAGON--------------------------------------------
    def octagon():
        a.fillcolor('sea green')
        a.begin_fill()
        for i in range(8):
           a.right(45)
           a.forward(100)
        a.end_fill()
        tts = gtts.gTTS("sea green octagon",lang="en")
        tts.save("hello.mp3")
        #playsound("hello.mp3")
        os.startfile('hello.mp3')

##BUTTONS----------------------------------------------------------------------
    buttonM = tk.Button(frame, text="⬤", fg="purple", command=circle)
    buttonM.pack(side=tk.LEFT)

    buttonN = tk.Button(frame,text="■", fg="light green", command=square)
    buttonN.pack(side=tk.LEFT)

    buttonO = tk.Button(frame, text="▲", fg="pink", command=triangle)
    buttonO.pack(side=tk.LEFT)

    buttonP = tk.Button(frame, text="▅▅", fg="orange", command=rectangle)
    buttonP.pack(side=tk.LEFT)

    buttonQ = tk.Button(frame, text="★", fg="yellow", command=star)
    buttonQ.pack(side=tk.LEFT)

    buttonR = tk.Button(frame, text="⬬", fg="blue", command=oval)
    buttonR.pack(side=tk.LEFT)

    buttonS = tk.Button(frame, text="⬟", fg="violet", command=pentagon)
    buttonS.pack(side=tk.LEFT)

    buttonT = tk.Button(frame, text="♦", fg="brown", command=kite)
    buttonT.pack(side=tk.LEFT)

    buttonU = tk.Button(frame, text="⬢", fg="white", command=hexagon)
    buttonU.pack(side=tk.LEFT)

    buttonV = tk.Button(frame, text="❤", fg="red", command=heart)
    buttonV.pack(side=tk.LEFT)

    buttonW = tk.Button(frame, text="", fg="lime", command=heptagon)
    buttonW.pack(side=tk.LEFT)

    buttonX = tk.Button(frame, text="−−", fg="black", command=line)
    buttonX.pack(side=tk.LEFT)

    buttonZ = tk.Button(frame, text="⯃", fg="sea green", command=octagon)
    buttonZ.pack(side=tk.LEFT)








### Objects--------------------------------------------------------------------------
##star = shape()
##star = a
##
##circle = shape()
##c = a
##
##square = shape()
##square = a
##
##triangle = shape()
##triangle = a
##
##rectangle = shape()
##rectangle = a
##
##oval = shape()
##oval = y
##
##heart = shape()
##heart = a
##
##kite = shape()
##kite = a
##
##hexagon = shape()
##hexagon = a
##
##heptagon = shape()
##heptagon = a
##
##octagon = shape()
##octagon = a
##
##pentagon = shape()
##pentagon = a
##
##line = shape()
##line = a

####FORMAT:
##b = input("Enter shape")
##if (b == star):
##    print(star.shape)
##elif (b == circle):
##    print(circle.shape)
##elif (b == square):
##    print(square.shape)
##elif (b == triangle):
##    print(triangle.shape)
##elif (b == rectangle):
##    print(rectangle.shape)
##elif (b == oval):
##    print(oval.shape)
##elif (b == pentagon):
##    print(pentagon.shape)
##elif (b == kite):
##    print(kite.shape)
##elif (b == hexagon):
##    print(hexagon.shape)
##elif (b == heart):
##    print(heart.shape)
##elif (b == heptagon):
##    print(heptagon.shape)
##elif (b == line):
##    print(line.shape)
##elif (b == octagon):
##    print(octagon.shape)
##else:
##    print("Shape not found")
##
##
##
##
##
##turtle.done()
