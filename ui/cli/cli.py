
class CLI:
    def requestNumRounds(self):
        numRounds = input("Entrer le nombre de rounds pour la partie: ")
        try:
            numRounds = int(numRounds)
        except Exception as e:
            print(e)
            print("Entrer un nombre de round valide")
            numRounds = self.requestNumRounds()
        return numRounds

    def requestPlayers(self):
        numPlayers = input("Entrer le nombre de joueurs pour la partie: ")
        try:
            numPlayers = int(numPlayers)
        except Exception as e:
            print(e)
            print("Entrer un nombre de round valide")
            numPlayers = self.requestPlayers()

        return numPlayers