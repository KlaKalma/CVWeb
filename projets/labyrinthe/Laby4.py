# coding: utf-8
from tkinter import*
from tkinter.messagebox import *
from time import *
from random import randint
#https://fr.wikipedia.org/wiki/Modelisation_mathematique_d'un_labyrinthe

FT = 3 # facteur qui réduit la taille du cube pour ne pas cacher les murs
TX = 10# Taille labyrinthe X
TY = 10# Taille labyrinthe Y

TC = [TX,TY] # stockage coordonnées temporaire

MF = 450 / TY # mini facteur pour la prévisualisation

FX = 600 / TX # calcule le facteur optimal pour une taille de labyrinthe donnée
FY = 600 / TY

F = min(FX , FY) # prend la valeur minimal pour ajuster a la taille de la fenetre

LABON = True # laby activé ou btaille navalle activée

coul = "white" # couleur des murs
RES = False # on ne recommence pas quand on cogne un mur
Couleu = "yellow" # couleur du perso
Alea = True # variable pour savoir si on fait un labyronthe aléatoire
REGE = True # regénérer en fin
BONAL = False # Bonus aléatoire
MULTI = False # mode multi

if TX * TY > 200:
    BONUS = False # doit aller chercher un bonus dans les coins avant de pouvoir ateindre la fin
    SBON = False
else:
    BONUS = True
    SBON = True # sert a stocker le paramètre pour les labyrnthe enregistrés

LM = [] # liste de tous les murs servie pour les afficher
MM = [] # liste de liste (matrice) des zones de chaques murs pour le générateur
c = 0 # nombre de murs crees pour savoir quand fini la génération
b = 0 # pour ne pas qu'il y ai trop d'oppération, et que le générateur ne bug pas
k = True # pour faire fonctionner le regénérateur en fon pour ne pas regénérer en début
h = False # sert a savoir si on print plusieurs fois le labyrinthe
MC = 0 # murs cognés, pour les statistiques
MC2 = 0
LB1 = [1,TY] # coordonnées des bonus
LB2 = [TX,1] # coordonnées des bonus
MODEC = False # mode création activé ou non
MODECFIN = False
CCL = [1,3,8,6] # r c rs cs  Canevas
CBLRG = [0,0] # r c    Re generer
CBLO = [0,1] # r c    Obtenir
CBLG = [0,0] # r c    précédent
CBLD = [0,1] # r c    suivant
BATchoisi = [None,"h"] # numéro du bateau séléctionné
Numbat = None
BATchoisi2 = [None,"h"] # numéro du bateau séléctionné
Numbat2 = None

# liste des murs temporaire enregistrée servie pour l'editage
TLM = []

# LMG lsite des murs temporaire aléatoirement générée
LMG = [[1,1,"v"],[1,5,"h"],[1,2,"v"],[1,3,"h"],[2,1,"v"],[3,1,"v"],[3,2,"h"],[5,1,"h"],[3,2,"v"],[4,2,"v"],[5,2,"v"],[5,3,"v"],[4,4,"v"],[5,3,"h"],[4,3,"h"],[4,3,"h"],[3,3,"h"],[5,4,"h"],[8,1,"h"],[9,3,"h"],[8,4,"h"],[8,2,"v"],[8,3,"v"],[7,2,"v"],[7,3,"v"],[8,3,"v"],[9,1,"v"],[9,2,"v"],[8,6,"v"],[8,7,"v"],[6,2,"v"],[7,3,"v"],[2,4,"v"],[1,5,"v"],[3,5,"v"],[2,5,"h"],[3,5,"h"],[4,5,"h"],[5,5,"h"],[6,5,"h"],[2,6,"h"],[3,6,"h"],[4,6,"h"],[5,6,"h"],[6,6,"h"],[1,6,"v"],[2,9,"v"],[3,8,"v"],[3,9,"v"],[2,8,"h"],[2,7,"h"],[1,9,"h"],[4,8,"h"],[3,7,"h"],[3,10,"v"],[6,9,"h"],[4,9,"v"],[8,9,"h"],[5,9,"v"],[4,7,"v"],[7,5,"v"],[7,4,"h"],[6,4,"h"],[5,8,"v"],[7,8,"h"],[8,8,"h"],[9,8,"h"],[9,7,"h"],[10,7,"h"],[9,9,"h"],[10,4,"h"],[7,7,"h"],[8,6,"h"],[7,7,"v"],[6,8,"v"],[9,10,"v"],[6,10,"v"],[9,6,"v"],[9,5,"v"],[6,3,"v"],[8,4,"v"],[6,4,"v"]] # liste qui stocke le labyrinthe aléatoire
# LSM lsite des murs enregistrés avec les dimentions, on peut en ajouter autant que l'on veut
LSMG = [

[[10,10] # dimentions des laby enregistrés
,[[1, 2, 'h'], [2, 2, 'h'], [3, 2, 'h'], [2, 1, 'h'], [2, 1, 'v'], [5, 2, 'v'], [5, 3, 'h'], [5, 3, 'v'], [4, 3, 'h'], [3, 4, 'v'], [3, 5, 'h'], [4, 5, 'h'], [4, 5, 'v'], [4, 4, 'v'], [2, 5, 'v'], [2, 4, 'v'], [2, 3, 'h'], [4, 2, 'v'], [7, 1, 'v'], [6, 5, 'v'], [6, 4, 'h'], [5, 6, 'h'], [5, 5, 'h'], [4, 7, 'v'], [1, 4, 'v'], [1, 5, 'h'], [2, 6, 'v'], [2, 7, 'v'], [3, 7, 'v'], [3, 8, 'v'], [2, 6, 'h'], [7, 5, 'h'], [8, 5, 'v'], [8, 5, 'h'], [6, 6, 'h'], [8, 3, 'v'], [8, 4, 'v'], [9, 1, 'h'], [9, 3, 'h'], [10, 2, 'h'], [9, 5, 'v'], [9, 5, 'h'], [5, 8, 'v'], [5, 8, 'h'], [6, 8, 'v'], [6, 9, 'h'], [7, 9, 'v'], [7, 9, 'h'], [4, 9, 'v'], [1, 9, 'v'], [8, 8, 'v'], [9, 9, 'v'], [9, 10, 'v'], [2, 9, 'h'], [7, 4, 'v'], [7, 8, 'h'], [9, 7, 'v'], [8, 9, 'v'], [10, 7, 'h'], [8, 9, 'h'], [9, 7, 'h'], [6, 7, 'v'], [8, 6, 'h'], [7, 6, 'v'], [7, 7, 'v'], [1, 7, 'h'], [4, 10, 'v'], [3, 9, 'v'], [3, 9, 'h'], [2, 8, 'v'], [7, 3, 'h'], [6, 2, 'v'], [3, 2, 'v'], [4, 1, 'h'], [7, 1, 'h'], [8, 2, 'h'], [6, 3, 'v'], [8, 2, 'v']],[[1,1,"v"],[1,5,"h"],[1,2,"v"],[1,3,"h"],[2,1,"v"],[3,1,"v"],[3,2,"h"],[5,1,"h"],[3,2,"v"],[4,2,"v"],[5,2,"v"],[5,3,"v"],[4,4,"v"],[5,3,"h"],[4,3,"h"],[4,3,"h"],[3,3,"h"],[5,4,"h"],[8,1,"h"],[9,3,"h"],[8,4,"h"],[8,2,"v"],[8,3,"v"],[7,2,"v"],[7,3,"v"],[8,3,"v"],[9,1,"v"],[9,2,"v"],[8,6,"v"],[8,7,"v"],[6,2,"v"],[7,3,"v"],[2,4,"v"],[1,5,"v"],[3,5,"v"],[2,5,"h"],[3,5,"h"],[4,5,"h"],[5,5,"h"],[6,5,"h"],[2,6,"h"],[3,6,"h"],[4,6,"h"],[5,6,"h"],[6,6,"h"],[1,6,"v"],[2,9,"v"],[3,8,"v"],[3,9,"v"],[2,8,"h"],[2,7,"h"],[1,9,"h"],[4,8,"h"],[3,7,"h"],[3,10,"v"],[6,9,"h"],[4,9,"v"],[8,9,"h"],[5,9,"v"],[4,7,"v"],[7,5,"v"],[7,4,"h"],[6,4,"h"],[5,8,"v"],[7,8,"h"],[8,8,"h"],[9,8,"h"],[9,7,"h"],[10,7,"h"],[9,9,"h"],[10,4,"h"],[7,7,"h"],[8,6,"h"],[7,7,"v"],[6,8,"v"],[9,10,"v"],[6,10,"v"],[9,6,"v"],[9,5,"v"],[6,3,"v"],[8,4,"v"],[6,4,"v"]]
,[[2, 1, 'h'], [2, 2, 'h'], [2, 3, 'h'], [2, 4, 'h'], [2, 6, 'h'], [2, 7, 'h'], [2, 8, 'h'], [2, 9, 'h'], [3, 1, 'h'], [4, 1, 'h'], [5, 1, 'h'], [6, 1, 'h'], [7, 1, 'h'], [3, 2, 'v'], [3, 3, 'v'], [3, 3, 'h'], [9, 1, 'h'], [8, 1, 'v'], [9, 1, 'v'], [7, 2, 'v'], [8, 2, 'h'], [9, 2, 'h'], [10, 2, 'h'], [3, 5, 'h'], [4, 5, 'h'], [5, 5, 'h'], [6, 5, 'h'], [7, 5, 'h'], [8, 5, 'h'], [9, 5, 'h'], [9, 4, 'h'], [7, 4, 'h'], [6, 4, 'h'], [5, 4, 'h'], [3, 4, 'h'], [4, 4, 'h'], [4, 4, 'v'], [4, 3, 'v'], [5, 2, 'h'], [5, 3, 'v'], [6, 3, 'v'], [6, 2, 'v'], [8, 3, 'h'], [7, 4, 'v'], [9, 3, 'v'], [9, 4, 'v'], [10, 5, 'h'], [2, 10, 'v'], [3, 8, 'h'], [4, 8, 'h'], [5, 8, 'h'], [6, 8, 'h'], [6, 9, 'v'], [5, 9, 'h'], [4, 9, 'h'], [3, 9, 'h'], [6, 10, 'v'], [3, 6, 'h'], [4, 6, 'h'], [4, 6, 'v'], [3, 7, 'h'], [4, 7, 'h'], [5, 7, 'h'], [6, 7, 'h'], [8, 7, 'h'], [7, 9, 'v'], [7, 10, 'v'], [8, 10, 'v'], [8, 9, 'v'], [8, 8, 'v'], [9, 8, 'h'], [10, 9, 'h'], [10, 7, 'h'], [8, 7, 'v'], [10, 6, 'h'], [7, 6, 'v'], [6, 6, 'v'], [5, 7, 'v'], [1, 5, 'h']]
],

[[15,15]
,[[1, 1, 'h'], [1, 2, 'v'], [1, 3, 'h'], [1, 4, 'v'], [1, 5, 'v'], [1, 7, 'v'], [1, 8, 'h'], [1, 9, 'v'], [1, 12, 'v'], [1, 13, 'h'], [1, 13, 'v'], [1, 14, 'v'], [2, 1, 'h'], [2, 2, 'h'], [2, 4, 'h'], [2, 4, 'v'], [2, 5, 'v'], [2, 6, 'v'], [2, 7, 'h'], [2, 8, 'v'], [2, 9, 'h'], [2, 10, 'h'], [2, 11, 'v'], [2, 14, 'h'], [2, 14, 'v'], [3, 2, 'h'], [3, 2, 'v'], [3, 3, 'v'], [3, 4, 'h'], [3, 5, 'h'], [3, 7, 'v'], [3, 8, 'h'], [3, 9, 'v'], [3, 11, 'h'], [3, 11, 'v'], [3, 12, 'h'], [3, 13, 'h'], [3, 13, 'v'], [3, 14, 'h'], [4, 2, 'h'], [4, 2, 'v'], [4, 4, 'v'], [4, 5, 'h'], [4, 5, 'v'], [4, 6, 'h'], [4, 7, 'v'], [4, 9, 'h'], [4, 9, 'v'], [4, 11, 'h'], [4, 11, 'v'], [4, 13, 'v'], [4, 14, 'v'], [4, 15, 'v'], [5, 1, 'h'], [5, 3, 'h'], [5, 3, 'v'], [5, 4, 'v'], [5, 6, 'h'], [5, 6, 'v'], [5, 7, 'v'], [5, 8, 'h'], [5, 9, 'v'], [5, 10, 'h'], [5, 11, 'v'], [5, 12, 'v'], [5, 14, 'h'], [6, 2, 'h'], [6, 2, 'v'], [6, 3, 'v'], [6, 5, 'h'], [6, 5, 'v'], [6, 6, 'v'], [6, 7, 'v'], [6, 8, 'h'], [6, 9, 'h'], [6, 10, 'v'], [6, 11, 'v'], [6, 12, 'h'], [6, 13, 'h'], [6, 13, 'v'], [6, 15, 'v'], [7, 1, 'v'], [7, 2, 'h'], [7, 4, 'h'], [7, 4, 'v'], [7, 6, 'h'], [7, 6, 'v'], [7, 7, 'v'], [7, 8, 'h'], [7, 9, 'h'], [7, 10, 'v'], [7, 11, 'h'], [7, 12, 'h'], [7, 12, 'v'], [7, 13, 'h'], [8, 2, 'v'], [8, 3, 'h'], [8, 4, 'v'], [8, 6, 'v'], [8, 7, 'h'], [8, 7, 'v'], [8, 8, 'v'], [8, 9, 'h'], [8, 11, 'h'], [8, 11, 'v'], [8, 12, 'v'], [8, 14, 'h'], [8, 14, 'v'], [8, 15, 'v'], [9, 2, 'h'], [9, 2, 'v'], [9, 4, 'v'], [9, 5, 'h'], [9, 7, 'h'], [9, 7, 'v'], [9, 8, 'v'], [9, 9, 'h'], [9, 9, 'v'], [9, 10, 'v'], [9, 11, 'v'], [9, 12, 'h'], [9, 13, 'v'], [9, 15, 'v'], [10, 1, 'h'], [10, 1, 'v'], [10, 2, 'h'], [10, 3, 'h'], [10, 4, 'v'], [10, 9, 'h'], [10, 9, 'v'], [10, 10, 'v'], [10, 11, 'v'], [10, 13, 'h'], [10, 14, 'v'], [11, 2, 'h'], [11, 3, 'h'], [11, 4, 'v'], [11, 5, 'h'], [11, 5, 'v'], [11, 6, 'h'], [11, 6, 'v'], [11, 7, 'h'], [11, 8, 'h'], [11, 8, 'v'], [11, 10, 'v'], [11, 12, 'h'], [11, 13, 'h'], [11, 14, 'v'], [12, 1, 'h'], [12, 1, 'v'], [12, 3, 'v'], [12, 4, 'h'], [12, 5, 'v'], [12, 6, 'h'], [12, 7, 'v'], [12, 9, 'h'], [12, 9, 'v'], [12, 10, 'v'], [12, 11, 'h'], [12, 12, 'h'], [12, 12, 'v'], [12, 13, 'h'], [12, 13, 'v'], [12, 14, 'v'], [13, 2, 'h'], [13, 2, 'v'], [13, 3, 'v'], [13, 4, 'v'], [13, 5, 'v'], [13, 6, 'h'], [13, 8, 'h'], [13, 8, 'v'], [13, 9, 'v'], [13, 10, 'v'], [13, 11, 'h'], [13, 13, 'v'], [13, 14, 'h'], [13, 14, 'v'], [14, 1, 'v'], [14, 2, 'h'], [14, 4, 'h'], [14, 6, 'h'], [14, 7, 'h'], [14, 7, 'v'], [14, 8, 'v'], [14, 9, 'v'], [14, 11, 'v'], [14, 13, 'h'], [14, 13, 'v'], [15, 3, 'h'], [15, 4, 'h'], [15, 5, 'h'], [15, 7, 'h'], [15, 10, 'h'], [15, 13, 'h'], [15, 14, 'h']]
,[[1, 1, 'v'], [1, 2, 'h'], [1, 3, 'h'], [1, 5, 'h'], [1, 6, 'h'], [1, 8, 'h'], [1, 9, 'v'], [1, 10, 'v'], [1, 11, 'v'], [1, 12, 'h'], [1, 13, 'v'], [1, 15, 'v'], [2, 2, 'v'], [2, 4, 'h'], [2, 4, 'v'], [2, 6, 'h'], [2, 6, 'v'], [2, 7, 'h'], [2, 7, 'v'], [2, 9, 'v'], [2, 11, 'v'], [2, 12, 'v'], [2, 13, 'h'], [3, 1, 'v'], [3, 2, 'h'], [3, 2, 'v'], [3, 3, 'h'], [3, 5, 'v'], [3, 6, 'h'], [3, 6, 'v'], [3, 7, 'v'], [3, 8, 'h'], [3, 8, 'v'], [3, 9, 'v'], [3, 10, 'v'], [3, 11, 'h'], [3, 12, 'v'], [3, 13, 'h'], [3, 13, 'v'], [3, 14, 'h'], [3, 14, 'v'], [4, 2, 'h'], [4, 2, 'v'], [4, 3, 'h'], [4, 3, 'v'], [4, 5, 'h'], [4, 5, 'v'], [4, 6, 'v'], [4, 7, 'v'], [4, 8, 'h'], [4, 9, 'h'], [4, 12, 'v'], [4, 13, 'h'], [4, 13, 'v'], [4, 15, 'v'], [5, 1, 'v'], [5, 3, 'h'], [5, 3, 'v'], [5, 4, 'h'], [5, 7, 'v'], [5, 8, 'h'], [5, 9, 'h'], [5, 10, 'h'], [5, 11, 'h'], [5, 12, 'h'], [5, 13, 'v'], [5, 14, 'v'], [6, 2, 'v'], [6, 3, 'h'], [6, 3, 'v'], [6, 4, 'h'], [6, 5, 'h'], [6, 6, 'h'], [6, 7, 'h'], [6, 8, 'v'], [6, 10, 'h'], [6, 10, 'v'], [6, 11, 'h'], [6, 11, 'v'], [6, 13, 'v'], [7, 2, 'v'], [7, 4, 'v'], [7, 5, 'h'], [7, 5, 'v'], [7, 6, 'h'], [7, 7, 'v'], [7, 9, 'h'], [7, 9, 'v'], [7, 11, 'v'], [7, 12, 'h'], [7, 14, 'h'], [7, 14, 'v'], [8, 1, 'h'], [8, 1, 'v'], [8, 2, 'h'], [8, 3, 'h'], [8, 4, 'v'], [8, 6, 'v'], [8, 7, 'h'], [8, 10, 'h'], [8, 11, 'h'], [8, 12, 'h'], [8, 12, 'v'], [8, 13, 'h'], [8, 13, 'v'], [8, 14, 'v'], [9, 1, 'h'], [9, 3, 'h'], [9, 3, 'v'], [9, 4, 'v'], [9, 5, 'h'], [9, 5, 'v'], [9, 6, 'v'], [9, 7, 'h'], [9, 7, 'v'], [9, 8, 'h'], [9, 8, 'v'], [9, 9, 'h'], [9, 10, 'h'], [9, 14, 'v'], [9, 15, 'v'], [10, 2, 'v'], [10, 3, 'h'], [10, 6, 'h'], [10, 6, 'v'], [10, 8, 'h'], [10, 8, 'v'], [10, 9, 'h'], [10, 10, 'h'], [10, 10, 'v'], [10, 11, 'h'], [10, 11, 'v'], [10, 12, 'h'], [10, 13, 'h'], [10, 15, 'v'], [11, 1, 'v'], [11, 2, 'h'], [11, 3, 'v'], [11, 4, 'h'], [11, 5, 'h'], [11, 5, 'v'], [11, 6, 'v'], [11, 9, 'h'], [11, 9, 'v'], [11, 10, 'h'], [11, 11, 'v'], [11, 12, 'h'], [11, 12, 'v'], [11, 13, 'v'], [11, 14, 'v'], [12, 2, 'v'], [12, 3, 'h'], [12, 3, 'v'], [12, 4, 'h'], [12, 4, 'v'], [12, 5, 'v'], [12, 7, 'h'], [12, 7, 'v'], [12, 8, 'v'], [12, 9, 'h'], [12, 9, 'v'], [12, 10, 'h'], [12, 11, 'h'], [12, 13, 'h'], [12, 14, 'v'], [13, 1, 'h'], [13, 1, 'v'], [13, 2, 'v'], [13, 3, 'v'], [13, 5, 'v'], [13, 6, 'h'], [13, 9, 'v'], [13, 10, 'v'], [13, 11, 'h'], [13, 11, 'v'], [13, 12, 'h'], [13, 13, 'v'], [13, 14, 'h'], [13, 15, 'v'], [14, 1, 'v'], [14, 2, 'v'], [14, 4, 'h'], [14, 4, 'v'], [14, 6, 'v'], [14, 7, 'h'], [14, 7, 'v'], [14, 8, 'h'], [14, 12, 'h'], [14, 12, 'v'], [14, 13, 'h'], [14, 15, 'v'], [15, 3, 'h'], [15, 7, 'h'], [15, 9, 'h'], [15, 10, 'h'], [15, 12, 'h']]

]
# mettre un virgule et ajouter les nouveau labyrinthe apres la virgule comme fait au dessus
]

LSM = None
I = 0 # labyrinthe en cours enregistré

# bataille navale

TBX = 10
TBY = 10

FBX = 400 / TBX # calcule le facteur optimal pour une taille de labyrinthe donnée
FBY = 400 / TBY

FB = min(FBX , FBY) # prend la valeur minimal pour ajuster a la taille de la fenetre

MBF = 320 / TBY # mini facteur pour la prévisualisation

MURSBAT = []

VSIA = True
BATPAR = True
quelJ = 1
TROMPE = True
NIVEAUIA = 1
Affiché = 1

CHANGE = False

COORDSBAT = []

"""
fonctionnalités a ajouter

( animation quand ca génere le laby)

bataille navale
    1v1

    nb de bateau parametrable
    fonction tirs adversaire ( pour savoir qui tire en premier )
    fonction droit de se tromper

    changer les bateaux de place avec la souris

    va faloir réorganiser le menu pour pouvoir voir quelle set l'orientation
"""
def PARAM(): # paramèttres

    global RES,PARA,b,l,CL,BLRG,k,TLA,BONUS1,BONUS2,MPerso,BLO,BLD,BLG,LSM,LSMG,TAILLELX,TAILLELY,pl,REUSSI,LBLLABY,LBBBN,COORDSBATBLOC,COORDSBAT

    k = 0
    REUSSI = False

    for i in range(len(LSMG)): # sert a svoir les labys enregistrés
        if LSMG[i][0][0] == TX and  LSMG[i][0][1] == TX:
            LSM = LSMG[i]
            LSM.pop(0)

    PARA = Tk()
    PARA.title("Paramètres")

    LBLLABY = LabelFrame(PARA, text="LABYRINTHE", padx=5, pady=5) # frame pour le laby pour affichage rapide
    LBLLABY.grid(row=1, column=0,columnspan = 1,sticky = N,padx = 5,pady = 6)

    LBBBN = LabelFrame(PARA, text="BATAILLE NAVALE", padx=5, pady=5) # frame pour le laby pour affichage rapide
    #LBLBN.grid(row=1, column=0,columnspan = 1,sticky = NW,padx = 5,pady = 6)

    LSWITCH = Label(PARA, text="Labyrinthe \ Bataille navale") # label pour aficher les choix du switch en haut
    LSWITCH.grid(row=0, column=0,sticky = NW,padx = 5,pady = 6)

    BSWITCH = Button(PARA, text ="             ", relief=RAISED, command = SWITCH) # pour switch entre bataille navale et laby
    BSWITCH.grid(row=0, column=0,padx = 5,pady = 6)

    # LABY !!!!

    LBLF = LabelFrame(LBLLABY, text="Paramètres généraux", padx=5, pady=5) # paramètres
    LBLF.grid(row=0, column=0,sticky = NW,padx = 5,pady = 6)

    LBLCA = LabelFrame(LBLLABY, text="Labyrinthe", padx=5, pady=5)
    LBLCA.grid(row=0, column=1,rowspan = 3,sticky = NW,padx = 5,pady = 6)

    LBLC = LabelFrame(LBLLABY, text="Paramètres labyrinthe", padx=5, pady=5)
    LBLC.grid(row=1, column=0,sticky = NW,padx = 5,pady = 6)

    LBLT = LabelFrame(LBLLABY, text="Taille Labyrinthe", padx=5, pady=5)
    LBLT.grid(row=2, column=0,sticky = NW,padx = 5,pady = 6)

    LBLL = LabelFrame(LBLLABY, text="Lancement", padx=5, pady=5)
    LBLL.grid(row=3, column=0,sticky = NW,padx = 5,pady = 6)

    b = [Button(LBLF, text ="             ", relief=RAISED, command = B0), # b[0] RES
    Button(LBLF, text ="             ", relief=RAISED, command = B1), # b[1] Couleu
    Button(LBLF, text ="             ", relief=RAISED, command = B2), # b[2] Alea
    Button(LBLF, text ="             ", relief=SUNKEN, command = B3), # b[3] REGE
    Button(LBLF, text ="             ", relief=SUNKEN, command = B4), # b[4] BONUS
    Button(LBLF, text ="             ", relief=RAISED, command = B5), # b[5] BONAL
    Button(LBLF, text ="             ", relief=RAISED, command = B6)  # b[6] MULTI
    ]

    l = [Label(LBLF, text="Recommencer quand tu te cogne au mur", bg="red"), #l[0]
    Label(LBLF, text="Mode Aveugle", bg="red"), #l[1]
    Label(LBLF, text="Labyrinthe Aléatoire"),  #l[2]
    Label(LBLF, text="Regénérer en fin", bg="green"), #l[3]
    Label(LBLF, text="Aller chercher les Bonus", bg="green"), #l[4]
    Label(LBLF, text="Bonus aléatoire", bg="red"), #l[5]
    Label(LBLF, text="Mode multijoueur", bg="red"), #l[6]
    ]

    for i in range(len(l)):
        l[i].grid(row=i, column=1,padx = 5,pady = 6) # affichage des labels
        b[i].grid(row=i, column=2,padx = 5,pady = 6) # affichage des boutons

    CL = Canvas(LBLCA, width = TX * MF, height = TY * MF, bg ="black")
    CL.grid(row=CCL[0], column=CCL[1], columnspan=CCL[3],rowspan=CCL[2],padx = 5,pady = 5,sticky=NW) # affichage de la prévisualisation du laby
    # Canvas

    gen()

    BLRG = Button(LBLC, text ="Re-generer", relief=GROOVE, command = REgen)
    BLRG.grid(row=CBLRG[0], column=CBLRG[1],padx = 5,pady = 5)
    #regenerer
    BLO = Button(LBLC, text ="obtenir", relief=GROOVE, command = obtenir) # sert a obtenir le labyrinte pour l'enregister
    BLO.grid(row=CBLO[0], column=CBLO[1],padx = 5,pady = 5)
    #obtenir
    BLD = Button(LBLC, text ="   >   ", relief=GROOVE, command = droite) # va au laby suivant
    BLG = Button(LBLC, text ="   <   ", relief=GROOVE, command = gauche) # laby avant

    BLA = Button(LBLT, text ="Actualiser", relief=GROOVE, command = Actualiser)
    BLA.grid(row=0, column=2,padx = 5,pady = 5)

    Button(LBLL, text ="Jouer", relief=GROOVE, command = lance).grid(row=0, column=0,padx = 5,pady = 5) # lance la partie
    Button(LBLL, text ="créateur de labyrinthe", relief=GROOVE, command = créa).grid(row=0, column=1,padx = 5,pady = 5) # lance le créateur de labyrinthe

    TAILLELX = IntVar()
    TAILLELX.set(TX)
    TAILLELY = IntVar()
    TAILLELY.set(TY)

    ELX = Entry(LBLT, textvariable=TAILLELX, width=5).grid(row=0, column=0,padx = 5,pady = 5)
    ELY = Entry(LBLT, textvariable=TAILLELY, width=5).grid(row=0, column=1,padx = 5,pady = 5)

    TLA = Label(PARA, text="")# il y a que moi qui sait a quoi ca sert ! ( pour faire des test )
    #TLA.grid(row=0, column=3,columnspan = 4,padx = 5,pady = 5)

    PARA.resizable(width=False, height=False) # sert a ne pas pouvor éditer la taille de la fenetre des paramètres

    # pour remettre les anciens paramètres et les aficher
    if RES == True: # changement 2 fois a chaque fois je sais pas pourquoi ca marche mais ca marche
        B0()
        B0()

    if Couleu == "black":
        B1()
        B1()

    if Alea == False:
        B2()
        B2()

    if REGE == False:
        B3()
        B3()

    if BONUS == False:
        B4()
        B4()

    if BONAL == False:
        B5()
        B5()

    if MULTI == False:
        B6()
        B6()

    murs2() # affiche les murs dans la prévisualisation

    # bataille navalle

    global LBBF,LBBCA,LBBC,LBBT,LBBL,CB,bB,lB,MURSBAT,CHANGE,TAILLEBX,TAILLEBY

    Button(LBBBN, text ="Jouer", relief=GROOVE,).grid(row=0, column=0,padx = 5,pady = 5) # rajouter une commande pour lancer

    LBBF = LabelFrame(LBBBN, text="Paramètres généraux", padx=5, pady=5) # paramètres
    LBBF.grid(row=0, column=0,sticky = NW,padx = 5,pady = 6)

    LBBCA = LabelFrame(LBBBN, text="Bataille Navale", padx=5, pady=5)
    LBBCA.grid(row=0, column=1,rowspan = 3,sticky = NW,padx = 5,pady = 6)

    LBBT = LabelFrame(LBBBN, text="Taille Bataille", padx=5, pady=5)
    LBBT.grid(row=1, column=0,sticky = NW,padx = 5,pady = 6)

    LBBJ = LabelFrame(LBBBN, text="Paramèttres Joueurs", padx=5, pady=5)
    LBBJ.grid(row=2, column=0,sticky = NW,padx = 5,pady = 6)

    LBBL = LabelFrame(LBBBN, text="Lancement", padx=5, pady=5)
    LBBL.grid(row=3, column=0,sticky = NW,padx = 5,pady = 6)

    CB = Canvas(LBBCA, width = TBX * MBF - 4, height = TBY * MBF - 4, bg ="black")# Canvas
    CB.grid(row=0, column=0,padx = 5,pady = 5,sticky=NW) # affichage de la prévisualisation du laby

    CB.bind("<Button-1>", Mouvbat) # changer de place les bateau
    CB.bind("<Button-3>", Changsens) # pour changer de sens le bateau

    Button(LBBL, text = "Jouer", relief=GROOVE,command = lanceB).grid(row=0, column=0,padx = 5,pady = 5)

    BBRG = Button(LBBJ, text ="Re-generer aliés", relief=GROOVE, command = REGENBAlies)
    BBRG.grid(row=1, column=0,padx = 5,pady = 5)

    BBRGADV = Button(LBBJ, text ="Re-generer adversaire", relief=GROOVE, command = REGENBADV)
    BBRGADV.grid(row=2, column=0,padx = 5,pady = 5)

    BBVB = Button(LBBJ, text ="Voir bateaux aliés", relief=GROOVE, command = afficheCB)
    BBVB.grid(row=1, column=1,padx = 5,pady = 5)

    BBVBADV = Button(LBBJ, text ="Voir bateau adverses", relief=GROOVE, command = afficheCB2)
    BBVBADV.grid(row=2, column=1,padx = 5,pady = 5)

    TAILLEBX = IntVar()
    TAILLEBX.set(TX)
    TAILLEBY = IntVar()
    TAILLEBY.set(TY)

    EBX = Entry(LBBT, textvariable=TAILLEBX, width=5).grid(row=0, column=0,padx = 5,pady = 5)
    EBY = Entry(LBBT, textvariable=TAILLEBY, width=5).grid(row=0, column=1,padx = 5,pady = 5)


    BBA = Button(LBBT, text ="Actualiser", relief=GROOVE, command = ActualiserB).grid(row=0, column=2,padx = 5,pady = 5)

    for i in range(1,TBX + 1): # création de tous les murs pour les X
        for j in range(1,TBY + 1): # pour les Y
            if j < TBY:
                MURSBAT.append([i,j,"h"])
            if i < TBX:
                MURSBAT.append([i,j,"v"])

    for i in range(0,len(MURSBAT)):
        if MURSBAT[i][2] == "v": # verticale
            CB.create_line((MURSBAT[i][0])*MBF,(MURSBAT[i][1]-1)*MBF,(MURSBAT[i][0])*MBF,(MURSBAT[i][1])*MBF,width=1,fill="white")
        else: # horizontale
            CB.create_line((MURSBAT[i][0]-1)*MBF,(MURSBAT[i][1])*MBF,(MURSBAT[i][0])*MBF,(MURSBAT[i][1])*MBF,width=1,fill="white")

    bB = [Button(LBBF, text ="             ", relief=GROOVE, command = BN0), # b[0] VSIA
    Button(LBBF, text ="             ", relief = SUNKEN, command = BN1), # b[1] BATPAR
    Button(LBBF, text ="             ", relief = GROOVE, command = BN2), # b[2] quelJ
    Button(LBBF, text ="             ", relief = SUNKEN, command = BN3), # b[3] TROMPE ( a faire la fontion )
    Button(LBBF, text ="             ", relief = GROOVE, command = BN4), # b[4] NIVEAUIA
    ]

    lB = [Label(LBBF, text="Contre L'IA"), #l[0]
    Label(LBBF, text="Choix différents bateaux", bg="green"), #l[1] sert a choisir quels bateau on veut
    Label(LBBF, text="Le joueur 1 commence"),  #l[2]
    Label(LBBF, text="Droit de se tromper", bg="green"),  #l[3] si on clique sur une case déja cliquée cela compte quand mème
    Label(LBBF, text="NIVEAU SIMPLE"),  #l[4]
    ]

    for i in range(len(lB)):
        if i != 2 and i != 1:
            lB[i].grid(row=i, column=1,padx = 5,pady = 6) # affichage des labels
            bB[i].grid(row=i, column=2,padx = 5,pady = 6) # affichage des boutons

    REGENBAlies()
    REGENBADV()

    if CHANGE == True: # si on finit une bataille navale et que l'on veut revoir les paramètres
        SWITCH()
        SWITCH()
        CHANGE = False

    PARA.mainloop() # sert a garder la fenetre active

def SWITCH(): # switch entre la laby et et la bataille navale dans le menu

    global LABON, LBLLABY , LBBBN , CB

    if LABON == True:
        LBLLABY.grid_forget()
        LBBBN.grid(row=1, column=0,columnspan = 1,sticky = NW,padx = 5,pady = 6)
        LABON = False
        CB.focus_set()
    else:
        LBLLABY.grid(row=1, column=0,columnspan = 1,sticky = NW,padx = 5,pady = 6)
        LBBBN.grid_forget()
        LABON = True

def LABY(): # Creation de la fenetre principale

    global Canevas,LM,Pos,RES,Perso,t1,fenetre,k,BON1,BON2,Cercle1,Cercle2,MC,LMG,LB1,LB2,Pos2,Canevas2,Cercle21,Cercle22,Perso2,BON21,BON22,MC2

    BON1 = False # les bonus ne sont pas pris
    BON2 = False
    BON21 = False # les bonus ne sont pas pris du mode multi
    BON22 = False

    MC = 0 # murs cognés 0
    MC2 = 0

    if k == True and MODECFIN == False: # si on a déja fait une partie
        if REGE == True:
            gen()
            if BONAL == True:
                LB1 = [randint(1,TX),randint(1,TY)] # coordonnées des bonus
                LB2 = [randint(1,TX),randint(1,TY)] # coordonnées des bonus
    else: # si on a pas déja fait une partie
        k = True

    fenetre = Tk()
    fenetre.title("Labyrinthe")

    Largeur = TX*F-FT
    Hauteur = TY*F-FT

    Canevas = Canvas(fenetre, width = Largeur, height = Hauteur, bg ="black")
    Canevas.focus_set()# met le canevas en pricipal
    Canevas.bind("<Key>",Clavier) # bind toutes les touches a la fonction clavier

    Canevas.grid(row = 1,column = 1,padx = 5, pady = 5) #  affiche le canevas

    # position absolue initiale du carre
    # pos[0] correspond a l'ancien PosaX
    # pos[1] correspond a l'ancien PosaY
    # pos[2] correspond a l'ancien PosX
    # pos[3] correspond a l'ancien PosY
    Pos = [1,1] # coordonnées de base
    Pos.append(Pos[0]/2)
    Pos.append(Pos[1]/2)

    if MODEC == False:
        for i in range(0,len(LM)): # création des murs
            if LM[i][2] == "v": # verticale
                Canevas.create_line((LM[i][0])*F,(LM[i][1]-1)*F,(LM[i][0])*F,(LM[i][1])*F,width=2,fill=coul)
            else: # horizontals
                Canevas.create_line((LM[i][0]-1)*F,(LM[i][1])*F,(LM[i][0])*F,(LM[i][1])*F,width=2,fill=coul)

        if BONUS == 1:
            Cercle1 = Canevas.create_oval((LB1[0]-1)*F+FT,(LB1[1]-1)*F+FT,LB1[0]*F-FT,LB1[1]*F-FT,fill = "blue")
            Cercle2 = Canevas.create_oval((LB2[0]-1)*F+FT,(LB2[1]-1)*F+FT,LB2[0]*F-FT,LB2[1]*F-FT,fill = "blue")

    Perso = Canevas.create_rectangle(Pos[2],Pos[3],Pos[2]+F-FT,Pos[3]+F-FT,width=1,outline="black",fill=Couleu) # création du carré

    if MODEC == False:

        Button(fenetre, text ="Quitter", command = fenetre.destroy, relief=GROOVE).grid(row = 2,column = 1,sticky = W,padx=5,pady=5)
        if MODECFIN == False:
            if MULTI == True:
                Button(fenetre, text ="Obtenir", command = obtenir, relief=GROOVE).grid(row = 2,column = 2,sticky = E,padx=5,pady=5)
            else:
                Button(fenetre, text ="Obtenir", command = obtenir, relief=GROOVE).grid(row = 2,column = 1,sticky = E,padx=5,pady=5)

        t1 = time()
    else:
        Button(fenetre, text ="Terminer", command = Terminer).grid(row = 2,column = 1,padx=5,pady=5)
        Label(fenetre, text ="Bas = 2 ; Gauche = 1 ; Haut = 5 ; droite = 3").grid(row = 2,column = 2,padx=5,pady=5)
    if MULTI == True:

        Canevas2 = Canvas(fenetre, width = Largeur, height = Hauteur, bg ="black")
        Canevas2.grid(row = 1,column = 2,padx = 5, pady = 5) #  affiche le canevas

        # position absolue initiale du carre
        # pos[0] correspond a l'ancien PosaX
        # pos[1] correspond a l'ancien PosaY
        # pos[2] correspond a l'ancien PosX
        # pos[3] correspond a l'ancien PosY
        Pos2 = [1,1] # coordonnées de base
        Pos2.append(Pos[0]/2)
        Pos2.append(Pos[1]/2)

        if MODEC == False:
            for i in range(0,len(LM)): # création des murs
                if LM[i][2] == "v": # verticale
                    Canevas2.create_line((LM[i][0])*F,(LM[i][1]-1)*F,(LM[i][0])*F,(LM[i][1])*F,width=2,fill=coul)
                else: # horizontals
                    Canevas2.create_line((LM[i][0]-1)*F,(LM[i][1])*F,(LM[i][0])*F,(LM[i][1])*F,width=2,fill=coul)

            if BONUS == 1:
                Cercle21 = Canevas2.create_oval((LB1[0]-1)*F+FT,(LB1[1]-1)*F+FT,LB1[0]*F-FT,LB1[1]*F-FT,fill = "blue")
                Cercle22 = Canevas2.create_oval((LB2[0]-1)*F+FT,(LB2[1]-1)*F+FT,LB2[0]*F-FT,LB2[1]*F-FT,fill = "blue")

        Perso2 = Canevas2.create_rectangle(Pos[2],Pos[3],Pos[2]+F-FT,Pos[3]+F-FT,width=1,outline="black",fill=Couleu) # création du carré

    fenetre.resizable(width=False, height=False)

    if MODEC == True and MULTI == False:
        murscréa()

    fenetre.mainloop()

def gen(): # générateur

    global TX,TY,MM,LM,OR,h,LMG,CL

    LM = [] # liste de tous les murs
    MM = [] # liste de liste (matrice) des zones de chaques murs
    c = 0 # nombre de murs crees
    b = 0 # nombre de se pour le test
    h = False

    for i in range(1,TX + 1): # création de tous les murs pour les X
        for j in range(1,TY + 1): # pour les Y
            if j < TY:
                LM.append([i,j,"h"])
            if i < TX:
                LM.append([i,j,"v"])

    for j in range(1,TY+1):
        for i in range(1,TX+1):
            MM.append([[i,j]])

    murs2()

    while c < TX * TY - 1:

        P1 = None
        P2 = None

        b += 1

        OR = randint(1,2) # 1 = horizontal 2 = vertical

        if OR == 1:# définit l'orientation du mur
            OR = "h"
        else:
            OR = "v"

        if OR == "h": # prend les cotés disponibles en fonction de l'orientation du mur
            MX = randint(1,TX) # coordonées x du mur
            MY = randint(1,TY-1) # coordonnées y du mur
        else:
            MX = randint(1,TX-1) # coordonées x du mur
            MY = randint(1,TY) # coordonnées y du mur

        if ([MX,MY,OR] in LM) == True: # teste si le mur est déja suprimé
            if OR == "h": # le mur est horizontal
                for i in range(len(MM)): # teste si les deux murs ne sont pas dans la meme zone
                    if [MX,MY] in MM[i]: # problème
                        P1 = i # position case au dessus du mur
                    if [MX,MY+1] in MM[i]:
                        P2 = i # position case en dessous du mur

            else: # le mur est vertival
                for i in range(len(MM)): # teste si les deux murs ne sont pas dans la meme zone
                    if [MX,MY] in MM[i]:#case a gauche du mur
                        P1 = i # position case a gauche du mur
                    if [MX + 1,MY] in MM[i]:#case a droite du mur
                        P2 = i # position case a droite du mur

        if P1 == P2 and P1 != None and "POUR UN TEST" == 0: # si c'est dans la mème zone le signale
            print("Mème zone")

        elif P1 == None and "POUR UN TEST" == 0:# pour des tests
            print("Mur déja suprimé")

        elif P1 != P2 and P1 != None and P2 != None: # si ils ne sont pas dans le mème zone et que le mur n'est pas suprimé

            MM[P1].extend(MM[P2])# ajoute P2 a P1
            MM[P1].sort()
            del MM[P2] # puis suprime P2

            LM.remove([MX,MY,OR])#suprime le mur de la liste des murs

            if OR == "v": # vertical
                CL.create_line((MX)*MF,(MY-1)*MF + 1,(MX)*MF,(MY)*MF,width=1,fill="black")
            else: # horizontal
                CL.create_line((MX-1)*MF +1,(MY)*MF,(MX)*MF,(MY)*MF,width=1,fill="black")

            PARA.update_idletasks()
            PARA.update()

            c += 1# compte le nombre de murs crées

        if b > 100000: # si vraiment le programe galère xD

            print("forcé")
            break
    LMG = LM

def obtenir(): # fonction pour onbtinir le laby généré aléatoirement
    global h

    if h == False: # il n'as pas été print
        print("Labyrinthe : ",LM)
        h = True

def REgen(): # sert a regénérer un labyronthe et l'aficher dans la prévisualisation
    gen()
    murs2()

def Actualiser():
    global TX,TY,CL,LB1,LB2,MF,F,FX,FY,LSM

    if TX != TAILLELX.get() or TY != TAILLELY.get():
        TX = TAILLELX.get()
        TY = TAILLELY.get()

        LSM = None

        MF = 450 / TY # mini facteur pour la prévisualisation

        CL.configure(width = TX * MF, height = TY * MF)

        FX = 1000 / TX # calcule le facteur optimal pour une taille de labyrinthe donnée
        if MULTI == False:
            FY = 800 / TY
        else:
            FY = 600 / TY

        F = min(FX , FY) # prend la valeur minimal pour ajuster a la taille de la fenetre

        for i in range(len(LSMG)): # sert a svoir les labys enregistrés
            if LSMG[i][0][0] == TX and  LSMG[i][0][1] == TX:
                LSM = LSMG[i]
                LSM.pop(0)

        if Alea == False:
            B2()

        LB1 = [1,TY] # coordonnées des bonus
        LB2 = [TX,1] # coordonnées des bonus

        REgen()

def droite(): # doit changer de labyrinthe aléatoire pour qu'il aille au suivant
    global I,LM

    I += 1

    if I > len(LSM) - 1:
        I = 0

    LM = LSM[I]

    murs2()

def gauche(): # doit changer de labyrinthe aléatoire pour qu'il aille au précédent
    global I,LM

    I -= 1

    if I < 0:
        I = len(LSM) - 1

    LM = LSM[I]

    murs2()

def lance(): # fonction pour lancer la labyronthe en lui mème

    PARA.destroy() # ferme la fenetre de paramètres

    LABY() # lance la fonction laby

def créa(): # active le mode création
    global MODEC, TLM

    MODEC = True

    lance()

def FIN(): # fonction quand on est arrivé a la fin
    global Pos,fenetre

    t2 = time() # finile chrono
    # le \n sert a sauter une ligne
    if askyesno("Recommencement","Vous avez mis " + str(int(t2-t1))+"s\net cogné "+str(MC)+" murs.\nVoulez vous recommencer ?") == False: # non
        showinfo("Non ?", "Tant pis...")
        fenetre.destroy()
    else: # oui a faire
        if askyesno("Paramètres", "Voulez-vous revoir vos paramètres ?") == False: # non
            showinfo("Vous n'allez pas revoir vos paramètres", "Vous recommencerez au debut!")
            fenetre.destroy()
            LABY()
        else:
            showinfo("Vous allez revoir vos paramètres", "Révision des paramètres !")
            fenetre.destroy()
            PARAM()

def Terminer(): # termine le mode création
    global MODEC,LM,MODECFIN,BONUS

    fenetre.destroy()

    MODEC = False
    MODECFIN = True

    BONUS = False

    LM = TLM

    LABY()

    BONUS = True

    if REUSSI == True: # si on a fini le labyrinthe créé le print pour pouvoir l'enregisrer
        print(TLM)

def murs2():
    global LM, CL,BONUS1,BONUS2,MPerso
    CL.delete(ALL) # suprime tout les murs du canvas
    # création les murs
    for i in range(0,len(LM)):
        if LM[i][2] == "v": # verticale
            CL.create_line((LM[i][0])*MF,(LM[i][1]-1)*MF,(LM[i][0])*MF,(LM[i][1])*MF,width=1,fill=coul)
        else: # horizontale
            CL.create_line((LM[i][0]-1)*MF,(LM[i][1])*MF,(LM[i][0])*MF,(LM[i][1])*MF,width=1,fill=coul)
    if BONUS == True:
        BONUS1 = CL.create_oval((LB1[0]-1)*MF+1,(LB1[1]-1)*MF+1,LB1[0]*MF-1,LB1[1]*MF-1,fill = "blue")
        BONUS2 = CL.create_oval((LB2[0]-1)*MF+1,(LB2[1]-1)*MF+1,LB2[0]*MF-1,LB2[1]*MF-1,fill = "blue")
    MPerso = CL.create_rectangle(0,0,MF-1,MF-1,fill = Couleu) # recréation

def murscréa(): # fonction pour le mode création
    global TLM, Canevas,Perso
    Canevas.delete(ALL) # suprime tout les murs du canvas
    # création les murs
    for i in range(0,len(TLM)): # création des murs
        if TLM[i][2] == "v": # verticals
            Canevas.create_line((TLM[i][0])*F,(TLM[i][1]-1)*F,(TLM[i][0])*F,(TLM[i][1])*F,width=2,fill=coul)
        else: # horizontals
            Canevas.create_line((TLM[i][0]-1)*F,(TLM[i][1])*F,(TLM[i][0])*F,(TLM[i][1])*F,width=2,fill=coul)
    Perso = Canevas.create_rectangle(Pos[2], Pos[3], Pos[2] + F - FT, Pos[3] + F - FT,fill = Couleu) # recréation

def Couleur(): # change la couleur du perso
    global Perso,Couleu,Canevas
    if Couleu == "black":
        Couleu = "yellow"
        Canevas.itemconfig(Perso,fill=Couleu)
    else:
        Couleu = "black"
        Canevas.itemconfig(Perso,fill=Couleu)

def BATAILLE():

    global fenetreB,CanevasB,BOUTONB,LTIRADV,NBTIRTOUCHE,NBTIRTOUCHEADV,COORDTIR,TIRTOUCHEIA,BOUTONB2

    fenetreB = Tk()
    fenetreB.title("Bataille Navale")

    LargeurB = TBX*FB
    HauteurB = TBY*FB

    BOUTONB = []
    BOUTONB2 = []
    LTIRADV = []

    NBTIRTOUCHE = 0
    NBTIRTOUCHEADV = 0

    COORDTIR = []
    TIRTOUCHEIA = []

    LBBBOUT = LabelFrame(fenetreB, text="Choix case a tirer") # label pour les boutons
    LBBBOUT.grid(row=0, column=0,sticky = NW,padx = 5,pady = 6)

    if VSIA == True: # si on jour contre une IA
        LBBCAB = LabelFrame(fenetreB, text="Adversaire") # Label pour la facilité de managing de l'espace dans la fenetre
        LBBCAB.grid(row=0, column=1,sticky = NW,padx = 5,pady = 6)

        CanevasB = Canvas(LBBCAB, width = LargeurB, height = HauteurB, bg ="black")
        CanevasB.grid(row = 0,column = 0,padx = 5, pady = 5) #  affiche le canevas

        for i in range(0,len(MURSBAT)):
            if MURSBAT[i][2] == "v": # verticale
                CanevasB.create_line((MURSBAT[i][0])*FB,(MURSBAT[i][1]-1)*FB,(MURSBAT[i][0])*FB,(MURSBAT[i][1])*FB,width=1,fill="white")
            else: # horizontale
                CanevasB.create_line((MURSBAT[i][0]-1)*FB,(MURSBAT[i][1])*FB,(MURSBAT[i][0])*FB,(MURSBAT[i][1])*FB,width=1,fill="white")

        Bateaux = []

        #COB [X,Y,orientation,taille]

        for i in range(len(COORDSBAT)):# affiche les bateaux
            if COORDSBAT[i][2] == "v": # si le abteau est horizontal
                COHX = COORDSBAT[i][0] - 1 # coordonnées points en haut a gauche
                COHY = COORDSBAT[i][1] - COORDSBAT[i][3]
            else: # si le bateau est vertical
                COHX = COORDSBAT[i][0] - COORDSBAT[i][3] # coordonnées points en haut a gauche
                COHY = COORDSBAT[i][1] - 1
            Bateaux.append(CanevasB.create_rectangle(COHX * FB,COHY * FB,COORDSBAT[i][0] * FB,COORDSBAT[i][1] * FB,width=1,outline="white",fill="blue"))

    else: # si on fait un 1v1
        LBBBOUT2 = LabelFrame(fenetreB, text="Choix case a tirer joueur 2") # label pour les boutons
        LBBBOUT2.grid(row=0, column=1,sticky = NW,padx = 5,pady = 6)

        for i in range(TBX): # Boutons du joueur 2
            BOUTONB2.append([])
            for j in range(TBY):
                BOUTONB2[i].append(Button(LBBBOUT2, text ="     ", relief = GROOVE, command = lambda x=(str(i)+str(j)):Tirer2(x)))
                BOUTONB2[i][j].grid(row=j, column=i,sticky = NW,padx = 5,pady = 6)

    for i in range(TBX): # affiche les boutons du joueur 1
        BOUTONB.append([])
        for j in range(TBY):
            BOUTONB[i].append(Button(LBBBOUT, text ="     ", relief = GROOVE, command = lambda x=(str(i)+str(j)):Tirer(x)))
            BOUTONB[i][j].grid(row=j, column=i,sticky = NW,padx = 5,pady = 6)

def GENBAT():
    global COB,NBBLOCS,CBADV,COBND

    refaire = True
    while refaire == True:
        refaire = False
        COBND = [] # coordonnes des blocs pas disponibles
        COB = [] # coordonnes bateaux
        for i in range(5): # pour chaque bateau lui cherche des coordonnes aléatoire
            #coords x, y, orientation, taille du bateau
            OBR = randint(1,2)# orientation bateau

            COTBND = [] # coordonnes temporaires bateau non disponible

            if i == 0: # le premier bateaux, le plus grand etc
                TAILLEBAT = 5 # porte-avion
                if OBR == 1: # obr = orientation bateau
                    OBR = "h" #mur horizontal
                    RANBX = randint(5,TBX) # fait un random en fonction de l'orientation du mur et de la taille du bateau
                    RANBY = randint(1,TBY) # coordonnes Y
                    for j in range(TAILLEBAT): # regarde toutes les cases qui sont occupées par le bateau
                        COTBND.append([RANBX - j,RANBY]) # sert a tester si il y a deja un bateaux qi occupe les case la ou il y a le nouveau bateau
                        if ([RANBX - j,RANBY] in COBND) == True: # fais le test
                            refaire = True # si il y a un autre bateau refait
                else:
                    OBR = "v"
                    RANBX = randint(1,TBX)
                    RANBY = randint(5,TBY)
                    for j in range(TAILLEBAT):
                        COTBND.append([RANBX,RANBY - j])
                        if ([RANBX,RANBY - j] in COBND) == True:
                            refaire = True
                COBND.extend(COTBND)

            elif i == 1:
                TAILLEBAT = 4
                if OBR == 1: # obr = orientation bateau
                    OBR = "h"
                    RANBX = randint(4,TBX)
                    RANBY = randint(1,TBY)
                    for j in range(TAILLEBAT):
                        COTBND.append([RANBX - j,RANBY]) # sert a tester si il y a deja un bateaux
                        if ([RANBX - j,RANBY] in COBND) == True:
                            refaire = True
                else:
                    OBR = "v"
                    RANBX = randint(1,TBX)
                    RANBY = randint(4,TBY)
                    for j in range(TAILLEBAT):
                        COTBND.append([RANBX,RANBY - j])
                        if ([RANBX,RANBY - j] in COBND) == True:
                            refaire = True

                COBND.extend(COTBND)
            elif i == 2:
                TAILLEBAT = 3
                if OBR == 1: # obr = orientation bateau
                    OBR = "h"
                    RANBX = randint(3,TBX)
                    RANBY = randint(1,TBY)
                    for j in range(TAILLEBAT):
                        COTBND.append([RANBX - j,RANBY]) # sert a tester si il y a deja un bateaux
                        if ([RANBX - j,RANBY] in COBND) == True:
                            refaire = True
                else:
                    OBR = "v"
                    RANBX = randint(1,TBX)
                    RANBY = randint(3,TBY)
                    for j in range(TAILLEBAT):
                        COTBND.append([RANBX,RANBY - j])
                        if ([RANBX,RANBY - j] in COBND) == True:
                            refaire = True
                COBND.extend(COTBND)
            elif i == 3:
                TAILLEBAT = 3
                if OBR == 1: # obr = orientation bateau
                    OBR = "h"
                    RANBX = randint(3,TBX)
                    RANBY = randint(1,TBY)
                    for j in range(TAILLEBAT):
                        COTBND.append([RANBX - j,RANBY]) # sert a tester si il y a deja un bateaux
                        if ([RANBX - j,RANBY] in COBND) == True:
                            refaire = True
                else:
                    OBR = "v"
                    RANBX = randint(1,TBX)
                    RANBY = randint(3,TBY)
                    for j in range(TAILLEBAT):
                        COTBND.append([RANBX,RANBY - j])
                        if ([RANBX,RANBY - j] in COBND) == True:
                            refaire = True
                COBND.extend(COTBND)
            else:
                TAILLEBAT = 2
                if OBR == 1: # obr = orientation bateau
                    OBR = "h"
                    RANBX = randint(2,TBX)
                    RANBY = randint(1,TBY)
                    for j in range(TAILLEBAT):
                        COTBND.append([RANBX - j,RANBY]) # sert a tester si il y a deja un bateaux
                        if ([RANBX - j,RANBY] in COBND) == True:
                            refaire = True
                else:
                    OBR = "v"
                    RANBX = randint(1,TBX)
                    RANBY = randint(2,TBY)
                    for j in range(TAILLEBAT):
                        COTBND.append([RANBX,RANBY - j])
                        if ([RANBX,RANBY - j] in COBND) == True:
                            refaire = True
                COBND.extend(COTBND)
            COB.append([RANBX,RANBY,OBR,TAILLEBAT])

    # COB = coordonnes du bateau en mode [X,Y,OR,TAille]
    # COBND = coordonnes des cases occupés par les bateaux

    NBBLOCS = 0 # nombres de blocs occupés par le bateau
    for i in range(len(COB)):
        NBBLOCS += COB[i][3]

def Tours(Joueur): # fait le tour a tour pour l'IA ou le 1v1

    global quelJ

    if Joueur == 1:# premier joueur a joué
        if VSIA == True:
            if TIREFFECTUE == True:
                TIRADV()
        else:
            if quelJ == 1: # quelJ sert a savoir c'est a quel joueur de jouer
                quelJ = 2# au joueur 2 de jouer
    else:# a joueur 2 de jouer
        if VSIA == False:
            if quelJ == 2:
                quelJ = 1# au joueur 1 de jouer

    if NBTIRTOUCHE == NBBLOCS: # si on a touche autant qu'il y a de cases de bateaux
        TerminerB(1)
    if NBTIRTOUCHEADV == NBBLOCS:
        TerminerB(2)

def ActualiserB():
    global TBX,TBY,CB,MBF,FB

    if TBX != TAILLEBX.get() or TY != TAILLEBY.get():
        TBX = TAILLEBX.get()
        TBY = TAILLEBY.get()

        MBF = 320 / TY # mini facteur pour la prévisualisation

        CB.configure(width = TBX * MBF, height = TBY * MBF)

        FBX = 400 / TX # calcule le facteur optimal pour une taille de labyrinthe donnée
        FBY = 400 / TY

        FB = min(FBX , FBY) # prend la valeur minimal pour ajuster a la taille de la fenetre

        REGENBAlies()

def afficheCB(): # sert a aficher les bateaux dans la prévisualisation
    global CB,Affiché

    CB.delete(ALL)
    Bateaux = []

    Affiché = 1

    for i in range(1,TBX + 1): # création de tous les murs pour les X
        for j in range(1,TBY + 1): # pour les Y
            if j < TBY:
                MURSBAT.append([i,j,"h"])
            if i < TBX:
                MURSBAT.append([i,j,"v"])

    for i in range(0,len(MURSBAT)):
        if MURSBAT[i][2] == "v": # verticale
            CB.create_line((MURSBAT[i][0])*MBF,(MURSBAT[i][1]-1)*MBF,(MURSBAT[i][0])*MBF,(MURSBAT[i][1])*MBF,width=1,fill="white")
        else: # horizontale
            CB.create_line((MURSBAT[i][0]-1)*MBF,(MURSBAT[i][1])*MBF,(MURSBAT[i][0])*MBF,(MURSBAT[i][1])*MBF,width=1,fill="white")

    for i in range(len(COORDSBAT)):# affiche les bateaux
        if COORDSBAT[i][2] == "v": # si le abteau est horizontal
            COHX = COORDSBAT[i][0] - 1 # coordonnées points en haut a gauche
            COHY = COORDSBAT[i][1] - COORDSBAT[i][3]
        else: # si le bateau est vertical
            COHX = COORDSBAT[i][0] - COORDSBAT[i][3] # coordonnées points en haut a gauche
            COHY = COORDSBAT[i][1] - 1
        Bateaux.append(CB.create_rectangle(COHX * MBF,COHY * MBF,COORDSBAT[i][0] * MBF,COORDSBAT[i][1] * MBF,width=1,outline="white",fill="blue"))

def afficheCB2(): # sert a aficher les bateaux dans la prévisualisation
    global CB,Affiché

    if VSIA == False:
        Affiché = 2
        CB.delete(ALL)
        Bateaux2 = []

        for i in range(1,TBX + 1): # création de tous les murs pour les X
            for j in range(1,TBY + 1): # pour les Y
                if j < TBY:
                    MURSBAT.append([i,j,"h"])
                if i < TBX:
                    MURSBAT.append([i,j,"v"])

        for i in range(0,len(MURSBAT)):
            if MURSBAT[i][2] == "v": # verticale
                CB.create_line((MURSBAT[i][0])*MBF,(MURSBAT[i][1]-1)*MBF,(MURSBAT[i][0])*MBF,(MURSBAT[i][1])*MBF,width=1,fill="white")
            else: # horizontale
                CB.create_line((MURSBAT[i][0]-1)*MBF,(MURSBAT[i][1])*MBF,(MURSBAT[i][0])*MBF,(MURSBAT[i][1])*MBF,width=1,fill="white")

        for i in range(len(COBADV)):# affiche les bateaux
            if COBADV[i][2] == "v": # si le abteau est horizontal
                COHX = COBADV[i][0] - 1 # coordonnées points en haut a gauche
                COHY = COBADV[i][1] - COBADV[i][3]
            else: # si le bateau est vertical
                COHX = COBADV[i][0] - COBADV[i][3] # coordonnées points en haut a gauche
                COHY = COBADV[i][1] - 1
            Bateaux2.append(CB.create_rectangle(COHX * MBF,COHY * MBF,COBADV[i][0] * MBF,COBADV[i][1] * MBF,width=1,outline="white",fill="blue"))

def Tirer(COORD): # fonction pour les tirs de bataille navalle

    global BOUTONB,NBTIRTOUCHE,CanevasB,NBTIRTOUCHEADV,COORDTIR,TIREFFECTUE

    if quelJ == 1:

        TEMP = [] # temporaire pour stocker les coordonnes du tir obtenues graces au coordonnes du bouton
        TIREFFECTUE = False

        for i in COORD: # pour les x et y fait un different item dans la liste
            TEMP.append(int(i))

        if ([TEMP[0]+1,TEMP[1]+1] in CBADV) == False: # si il n'y a pas de bateaux la où on tir
            BOUTONB[TEMP[0]][TEMP[1]].configure(bg="green")
            if ([TEMP[0],TEMP[1]] in COORDTIR) == False:
                COORDTIR.append([TEMP[0],TEMP[1]])
                if TROMPE == True: # si on a le droit de se tromper de cases
                    TIREFFECTUE = True
            if TROMPE == False: # si on a pas le droit de se tromper
                TIREFFECTUE = True
        else: # si il y a un bateau
            BOUTONB[TEMP[0]][TEMP[1]].configure(bg="red")
            if ([TEMP[0],TEMP[1]] in COORDTIR) == False:
                NBTIRTOUCHE += 1 # ajoute un au nombre de tirs touches
                COORDTIR.append([TEMP[0],TEMP[1]])
                if TROMPE == True: # si on a le droit de se tromper de cases
                    TIREFFECTUE = True
            if TROMPE == False: # si on a cliqué sur une case déja touchée
                TIREFFECTUE = True

        if TIREFFECTUE == True:
            Tours(1)

    else:
        print("pas a toi")

def Tirer2(COORD): # fonction pour les tirs de bataille navalle

    global BOUTONB,NBTIRTOUCHE,CanevasB,NBTIRTOUCHEADV,LTIRADV
    if quelJ == 2:
        TEMP = [] # temporaire pour stocker les coordonnes du tir obtenues graces au coordonnes du bouton
        TIREFFECTUE2 = False

        for i in COORD: # pour les x et y fait un different item dans la liste
            TEMP.append(int(i))

        if ([TEMP[0]+1,TEMP[1]+1] in COORDSBATBLOC) == False: # si il n'y a pas de bateaux la où on tir
            BOUTONB2[TEMP[0]][TEMP[1]].configure(bg="green")
            if ([TEMP[0],TEMP[1]] in LTIRADV) == False:
                LTIRADV.append([TEMP[0],TEMP[1]])
                if TROMPE == True: # si on a le droit de se tromper de cases
                    TIREFFECTUE2 = True
            if TROMPE == False: # si on a pas le droit de se tromper
                TIREFFECTUE2 = True
        else: # si il y a un bateau
            BOUTONB2[TEMP[0]][TEMP[1]].configure(bg="red")
            if ([TEMP[0],TEMP[1]] in LTIRADV) == False:
                NBTIRTOUCHEADV += 1 # ajoute un au nombre de tirs touches
                LTIRADV.append([TEMP[0],TEMP[1]])
                if TROMPE == True: # si on a le droit de se tromper de cases
                    TIREFFECTUE2 = True
            if TROMPE == False:
                TIREFFECTUE2 = True

        if TIREFFECTUE2 == True:
            Tours(2)

    else:
        print("pas a toi")

def TIRADV():
    global BOUTONB,NBTIRTOUCHE,CanevasB,NBTIRTOUCHEADV,TIRREUSSIIA,TIRTOUCHEIA
    TIRREUSSIIA = False

    if NIVEAUIA == 1: # NIVEAU tres simple total random
        IAX = randint(1,TBX) # coordonnes au hazard du tir de l'adversaire ( a améliorer pour qu'il tir autour des tirs qui ont touchés )
        IAY = randint(1,TBY)
        while ([IAX,IAY] in LTIRADV) == True: # tant que le tir n'as pas deja te tire continue de générer des nombres random
            IAX = randint(1,TBX)
            IAY = randint(1,TBY)
        LTIRADV.append([IAX,IAY]) # ajoute a la liste des tirs de l'ia le tir
        if([IAX,IAY] in COORDSBATBLOC) == True: # si il tire sur un de nos bateaux fait un carré rouge
            CanevasB.create_rectangle((IAX - 1) * FB,(IAY - 1) * FB,IAX * FB,IAY * FB,outline = "white",fill = "red")
            NBTIRTOUCHEADV += 1 # ajoute un tir touche par l'adversaire
        else: # si il ne touche pas
            CanevasB.create_rectangle((IAX - 1) * FB,(IAY - 1) * FB,IAX * FB,IAY * FB,outline = "white",fill = "green")
    elif NIVEAUIA == 2: # Niveau MOYEN marche pas ;(
        TIRREUSSIIA == False
        while TIRREUSSIIA == False:
            TEMPORAIRE = randint(1,10) # pour savoir si on prend une case aléatoire ou une case a coté d'un déja touchée
            print(TEMPORAIRE)
            if TEMPORAIRE > 7: # on fait un tir au hazard si c'est plus de 7
                IAX = randint(1,TBX) # coordonnes au hazard du tir de l'adversaire ( a améliorer pour qu'il tir autour des tirs qui ont touchés )
                IAY = randint(1,TBY)
                while ([IAX,IAY] in LTIRADV) == True: # tant que le tir n'as pas deja te tire continue de générer des nombres random
                    IAX = randint(1,TBX)
                    IAY = randint(1,TBY)
                LTIRADV.append([IAX,IAY]) # ajoute a la liste des tirs de l'ia le tir
                if([IAX,IAY] in COORDSBATBLOC) == True: # si il tire sur un de nos bateaux fait un carré rouge
                    CanevasB.create_rectangle((IAX - 1) * FB,(IAY - 1) * FB,IAX * FB,IAY * FB,fill = "red")
                    NBTIRTOUCHEADV += 1 # ajoute un tir touche par l'adversaire
                    TIRTOUCHEIA.append([IAX,IAY]) # ajoute un tir touché piur l'inteligence de l'IA
                    TIRREUSSIIA = True
                else: # si il ne touche pas
                    print(IAX,IAY)
                    CanevasB.create_rectangle((IAX - 1) * FB,(IAY - 1) * FB,IAX * FB,IAY * FB,fill = "green")
                    TIRREUSSIIA = True
            elif len(TIRTOUCHEIA) != 0: # si on peut tirer autour de TIRS déja touchés
                TESTTIRS = 0
                while TESTTIRS < 5 and TIRREUSSIIA == False:
                    i = randint(1,4)# chaque chifre corespond a une direction autour de la case touchée
                    if i == 1: # droite
                        X = 1
                        Y = 0
                    elif i == 2: # bas
                        X = 0
                        Y = 1
                    elif i == 3: # gauche
                        X = -1
                        Y = 0
                    elif i == 4: # haut
                        X = 0
                        Y = -1

                    #IAX = coordonnées X de la case touchée ( a faire ) + X
                    #IAY = coordonnées Y de la case touchée ( a faire aussi ) + Y

                    TESTTIRS += 1

                    if([IAX,IAY] in COORDSBATBLOC) == True: # si il tire sur un de nos bateaux fait un carré rouge
                        CanevasB.create_rectangle((IAX - 1) * FB,(IAY - 1) * FB,IAX * FB,IAY * FB,fill = "red")
                        NBTIRTOUCHEADV += 1 # ajoute un tir touche par l'adversaire
                        TIRTOUCHEIA.append([IAX,IAY]) # ajoute un tir touché piur l'inteligence de l'IA
                        LTIRADV.append([IAX,IAY]) # ajoute a la liste des tirs de l'ia le tir
                        TIRREUSSIIA = True
                    else: # si il ne touche pas mais qu'il tire quand meme
                        CanevasB.create_rectangle((IAX - 1) * FB,(IAY - 1) * FB,IAX * FB,IAY * FB,fill = "green")
                        LTIRADV.append([IAX,IAY]) # ajoute a la liste des tirs de l'ia le tir
                        TIRREUSSIIA = True

def NuméroBateau():# sert a définir le Numro du bateau pour chaques rectangle

    global OccupBAT

    OccupBAT = [[],[]]

    for i in range(len(COORDSBAT)):
        if COORDSBAT[i][2] == "h":
            for j in range(COORDSBAT[i][3]):
                OccupBAT[0].append([COORDSBAT[i][0]-j,COORDSBAT[i][1]])
                OccupBAT[1].append(i)
        if COORDSBAT[i][2] == "v":
            for j in range(COORDSBAT[i][3]):
                OccupBAT[0].append([COORDSBAT[i][0],COORDSBAT[i][1]-j])
                OccupBAT[1].append(i)

def NuméroBateau2():# sert a définir le Numro du bateau pour chaques rectangle

    global OccupBAT2

    OccupBAT2 = [[],[]]

    for i in range(len(COBADV)):
        if COBADV[i][2] == "h":
            for j in range(COBADV[i][3]):
                OccupBAT2[0].append([COBADV[i][0]-j,COBADV[i][1]])
                OccupBAT2[1].append(i)
        if COBADV[i][2] == "v":
            for j in range(COBADV[i][3]):
                OccupBAT2[0].append([COBADV[i][0],COBADV[i][1]-j])
                OccupBAT2[1].append(i)

def Mouvbat(event):# sert a bouger les bateaux

    global BATchoisi,Numbat,OccupBAT,COORDSBATBLOC,COORDSBAT,COBADV,Numbat2,CBADV,BATchoisi2

    COclic = [int(event.x/MBF)+1,int(event.y/MBF)+1]

    if Affiché == 1:
        if Numbat == None:
            Numbat =" Si tu vois ca c'est qu'il y a un bug"

        if (COclic in OccupBAT[0]) == True:
                Numbat = OccupBAT[1][OccupBAT[0].index(COclic)]# sert a savoir quelles sont les coordonnes du bateau ( recherche si on a bien clique sur un bateau, si oui va trouver sa poisition ( index ) et va la faire correspondre dans la liste ou il y a les numéros des bateau

        if (COclic in COORDSBATBLOC) == True: # si on clique sur un bateau
            if Numbat == BATchoisi[0]: # si on reclique sur le bateau
                BATchoisi[0] = None
                Numbat = None
                afficheCB()
            else: # si on ne clique pas sur un bateau déja séléctionné
                BATchoisi = [Numbat,COORDSBAT[Numbat][2]] # le 2 e argument sert a stocker l'orientation temporaire du bateau
                afficheCB()
                if COORDSBAT[BATchoisi[0]][2] == "v": # si le bateau est vertical
                    COBCX = COORDSBAT[BATchoisi[0]][0] - 1 # coordonnées points en haut a gauche
                    COBCY = COORDSBAT[BATchoisi[0]][1] - COORDSBAT[BATchoisi[0]][3] # COBCX coordonnes bateau choisi X
                else: # si le bateau est horizontal
                    COBCX = COORDSBAT[BATchoisi[0]][0] - COORDSBAT[BATchoisi[0]][3] # coordonnées points en haut a gauche
                    COBCY = COORDSBAT[BATchoisi[0]][1] - 1
                CB.create_rectangle(COBCX * MBF,COBCY * MBF,COORDSBAT[BATchoisi[0]][0] * MBF,COORDSBAT[BATchoisi[0]][1] * MBF,width=1,outline="white",fill="red")
        else:
            if BATchoisi[0] != None:
                Stockcoord = COORDSBAT
                if BATchoisi[1] == "h":# en fonction de l'orientation du bateau
                    if COclic[0] - COORDSBAT[Numbat][3] >= 0:
                        COORDSBAT[Numbat][0] = COclic[0]
                        COORDSBAT[Numbat][1] = COclic[1]
                        COORDSBAT[Numbat][2] = BATchoisi[1]
                elif BATchoisi[1] == "v":# en fonction de l'orientation du bateau
                    if COclic[1] - COORDSBAT[Numbat][3] >= 0:
                        COORDSBAT[Numbat][0] = COclic[0]
                        COORDSBAT[Numbat][1] = COclic[1]
                        COORDSBAT[Numbat][2] = BATchoisi[1]
                if blococcupés() == True:
                    afficheCB() # affiche mais tu le sais deja ca ^^
                    NuméroBateau() # pour remettre a jour le calcul du numéro des bateau en fonction de la case cliquée
                    blococcupés() # pour remettre a jour COORDSBATBLOC
                    Numbat = None
                    BATchoisi[0] = None
                else:
                    COORDSBAT = Stockcoord
            else:
                print("choisis un bateau")
    else:# si on a le joeur 2 affiché
        if Numbat2 == None:
            Numbat2 =" Si tu vois ca c'est qu'il y a un bug"

        if (COclic in OccupBAT2[0]) == True:
                Numbat2 = OccupBAT2[1][OccupBAT2[0].index(COclic)]# sert a savoir quelles sont les coordonnes du bateau ( recherche si on a bien clique sur un bateau, si oui va trouver sa poisition ( index ) et va la faire correspondre dans la liste ou il y a les numéros des bateau

        if (COclic in CBADV) == True: # si on clique sur un bateau
            if Numbat2 == BATchoisi2[0]: # si on reclique sur le bateau
                BATchoisi2[0] = None
                Numbat2 = None
                afficheCB2()
            else: # si on ne clique pas sur un bateau déja séléctionné
                BATchoisi2 = [Numbat2,COBADV[Numbat2][2]] # le 2 e argument sert a stocker l'orientation temporaire du bateau
                afficheCB2()
                if COBADV[BATchoisi2[0]][2] == "v": # si le bateau est vertical
                    COBCX = COBADV[BATchoisi2[0]][0] - 1 # coordonnées points en haut a gauche
                    COBCY = COBADV[BATchoisi2[0]][1] - COBADV[BATchoisi2[0]][3] # COBCX coordonnes bateau choisi X
                else: # si le bateau est horizontal
                    COBCX = COBADV[BATchoisi2[0]][0] - COBADV[BATchoisi2[0]][3] # coordonnées points en haut a gauche
                    COBCY = COBADV[BATchoisi2[0]][1] - 1
                CB.create_rectangle(COBCX * MBF,COBCY * MBF,COBADV[BATchoisi2[0]][0] * MBF,COBADV[BATchoisi2[0]][1] * MBF,width=1,outline="white",fill="red")
        else:
            if BATchoisi2[0] != None:
                Stockcoord2 = COBADV
                if BATchoisi2[1] == "h":# en fonction de l'orientation du bateau
                    if COclic[0] - COBADV[Numbat2][3] >= 0:
                        COBADV[Numbat2][0] = COclic[0]
                        COBADV[Numbat2][1] = COclic[1]
                        COBADV[Numbat2][2] = BATchoisi2[1]
                elif BATchoisi2[1] == "v":# en fonction de l'orientation du bateau
                    if COclic[1] - COBADV[Numbat2][3] >= 0:
                        COBADV[Numbat2][0] = COclic[0]
                        COBADV[Numbat2][1] = COclic[1]
                        COBADV[Numbat2][2] = BATchoisi2[1]
                if blococcupés2() == True:
                    afficheCB2() # affiche mais tu le sais deja ca ^^
                    NuméroBateau2() # pour remettre a jour le calcul du numéro des bateau en fonction de la case cliquée
                    blococcupés2() # pour remettre a jour COORDSBATBLOC
                    Numbat2 = None
                    BATchoisi2[0] = None
                else:
                    COBADV = Stockcoord2
            else:
                print("choisis un bateau")

def blococcupés():# sert a remettre quels blocs sont occupés apres un changement de place de bateau

    global COORDSBATBLOC

    Stockblocs = COORDSBATBLOC
    COORDSBATBLOC = []
    Remettre = False

    for i in range(len(COORDSBAT)): # pour chaque bateau
        for j in range(COORDSBAT[i][3]): # pour chaque case occupée par la bateau ( taille )
            if COORDSBAT[i][2] == "h": #
                COORDSBATBLOC.append([COORDSBAT[i][0]-j,COORDSBAT[i][1]])
            elif COORDSBAT[i][2] == "v": #
                COORDSBATBLOC.append([COORDSBAT[i][0],COORDSBAT[i][1]-j])

    for i in COORDSBATBLOC:
        if COORDSBATBLOC.count(i) != 1:
            Remettre = True

    if Remettre == True:# on doit refaire parce que ca se superpose
        COORDSBATBLOC = Stockblocs
        return(False)
    else:
        return(True)

def blococcupés2():# sert a remettre quels blocs sont occupés apres un changement de place de bateau

    global CBADV

    Stockblocs2 = CBADV
    CBADV = []
    Remettre = False

    for i in range(len(COBADV)): # pour chaque bateau
        for j in range(COBADV[i][3]): # pour chaque case occupée par la bateau ( taille )
            if COBADV[i][2] == "h": #
                CBADV.append([COBADV[i][0]-j,COBADV[i][1]])
            elif COBADV[i][2] == "v": #
                CBADV.append([COBADV[i][0],COBADV[i][1]-j])

    for i in CBADV:
        if CBADV.count(i) != 1:
            Remettre = True

    if Remettre == True:# on doit refaire parce que ca se superpose
        CBADV = Stockblocs2
        return(False)
    else:
        return(True)

def Changsens(event):# changer l'orientation du bateau choisi
    global COORDSBAT,BATchoisi,COBADV,BATchoisi2

    if Affiché == 1:
        if Numbat != None:
            print("Tourne le bateau",Numbat)
            if BATchoisi[1] == "h":
                COORDSBAT[Numbat][2] = "v"
                BATchoisi[1] = "v"
            else:
                COORDSBAT[Numbat][2] = "h"
                BATchoisi[1] = "h"
    else:
        if Numbat2 != None:
            print("Tourne le bateau",Numbat2)
            if BATchoisi2[1] == "h":
                COBADV[Numbat2][2] = "v"
                BATchoisi2[1] = "v"
            else:
                COBADV[Numbat2][2] = "h"
                BATchoisi2[1] = "h"


def lanceB(): # lance la bataille navale

    PARA.destroy() # ferme la fenetre de paramètres

    BATAILLE() # lance la bataille navale

def TerminerB(gagnant):
    global CHANGE

    if gagnant == 1:
        if VSIA == True:
            print("le joueur a gagné")
            TXTFIN = "le joueur a gagné"
        else:
            print("le joueur 1 a gagné")
            TXTFIN ="le joueur 1 a gagné"
    else: # si le joueur 2 ou l'ia a gagné
        if VSIA == True:
            print("L'IA a gagné")
            TXTFIN ="L'IA a gagné"
        else:
            print("Le joueur 2 a gagné")
            TXTFIN ="le joueur 2 a gagné"
    if askyesno("Recommencement",TXTFIN + "\nVoulez vous recommencer ?") == False: # non
        showinfo("Non ?", "Tant pis...")
        fenetreB.destroy()
    else: # oui a faire
        if askyesno("Paramètres", "Voulez-vous revoir vos paramètres ?") == False: # non
            showinfo("Vous n'allez pas revoir vos paramètres", "Vous recommencerez au debut!")
            fenetreB.destroy()
            BATAILLE()
        else:
            showinfo("Vous allez revoir vos paramètres", "Révision des paramètres !")
            fenetreB.destroy()
            CHANGE = True
            PARAM()

def REGENBAlies(): # regenerer les bateaux aliés
    global COORDSBAT,COORDSBATBLOC
    print("générere les bateau aliés")
    GENBAT()
    COORDSBAT = COB # coordonnes des bateau du joueur 1
    COORDSBATBLOC = COBND # coordonnes des blocs du bateaux du joueur 1
    NuméroBateau()
    afficheCB()

def REGENBADV(): # regenerer les bateaux adverses de l'IA ou J2
    global CBADV,COBADV
    print("génére les bateau adverses")
    GENBAT()
    CBADV = COBND # coordonnes bloc occupes par les bateaux énemis
    COBADV = COB # coordonnes bateaux [x,y,OR,T]
    if VSIA == False:
        afficheCB2()
    NuméroBateau2()

def BN0(): # contre l'ia ou en 1v1
    global VSIA,bB,lB

    if VSIA == False:
        lB[0].configure(text="Contre l'IA")
        VSIA = True # change la variable
        if Affiché == 2:
            afficheCB()
        lB[2].grid_forget()
        bB[2].grid_forget()
    else:
        lB[0].configure(text="1v1")
        VSIA = False
        lB[2].grid(row=2, column=1,padx = 5,pady = 6) # affichage des labels
        bB[2].grid(row=2, column=2,padx = 5,pady = 6) # affichage des boutons

def BN1(): # bateaux paramétrés
    global BATPAR,bB,lB

    if BATPAR == False:
        bB[1].configure(relief = SUNKEN) # sert a enfoncer le bouton
        lB[1].configure(bg="green")
        BATPAR = True # change la variable
    else:
        bB[1].configure(relief = RAISED)
        lB[1].configure(bg="red")
        BATPAR = False

def BN2(): # bateau aléatoires
    global quelJ,bB,lB

    if quelJ == 1:
        quelJ = 2 # change la variable
    else:
        quelJ = 1
    lB[2].configure(text = "Le joueur " + str(quelJ) + " commence")

def BN3():
    global TROMPE,bB,lB

    if TROMPE == False:
        bB[3].configure(relief = SUNKEN) # sert a enfoncer le bouton
        lB[3].configure(bg="green")
        TROMPE = True # change la variable
    else:
        bB[3].configure(relief = RAISED)
        lB[3].configure(bg="red")
        TROMPE = False

def BN4():
    global NIVEAUIA,lB

    if NIVEAUIA == 1 and 0 == 1: # pour chaque niveau d'IA
        lB[4].configure(text="NIVEAU MOYEN") # marche pas
        NIVEAUIA = 2
    elif NIVEAUIA == 2 and 0 == 1:
        lB[4].configure(text="NIVEAU DIFFICILE") # marche pas
        NIVEAUIA = 3
    else:
        lB[4].configure(text="NIVEAU SIMPLE")
        NIVEAUIA = 1

def B0(): # recommencer quand on se cogne a un mur

    global RES,b,l,coul # sert a rendre général les variables utilisées dans la fonction

    if RES == False:
        b[0].configure(relief = SUNKEN) # sert a enfoncer le bouton
        l[0].configure(bg="green") # sert a changer la ouleur du texte
        RES = True # change la variable
        coul = "red" # change la couleur des murs
    else:
        b[0].configure(relief = RAISED)
        l[0].configure(bg="red")
        RES = False
        coul = "white"

    murs2() # applique le changement de couleur des murs

def B1(): # mode aveugle
    global b,l,Couleu,MPerso

    if Couleu == "yellow":
        b[1].configure(relief = SUNKEN)
        l[1].configure(bg="green")
        Couleu = "black"
    else:
        b[1].configure(relief = RAISED)
        l[1].configure(bg="red")
        Couleu = "yellow"
    CL.itemconfig(MPerso,fill=Couleu)

def B2(): # laby aléatoire

    global b,l,Alea,CL,BLRG,LM,BLO,LMG,SBON

    if Alea == False:
        b[2].configure(relief = RAISED)
        l[2].configure(text="Labyrinthe Aleatoire")
        Alea = True
        LM = LMG
        murs2()
        BLRG.grid(row=CBLRG[0], column=CBLRG[1],padx = 5,pady = 5) # n'affiche que les bons boutons
        BLO.grid(row=CBLO[0], column=CBLO[1],padx = 5,pady = 5)
        BLD.grid_forget()
        BLG.grid_forget()
        if SBON == True:
            B4()
    elif Alea == True and LSM != None:
        b[2].configure(relief = SUNKEN)
        l[2].configure(text="Labyrinthe Enregistré")
        Alea = False
        LM = LSM[I]
        murs2()
        BLRG.grid_forget() # regenerer
        BLO.grid_forget() # obtenir
        BLD.grid(row=CBLD[0], column=CBLD[1],padx = 5,pady = 5)# va au laby suivant
        BLG.grid(row=CBLG[0], column=CBLG[1],padx = 5,pady = 5)# va au laby précédent
        SBON = BONUS
        if BONUS == True:
            B4()
    else:
        print("Des labyrinthes doivent etre enregistrés dans ces dimentions")

def B3(): # regénérer le laby en fin

    global b,l,REGE

    if REGE == True:
        b[3].configure(relief = RAISED)
        l[3].configure(bg="red")
        REGE = False
    else:
        b[3].configure(relief = SUNKEN)
        l[3].configure(bg="green")
        REGE = True # merci pour la participation de florian

def B4(): # aller chercher les bonus

    global b,l,BONUS,TLA,BONUS1,BONUS2,SBON

    if BONUS == True:# on doit aller chercher les bonus
        b[4].configure(relief = RAISED)
        l[4].configure(bg="red")
        BONUS = False
        #TLA.configure(text=Alea)
        CL.delete(PARA,BONUS1) # suprime les ronds bleus de la prévisualisation
        CL.delete(PARA,BONUS2)
    else:
        b[4].configure(relief = SUNKEN)
        l[4].configure(bg="green")
        BONUS = True
        #TLA.configure(text=Alea)
        BONUS1 = CL.create_oval((LB1[0]-1)*MF+1,(LB1[1]-1)*MF+1,LB1[0]*MF-1,LB1[1]*MF-1,fill = "blue")
        BONUS2 = CL.create_oval((LB2[0]-1)*MF+1,(LB2[1]-1)*MF+1,LB2[0]*MF-1,LB2[1]*MF-1,fill = "blue")

def B5(): # avoir des Bonus aléatoire

    global b,l,BONAL,LB1,LB2

    if BONAL == True:
        b[5].configure(relief = RAISED)
        l[5].configure(bg="red")
        BONAL = False
        LB1 = [1,TY] # coordonnées des bonus
        LB2 = [TX,1] # coordonnées des bonus
    else:
        b[5].configure(relief = SUNKEN)
        l[5].configure(bg="green")
        BONAL = True
        LB1 = [randint(1,TX),randint(1,TY)] # coordonnées des bonus
        LB2 = [randint(1,TX),randint(1,TY)] # coordonnées des bonus
    murs2()

def B6(): # avoir un mode multi

    global b,l,MULTI,F

    if MULTI == True:
        b[6].configure(relief = RAISED)
        l[6].configure(bg="red")
        MULTI = False
        FX = 1000 / TX # calcule le facteur optimal pour une taille de labyrinthe donnée
        FY = 600 / TY

        F = min(FX , FY) # prend la valeur minimal pour ajuster a la taille de la fenetre

    else:
        b[6].configure(relief = SUNKEN)
        l[6].configure(bg="green")
        MULTI = True # merci pour la participation de florian

        FX = 1000 / TX # calcule le facteur optimal pour une taille de labyrinthe donnée
        FY = 600 / TY
        F = min(FX , FY) # prend la valeur minimal pour ajuster a la taille de la fenetre


def Clavier(event):# fonction des binding des touches

    """ Gestion de l'evenement Appui sur une touche du clavier """
    global Pos,RES,BON1,BON2,BONUS,MC,TLM,REUSSI,BON21,BON22,MC2 #recherche la variable dans tout le programe

    touche = event.char # prend quelle touche on presse
    touchef = event.keysym # pas la cahractère mais le numéro de la touche ( poru les touches comme les fleches ou entrer )
    #deplacement vers le bas
    if touche == "s": # test quelle touche est appuyée
        if MODEC == False: # testesi le mode création est activé
            if Pos[3] + F < F*TY and ([Pos[0],Pos[1],"h"] in LM) == False: # si on ne vas pas vers le bord et que l'on ne touche pas un mur
                Pos[3] += F# deplacment position Y 10 vers le bas
                Pos[1] += 1
            elif RES == True: # si les murs sont roucges et que l'on recommence au début quand on les touche
                print("bang, un mur, vous vous retrouvez a votre position initiale")
                Pos[0] = 1
                Pos[1] = 1
                Pos[2] = Pos[0]/2
                Pos[3] = Pos[1]/2
                MC += 1
            else: # si on ne recommence pas quand on touche les murs
                print("bang, un mur")
                MC += 1
        else: # si le mode création est activé
            if Pos[3] + F < F*TY:
                Pos[3] += F# deplacment position Y 10 vers le bas
                Pos[1] += 1
    # deplacement vers le haut
    if touchef == "Down": # test quelle touche est appuyée
        if MULTI == False:
            if MODEC == False: # teste si le mode création est activé
                if Pos[3] + F < F*TY and ([Pos[0],Pos[1],"h"] in LM) == False: # si on ne vas pas vers le bord et que l'on ne touche pas un mur
                    Pos[3] += F# deplacment position Y 10 vers le bas
                    Pos[1] += 1
                elif RES == True: # si les murs sont roucges et que l'on recommence au début quand on les touche
                    print("bang, un mur, vous vous retrouvez a votre position initiale")
                    Pos[0] = 1
                    Pos[1] = 1
                    Pos[2] = Pos[0]/2
                    Pos[3] = Pos[1]/2
                    MC += 1
                else: # si on ne recommence pas quand on touche les murs
                    print("bang, un mur")
                    MC += 1
            else: # si le mode création est activé
                if Pos[3] + F < F*TY:
                    Pos[3] += F# deplacment position Y 10 vers le bas
                    Pos[1] += 1
        else: # mode multi
            if MODEC == False: # teste si le mode création est activé
                if Pos2[3] + F < F*TY and ([Pos2[0],Pos2[1],"h"] in LM) == False: # si on ne vas pas vers le bord et que l'on ne touche pas un mur
                    Pos2[3] += F# deplacment position Y 10 vers le bas
                    Pos2[1] += 1
                elif RES == True: # si les murs sont roucges et que l'on recommence au début quand on les touche
                    print("bang, un mur, vous vous retrouvez a votre position initiale")
                    Pos2[0] = 1
                    Pos2[1] = 1
                    Pos2[2] = Pos2[0]/2
                    Pos2[3] = Pos2[1]/2
                    MC2 += 1
                else: # si on ne recommence pas quand on touche les murs
                    print("bang, un mur")
                    MC2 += 1
            else: # si le mode création est activé
                if Pos2[3] + F < F*TY:
                    Pos2[3] += F# deplacment position Y 10 vers le bas
                    Pos2[1] += 1
    # deplacement vers le haut
    elif touche == "z":
        if MODEC == False:
            if Pos[3] - F > 0 and ([Pos[0],Pos[1] - 1,"h"] in LM) == False:
                Pos[3] -= F # deplacement position y 10 vers le haut
                Pos[1] -= 1
            elif RES == True:
                print("bang, un mur, vous vous retrouvez a votre position initiale")
                Pos[0] = 1
                Pos[1] = 1
                Pos[2] = Pos[0]/2
                Pos[3] = Pos[1]/2
                MC += 1
            else:
                print("bang, un mur")
                MC += 1
        else:
            if Pos[3] - F > 0:
                Pos[3] -= F # deplacement position y 10 vers le haut
                Pos[1] -= 1
    # deplacement vers la droite
    elif touchef == "Up":
        if MULTI == False:
            if MODEC == False:
                if Pos[3] - F > 0 and ([Pos[0],Pos[1] - 1,"h"] in LM) == False:
                    Pos[3] -= F # deplacement position y 10 vers le haut
                    Pos[1] -= 1
                elif RES == True:
                    print("bang, un mur, vous vous retrouvez a votre position initiale")
                    Pos[0] = 1
                    Pos[1] = 1
                    Pos[2] = Pos[0]/2
                    Pos[3] = Pos[1]/2
                    MC += 1
                else:
                    print("bang, un mur")
                    MC += 1
            else:
                if Pos[3] - F > 0:
                    Pos[3] -= F # deplacement position y 10 vers le haut
                    Pos[1] -= 1
        else: # mode multi
            if MODEC == False:
                if Pos2[3] - F > 0 and ([Pos2[0],Pos2[1] - 1,"h"] in LM) == False:
                    Pos2[3] -= F # deplacement position y 10 vers le haut
                    Pos2[1] -= 1
                elif RES == True:
                    print("bang, un mur, vous vous retrouvez a votre position initiale")
                    Pos2[0] = 1
                    Pos2[1] = 1
                    Pos2[2] = Pos2[0]/2
                    Pos2[3] = Pos2[1]/2
                    MC2 += 1
                else:
                    print("bang, un mur")
                    MC2 += 1
            else:
                if Pos2[3] - F > 0:
                    Pos2[3] -= F # deplacement position y 10 vers le haut
                    Pos2[1] -= 1
    # deplacement vers la droite
    elif touche == "d":
        if MODEC == False:
            if Pos[2] + F < F*TX and ([Pos[0],Pos[1],"v"] in LM) == False:
                Pos[2] += F# deplacment position x 10 vers la droite
                Pos[0] += 1
            elif RES == True:
                print("bang, un mur, vous vous retrouvez a votre position initiale")
                Pos[0] = 1
                Pos[1] = 1
                Pos[2] = Pos[0]/2
                Pos[3] = Pos[1]/2
                MC += 1
            else:
                print("bang, un mur")
                MC += 1
        else:
            if Pos[2] + F < F*TX:
                Pos[2] += F# deplacment position x 10 vers la droite
                Pos[0] += 1
    # deplacement vers la gauche
    elif touchef == "Right":
        if MULTI == False:
            if MODEC == False:
                if Pos[2] + F < F*TX and ([Pos[0],Pos[1],"v"] in LM) == False:
                    Pos[2] += F# deplacment position x 10 vers la droite
                    Pos[0] += 1
                elif RES == True:
                    print("bang, un mur, vous vous retrouvez a votre position initiale")
                    Pos[0] = 1
                    Pos[1] = 1
                    Pos[2] = Pos[0]/2
                    Pos[3] = Pos[1]/2
                    MC += 1
                else:
                    print("bang, un mur")
                    MC += 1
            else:
                if Pos[2] + F < F*TX:
                    Pos[2] += F# deplacment position x 10 vers la droite
                    Pos[0] += 1
        else: # mode multi
            if MODEC == False:
                if Pos2[2] + F < F*TX and ([Pos2[0],Pos2[1],"v"] in LM) == False:
                    Pos2[2] += F# deplacment position x 10 vers la droite
                    Pos2[0] += 1
                elif RES == True:
                    print("bang, un mur, vous vous retrouvez a votre position initiale")
                    Pos2[0] = 1
                    Pos2[1] = 1
                    Pos2[2] = Pos[0]/2
                    Pos2[3] = Pos[1]/2
                    MC2 += 1
                else:
                    print("bang, un mur")
                    MC2 += 1
            else:
                if Pos2[2] + F < F*TX:
                    Pos2[2] += F# deplacment position x 10 vers la droite
                    Pos2[0] += 1
    # deplacement vers la gauche
    elif touche == "q":
        if MODEC == False:
            if Pos[2] - F > 0 and ([Pos[0] - 1,Pos[1],"v"] in LM) == False:
                Pos[2] -= F# deplacment position x 10 vers la droite
                Pos[0] -= 1
            elif RES == True:
                print("bang, un mur, vous vous retrouvez a votre position initiale")
                Pos[0] = 1
                Pos[1] = 1
                Pos[2] = Pos[0]/2
                Pos[3] = Pos[1]/2
                MC += 1
            else:
                print("bang, un mur")
                MC += 1
        else:
            if Pos[2] - F > 0:
                Pos[2] -= F# deplacment position x 10 vers la droite
                Pos[0] -= 1
    elif touchef == "Left":
        if MULTI == False:
            if MODEC == False:
                if Pos[2] - F > 0 and ([Pos[0] - 1,Pos[1],"v"] in LM) == False:
                    Pos[2] -= F# deplacment position x 10 vers la droite
                    Pos[0] -= 1
                elif RES == True:
                    print("bang, un mur, vous vous retrouvez a votre position initiale")
                    Pos[0] = 1
                    Pos[1] = 1
                    Pos[2] = Pos[0]/2
                    Pos[3] = Pos[1]/2
                    MC += 1
                else:
                    print("bang, un mur")
                    MC += 1
            else:
                if Pos[2] - F > 0:
                    Pos[2] -= F# deplacment position x 10 vers la droite
                    Pos[0] -= 1
        else: # mode multi
            if MODEC == False:
                if Pos2[2] - F > 0 and ([Pos2[0] - 1,Pos2[1],"v"] in LM) == False:
                    Pos2[2] -= F# deplacment position x 10 vers la droite
                    Pos2[0] -= 1
                elif RES == True:
                    print("bang, un mur, vous vous retrouvez a votre position initiale")
                    Pos2[0] = 1
                    Pos2[1] = 1
                    Pos2[2] = Pos2[0]/2
                    Pos2[3] = Pos2[1]/2
                    MC2 += 1
                else:
                    print("bang, un mur")
                    MC2 += 1
            else:
                if Pos2[2] - F > 0:
                    Pos2[2] -= F# deplacment position x 10 vers la droite
                    Pos2[0] -= 1
    # on dessine le perso a sa nouvelle position
    elif touche == "t": # sert a changer la couleur du perso ( a ne pas utiliser )
        Couleur()
    elif touche == "y": # ferme la fenetre ( a ne pas utiliser ) ( seulement pour les tests )
        fenetre.destroy()
    elif touche == "2": # mur horizontal
        if MODEC == True: # seulement en mode création
            if  ([Pos[0],Pos[1],"h"] in TLM) == False and Pos[1] != TY: # florian
                print("mur horizontal ajouté")
                TLM.append([Pos[0],Pos[1],"h"])
            elif ([Pos[0],Pos[1],"h"] in TLM) == True:
                TLM.remove([Pos[0],Pos[1],"h"])
                print("mur suprimé")
            else:
                print("Mur non possible")
            murscréa()
        else:
            print("mode création désactivé") # merci pour la participation de florian

    elif touche == "3": # mur vertical
        if MODEC == True:
            if  ([Pos[0],Pos[1],"v"] in TLM) == False and Pos[0] != TX:
                print("mur vertical ajouté")
                TLM.append([Pos[0],Pos[1],"v"])
            elif ([Pos[0],Pos[1],"v"] in TLM) == True:
                TLM.remove([Pos[0],Pos[1],"v"])
                print("mur suprimé")
            else:
                print("Mur non possible")
            murscréa()
        else:
            print("mode création désactivé")
    elif touche == "1": # mur vertical - 1
        if MODEC == True:
            if  ([Pos[0] - 1,Pos[1],"v"] in TLM) == False and Pos[0] != 1:
                print("mur vertical ajouté")
                TLM.append([Pos[0] - 1,Pos[1],"v"])
            elif ([Pos[0] - 1,Pos[1],"v"] in TLM) == True:
                TLM.remove([Pos[0] - 1,Pos[1],"v"])
                print("mur suprimé")
            else:
                print("Mur non possible")
            murscréa()
        else:
            print("mode création désactivé")
    elif touche == "5": # mur horizontal - 1
        if MODEC == True:
            if  ([Pos[0],Pos[1] - 1,"h"] in TLM) == False and Pos[1] != 1: # merci pour la participation de florian
                print("mur horizontal ajouté")
                TLM.append([Pos[0],Pos[1] - 1,"h"])
            elif ([Pos[0],Pos[1] - 1,"h"] in TLM) == True:
                TLM.remove([Pos[0],Pos[1] - 1,"h"])
                print("mur suprimé")
            else:
                print("Mur non possible")
            murscréa()
        else:
            print("mode création désactivé") # merci pour la participation de florian
    if MULTI == False:
        print(Pos[0],Pos[1]) # esrt a print les coordonnées actuelles
    Canevas.coords(Perso,Pos[2], Pos[3], Pos[2] + F - FT, Pos[3] + F - FT)
    if MULTI == True:
        Canevas2.coords(Perso2,Pos2[2], Pos2[3], Pos2[2] + F - FT, Pos2[3] + F - FT)
    if Pos[0] == LB1[0] and Pos[1] == LB1[1] and BONUS == True and BON1 != True and MODEC == False:
        BON1 = True
        Canevas.delete(fenetre,Cercle1)
    if Pos[0] == LB2[0] and Pos[1] == LB2[1] and BONUS == True and BON2 != True and MODEC == False:
        BON2 = True
        Canevas.delete(fenetre,Cercle2)
    if MULTI == True:
        if Pos2[0] == LB1[0] and Pos2[1] == LB1[1] and BONUS == True and BON21 != True and MODEC == False:
            BON21 = True
            Canevas2.delete(fenetre,Cercle21)
        if Pos2[0] == LB2[0] and Pos2[1] == LB2[1] and BONUS == True and BON22 != True and MODEC == False:
            BON22 = True
            Canevas2.delete(fenetre,Cercle22)

    if Pos[0] == TX and Pos[1] == TY and MODEC == False:
        REUSSI = True
        if BON1 == True and BON2 == True and BONUS == True:
            if MULTI == False:
                print("vous avez gagné")
            else:
                print("le 1 a gagné")
            FIN()
        elif BONUS == True:
            if MULTI == False:
                print("il vous manque", 2-(int(BON1)+int(BON2))," bonus")
            else:
                print("il manque au 1", 2-(int(BON1)+int(BON2))," bonus")
        else:
            if MODECFIN == False:
                FIN()
                if MULTI == False:
                    print("Vous avez gagné")
                else:
                    print("le 1 a gagné")
            else:
                fenetre.destroy()
    if MULTI == True:
        if Pos2[0] == TX and Pos2[1] == TY and MODEC == False:
            if BON21 == True and BON22 == True and BONUS == True:
                print("le 2 a gagné")
                MC = MC2
                FIN()
            elif BONUS == True:
                print("il manque au 2", 2-(int(BON21)+int(BON22))," bonus")
            else:
                if MODECFIN == False:
                    FIN()
                    print("le 2 a gagné")
                    MC = MC2
                else:
                    fenetre.destroy()
PARAM()