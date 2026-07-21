"""Partie 1 — Classe mère : Membre"""
class  Membre :
    def __init__(self,numero,nom,succursale,duree,prix_mens,actif):
        self.numero=numero
        self.nom=nom
        self.succursale=succursale
        self.duree=duree
        self.prix_mens=prix_mens
        self.actif=actif
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, num):
        self.__numero = num

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, n):
        self.__nom = n


    @property
    def succursale(self):
        return self.__succursale

    @succursale.setter
    def succursale(self, S):
        self.__succursale = S

    @property
    def duree(self):
        return self.__duree

    @duree.setter
    def duree(self, D):
        if D > 0:
            self.__duree = D
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
    def actif(self, A):

        if A.lower() == "oui" or A.lower() == "non":
            self.__actif = A.capitalize()
        else:
            print("Valeur invalide.")

    def afficher(self):
            print(f" le numero {self.numero} avec le nom {self.nom} est inscrit a la succursale {self.succursale} pour {self.duree}, au prix de {self.prix_mens} $ par mois,actif:{self.actif}")
M1=Membre(1,'mai','dakar',5,1000,'oui' )
M2=Membre(2,'awa','scotia',6,2000,'non')
M1.afficher()
M2.afficher()
"""Partie 3 — Héritage"""
class MembreStandart(Membre):
    def __init__(self,casier,numero,nom,succursale,duree,prix_mens,actif):
        super.__init__(self,numero,nom,succursale,duree,prix_mens,actif)
        self.casier=casier
        def afficher():
            super._afficher()
        print(f"casier:{self.casier}")
class Membrepremium(Membre):
    def __init__(self,coach_perso,numero,nom,succursale,duree,prix_mens,actif):
        super.__init__(self,numero,nom,succursale,duree,prix_mens,actif)
        self.coach_perso=coach_perso
        def afficher():
            super._afficher()
        print(f"casier:{self.coach_perso}")
Membre1 = MembreStandart('OUI', 1, "ruth", "Montreal", 12, 50, 'OUI')
Membre2 = MembreStandart('NON', 2, "jean", "Toronto", 6, 40, 'OUI')
Membre3 = Membrepremium('OUI', 3, "ahou", "Montreal", 12, 100, 'OUI')
Membre4 = Membrepremium('NON', 4, "idris", "Toronto", 6, 90, 'NON')
"""Partie 5 — Liste d'objets"""
Membres=[Membre1,Membre2,Membre3,Membre4]
for i in Membres:
     print(i.afficher())
