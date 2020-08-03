from tkinter import *
import hashlib

master = Tk()
master.title = "MD5 Calculator"
master.width = 200

text_var = StringVar()  # objet spécial Tkinter pour contenir
                        # le texte tapé par l'utilisateur
entry = Entry(master, textvariable=text_var)
entry.grid(row=0, column=0)

button = Button(text="Calculer MD5")
button.grid(row=1, column=0)

label = Label(text="< Cliquez sur 'Calculer MD5' >")
label.grid(row=2, column=0)

def compute_md5(*args):
    text = text_var.get()
    text_binary = text.encode("utf-8")
    md5 = hashlib.md5(text_binary).hexdigest()
    label.configure(text=md5)

button.configure(command=compute_md5)

master.mainloop()
