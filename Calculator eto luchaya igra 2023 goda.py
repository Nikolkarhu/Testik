from tkinter import*
import math
window = Tk()
calculate_RTX = ''
pervoe_slogaemoe = 0
vtoroe_slogaemoe = 0
davai_plus = False
davai_minus = False
davai_delenie = False
davai_umnozenie = False
davai_stepen = False
window.title('CALCULATOR RTX REMASTERED 13 DELUXE VERSION')
window.geometry('500x500')
window.resizable(height=False, width=False)
frame = Frame(window, bg='#00BFFF')
frame.place(relheight=0.98, relwidth=0.98, relx=0.01, rely=0.01)
label = Label(frame, text='0', font=100)
label.place(x=1, y=1, width=488)
buttons = []
xb = 50
yb = 300
for i in range(10):
        buttons.append(Button(frame, text=i, font=50, bg="#B0E0E6", relief="groove", activebackground= '#B0E0E6', activeforeground='#B0E0E6'))
        if i == 0:
            buttons[0].place (x=175, y=425, width = 100, height=60)
        else:
            buttons [i].place(x=xb, y=yb, width=100, height=100)
            xb += 125
            if xb > 300:
                yb -= 125
                xb = 50
ravno_ravno = Button(frame, text= "=", font=50)
ravno_ravno.place(x=300, y=425, width=100, height=50)
def button(pervoe_slogaemoe):
    global calculate_RTX
    pervoe_slogaemoe = str(pervoe_slogaemoe)
    calculate_RTX += pervoe_slogaemoe
    label.config (text = calculate_RTX)
for i in range(10):
    buttons[i].config(command = lambda i = i :button (i))
def ravno():
    global calculate_RTX, vtoroe_slogaemoe, davai_plus, davai_minus, davai_umnozenie, davai_delenie
    vtoroe_slogaemoe = calculate_RTX
    vtoroe_slogaemoe = float(vtoroe_slogaemoe)
    if davai_plus:
        calculate_RTX = pervoe_slogaemoe + vtoroe_slogaemoe
        label.config (text = calculate_RTX)
        davai_plus = False
    elif davai_minus:
        calculate_RTX = pervoe_slogaemoe - vtoroe_slogaemoe
        label.config (text = calculate_RTX)
        davai_minus = False
    elif davai_delenie:
        if vtoroe_slogaemoe == 0:
            label.config (text = "Ты что? Прогуливал уроки по математике!? Позор!!!")
            return
        else:
            calculate_RTX = pervoe_slogaemoe / vtoroe_slogaemoe
            label.config (text = calculate_RTX)
            davai_delenie = False
    elif davai_umnozenie:
        calculate_RTX = pervoe_slogaemoe * vtoroe_slogaemoe
        label.config (text = calculate_RTX)
        davai_umnozenie = False
    # elif davai_stepen:



def kakaya_Stepen(N):
    global pervoe_slogaemoe, calculate_RTX
    pervoe_slogaemoe = float(calculate_RTX)
    pervoe_slogaemoe = math.pow(pervoe_slogaemoe,N)
    calculate_RTX = str(pervoe_slogaemoe)
    label.config(text=calculate_RTX) 
def OVERWRITE():
    global pervoe_slogaemoe, vtoroe_slogaemoe, calculate_RTX
    calculate_RTX = ""
    pervoe_slogaemoe = 0
    vtoroe_slogaemoe = 0
    label.config(text=calculate_RTX)
def minuplus(mode):
    global calculate_RTX, pervoe_slogaemoe, davai_plus, davai_minus, davai_delenie, davai_umnozenie
    if calculate_RTX:
        pervoe_slogaemoe = float(calculate_RTX)
        calculate_RTX = ""
        label.config(text=calculate_RTX)
        if mode == "+":
            davai_plus = True
        elif mode == "-":
            davai_minus = True
        elif mode == "/":
            davai_delenie = True
        elif mode == "*":
            davai_umnozenie = True
def kakoy_koren():
    global pervoe_slogaemoe, calculate_RTX
    pervoe_slogaemoe = float(calculate_RTX)
    pervoe_slogaemoe = math.sqrt(pervoe_slogaemoe)
    calculate_RTX = str(pervoe_slogaemoe)
    label.config(text=calculate_RTX)
plys = Button(frame, text= "+", font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command=lambda:minuplus ("+"))
plys.place(x=400, y=175, width=100, height=50)
minys = Button(frame, text= "-", font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command=lambda:minuplus ("-"))
minys.place(x=400, y=300, width=100, height=50)
delenie = Button(frame, text = '/', font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command=lambda:minuplus ('/'))
delenie.place(x=400, y=350, width=100, height=50)
umnozenie = Button(frame, text = "*", font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command=lambda:minuplus ("*"))
umnozenie.place(x=400, y=225, width=100, height=50)
stepen = Button(frame, text='x2', font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command=lambda:kakaya_Stepen (2))
stepen.place(x=400, y=100,width=100, height=50)
stepen3 = Button(frame, text='x3', font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command= lambda:kakaya_Stepen (3))
stepen3.place(x=400, y=50, width=100, height=50)
stepen4 = Button(frame, text='x4', font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command= lambda:kakaya_Stepen (4))
stepen4.place(x=0, y=70, width=50, height=50)
koren = Button(frame, text='sq', font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command= kakoy_koren)
koren.place(x=400, y=425, width=50, height=50)
ravno_ravno = Button(frame, text= "=", font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command=ravno) 
ravno_ravno.place(x=300, y=425, width=100, height=50)
clear = Button(frame, text= "C", font=50, bg='#B0E0E6', activebackground= '#B0E0E6', activeforeground='#B0E0E6', relief="groove", command=OVERWRITE)
clear.place(x=50,y=425, width=100, height=50)
window.mainloop()
