from tk import canvas, root


def head():
    canvas.create_oval(79, 59, 120, 80, width=4, fill="white")
    root.update()


def body():
    canvas.create_line(100, 80, 100, 200, width=4)
    root.update()


def armR():
    canvas.create_line(100, 80, 145, 100, width=4)
    root.update()


def armL():
    canvas.create_line(100, 80, 45, 100, width=4)
    root.update()


def footL():
    canvas.create_line(100, 200, 45, 300, width=4)
    root.update()


def footR():
    canvas.create_line(100, 200, 145, 300, width=4)
    root.update()
