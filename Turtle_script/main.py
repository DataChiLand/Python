import turtle as t

tod = t.Turtle()
# """Challenge 2 - Draw a Dashed Line"""
# for _ in range(15):
#     tod.forward(10)
#     tod.penup()
#     tod.forward(10)
#     tod.pendown()



colours = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tod.forward(100)
        tod.right(angle)

for shape_side_n in range(3, 11):
    tod.color(colours[shape_side_n % len(colours)])
    draw_shape(shape_side_n)
    tod.right(360 / shape_side_n)