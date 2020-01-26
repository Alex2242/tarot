
class CLI:
    @staticmethod
    def display(*args):
        for e in args:
            print(e)

    @staticmethod
    def requestNumRounds():
        numRounds = input("Entrer le nombre de rounds pour la partie: ")
        try:
            numRounds = int(numRounds)
        except Exception as e:
            print(e)
            print("Erreur dans la saisie !")
            numRounds = CLI.requestNumRounds()
        return numRounds

    @staticmethod
    def requestPlayers():
        numPlayers = input("Entrer le nombre de joueurs pour la partie: ")
        try:
            numPlayers = int(numPlayers)
        except Exception as e:
            print(e)
            print("Erreur dans la saisie !")
            numPlayers = CLI.requestPlayers()

        return numPlayers
    

    @staticmethod
    def displayBoard(game):
        CLI.display(game)