"""partie 4 """

class MembreStandart(Membre):
    def _init_(self,casier,numero,nom,succursale,duree,prix_mens,actif):
        super._init_(self,numero,nom,succursale,duree,prix_mens,actif)
        self.casier=casier
def afficher(self):
        super().afficher()
        print(f"Casier : {'Oui' if self.casier else 'Non'}")

class Membrepremium(Membre):
    def _init_(self,coach_perso,numero,nom,succursale,duree,prix_mens,actif):
        super._init_(self,numero,nom,succursale,duree,prix_mens,actif)
        self.coach_perso=coach_perso

    def afficher(self):
        super().afficher()
        print(f"Coach personnel : {'Oui' if self.coach_perso else 'Non'}")
membre1 = MembreStandart(True, 1, "ruth", "Montreal", 12, 50, True)
membre2 = MembreStandart(False, 2, "jean", "Toronto", 6, 40, True)


membre3 = Membrepremium(True, 3, "ahou", "Montreal", 12, 100, True)
membre4 = Membrepremium(False, 4, "idris", "Toronto", 6, 90, False)


membres = [membre1, membre2, membre3, membre4]


for membre in membres:
    membre.afficher()





""" partie 10 """

def hacher_membre(self,nom, succursal):
     return hash(nom+ succursal)
def supp_doublons(menbre):
     membre_double = set
     doublons = 0

     