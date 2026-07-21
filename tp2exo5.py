#exercice 2
class Membre:

    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.__numero = numero
        self.__nom = nom
        self.__succursale = succursale
        self.__duree = duree
        self.__prix = prix
        self.__actif = actif


    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valeur):
        self.__numero = valeur

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, valeur):
        self.__nom = valeur


    @property
    def succursale(self):
        return self.__succursale

    @succursale.setter
    def succursale(self, valeur):
        self.__succursale = valeur

    @property
    def duree(self):
        return self.__duree

    @duree.setter
    def duree(self, valeur):
        if valeur > 0:
            self.__duree = valeur
        else:
            print("Durée invalide.")

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, valeur):
        if valeur > 0:
            self.__prix = valeur
        else:
            print("Prix invalide.")

    @property
    def actif(self):
        return self.__actif

    @actif.setter
    def actif(self, valeur):

        if valeur.lower() == "oui" or valeur.lower() == "non":
            self.__actif = valeur.capitalize()
        else:
            print("Valeur invalide.")

    def afficher(self):
        print("Numéro :", self.numero)
        print("Nom :", self.nom)
        print("Succursale :", self.succursale)
        print("Durée :", self.duree, "mois")
        print("Prix mensuel :", self.prix, "$")
        print("Actif :", self.actif)

"""Partie 3 — Héritage"""
class MembreStandart(Membre):
    def __init__(self,casier,numero,nom,succursale,duree,prix_mens,actif):
        super.__init__(self,numero,nom,succursale,duree,prix_mens,actif)
        self.casier=casier
class Membrepremium(Membre):
    def __init__(self,coach_perso,numero,nom,succursale,duree,prix_mens,actif):
        super.__init__(self,numero,nom,succursale,duree,prix_mens,actif)
        self.coach_perso=coach_perso
"""Partie 5 — Liste d'objets"""




#exercice 6
def sauvegarder_membres(membres):

    fichier = open("membres.txt", "w")

    for membre in membres:

        if isinstance(membre,MembreStandart ):

            ligne = (
                "STANDARD;"
                + str(membre.numero) + ";"
                + membre.nom + ";"
                + membre.succursale + ";"
                + str(membre.duree) + ";"
                + str(membre.prix) + ";"
                + membre.actif + ";"
                + membre.casier + "\n"
            )

        elif isinstance(membre, Membrepremium):

            ligne = (
                "PREMIUM;"
                + str(membre.numero) + ";"
                + membre.nom + ";"
                + membre.succursale + ";"
                + str(membre.duree) + ";"
                + str(membre.prix) + ";"
                + membre.actif + ";"
                + membre.coach + "\n"
            )

        fichier.write(ligne)

    fichier.close()

    print("Les membres ont été sauvegardés.")



#exercice7
def charger_membres():

    membres = []

    fichier = open("membres.txt", "r")

    for ligne in fichier:

        ligne = ligne.strip()

        informations = ligne.split(";")

        type_membre = informations[0]

        if type_membre == "STANDARD":

            membre = MembreStandart(
                int(informations[1]),
                informations[2],
                informations[3],
                int(informations[4]),
                float(informations[5]),
                informations[6],
                informations[7]
            )

        elif type_membre == "PREMIUM":

            membre = Membrepremium(
                int(informations[1]),
                informations[2],
                informations[3],
                int(informations[4]),
                float(informations[5]),
                informations[6],
                informations[7]
            )

        membres.append(membre)

    fichier.close()

    return membres



#exercice 8
def afficher_membres_actifs(membres):

    print("=== Membres actifs ===")

    for membre in membres:

        if membre.actif.lower() == "oui":
            membre.afficher()





