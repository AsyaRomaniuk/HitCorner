from tkinter import Tk, Canvas, BOTH
from random import randint, shuffle

def move_figure(figure, x_px, y_px):
        canv.move(figure, x_px, y_px)
        hit_border(canv.coords(figure)[:2], canv.coords(figure)[2:])
        if moving: # can be deleted
            root.after(time, lambda: move_figure(rect, step_px*x_s, step_px*y_s))


def hit_border(pos1, pos2):
    global x_s, y_s, moving # can be deleted
    if pos1[0] <= 0:
        x_s = 1
        if pos1[1] <= 0 or pos2[1] >= height: # can be deleted
            moving = False # can be deleted
    elif pos2[0] >= width:
        x_s = -1
        if pos1[1] <= 0 or pos2[1] >= height: # can be deleted
            moving = False # can be deleted
    if pos1[1] <= 0:
        y_s = 1
        if pos1[0] <= 0 or pos2[0] >= width: # can be deleted
            moving = False # can be deleted
    elif pos2[1] >= height:
        y_s = -1        
        if pos1[0] <= 0 or pos2[0] >= width: # can be deleted
            moving = False # can be deleted
    
root = Tk()
width, height = 800, 400
root.geometry(f"{width}x{height}")
root.resizable(False, False)
canv = Canvas(root, bg="silver")
moving = True # can be deleted
figure_xsize, figure_ysize = 100, 100
step_px = 2
time = 30
s = [-1, 1]
shuffle(s)
x_s = s[0]
shuffle(s)
y_s = s[0]
xcoord = randint(figure_xsize/2, width-1-figure_xsize/2)
ycoord = randint(figure_ysize/2, height-1-figure_ysize/2)
rect = canv.create_rectangle(xcoord+figure_xsize/2, ycoord+figure_ysize/2,
                             xcoord-figure_xsize/2, ycoord-figure_ysize/2,
                             fill="blue")
root.after(time, lambda: move_figure(rect, step_px*x_s, step_px*y_s))
canv.pack(fill=BOTH, expand=True)
root.mainloop()
