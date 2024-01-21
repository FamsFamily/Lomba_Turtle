import turtle
import random
import time

t = turtle.Turtle()
s = turtle.Screen()
s.title("Lomba Turtle")
t.up()
t.goto(-280, 210)
t.down()
t.speed(0)
turtle.colormode(255)

# arena balapan
t.right(90)
for i in range(21):
    t.write(i)
    t.forward(360)
    t.up()
    t.goto(-280+20*(i+1),210)
    t.down()
t.left(90)
t.forward(10)
t.goto(-280,210)
t.up()
t.goto(150,210)
t.stamp()

rd = 0
be = 0
yw = 0
gn = 0
oe = 0
pe = 0
pk = 0
we = 0
bk = 0
bn = 0
cm = 0
gy = 0
v1 = [rd, be, yw, gn, oe, pe, pk, we, bk, bn, cm, gy]
color1 = ["red", "dodgerblue", "yellow", "limegreen", "darkorange", "darkorchid", "hotpink", "white", "black", "saddlebrown", "navajowhite", "gray"]
at = int(input("Berapa jumlah turtle yang akan berlomba? (2-12): "))

for a in range(at):
    v1[a] = turtle.Turtle()
    v1[a].shape("turtle")
    v1[a].color(color1[a])
    v1[a].pencolor("black")
    v1[a].up()
    v1[a].goto(-290,195-30*a)

jumlah_pn = random.randint(1,20)
pn = turtle.Turtle()
pn.left(90)
pn.shape("turtle")
pn.up()
pn.speed(1)
for i in range(jumlah_pn):
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    pn.color(r, b, g)
    pn.pencolor("black")
    pn.goto(-290+20*(i+1),-170)
    pn.stamp()

color2 = ["Merah!", "Biru!", "Kuning!", "Hijau!", "Jingga!", "Ungu!", "Merah Muda!", "Putih!", "Hitam!", "Cokelat!", "Krem!", "Abu-abu!"]
v2 = []
for aa in range(at):
    v2.append(color2[aa])
print("Turtle yang akan berlomba: ",v2)
win = input("Menurutmu, Turtle mana yang akan menang: ")
t.goto(150,170)
t.write("Menurutmu pemenangnya")
t.goto(150,155)
t.write("adalah Turtle "+win)

x_d = 0
x_b = 0
x_y = 0
x_g = 0
x_o = 0
x_p = 0
x_k = 0
x_h = 0
x_l = 0
x_w = 0
x_c = 0
x_e = 0
v3 = [x_d, x_b, x_y, x_g, x_o, x_p, x_k, x_h, x_l, x_w, x_c, x_e]

while True:

    FPS = 10*at

    for aaa in range(at):
        maju = random.randint(1,5)
        v1[aaa].forward(maju)
        v3[aaa] += maju

    for aaaa in range(at):
        if v3[aaaa] >= 420:
            winfix = color2[aaaa]
            t.goto(150,125)
            t.write("Pemenangnya adalah...")
            time.sleep(1)
            t.goto(150,110)
            t.write("Turtle "+winfix)
            t.goto(150,80)
            if win == winfix:
                t.write("Tebakanmu Benar!")
            else:
                t.write("Tebakanmu Salah!")
            turtle.done()
