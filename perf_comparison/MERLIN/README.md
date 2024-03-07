yolo_interpreter.py (Internship) By Lucille Herbay:

Date:
9/11/2021 au 3/12/2021


Notebook en python qui permet deux choses:
- Dans un premier temps passer d'une sortie YOLO (positions d'erreur prédites en pixel) à une sortie plus SIBIS like (avec des positions d'erreur par numéro de colones)
- Dans un deuxième temps évaluer la qualité des prédictions du modèle, avec différentes metrics (precision, recall, f1_score...)

/!\ Les dépendances:
numpy, matplotlib(pyplot), math, sys, pandas

/!\ Les éléments à changer dans le code pour que ça fonctionne:
En bas de la première cellule:
-> pars = yolo_pars("/home/herbay/Stage_Novembre_2021/data_internship_2/predictions.txt")
Il faut remplacer le chemin par celui où se situe le fichier de predictions de YOLO.
Les annotations SIBIS nécessaires pour calculer les différents scores doivent aussi se situer dans ce dossier.

Dans le fichier de predictions de YOLO utilisé, il faut penser à changer les chemins d'accès (indiqués à chaque nouvel alignement étudié) par le chemin du dossier où se trouve les annotations SIBIS et le fichier de prédiction.
Par exemple dans mon cas, j'ai changé les chemins indiqué dans le fichier de predictions yolo initial: "/home/hiba/..../data_int/XXXX.jpg" par: "/home/herbay/Stage_Novembre_2021/data_internship_2/XXXX.jpg" (tous les fichiers jpg n'ont pas besoin d'etre dans le dossier, je ne m'en sers pas du tout. J'ai juste besoin, en parsant le fichier predictions.txt, de pouvoir récupérer le chemin vers l'annotation correspondante à chaque image d'alignement)
C'est pas pratique du tout et si j'ai le temps je vais modifier le point là pour que ce soit fait automatiquement.



