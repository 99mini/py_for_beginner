import turtle as t

def draw(n):
    angle = 180*(1-2/n)
    for i in range(n):
        t.forward(100)
        t.right(180 - angle)
    while True:
        pass
    
draw(3)