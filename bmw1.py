import tkinter as tk
import os

window = tk.Tk()
window.geometry("800x500")
window.title("bemarikuskin unelma")

jonne = 1
jonne2 = "tää on magee kaare t. bemari pete"
def check():
    global jonne2
    if jonne == 1:
        jonne2 = "tää on magee kaara t. bemari pete"
        bmw2.pack()
    else:
        if jonne == 2:
            jonne2 = "tää kaara ei oo tien vaara"
            bmw2.pack()
        else:
            if jonne == 3:
                jonne2 = "jos kaara on vaara niin ei tie sitä kaada"
                bmw2.pack()
            else:
                pass

            
def elamys1():
    global jonne
    if jonne == 1:
        jonne = 2
    else:
        if jonne == 2:
            jonne = 3
        else:
            if jonne == 3:
                jonne = 1

            
    check()
    

bmw = tk.Label(window, text="bmw autovalikoima")
bmw2 = tk.Label(window, text=jonne2)

buttonxd = tk.Button(window, text="lisää bmw elämyksiä", command=elamys1)
basejuttu = os.path.dirname(__file__)
imgpth = os.path.join(basejuttu, 'timo.png')
jonneasia = tk.Canvas(window, width = 1500, height = 100)

jonneasia.pack()
kuva = tk.PhotoImage(file=imgpth)
jou = jonneasia.create_image(20,20, image=kuva)

buttonxd.pack()

bmw.pack()
bmw2.pack()
window.mainloop()