import numpy as np
import random
from game import Manche
from ui import CLI

class Jeu:
	def __init__(self, joueur1, joueur2, joueur3, joueur4, ui):
		self.joueur1 = joueur1
		self.joueur1.setNumero(1)
		self.joueur2 = joueur2
		self.joueur2.setNumero(2)
		self.joueur3 = joueur3
		self.joueur3.setNumero(3)
		self.joueur4 = joueur4
		self.joueur4.setNumero(4)
		
		self.joueurs = {
			1: self.joueur1,
			2: self.joueur2,
			3: self.joueur3,
			4: self.joueur4
		}

		self.nbrCarte = 5
		self.ui = ui

	def distribuerCarte(self, nbrCarte):
		#liste contenant toutes les cartes dans l'ordre
		carte = np.linspace(0,21,22, dtype=int)	
		#Liste des cartes mélangées
		random.shuffle(carte) 	

		for _ in range(nbrCarte):
			self.joueur1.rajouterCarte(carte[0])	#Ajout le la première carte
			carte = np.delete(carte,0)		#supression de la carte dans la liste des cartes
			self.joueur2.rajouterCarte(carte[0])	#Ajout le la première carte
			carte = np.delete(carte,0)		#supression de la carte dans la liste des cartes
			self.joueur3.rajouterCarte(carte[0])	#Ajout le la première carte
			carte = np.delete(carte,0)		#supression de la carte dans la liste des cartes
			self.joueur4.rajouterCarte(carte[0])	#Ajout le la première carte
			carte = np.delete(carte,0)		#supression de la carte dans la liste des cartes


	def afficherJeu(self):		#Permet d'afficher les joueurs
		self.joueur1.afficherJeuComplet()
		self.joueur2.afficherJeuComplet()
		self.joueur3.afficherJeuComplet()
		self.joueur4.afficherJeuComplet()

	def affichageFinJeu(self):
		self.joueur1.afficherJeu()
		self.joueur2.afficherJeu()
		self.joueur3.afficherJeu()
		self.joueur4.afficherJeu()

	def getNbrCarte(self):		#getter pour le nbr de carte de la partie.
		return self.nbrCarte

	def setNbrCarte(self, nbrCart):		#Setter du nbr de carte
		self.nbrCarte = nbrCart

	def setJoueur1(self, nom, typeJoueur):
		self.joueur1.setType(typeJoueur)
		self.joueur1.setNom(nom)

	def setJoueur2(self, nom, typeJoueur):
		self.joueur2.setType(typeJoueur)
		self.joueur2.setNom(nom)

	def setJoueur3(self, nom, typeJoueur):
		self.joueur3.setType(typeJoueur)
		self.joueur3.setNom(nom)

	def setJoueur4(self, nom, typeJoueur):
		self.joueur4.setType(typeJoueur)
		self.joueur4.setNom(nom)

	def jouer(self, nbrManche):
		if (nbrManche > self.getNbrCarte()):
			raise Exception("impossible de faire plus de manches que de cartes / joueur")

		for k in range (nbrManche):
			self.distribuerCarte(5-k)
			manche = Manche(self, 1)
			manche.jouerManche()
			print("Fin de la manche résultats:")
			self.affichageFinJeu()

		print("Fin de la partie résultats:")
		self.affichageFinJeu()
