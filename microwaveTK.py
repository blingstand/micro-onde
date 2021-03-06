import tkinter
from time import sleep
#changer couleur dans micro-onde

def plus():
  int(temps_aff.get())
  temps_aff.set(int(temps_aff.get())+5)

def moins():
  if int(temps_aff.get()) > 0 :
    temps_aff.set(int(temps_aff.get())-5)

def change_couleur(objet_a_detruire, couleur):
  canvas.delete(objet_a_detruire)
  rectangle = canvas.create_rectangle(100,80, 480, 300, fill=couleur)

def start():
  temps = int(temps_aff.get())
  change_couleur(rectangle, "#cca300")
  for i in range(temps, 0, -1):
    temps_aff.set(i)
    fenetre.update()
    print("Cuisson en cours ... ({})".format(i))
    sleep(1)
  if i ==  1 :
    change_couleur(rectangle, "grey")
    for repeat in range(3):
      temps_aff.set("FIN")
      fenetre.update()
      sleep(0.5)
      temps_aff.set("")
      fenetre.update()
      sleep(0.5)
    temps_aff.set(0)
    print("Cuisson terminée")

fenetre = tkinter.Tk()
fenetre.geometry("800x400")
fenetre.title("Micro-onde")
fenetre["bg"] = "black"

canvas = tkinter.Canvas(fenetre, width=780, height=380, borderwidth=10, background='black')
rectangle = canvas.create_rectangle(100,80, 480, 300, fill="grey")
canvas.create_line(580,10, 580, 380, fill="white")
canvas.create_line(600,10, 600, 380, fill="white")
canvas.pack()

# - - - - -
temps_aff = tkinter.StringVar()
temps_aff.set("0")

#un champ pour afficher le temps restant
lbl_aff_temps = tkinter.Label(fenetre, textvariable=temps_aff, fg="green", bg="black", font="times 80 bold")
lbl_aff_temps_fen = canvas.create_window(700, 110, window=lbl_aff_temps)

#un bouton + pour augmenter le temps
bt_tempsP = tkinter.Button(fenetre, text="+", width=7, command=plus)
bt_tempsP_fen = canvas.create_window(650, 250, window=bt_tempsP)
#un bouton - pour diminuer le temps
bt_tempsM = tkinter.Button(fenetre, text="-", width=7, command=moins)
bt_tempsM_fen = canvas.create_window(750, 250, window=bt_tempsM)
#un bouton start pour lancer la cuisson

bt_start = tkinter.Button(fenetre, text="Start", width=20, command=start)
bt_start_fen = canvas.create_window(700, 330, window=bt_start)

fenetre.mainloop()
