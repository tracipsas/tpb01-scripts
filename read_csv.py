#!/usr/bin/env python3

import csv
import datetime

with open("data.csv", "r", encoding="utf-8") as fichier_csv:
    iterateur_lignes = csv.reader(
        fichier_csv, delimiter=",", quotechar="\"")
    next(iterateur_lignes)  # pour ne pas lire le header
    for ligne in iterateur_lignes:
        if not ligne:
            continue
        sens, numero, nom, chaîne_date = ligne
        # ligne[0] va dans la variable sens, ligne[1] dans numero...
        if sens == "R":
            sens = "<-"
        else:  # si sens == "S"
            sens = "->"
        nom, prenom = nom.split(", ")
        nom = "{} {}".format(prenom, nom.upper())
        objet_datetime = datetime.datetime.strptime(
            chaîne_date, "%d/%m/%Y %H:%M:%S")
        chaîne_date = objet_datetime.strftime("le %A %d %B %Y à %Hh%M")
        print("Appel : moi {} {} ({}) {}"
              .format(sens, nom, numero, chaîne_date))
