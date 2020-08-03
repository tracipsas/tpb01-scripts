from tkinter import *

# On créé la fenêtre principale, et on choisit son titre
master = Tk()
master.title = "Titre"

# On ajoute un label (affichage d'une ligne de texte, en lecture seule)
label = Label(master, text="Hello f0rensics!")
label.grid(row=0, column=0)

# On lance l'interface graphique
# Cette commande bloque l'exécution du code Python situé en dessous
master.mainloop()
