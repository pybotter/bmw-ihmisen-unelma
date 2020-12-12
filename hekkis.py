
import tkinter as tk
from time import sleep
import random
sleep(1)
colors = ['red', 'blue', 'green']

window = tk.Tk()

window.geometry("800x500")

window.title("BMW PELI")

wd = tk.Label(window, text="OSAATKO SINÄ PELATA BMW PELIÄ?")
def jonne():
    print("es")


def gedit():
    global joujou

    try:
        joujou = perustele.get()
    except:
        pass

    wt = tk.Tk()
    wt.title("ok")
    wi = tk.Label(wt, text="ok")
    wn = tk.Label(wt, text=joujou)
    
    win = tk.Canvas(wt, height="50", width="80")
    win.pack()
    wi.pack()
    wn.pack()
    
    wt.mainloop()

w = tk.Radiobutton(window, text="VAIKEE")
b = tk.Radiobutton(window, text="HAIKEE")
c = tk.Canvas(window, height="500", width="800", bg=random.choice(colors))
def aloita():
    global c
    global bma
    global pw
    global perustele
    global getfile
    
    try:
        bma.pack_forget()
        c.pack_forget()
        pw.pack_forget()
        perustele.pack_forget()
        getfile.pack_forget()
    except:
        pass
    c = tk.Canvas(window, height="500", width="800", bg=random.choice(colors))
    pw = tk.Label(window, text="perustele:")
    perustele = tk.Entry(window)
    perustele.pack()

    getfile = tk.Button(window, text="JATKA", command=gedit)
    
    pw.pack()
    bma = tk.Checkbutton(window, text="bmw on hyvä", command=jonne)
    bma.pack()
    getfile.pack()
    c.pack()
    


wp = tk.Label(window, text="VAIKEUSTASO:")
wb = tk.Button(window, text="ALOITA PELI", command=aloita)

wp.pack()
wd.pack()
w.pack()
b.pack()
wb.pack()
window.mainloop()
sleep(1)