import numpy as np
from random import random
from joueur import Joueur
from jeu import Jeu


class Manche:

	def __init__(self, jeu, tourJoueur):
		self.jeu = jeu 			#Nous avons donc les différents joueurs et le nombre de cartes de la partie
		self.tourJoueur = tourJoueur;	#Sachant que les joueurs vont de 1 à 4

	def changementJoueur(self):
		if (self.tourJoueur == 4):
			self.tourJoueur = 1
			return True
		else:
			self.tourJoueur += 1
			return True

	def joueurJouer(self, nbrJoueur):	#en fonction du joueur, cette fonction renvoie le joueur correspondant
		if (nbrJoueur == 1):
			return self.jeu.getJoueur1()
		if (nbrJoueur == 2):
			return self.jeu.getJoueur2()
		if (nbrJoueur == 3):
			return self.jeu.getJoueur3()
		if (nbrJoueur == 4):
			return self.jeu.getJoueur4()

	def jouerManche(self):	#La distribution des cartes à déjà été faite à ce point de la partie
		for j in range(4):
			joueurJoue = self.joueurJoue(self.tourJoueur)		#renvoie le joueur qui doit jouer
			nbrpli = 0
			if (joueurJoue.getType() == 0):		#Distinction du type de joueur, si c'est une IA ou un joueur réel, ici, c'est une IA
				pli = random.randint(0, self.getNbrCarte())
				#Fin
			print("Entrer le nbr de carte que vous pensez gagner")
			self.input(int(nbr))									#Voir si le nombre annoncé est possible
			changementJoueur()
		for k in range(self.jeu.getNbrCarte):	#Pour le nombre de carte que l'on a
			for j in range(4):		#Pour chaque joueur
				print("Entrer le nbr de carte que vous pensez gagner")
				input(int(nbr))



