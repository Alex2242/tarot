import numpy as np


class Joueur:
	#les attributs sont le nom, une photo, la liste des cartes, le type de joueur, humain ou bot, nbr de pli et pénalité (score)
	# communication entre les personnes
	# interface avec git, le mettre dans une tâches?
	# automatiser des tests

	def __init__(self, nom, typeJoueur):
		self.nom = nom
		self.typeJ = typeJoueur		#0 = bot et 1 = humain
		self.listeCarte = np.array([])	#Sera une liste d'entiers
		self.nbr_pli = 0	#Pour l'initialisation
		self.penalite = 0

	def afficher(self):
		print(self.nom+" a les cartes |"+' '.join(str(elem) for elem in self.listeCarte)+"| le nombre de penalite est de :",self.penalite)
	
	def rajouterCarte(self,carte):
		self.listeCarte.append(carte)

	def enleverCarte(self):
		while 'a' in self.listeCarte:
		    del self.listeCarte[self.listeCarte.index('a')]

	def getNbrCarte(self):
		return len(self.listeCarte)

	def getPenalite(self):
		return self.penalite

	def getType(self):
		return self.typeJ


A=Joueur("jen",1)
A.afficher()
