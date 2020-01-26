import numpy as np


class Joueur:
	#les attributs sont le nom, une photo, la liste des cartes, le type de joueur, humain ou bot, nbr de pli et pénalité (score)
	# communication entre les personnes
	# interface avec git, le mettre dans une tâches?
	# automatiser des tests

	def __init__(self, nom, numero, typeJoueur):
		self.nom = nom
		self.numero = numero
		self.typeJ = typeJoueur		#0 = bot et 1 = humain
		self.listeCarte = np.array([], dtype=int)	#Sera une liste d'entiers
		self.carte = 23	#Correspond à la carte que va jouer le joueur, le 23 correspond au fait que le joueur n'a pas possé de carte
		self.nbr_pli = 0	#Pour l'initialisation
		self.nbrPliVoulu =0
		self.penalite = 0

	def afficherJeuComplet(self):
		print(self.nom+" a les cartes |"+' '.join(str(elem) for elem in self.listeCarte)+"| le nombre de pli actuel est de :",self.nbr_pli,"le nombre de pli voulu est de :",self.nbrPliVoulu)
	
	def afficherJeu(self):
		print(self.nom,"le nombre de penalite est de :",self.penalite)


	def rajouterCarte(self,carte):
		# self.listeCarte.colonstack(carte,axis =1)
		self.listeCarte = np.append(self.listeCarte,carte)
		return True

	def enleverCarte(self,carte):
		self.listeCarte = np.delete(self.listeCarte,np.where(self.listeCarte == carte))
		return True

	def getListeCarte(self):
		return self.listeCarte

	def getNbrCarte(self):
		return len(self.listeCarte)

	def getPenalite(self):
		return self.penalite

	def getType(self):
		return self.typeJ

	def getNumero(self):
		return self.numero

	def getCarte(self):
		return self.carte

	def getNbrPli (self):
		return self.nbr_pli

	def getNbrPliVoulu (self):
		return self.nbrPliVoulu

	def setNbrPli(self, nbr):
		self.nbr_pli = nbr
		return True

	def setNbrPliVoulu(self, nbr):
		self.nbrPliVoulu = nbr
		return True

	def setCarte(self, card):
		self.carte = card
		return True

	def setNumero(self, nbr):
		self.numero = nbr
		return True

	def setType(self, typeJoueur):
		self.typeJ = typeJoueur
		return True

	def setNom (self, nom):
		self.nom = nom
		return True

	def setPenalite(self, nbr):
		self.penalite = nbr
		return True


# ---------------------------------------------------------------------------------------------------------------
# Test des fonctions de la classe joueur
# ---------------------------------------------------------------------------------------------------------------
# A=Joueur("jen",1,1)
# A.rajouterCarte(2)
# A.rajouterCarte(5)
# A.rajouterCarte(7)
# A.afficherJeuComplet()
# A.enleverCarte(5)
# A.afficherJeu()