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
        super._init_(numero,nom,succursale,duree,prix_mens,actif)
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

import random
import time



def hacher_membre(nom, succursale):
    combinaison = nom + succursale
    return hash(combinaison)




def detecter_doublons_hash(membres):

    membres_hash = set()
    doublons = 0

    for membre in membres:

        cle = hacher_membre(
            membre["nom"],
            membre["succursale"]
        )

        if cle in membres_hash:
            doublons += 1
        else:
            membres_hash.add(cle)

    return doublons



def detecter_doublons_lineaire(membres):

    membres_ajoutes = []
    doublons = 0

    for membre in membres:

        est_doublon = False

        for ancien_membre in membres_ajoutes:

            if (membre["nom"] == ancien_membre["nom"] and
                    membre["succursale"] == ancien_membre["succursale"]):

                est_doublon = True
                break

        if est_doublon:
            doublons += 1
        else:
            membres_ajoutes.append(membre)

    return doublons




noms = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma",
    "Frank",
    "George",
    "Hugo",
    "Julie",
    "Kevin"
]



succursales = [
    "Montreal",
    "Toronto",
    "Ottawa",
    "Quebec"
]



membres = []

for i in range(1000):

    membre = {
        "nom": random.choice(noms),
        "succursale": random.choice(succursales)
    }

    membres.append(membre)




debut_hash = time.perf_counter()

doublons_hash = detecter_doublons_hash(membres)

fin_hash = time.perf_counter()

temps_hash = fin_hash - debut_hash




debut_lineaire = time.perf_counter()

doublons_lineaire = detecter_doublons_lineaire(membres)

fin_lineaire = time.perf_counter()

temps_lineaire = fin_lineaire - debut_lineaire






print("Nombre de membres générés :", len(membres))

print("Nombre de doublons avec le hash :", doublons_hash)

print("Nombre de doublons avec la recherche linéaire :", doublons_lineaire)

print()

print(
    f"Temps avec le set de hachage : "
    f"{temps_hash:.8f} secondes"
)

print(
    f"Temps avec la recherche linéaire : "
    f"{temps_lineaire:.8f} secondes"
)



"""partie 11"""


class Membre:

    def __init__(self, numero, nom, succursale, duree, prix_mens, actif):
        self.numero = numero
        self.nom = nom
        self.succursale = succursale
        self.duree = duree
        self.prix_mens = prix_mens
        self.actif = actif

    def afficher(self):
        print("Numéro :", self.numero)
        print("Nom :", self.nom)
        print("Succursale :", self.succursale)
        print("Durée :", self.duree)
        print("Prix mensuel :", self.prix_mens)
        print("Actif :", self.actif)




def construire_index(membres):

    index_membres = {}

    for membre in membres:
        index_membres[membre.numero] = membre

    return index_membres




def rechercher_par_numero(index_membres, numero):

    if numero in index_membres:
        return index_membres[numero]

    return "Aucun membre ne possède le numéro " + str(numero)




def rechercher_lineaire(membres, numero):

    for membre in membres:

        if membre.numero == numero:
            return membre

    return None



membres = []

for i in range(10000):

    membre = Membre(
        i,
        "Membre" + str(i),
        "Montreal",
        12,
        50,
        True
    )

    membres.append(membre)



index_membres = construire_index(membres)



numero_recherche = 9999




debut_lineaire = time.perf_counter()

membre_lineaire = rechercher_lineaire(
    membres,
    numero_recherche
)

fin_lineaire = time.perf_counter()

temps_lineaire = fin_lineaire - debut_lineaire




debut_dictionnaire = time.perf_counter()

membre_dictionnaire = rechercher_par_numero(
    index_membres,
    numero_recherche
)

fin_dictionnaire = time.perf_counter()

temps_dictionnaire = fin_dictionnaire - debut_dictionnaire



print("Nombre de membres :", len(membres))

print("Numéro recherché :", numero_recherche)

print()



if membre_lineaire is not None:
    print("Membre trouvé :", membre_lineaire.nom)
else:
    print("Aucun membre trouvé")

print(
    f"Temps de recherche linéaire : "
    f"{temps_lineaire:.8f} secondes"
)

print()



if isinstance(membre_dictionnaire, Membre):
    print("Membre trouvé :", membre_dictionnaire.nom)
else:
    print(membre_dictionnaire)

print(
    f"Temps de recherche avec dictionnaire : "
    f"{temps_dictionnaire:.8f} secondes"
)