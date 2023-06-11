import turtle
import os
import gtts
from playsound import playsound


y = turtle
a = turtle.Turtle()
turtle.bgcolor("cyan")
# Class----------------------------------------------------------------------------
class shape():
    pass
    def details(self):
        return f"right is (self.right), left is (self.left), forward is (self.forward), backward is (self.backward)"

# Objects--------------------------------------------------------------------------
star = shape()
star = a

circle = shape()
c = a

square = shape()
square = a

triangle = shape()
triangle = a

rectangle = shape()
rectangle = a

oval = shape()
oval = y

heart = shape()
heart = a

kite = shape()
kite = a

hexagon = shape()
hexagon = a

heptagon = shape()
heptagon = a

octagon = shape()
octagon = a

pentagon = shape()
pentagon = a

line = shape()
line = a


##------------------STAR-----------------------------------------------------------
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
##playsound("hello.mp3")
os.startfile('hello.mp3')

##-------------------CIRCLE--------------------------------------------------------
c.fillcolor('purple')
c.begin_fill()
l = 50
c.circle(l)
c.end_fill()
tts = gtts.gTTS("circle",lang="en")
tts.save("hello.mp3")
##playsound("hello.mp3")
os.startfile('hello.mp3')

##-------------------SQUARE------------------------------------------------------
square.fillcolor('light green')
square.begin_fill()
square.right(90)
square.forward(100)
for i in range(3):
   square.right(90)
   square.forward(100)
square.end_fill()
tts = gtts.gTTS("square",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')

##-----------------TRIANGLE------------------------------------------------------
triangle.fillcolor('red')
triangle.begin_fill()
triangle.right(120)
triangle.backward(100)
for i in range(2):
   triangle.right(120)
   triangle.backward(100)
triangle.end_fill()
tts = gtts.gTTS("triangle",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')

##-----------------RECTANGLE-----------------------------------------------------
rectangle.fillcolor('orange')
rectangle.begin_fill()
for i in range(2):
   rectangle.right(90)
   rectangle.forward(100)
   rectangle.right(90)
   rectangle.forward(160)
rectangle.end_fill()
tts = gtts.gTTS("rectangle",lang="en")
tts.save("hello.mp3")
##playsound("hello.mp3")
os.startfile('hello.mp3')

##-------------------------OVAL-------------------------------------------
oval.fillcolor('blue')
oval.begin_fill()
def draw(rad):
   for i in range(2):
       turtle.circle(rad,90)
       turtle.circle(rad//3,90)
turtle.seth(-45)
draw(100)
oval.end_fill()
tts = gtts.gTTS("oval",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')

##-----------------------HEPTAGON------------------------------------------------------
heptagon.fillcolor('lime')
heptagon.begin_fill()
for i in range(7):
   heptagon.right(51)
   heptagon.forward(100)
heptagon.end_fill()
tts = gtts.gTTS("heptagon",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')

##-----------------------HEART------------------------------------------------
heart.fillcolor('pink')
heart.begin_fill()
def curve():
   for i in range(200):
       heart.right(1)
       heart.forward(1)
def pen():
   heart.left(140)
   heart.forward(113)
   curve()
   heart.left(120)
   curve()
   heart.forward(112)
pen()
heart.end_fill()
tts = gtts.gTTS("heart",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')

##-------------------------OCTAGON--------------------------------------------
octagon.fillcolor('sea green')
octagon.begin_fill()
for i in range(8):
   octagon.right(45)
   octagon.forward(100)
octagon.end_fill()
tts = gtts.gTTS("octagon",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')

##-----------------------KITE------------------------------------------------
kite.fillcolor('brown')
kite.begin_fill()
kite.forward(40)
kite.left(120)
kite.forward(40)
kite.left(120)
kite.forward(40)
kite.right(100)
for i in range(4):
   kite.forward(150)
   kite.right(90)
kite.right(45)
kite.forward(210)
kite.right(45)
kite.end_fill()
tts = gtts.gTTS("kite",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')

##-------------------------HEXAGON------------------------------------------
hexagon.fillcolor('white')
hexagon.begin_fill()
for i in range(6):
   hexagon.forward(90)
   hexagon.left(300)
hexagon.end_fill()
tts = gtts.gTTS("hexagon",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')

##-------------------------PENTAGON----------------------------------------------------
pentagon.fillcolor('violet')
pentagon.begin_fill()
for i in range(5):
   pentagon.left(72)
   pentagon.forward(100)
pentagon.end_fill()
tts = gtts.gTTS("pentagon",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')

##------------------------LINE------------------------------------------------
line.fillcolor('silver')
line.begin_fill()
line.forward(300)
line.left(180)
line.end_fill()
tts = gtts.gTTS("line",lang="en")
tts.save("hello.mp3")
#playsound("hello.mp3")
os.startfile('hello.mp3')


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





turtle.done()
