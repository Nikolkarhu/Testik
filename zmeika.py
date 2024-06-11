from tkinter import*
from PIL import Image, ImageTk
import PIL
from random import randrange, random
import random
import time
colors = ["red", "orange", "yellow", "green", "blue", "cyan", "blue", "purple"]
height = 500
width = 500
Sneakers = 10
tk = Tk()
sneakersni_list = []
sneakersize = 2

turemnoe_foto = Image.open("foto_cannibala_sneakersa.png")
turemnoe_foto = turemnoe_foto.resize((10,10), Image.NEAREST)
turemnoe_foto_v_turme = ImageTk.PhotoImage(turemnoe_foto)

BANus_list = []
BANus_siz = 3

best_cells_donat_x = width / Sneakers
best_cells_donat_y = height / Sneakers

x = 25
y = 25

x_Ctrl = 0
y_Ctrl = 0

tk.resizable(0,0)
tk.title("Sneakers advanture RTX 3000000000060 ONLY FOR DONAT 300 bucks")
canvas = Canvas(tk,width= width, height= height)
canvas.photo = turemnoe_foto
canvas.pack()
def bonusi_v_ataku():
    global turemnoe_foto_v_turme
    for i in range(BANus_siz):
        Bx = randrange(best_cells_donat_x)
        By = randrange(best_cells_donat_y)
        # item = canvas.create_oval(Bx * Sneakers, By * Sneakers, Bx * Sneakers + Sneakers, By * Sneakers + Sneakers, fill="darkred")
        item = canvas.create_image(Bx * Sneakers, By * Sneakers, anchor = NW, image = turemnoe_foto_v_turme)
        BANus_list.append([Bx, By, item])
def sneakers_cannibalism():
    global sneakersize
    for i in range(len(BANus_list)):
        if BANus_list[i][0] == x and BANus_list[i][1] == y:
            sneakersize += 1
            canvas.delete(BANus_list[i][2])
            bonusi_v_ataku()
def ugolovka():
    tochno_ne_ono = random.randint(0, 255)
    Mozna_robaxov_pj = random.randint(0, 255)
    net_skushaj_ti_omlet = random.randint(0, 255)
    return f'#{tochno_ne_ono:02x}{Mozna_robaxov_pj:02x}{net_skushaj_ti_omlet:02x}'
def update ():
    if len(sneakersni_list) >= sneakersize:
        item = sneakersni_list.pop(0)
        canvas.delete(item[2])
def sneaker_items(canvas, x, y):
    global sneakersni_list
    item = canvas.create_rectangle(x * Sneakers, y * Sneakers, x * Sneakers + Sneakers, y * Sneakers + Sneakers, fill = ugolovka)
    sneakersni_list.append([x, y, item])
def prestupnik_poiman(sneaker_x, sneaker_y):
    if x > best_cells_donat_x -1 or y > best_cells_donat_y -1 or x < 0 or y < 0:
        exit()
    if not (x_Ctrl == 0 and y_Ctrl == 0):
        for i in range(len(sneakersni_list)):
            if sneakersni_list[i][0] == sneaker_x and sneakersni_list[i][1] == sneaker_y:
                exit()
def move(event):
    global x_Ctrl, y_Ctrl, x, y
    if event.keysym == "Left":
        x_Ctrl = -1
        y_Ctrl = 0
    elif event.keysym == "Right":
        x_Ctrl = 1
        y_Ctrl = 0
    elif event.keysym == "Up":
        x_Ctrl = 0
        y_Ctrl = 1
    elif event.keysym == "Down":
        x_Ctrl = 0
        y_Ctrl = -1
    update()
    x += x_Ctrl
    y += y_Ctrl
sneaker_items(canvas, x, y)
bonusi_v_ataku()
canvas.bind_all("KeyPress-Left", move)
canvas.bind_all("KeyPress-Right", move)
canvas.bind_all("KeyPress-Up", move)
canvas.bind_all("KeyPress-Down", move)

while True:
    time.sleep(0.1)
    prestupnik_poiman(x + x_Ctrl, y + y_Ctrl)
    update()
    sneakers_cannibalism()
    x += x_Ctrl
    y += y_Ctrl
    sneaker_items(canvas, x, y)
    tk.update()
# tk.mainloop()