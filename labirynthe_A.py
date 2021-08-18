# Import
from tkinter import Tk, Canvas
import random
import time
import os.path
import sys
sys.setrecursionlimit(10**6)
from PIL import Image, ImageDraw
import PIL

longeur, largeur = input("Size of laberynth (longxwide): ").split("x")
start_time = time.time()
longeur=int(longeur)
largeur=int(largeur)
epaisseur_ligne = 800/(longeur*10)
taille_fenetre = 800
longueur_case = taille_fenetre / longeur
largeur_case= taille_fenetre / largeur

LMurs = []
for y in range(largeur):
    for x in range(longeur - 1):
        LMurs.append((x, y, x + 1, y))
for y in range(largeur - 1):
    for x in range(longeur):
        LMurs.append((x, y, x, y + 1))


# Fonctions


def Affichage():
    global LMurs

    def DessineBordDroit(x, y, coul):
        pos_x = x * longueur_case + longueur_case
        pos_y = y * largeur_case
        canvas.create_line(pos_x, pos_y, pos_x,
                           pos_y + largeur_case, fill=coul, width=epaisseur_ligne)

    def DessineBordBas(x, y, coul):
        pos_x = x * longueur_case
        pos_y = y * largeur_case + largeur_case
        canvas.create_line(pos_x, pos_y, pos_x + longueur_case,
                           pos_y, fill=coul, width=epaisseur_ligne)

    def DessineMur(coords, coul):
        x, y, x2, y2 = coords
        if y == y2:
            DessineBordDroit(x, y, coul)
        else:
            DessineBordBas(x, y, coul)


    canvas.delete("all")
    for f in LMurs:
        x1, y1, x2, y2 = f
        DessineMur((x1, y1, x2, y2), "black")

    canvas.create_line(0, largeur_case, 0, taille_fenetre - (epaisseur_ligne / 2), fill="black", width=epaisseur_ligne)
    canvas.create_line(longueur_case, 0, taille_fenetre - (epaisseur_ligne / 2), 0, fill="black", width=epaisseur_ligne)
    canvas.create_line(0, taille_fenetre - (epaisseur_ligne / 2), taille_fenetre - longueur_case,
                       taille_fenetre - (epaisseur_ligne / 2), fill="black", width=epaisseur_ligne)
    canvas.create_line(taille_fenetre - (epaisseur_ligne / 2), 0, taille_fenetre - (epaisseur_ligne / 2),
                       taille_fenetre - largeur_case, fill="black", width=epaisseur_ligne)


def generation():
    global LMurs, longeur, largeur

    explored=[(0,0)]
    marked=[(1,0),(0,1)]


    while len(explored)!=longeur*largeur:
        select=marked[random.randint(0,len(marked)-1)]

        marked.remove(select)
        explored.append(select)

        explored_neighbours=[]
        for i in ((0,1),(0,-1),(1,0),(-1,0)):
            neighbour=(select[0]+i[0],select[1]+i[1])
            if neighbour[0]==-1 or neighbour[1]==-1 or neighbour[0]==longeur or neighbour[1] == largeur:
                continue
            if neighbour not in explored:
                if neighbour not in marked:
                    marked.append(neighbour)
            else:
                explored_neighbours.append(neighbour)
        if explored_neighbours:
            break_wall_towards=explored_neighbours[random.randint(0,len(explored_neighbours)-1)]
            LMurs.remove((min(break_wall_towards[0],select[0]),min(break_wall_towards[1],select[1]),max(break_wall_towards[0],select[0]),max(break_wall_towards[1],select[1])))




generation()
print(LMurs)
print("--- %s seconds ---" % (time.time() - start_time))

Fenetre = Tk()
Fenetre.geometry(str(taille_fenetre) + "x" + str(taille_fenetre))
Fenetre.title("Labyrinthe")
canvas = Canvas(Fenetre, width=taille_fenetre, height=taille_fenetre, borderwidth=0, highlightthickness=0,
                bg="lightgray")

Affichage()

canvas.pack()
Fenetre.mainloop()


def CreateUrlImage(file):
    i=0
    while os.path.isfile(file+str(i)+").png"):
        i+=1
    return file+str(i)+").png"
def EngeristreLabyrinthe(murs):
    for f in murs:
        x1,y1,x2,y2=f
        if y1 == y2:
            draw.line([x1 * longueur_case + longueur_case, y1 * largeur_case, x1 * longueur_case + longueur_case, y1 * largeur_case + largeur_case], (0, 0, 0), width=int(epaisseur_ligne))
        else:
            draw.line([x1 * longueur_case, y1 * largeur_case + largeur_case, x1 * longueur_case + longueur_case, y1 * largeur_case + largeur_case], (0, 0, 0), width=int(epaisseur_ligne))
        draw.line([0, largeur_case, 0, taille_fenetre - (epaisseur_ligne / 2)], (0, 0, 0), width=int(epaisseur_ligne))
        draw.line([longueur_case, 0, taille_fenetre - (epaisseur_ligne / 2), 0], (0, 0, 0), width=int(epaisseur_ligne))
        draw.line([0, taille_fenetre - (epaisseur_ligne / 2), taille_fenetre - longueur_case, taille_fenetre - (epaisseur_ligne / 2)], (0, 0, 0), width=int(epaisseur_ligne))
        draw.line([taille_fenetre - (epaisseur_ligne / 2), 0, taille_fenetre - (epaisseur_ligne / 2), taille_fenetre - largeur_case], (0, 0, 0), width=int(epaisseur_ligne))
def EngeristreSolution(chemin):
    for i in range(len(chemin)):
        case_i=chemin[i]
        case_avant=chemin[i-1]
        x_i,y_i=case_i
        x_avant,y_avant=case_avant
        if i != 0:
            draw.line([x_i * longueur_case + longueur_case / 2, y_i * largeur_case + largeur_case / 2, x_avant * longueur_case + longueur_case / 2, y_avant * largeur_case + largeur_case / 2], (255, 0, 0), width=int(epaisseur_ligne))
if input("Do you want to save the laberynth?")=="yes":
    img_labyrinthe = PIL.Image.new("RGB",(taille_fenetre,taille_fenetre),(255,255,255))
    draw = ImageDraw.Draw(img_labyrinthe)
    EngeristreLabyrinthe(LMurs)
    img_labyrinthe.save(CreateUrlImage(input("Location of the file: ")+"("))

def AfficheSolution(liste_solution):
    Affichage()
    for i in range(len(liste_solution)):
        case_i=liste_solution[i]
        case_avant=liste_solution[i-1]
        x_i,y_i=case_i
        x_avant,y_avant=case_avant
        if i != 0:
            canvas.create_line(x_i * longueur_case + longueur_case / 2, y_i * largeur_case + largeur_case / 2, x_avant * longueur_case + longueur_case / 2, y_avant * largeur_case + largeur_case / 2, fill="red", width=int(epaisseur_ligne))


def keySort(elem):
    return elem[0][0]

def Solution(murs,longueur,largeur):
    parents_explored=[]
    explored = []

    #[(H_cost,G_cost),cell_pos,parent_pos]
    marked=[((longeur+largeur,0),(0, 0),(0,0))]

    while True:
        marked.sort(key=keySort)
        current=marked[0]
        marked=marked[1:]

        explored.append(current[1])
        parents_explored.append(current[2])

        if current[1]==(longueur-1,largeur-1):  #Case finale
            #print(explored)
            #print(parents_explored)

            path=[(longeur-1,largeur-1)]
            previous=(longeur-1,largeur-1)
            while True:
                previous=parents_explored[explored.index(previous)]
                path.append(previous)
                if previous==(0,0):
                    return path

        for i in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            neighbour = (current[1][0] + i[0], current[1][1] + i[1])
            if neighbour[0]==-1 or neighbour[1]==-1 or neighbour[0]==longeur or neighbour[1]==largeur:
                continue
            if neighbour in explored or (min(neighbour[0],current[1][0]),min(neighbour[1],current[1][1]),max(neighbour[0],current[1][0]),max(neighbour[1],current[1][1])) in murs:
                continue

            found=False
            for a in marked:
                if a[1]==neighbour:
                    found=True

            if not found:
                GCost=current[0][0]-(i[0]+i[1])*10
                Fcost=current[0][1]+(i[0]+i[1])*10
                marked.append(((GCost,Fcost),neighbour,current[1]))





if input("Do you want to see the solution of the laberynth? ")=="yes":
    start_time = time.time()
    solution=Solution(LMurs,longeur,largeur)
    Fenetre = Tk()
    Fenetre.geometry(str(taille_fenetre) + "x" + str(taille_fenetre))
    Fenetre.title("Solution labyrinthe")
    canvas = Canvas(Fenetre, width=taille_fenetre, height=taille_fenetre, borderwidth=0, highlightthickness=0,
                    bg="lightgray")
    canvas.pack()
    Fenetre.after(100, AfficheSolution(solution))
    print("--- %s seconds ---" % (time.time() - start_time))
    Fenetre.mainloop()
    if input("Do you want to save this solution? ") == "yes":
        img_solution = PIL.Image.new("RGB", (taille_fenetre, taille_fenetre), (255, 255, 255))
        draw = ImageDraw.Draw(img_solution)
        EngeristreLabyrinthe(LMurs)
        EngeristreSolution(solution)
        img_solution.save(CreateUrlImage(input("Location of the file: ")+"("))