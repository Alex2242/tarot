import numpy as np
import random
from ui import CLI

class Manche:
	def __init__(self, jeu, tourJoueur):
		self.jeu = jeu 			#Nous avons donc les différents joueurs et le nombre de cartes de la partie
		self.tourJoueur = tourJoueur	#Sachant que les joueurs vont de 1 à 4


	def changementJoueur(self):
		self.tourJoueur = (self.tourJoueur % 4) + 1

	def joueurJouer(self, numJoueur):	#en fonction du joueur, cette fonction renvoie le joueur correspondant
		return self.jeu.joueurs[numJoueur]

	def affichageManche(self):
		for k in range (4):
			self.joueurJouer(k+1).afficheJeu()

	def jouerManche(self):	#La distribution des cartes à déjà été faite à ce point de la partie
		print("\n" * 10)
		print("Selection des plis")
		nbrpli = 0

		for j in range(4):		#Choix du nbr de plis que l'on pense gagner
			joueurJoue = self.joueurJouer(self.tourJoueur)		#renvoie le joueur qui doit jouer
			joueurJoue.afficherJeuComplet()
			
			if (joueurJoue.getType() == 0):		#Distinction du type de joueur, si c'est un bot ou un joueur réel, ici, c'est un bot
				pli = random.randint(0, joueurJoue.getNbrCarte())
				nbrpli += pli
			
			else:
				pli = int(input("Entrer le nbr de carte que vous pensez gagner: "))

				while (j == 3 and (nbrpli + pli) == 4):
					pli = int(input("Entrée invalide pour le dernier joueur, remisez: "))

				nbrpli += pli
			
			joueurJoue.setNbrPliVoulu(pli)
			self.changementJoueur()
			print("\n" * 10)
		
		print("Debut de la manche")

		for _ in range(self.jeu.getNbrCarte()):	#Lancement de la partie pour le nombre de carte que l'on a en main
			print("Début du pli")
			
			for j in range(4):		#Pour chaque joueur
				self.joueurJouer(self.tourJoueur).afficherJeuComplet()
				if (self.joueurJouer(self.tourJoueur).getType() == 0):		#Si le joueur est un bot
					lenghtList = self.joueurJouer(self.tourJoueur).getNbrCarte()
					indiceCarte = np.random.choice(lenghtList, 1)		#Nous prenons une carte au hasard dans la liste
					self.joueurJouer(self.tourJoueur).setCarte(self.joueurJouer(self.tourJoueur).getListeCarte()[indiceCarte])	#On garde la carte jouee
					self.joueurJouer(self.tourJoueur).enleverCarte(self.joueurJouer(self.tourJoueur).getListeCarte()[indiceCarte])	#On enleve la carte joue de la liste
				else:
					print("Jouer une carte")
					lenghtList = self.joueurJouer(self.tourJoueur).getNbrCarte()
					indiceCarte = int(input())

					while (indiceCarte > lenghtList-1 or indiceCarte < -1):	#Ne sort pas de la boucle while tant qu'une bonne carte n'a pas été choisi
						print("Choisir un autre numéro de carte")
						indiceCarte = int(input())	#input(int(nbr))setCarte

					if (indiceCarte == 23):	#Gestion du joker
						print("Choisir la valeur du joker (0 ou 22)")
						indiceCarte = int(input())	#input(int(nbr))setCarte

					self.joueurJouer(self.tourJoueur).setCarte(self.joueurJouer(self.tourJoueur).getListeCarte()[indiceCarte])	#On garde la carte jouee
					self.joueurJouer(self.tourJoueur).enleverCarte(self.joueurJouer(self.tourJoueur).getListeCarte()[indiceCarte])	#On enleve la carte joue de la liste
				#Afficher le jeu complet
				self.changementJoueur()	#Changement du joueur
			
			print("Voir qui gagne le pli")
			joueur_gagnant = self.tourJoueur
			carte_gagnante = self.joueurJouer(self.tourJoueur).getCarte()
			
			print("carte jouee =", carte_gagnante)
			self.changementJoueur()

			for i in range (3):		#Voir qui à gargner et perdu la manche, on utilise
				joueurJoueCarte = self.joueurJouer(self.tourJoueur).getCarte()	#Correspond à la carte du joueur en question
				print("carte jouee =", joueurJoueCarte)
				if(joueurJoueCarte > carte_gagnante):
					carte_gagnante = joueurJoueCarte
					joueur_gagnant = self.tourJoueur
				self.changementJoueur()
				
			print(carte_gagnante, joueur_gagnant)
			self.joueurJouer(joueur_gagnant).setNbrPli(self.joueurJouer(joueur_gagnant).getNbrPli()+1)	#Ajout d'un pli
			print("fin du pli")
			self.tourJoueur = joueur_gagnant #changement du joueur de départ	, celui qui a gagné commence à jouer
		for i in range (4):
			joueur_gagnant = self.joueurJouer(self.tourJoueur)
			if (joueur_gagnant.getNbrPli() != joueur_gagnant.getNbrPliVoulu()):
				joueur_gagnant.setPenalite(joueur_gagnant.getPenalite()+1)
			self.changementJoueur()
		
		print("fin de la manche")
