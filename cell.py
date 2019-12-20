from tk import canvas


def cell():
    y=0
    while y < 600:
        x =0
        while x < 600:
            canvas.create_rectangle(x, y, x+33, y+27, fill="white", outline="blue")
            x = x+33
        y = y+27