import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.title("Lomba Turtle")
t.up()
t.goto(-100,100)
t.down()
t.speed(0)
turtle.colormode(255)

# arena balapan
t.right(90)
for i in range(15):
    t.write(i)
    t.forward(250)
    t.up()
    t.goto(-100+20*(i+1),100)
    t.down()
t.goto(-100,100)
t.goto(210,100)
t.left(90)

r = turtle.Turtle()
r.shape("turtle")
r.color("red")
r.up()
r.goto(-120,70)


b = turtle.Turtle()
b.shape("turtle")
b.color("blue")
b.up()
b.goto(-120,40)

y = turtle.Turtle()
y.shape("turtle")
y.color("yellow")
y.up()
y.goto(-120,10)

x_r = 0
x_b = 0
x_y = 0

jumlah_p = random.randint(1,14)
for i in range(jumlah_p):
    rr = random.randint(0,255)
    rb = random.randint(0,255)
    rg = random.randint(0,255)
    p = turtle.Turtle()
    p.left(90)
    p.shape("turtle")
    p.color(rr, rb, rg)
    p.up()
    p.goto(-110+20*(i+1),-170)

win = input ("Turtle mana yang akan menang:")
text = turtle.Turtle()
text.up()
text.goto(-120,120)
text.write("Menurut Anda pemenangnya adalah " + win)

while True:
    maju_r = random.randint(1,5)
    maju_b = random.randint(1,5)
    maju_y = random.randint(1,5)
    
    r.forward(maju_r)
    b.forward(maju_b)
    y.forward(maju_y)
    
    x_r = x_r + maju_r
    x_b = x_r + maju_b
    x_y = x_r + maju_y

    if x_r >= 300:
        t.write("Pemenangnya Turtle Merah!")
        break
    elif x_b >= 300:
        t.write("Pemenangnya Turtle Biru!")
        break
    elif x_y >= 300:
        t.write("Pemenangnya Turtle Kuning!")
        break
turtle.done()
