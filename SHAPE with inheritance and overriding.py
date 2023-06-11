import turtle
import os
import gtts
from playsound import playsound

y = turtle
a = turtle.Turtle
turtle.bgcolor("cyan")

star = a
##INHERITANCE-----------------------------------------------------------------------------
##OVERRIDING------------------------------------------------------------------------------
##ENCAPSULATION---------------------------------------------------------------------------
##-------------------------CLASS
class shape:
    def details(self):
        return f"right is (self.right), left is (self.left), forward is (self.forward), backward is (self.backward)"

class star(shape):
    star.fillcolor('yellow')
    star.begin_fill()
    star.right(105)
    star.backward(100)
    for i in range(4):
        star.right(144)
        star.backward(100)
    star.end_fill()
    tts = gtts.gTTS("star",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')

class circle(shape):
    c.fillcolor('purple')
    c.begin_fill()
    l = 50
    c.circle(l)
    c.end_fill()
    tts = gtts.gTTS("circle",lang="en")
    tts.save("hello.mp3")
    os.startfile('hello.mp3')



##----------------------OBJECTS
a = star()
b = circle()
