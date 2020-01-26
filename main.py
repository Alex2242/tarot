import numpy as np
import random
from game import Joueur
from game import Jeu
from ui import CLI



if __name__ == "__main__":
	###################### Test de la fonction distribuer et de la fonction afficherJeu ################
	ui = CLI()
	A=Joueur("jen1", 1, 1)
	B=Joueur("jen2", 1, 1)
	C=Joueur("jen3", 1, 1)
	D=Joueur("jen4", 1, 1)
	jeu = Jeu(A, B, C, D, ui)
	# jeu.distribuerCarte(5)
	# jeu.afficherJeu()
	jeu.jouer(1)
	###################### Fin du Test ########################################

	#A faire: Gestion de l'initialisation des joueurs avec la création du jeu (de la partie).