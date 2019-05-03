from tkinter import *
# from microwave import *

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
#un champ pour afficher le temps restant
texte = StringVar()
lbl_aff_temps = Label(fenetre, text="100", fg="green", bg="white", font="times 80 bold")
lbl_aff_temps_fen = canvas.create_window(700, 110, window=lbl_aff_temps)

#un bouton + pour augmenter le temps
bt_tempsP = Button(fenetre, text="+", width=7)
bt_tempsP_fen = canvas.create_window(650, 250, window=bt_tempsP)
#un bouton - pour diminuer le temps
bt_tempsM = Button(fenetre, text="-", width=7)
bt_tempsM_fen = canvas.create_window(750, 250, window=bt_tempsM)
#un bouton start pour lancer la cuisson

bt_start = Button(fenetre, text="Start", width=20)
bt_start_fen = canvas.create_window(700, 330, window=bt_start)

fenetre.mainloop()
