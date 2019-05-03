from tkinter import *

#bug passage dans le négatif

def plus():
  temps_aff.set(int(temps_aff.get())+5)

def moins():
  if int(temps_aff.get()) > 0 :
    temps_aff.set(int(temps_aff.get())-5)

def start():
  temps_aff.set(temps)







fenetre = Tk()
fenetre.geometry("800x400")
fenetre.title("Micro-onde")
fenetre["bg"] = "black"

canvas = Canvas(fenetre, width=780, height=380, borderwidth=10, background='black')
canvas.create_rectangle(100,80, 480, 300, fill="grey")
canvas.create_line(580,10, 580, 380, fill="white")
canvas.create_line(600,10, 600, 380, fill="white")
canvas.pack()

# - - - - -
temps_aff = StringVar()
temps_aff.set("0")

#un champ pour afficher le temps restant
lbl_aff_temps = Label(fenetre, textvariable=temps_aff, fg="green", bg="white", font="times 80 bold")
lbl_aff_temps_fen = canvas.create_window(700, 110, window=lbl_aff_temps)

#un bouton + pour augmenter le temps
bt_tempsP = Button(fenetre, text="+", width=7, command=plus)
bt_tempsP_fen = canvas.create_window(650, 250, window=bt_tempsP)
#un bouton - pour diminuer le temps
bt_tempsM = Button(fenetre, text="-", width=7, command=moins)
bt_tempsM_fen = canvas.create_window(750, 250, window=bt_tempsM)
#un bouton start pour lancer la cuisson

bt_start = Button(fenetre, text="Start", width=20, command=start)
bt_start_fen = canvas.create_window(700, 330, window=bt_start)

fenetre.mainloop()
