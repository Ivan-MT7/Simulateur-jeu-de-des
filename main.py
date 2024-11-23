from turtle import*
from random import randint
speed("fastest")
def nombre_aleatoire(n): 
    """
    Fonction renvoyant un entier aléatoire compris entre 1 et n.
    
    Argument d'entrée:
    n : nombre maximum du tirage aléatoire
        type : entier
        
    Sortie :
    nombre : nombre choisi alétoirement
        type : entier
    """
    ## Ecrivez ici le code de la fonction
    assert n>=1 and n<=6
    nombre = randint(1, n)
    return nombre
def couleur_aleatoire():
    """ Fonction renvoyant un tuple de 3 nombres entiers compris entre 0 et 255
    Ce tuple correspond à une couleur codée en RVB. Par exemple rouge (255,0,0),
    vert (0,255,0), bleu (0,0,255)
    
    Argument d'entrée:
    aucun
        
    Sortie :
    couleur : un tuple composé de trois entiers compris entre 0 et 255
        type : tuple
    """
    ## Ecrivez ici le code de la fonction
    return randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255 
def comparer_chiffre(chiffre1, chiffre2, chiffre3):
    """ Fonction comparant trois chiffres décimaux et renvoyant le plus grand 
    nombre composé par ces trois chiffres
    
    Arguments d'entrée:
    chiffre1, chiffre2, chiffre3 : chiffre décimaux
        type : entier
        
    Sortie :
    résultat : un nombre décimal
        type : entier
    
    Exemples d'exécution
    --------------------
    >>> comparer_chiffre(1, 5, 3)
    531
    >>> comparer_chiffre(5, 1, 1)
    511
    >>> comparer_chiffre(1, 1, 1)
    111
    >>> comparer_chiffre(1, 3, 3)
    331
    """
    ## Ecrivez ici le code de la fonction
    if chiffre1 > chiffre2 and chiffre1 > chiffre3 :
        if chiffre2>chiffre3 :
            return str(chiffre1)+str(chiffre2)+str(chiffre3)
        else :
            return str(chiffre1)+str(chiffre3)+str(chiffre2)
    elif chiffre2 > chiffre1 and chiffre2> chiffre3 :
        if chiffre1>chiffre3 :
            return str(chiffre2)+str(chiffre1)+str(chiffre3)
        else :
            return str(chiffre2)+str(chiffre3)+str(chiffre1)
    elif chiffre3 > chiffre1 and chiffre3 > chiffre2 :
        if chiffre2 > chiffre1 :
            return str(chiffre3)+str(chiffre2)+str(chiffre1)
        else :
            return str(chiffre3)+str(chiffre1)+str(chiffre2)
    else :
        return str(chiffre1) + str(chiffre2) + str(chiffre3)
# print(comparer_chiffre(5, 1, 1))
# print(comparer_chiffre(1, 1, 1))
# print(comparer_chiffre(1, 3, 3))
# print(comparer_chiffre(1, 5, 3))
def tracer_carre(x, y, longueur):
    """ Procédure tracant un carré dont la longueur d'un 
    coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce carré."""
    ## Ecrivez ici le code de la fonction
    begin_fill()
    fillcolor(couleur_aleatoire())
    goto(x+(longueur), y)
    goto(x+longueur, y+longueur)
    goto(x, y + longueur)
    goto(x, y)
    end_fill()
# tracer_carre(0, 0, 200)




def tracer_point(x, y, longueur):
    """Procédure tracant un point aux coordonnés x,y. Ce point possède un 
    rayon égal à longueur/5."""
    ## Ecrivez ici le code de la fonction
    up()
    goto(x, y)
    down()
    fillcolor("black")
    begin_fill()
    circle(longueur/6)
    end_fill()

def afficher_message(x, y, texte):
    """
    Procédure affichant le message 'texte' aux coordonnés x,y.
    """
    ## Ecrivez ici le code de la fonction
    up()
    goto(x, y)
    down()
   
    if texte == "Joueur1" or texte == "Joueur2" or texte == "Score1" or texte == "Score2" :
        write(texte, False, font=('Courrier', 30, 'normal'))
    else : 
         write(texte, False, font=('Courrier', 12, 'normal'))


# afficher_message(0, -50, "Bienvenue dans un jeu de dé !")


def afficher_un(x, y, longueur):
    """
    Procédure affichant le point milieu d'un dé, dont la longueur d'un 
    coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    tracer_point(x +(longueur/2), y+(longueur/2)-20, longueur)
# afficher_un(0, 0, 200)#X
def afficher_diagonale_1(x, y, longueur):
    """
    Procédure affichant les deux points de la diagonale 1 d'un dé, dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    tracer_point(x+(longueur/6), y+(longueur/longueur), longueur)
    tracer_point(x+(longueur/1.25), y+(longueur/1.5), longueur)

    
# afficher_diagonale_1(0, 0, 200)#X


#afficher_un et afficer_diagonale_1 forment un trois
def afficher_diagonale_2(x, y, longueur):
    """
    Procédure affichant les deux points de la diagonale 2 d'un dé, dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    tracer_point(x+(longueur/6), y+(longueur/1.5), longueur)
    tracer_point(x+(longueur/1.25), y+(longueur/longueur), longueur)

# afficher_diagonale_2(0, 0, 200)#X

#afficher_un, afficher_diagonale_1, afficher_diagonale_2 forment un 5
def afficher_horizontale_milieu(x, y, longueur):
    """
    Procédure affichant les deux points de l'horizontale du milieu d'un dé, dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    tracer_point(x+(longueur/6), y+(longueur/2)-30, longueur)
    tracer_point(x+(longueur/1.25), y+(longueur /2)-30, longueur)
    
# afficher_horizontale_milieu(0, 0, 200)#X


def choisir_face_a_afficher(x, y, lance, longueur):
    """
    Procédure affichant la face d'un dé correpondant à "lance", dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    assert lance>=1
    if lance == 1:
        afficher_un(x, y, longueur)
    elif lance == 2 :
        afficher_diagonale_2(x, y, longueur)
    elif lance == 3 :
        afficher_un(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
    elif lance == 4 :
        afficher_diagonale_1(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
    elif lance == 5 :
        afficher_un(x, y, longueur)
        afficher_diagonale_1(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
    else :
        afficher_diagonale_1(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
        afficher_horizontale_milieu(x, y, longueur)

def lancer_jeu():
    """ Programme prinicipal de la gestion du jeu"""
    ## Ecrivez ici le code de la fonction
    x = -250
    afficher_message(0, 250, "Bienvenue dans un jeu de dé !")
    for i in range(3) :
        up()
        goto(x, 0)
        down()
        tracer_carre(x, 0, 200)
        choisir_face_a_afficher(x, 0, nombre_aleatoire(6), 200)
        x = x+250
    x = -250
    for a in range(3) :
        
        up()
        goto(x, -200)
        down()
        tracer_carre(x, -200, 200)
        le_truc_aléatoire = nombre_aleatoire(6)
        choisir_face_a_afficher(x, -200, le_truc_aléatoire, 200)
        x = x+250
    afficher_message(-400, 0, "Joueur1")
    afficher_message(-400, -200, "Joueur2")
    afficher_message(450, 0, "Score1:")
    afficher_message(450, -200, "Score2:")


    
    # up()
    # goto(-500, 0)
    # down()
    # tracer_carre(-500, 0, 200)
    # choisir_face_a_afficher(-500, 0, nombre_aleatoire(2), 200)
    # up()
    # goto(-750, 0)
    # down()
    # tracer_carre(-750, 0, 200)
    # choisir_face_a_afficher(-750, 0, nombre_aleatoire(2), 200)
    
lancer_jeu()

    
TurtleScreen._RUNNING = True
hideturtle()
## testez ici vos fonctions
exitonclick()