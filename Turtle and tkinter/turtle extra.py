import turtle
import os
import gtts
from playsound import playsound

y = turtle
a = turtle.Turtle()
turtle.bgcolor("cyan")

    
# Class
class shape():
    pass
    def details(self):
        return f"right is (self.right), backward is (self.backward)"

class star(shape):
    a.fillcolor('yellow')
    a.begin_fill()
    a.right(105)
    a.backward(100)
    for i in range(4):
        a.right(144)
        a.backward(100)
    a.end_fill()
    tts = gtts.gTTS("star",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class circle(shape):
    a.fillcolor('purple')
    a.begin_fill()
    l = 50
    a.circle(l)
    a.end_fill()
    tts = gtts.gTTS("circle",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class square(shape):
    a.fillcolor('light green')
    a.begin_fill()
    a.right(90)
    a.forward(100)
    for i in range(3):
       a.right(90)
       a.forward(100)
    a.end_fill()
    tts = gtts.gTTS("square",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class triangle(shape):
    a.fillcolor('red')
    a.begin_fill()
    a.right(120)
    a.backward(100)
    for i in range(2):
       a.right(120)
       a.backward(100)
    a.end_fill()
    tts = gtts.gTTS("triangle",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class rectangle(shape):
    a.fillcolor('orange')
    a.begin_fill()
    for i in range(2):
       a.right(90)
       a.forward(100)
       a.right(90)
       a.forward(160)
    a.end_fill()
    tts = gtts.gTTS("rectangle",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class oval(shape):
    a.fillcolor('blue')
    a.begin_fill()
    def draw(rad):
       for i in range(2):
           y.circle(rad,90)
           y.circle(rad//3,90)
    turtle.seth(-45)
    draw(100)
    a.end_fill()
    tts = gtts.gTTS("oval",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class pentagon(shape):
    a.fillcolor('violet')
    a.begin_fill()
    for i in range(5):
       a.left(72)
       a.forward(100)
    a.end_fill()
    tts = gtts.gTTS("pentagon",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class kite(shape):
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
    tts = gtts.gTTS("kite",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class hexagon(shape):
    a.fillcolor('white')
    a.begin_fill()
    for i in range(6):
       a.forward(90)
       a.left(300)
    a.end_fill()
    tts = gtts.gTTS("hexagon",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class heart(shape):
    a.fillcolor('pink')
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
    tts = gtts.gTTS("heart",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class heptagon(shape):
    a.fillcolor('lime')
    a.begin_fill()
    for i in range(7):
       a.right(51)
       a.forward(100)
    a.end_fill()
    tts = gtts.gTTS("heptagon",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class line(shape):
    a.fillcolor('silver')
    a.begin_fill()
    a.forward(300)
    a.left(180)
    a.end_fill()
    tts = gtts.gTTS("line",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class octagon(shape):
    a.fillcolor('sea green')
    a.begin_fill()
    for i in range(8):
       a.right(45)
       a.forward(100)
    a.end_fill()
    tts = gtts.gTTS("octagon",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

    
# Objects
star = shape()

circle = shape()

square = shape()

triangle = shape()

rectangle = shape()

oval = shape()


heart = shape()

kite = shape()

hexagon = shape()

heptagon = shape()

octagon = shape()

pentagon = shape()

line = shape()


turtle.done()
                 
##FORMAT:
b = input("Enter shape")
if (b == star):
    print(star.shape)
elif (b == circle):
    print(circle.shape)
elif (b == square):
    print(square.shape)
elif (b == triangle):
    print(triangle.shape)
elif (b == rectangle):
    print(rectangle.shape)
elif (b == oval):
    print(oval.shape)
elif (b == pentagon):
    print(pentagon.shape)
elif (b == kite):
    print(kite.shape)
elif (b == hexagon):
    print(hexagon.shape)
elif (b == heart):
    print(heart.shape)
elif (b == heptagon):
    print(heptagon.shape)
elif (b == line):
    print(line.shape)
elif (b == octagon):
    print(octagon.shape)
else:
    print("Shape not found")



