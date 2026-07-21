"""Partie 1 — Classe mère : Membre"""
class  Membre :
    def __init__(self,numero,nom,succursale,duree,prix_mens,actif):
        self.numero=numero
        self.nom=nom
        self.succursale=succursale
        self.duree=duree
        self.prix_mens=prix_mens
        self.actif=actif
    def afficher(self):
            print(f" le numero {self.numero} avec le nom {self.nom} est inscrit a la succursale {self.succursale} pour {self.duree}, au prix de {self.prix_mens} $ par mois,actif:{self.actif}")
M1=Membre(1,'mai','rbc',5,1000,'oui' )
M2=Membre(2,'awa','scotia',6,2000,'non')
M1.afficher()
M2.afficher()
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

Membres=[]
for i in Membres:
     print(i)
