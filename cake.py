import turtle

name = input("Enter Name")
age = int(input("Enter Age"))

bg = turtle.Screen()
turtle.title("Happy Birthday "+name)
bg.bgcolor("pink")

#ທາດເຄັກ-----------------------------------------

turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(260)

#ເຄັກ--------------------------------------------

def draw_rectangle(x, y, width, height):
    turtle.color("floralwhite")
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

draw_rectangle(-120, -120, 200, 95)
draw_rectangle(-95, -30, 150, 95)


#ທຽນ--------------------------------------------

def draw_candle(x, y, z, color, length, direction):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.width(5)
    turtle.setheading(direction)
    turtle.pendown()
    turtle.forward(length)

    turtle.penup()
    turtle.goto(x+3,z)
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(3) 
    turtle.end_fill()

   

draw_candle(-80, 67, 98, "lightcoral", 25, 90)
draw_candle(40, 67, 98, "lightcoral", 25, 90)
draw_candle(-50, 67, 104, "lightcoral", 30, 90)
draw_candle(10, 67, 104, "lightcoral", 30, 90)
draw_candle(-20, 67, 108, "lightcoral", 35, 90)




#ຊະຕໍ່ເບີ້ລີ້---------------------------------------------

def draw_strawberry(x, y, z):

    turtle.fillcolor("#FB2943")

    for i in range(z):
        turtle.penup()
        turtle.goto(x,y)
        turtle.begin_fill()
        turtle.circle(5) 
        turtle.end_fill()
        x += 28

draw_strawberry(-112,-27,8)
draw_strawberry(-85,70,6)


#Happy Birthday message----------------------------

def write_text(text, position, font_name, font_size, font_style):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    turtle.write(text, font=(font_name, font_size, font_style))


write_text("Happy Birthday!"+name, (-150, 170), 'Lovea', 30, 'italic')
write_text(age, (-50, -250), 'Lovea', 50, 'italic')



turtle.hideturtle()
turtle.done()