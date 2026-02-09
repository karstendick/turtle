from ast import main
import turtle as t
t.speed(1) # 1 to 10

# print(t.heading())
# t.forward(100)

# drawing a square
# for i in range(4):
#     t.right(90)
#     t.forward(150)


#draw a bunch of squares
# for i in range(1000):
#     t.right(90)
#     t.forward(1+i)

# hexagon with spikes
# for i in range(6):
#     t.forward(100)
#     t.left(60)
#     t.forward(100)
#     t.right(180)
#     t.forward(100)
#     t.left(60)
# t.mainloop()
# a
# for i in range(3):
#     t.forward(150)
#     t.right(90)
# t.forward(25)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(25)

#t.mainloop()

# t.right(90)
# t.forward(100)
# t.pu()
# t.forward(50)
# t.pd()
# t.forward(100)

# a 5-sided shape called a pentagon
# for i in range(5):
#     t.forward(100)
#     t.right(72)

# a pentagon rotated so it's pointing up
for i in range(5):
    t.left(72)
    t.forward(100)

t.mainloop()