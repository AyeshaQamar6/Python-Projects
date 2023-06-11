import turtle
y = turtle
a = turtle.Turtle()
turtle.bgcolor("cyan")

# Class----------------------------------------------------------------------------
class shape():
    def details(self):
        return f"right is (self.right), left is (self.left), forward is (self.forward), backward is (self.backward)"
    
##-------------------CIRCLE--------------------------------------------------------
    def circle(details):
        c.fillcolor('red')
        c.begin_fill()
        l = 50
        c.circle(l)
        c.end_fill()

##-------------------SQUARE------------------------------------------------------
    def square(details):
        square.right(90)
        square.forward(100)
        for i in range(3):
            square.right(90)
            square.forward(100)

##-----------------TRIANGLE------------------------------------------------------
    def triangle(details):
        triangle.right(120)
        triangle.backward(100)
        for i in range(2):
            triangle.right(120)
            triangle.backward(100)

##-----------------RECTANGLE-----------------------------------------------------
    def rectangle(details):
        for i in range(2):
            rectangle.right(90)
            rectangle.forward(100)
            rectangle.right(90)
            rectangle.forward(160)

# Objects--------------------------------------------------------------------------
circle = shape()
c = turtle.Turtle()

square = shape()
square = turtle.Turtle()

triangle = shape()
triangle = turtle.Turtle()

rectangle = shape()
rectangle = turtle.Turtle()

#---------------------FORMAT------------------------------------------------
b = input("shape?")
if (b == square):
    print(square.details)
elif (b == circle):
    print(circle.details)
elif (b == triangle):
    print(triangle.details)
elif (b == rectangle):
    print(rectangle.details)
else:s
print("Shape not found")

turtle.done()
