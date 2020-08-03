def aff_lignes(liste_lignes):
    for num_ligne, ligne in enumerate(liste_lignes):
        print("{: <2}: {}".format(num_ligne + 1, repr(ligne)))
