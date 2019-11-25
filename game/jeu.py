import numpy as np
from random import random
from joueur import Joueur

class Jeu:
	#Connaitre le joueur qui doit jouer, variable
	
	def __init__(self, joueur1, joueur2, joueur3, joueur4):
		self.joueur1 = joueur1
		self.joueur2 = joueur2
		self.joueur3 = joueur3
		self.joueur4 = joueur4
		self.nbrCarte = 5		#Correspond au nbr de cartes distribuées au début


	def distribuerCarte(self):
		carte = np.linspace(0,21,22)	#liste contenant toutes les cartes dans l'ordre
		random.shuffle(carte) 	#Liste des cartes mélangées
		for k in range(self.nbrCarte):
			self.joueur1.rajouterCarte(carte[0])	#Ajout le la première carte
			carte = np.delete(carte,0)		#supression de la carte dans la liste des cartes
			self.joueur2.rajouterCarte(carte[0])	#Ajout le la première carte
			carte = np.delete(carte,0)		#supression de la carte dans la liste des cartes
			self.joueur3.rajouterCarte(carte[0])	#Ajout le la première carte
			carte = np.delete(carte,0)		#supression de la carte dans la liste des cartes
			self.joueur4.rajouterCarte(carte[0])	#Ajout le la première carte
			carte = np.delete(carte,0)		#supression de la carte dans la liste des cartes
		return True	


	def afficherJeu(self):		#A compléter, gérer ke tour des joueurs
		pass

	def getNbrCarte(self):		#getter pour le nbr de carte de la partie.
		return self.nbrCarte

	def setNbrCarte(self, nbrCart)		#Setter du nbr de carte
		self.nbrCarte = nbrCart
		return True		#Une fois terminé

	def getJoueur1(self):		#Getter pour les différents joueurs
		return self.joueur1

	def getJoueur2(self):
	return self.joueur2

	def getJoueur3(self):
	return self.joueur3

	def getJoueur4(self):
	return self.joueur4

	# def jouer(self):		#Première version, 1 joueur vs 3 ordis
	# 	distribuerCarte()	#distribution des cartes
	# 	joueur1.afficher()	#affichage des cartes du joueur1
	# 	for k in range:
	# 	return True
	# def jouer(self):		#Première version, 1 joueur vs 3 ordis
	# 	distribuerCarte()	#distribution des cartes
	# 	joueur1.afficher()	#affichage des cartes du joueur1
	# 	for k in range:
	# 	return True

	