import turtle

bob = turtle.Turtle()

# bob.color("red", "cyan")
# for i in range(5):
#     bob.forward(10)
#     bob.left(90)
#     bob.forward(10)
#     bob.right(90)
#     bob.forward(10)
#     bob.right(90)
#     bob.forward(10)
#     bob.left(90)
# bob.forward(100)

l = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
b = True

def carre():
    for i in range(4):
        bob.forward(50)
        bob.left(90)
def carre_plein(b, f):
    bob.color(b, f)
    bob.begin_fill()
    for i in range(4):
        bob.forward(50)
        bob.left(90)
    bob.end_fill()


def my_circle():
    r = 15
    bob.pendown()
    bob.right(90)
    bob.circle(r, 360)
    bob.up()
    bob.left(90)
    bob.forward(2*r)

def branche(r):
    bob.forward(r)
    bob.right(90)
    bob.circle(r/10, 360)
    bob.up()
    bob.home()
    bob.pendown()

def spirale(n):
    c = 360
    i = 1
    a = 360/n
    while(i < n):
        branche(10*i)
        i += 1
        bob.left(a*i)

def etoile(n):
    c = 360
    i = 1
    a = 360/n
    while(i <= n):
        branche(100)
        bob.right(a*i)
        i += 1
        # print(a*i)
bob.speed(10)
# i = 20
# a = 360//i
# for j in range(a):
#     bob.setheading(i*j)
#     bob.fd(100)
#     print(i)
# bob.goto(10, 20)
# bob.setpos(20, 30)
# bob.setposition(30, 40)
# bob.setx(20)


# bob.home()
# bob.begin_poly()
# bob.fd(100)
# bob.left(20)
# bob.fd(30)
# bob.left(60)
# bob.fd(50)
# bob.end_poly()
# bob.get_poly()
# register_shape("myFavouriteShape",p)

# bob.speed(3)
bob.color('cyan', 'red')
bob.begin_fill()
spirale(20)
bob.end_fill()
#
# etoile(12)

# branche(100)
# for i in range(1,20,1):
#     print(i)
#     bob.circle(10*i,90)


    # bob.home()
    # bob.circle(-15, 450)
# for i in range(10):
#     my_circle()
# carre()
# carre_plain('red', 'yellow')
#
# bob.begin_fill()
# bob.color('light green', 'pink')
# for i in range(3):
#     carre()
#     bob.forward(40)
# bob.end_fill()
# for i in range(3):
#     carre_plein('red', 'yellow')
#     bob.forward(40)
# for j in range(4):
#     i = 0
#     while (i < 7):
#         if(b is True):
#             bob.pendown()
#             bob.pencolor(l[i])
#             b = not b
#             print(i)
#             i +=1
#         else:
#             b = not b
#             bob.penup()
#             print(i)
#
#         bob.forward(5)

# bob.begin_fill()
# bob.right(90)
# # bob.penup()
# bob.speed(1)
# bob.forward(100)
# bob.right(90)
# bob.forward(100)
# bob.right(90)
# bob.forward(100)
# bob.end_fill()
# bob.color("blue", "red")
# bob.begin_fill()
# bob.goto(-50,-50)
# bob.circle(200, 360)
# bob.end_fill()
# exitonclick()
# bob.reset()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()









turtle.done()
