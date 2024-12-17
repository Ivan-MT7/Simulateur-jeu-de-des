from turtle import*
from random import randint
speed("fastest")
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
    return nombre_aleatoire(255)/255, nombre_aleatoire(255)/255, nombre_aleatoire(255)/255 
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
    return str(''.join(sorted([str(chiffre1), str(chiffre2), str(chiffre3)], reverse = True)))
print(comparer_chiffre(2, 5, 5))
def tracer_carre(x, y, longueur):
    """ Procédure tracant un carré dont la longueur d'un 
    coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce carré."""
    ## Ecrivez ici le code de la fonction
    up()
    goto(x,y)
    down()
    fillcolor(couleur_aleatoire())
    begin_fill()
    for i in range(4) :
        forward(longueur)
        circle(10, 90)
    end_fill()
def tracer_point(x, y, longueur):
    """Procédure tracant un point aux coordonnés x,y. Ce point possède un 
    rayon égal à longueur/5."""
    ## Ecrivez ici le code de la fonction
    fillcolor('Black')
    up()
    goto(x,y)
    begin_fill()
    down()
    circle(longueur / 10)
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
def afficher_un(x, y, longueur):
    """
    Procédure affichant le point milieu d'un dé, dont la longueur d'un 
    coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    tracer_point(x + longueur / 2, y + longueur/ 2 - longueur / 10, longueur)

def afficher_diagonale_1(x, y, longueur):
    """
    Procédure affichant les deux points de la diagonale 1 d'un dé, dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    tracer_point(x + longueur/10*8,y + longueur/10*8 - longueur/10, longueur)
    tracer_point(x + longueur/10*2,y + longueur/10*2 - longueur/10, longueur)
def afficher_diagonale_2(x, y, longueur):
    """
    Procédure affichant les deux points de la diagonale 2 d'un dé, dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    tracer_point(x + longueur/10*2,y + longueur/10*8 - longueur/10, longueur)
    tracer_point(x + longueur/10*8,y + longueur/10*2 - longueur/10, longueur)
def afficher_horizontale_milieu(x, y, longueur):
    """
    Procédure affichant les deux points de l'horizontale du milieu d'un dé, dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    tracer_point(x + longueur/10*2,y + longueur/2 - longueur/10, longueur)
    tracer_point(x + longueur/10*8,y + longueur/2 - longueur/10, longueur)
def choisir_face_a_afficher(x, y, lance, longueur):
    """
    Procédure affichant la face d'un dé correpondant à "lance", dont la longueur 
    d'un coté est 'longueur'. Ce tracé s'effecue à partir des coordonnées x,y du 
    point inférieur gauche de ce dé.
    """
    ## Ecrivez ici le code de la fonction
    assert lance>=1
    if lance == 1:
        tracer_carre(x, y, longueur)
        afficher_un(x, y, longueur)
      
    elif lance == 2 :
        tracer_carre(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
    elif lance == 3 :
        tracer_carre(x, y, 200)
        afficher_un(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
    elif lance == 4 :
        tracer_carre(x, y, 200)
        afficher_diagonale_1(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
    elif lance == 5 :
        tracer_carre(x, y, 200)
        afficher_un(x, y, longueur)
        afficher_diagonale_1(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
    else :
        tracer_carre(x, y, 200)
        afficher_diagonale_1(x, y, longueur)
        afficher_diagonale_2(x, y, longueur)
        afficher_horizontale_milieu(x, y, longueur)
def lancer_jeu():
    """ Programme prinicipal de la gestion du jeu"""
    ## Ecrivez ici le code de la fonction
    x = -250
    toto = []
    for i in range(3) :
        afficher_message(0, 250, "Bienvenue dans un jeu de dés !")
        chiffre = nombre_aleatoire(6)
        toto.append(chiffre)
        choisir_face_a_afficher(x,0, chiffre, 200)
        x = x+250   
        chiffre = 0
        if i == 2 : 
            score1 = int(comparer_chiffre(toto[0], toto[1], toto[2]))
            afficher_message(580, 0,score1)
    x = -250
    list = []
    for a in range(3) :
        afficher_message(0, 250, "Bienvenue dans un jeu de dés !")
        chiffre = nombre_aleatoire(6)
        choisir_face_a_afficher(x,-250, chiffre, 200)
        list.append(chiffre)
        x = x+250
        if a == 2 : 
            score2 = int(comparer_chiffre(list[0], list[1], list[2]))
            afficher_message(580, -200, score2)
    afficher_message(-400, 80, "Joueur1")
    afficher_message(-400, -175, "Joueur2")
    afficher_message(500, 0, "Score1:")
    afficher_message(500, -200, "Score2:")
    if score1 > score2 :
        afficher_message(0, -300, "Joueur1 a gagné")
    else :
        afficher_message(0, -300, "Joueur2 a gagné")
lancer_jeu()
TurtleScreen._RUNNING = True
hideturtle()
## testez ici vos fonctions
exitonclick()







