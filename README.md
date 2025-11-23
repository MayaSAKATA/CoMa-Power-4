# CoMa-Power-4
## Partie 1 

# tache 1.1
1. Quelles sont les dimensions d'un plateau de Puissance 4 ?
6x7
2. Comment un joueur gagne-t-il la partie ?
s'il fait une suite de 4 jetons en ligne, en colonne, ou diagonale.  
3. Que se passe-t-il si le plateau est complètement rempli sans gagnant ?
fin du jeu sans gagnant 
4. Un joueur peut-il placer un pion dans une colonne qui est déjà pleine ?
non
5. Quels sont les résultats possibles d'une partie ?
joueur 1 gagne 
joueur 2 gagne 
égalité 

# tache 1.2 
1. Dessinez un diagramme montrant les quatre motifs de victoire différents
victoire de X en diagonale croissante
|_|_|_|_|_|_|_|  
|_|_|_|_|_|_|_|
|_|_|_|X|X|_|_|
|_|_|_|X|X|_|_|
|_|O|X|O|O|_|_|
|O|X|O|X|O|O|_|  

Victoire de X en colonne 
|_|_|_|X|_|_|_|  
|_|_|_|X|_|_|_|
|_|_|_|X|_|_|_|
|_|_|O|X|_|_|_|
|_|O|X|O|O|_|_|
|O|X|O|X|O|_|_| 

Victoire de O en ligne 
|_|_|_|_|_|_|_|  
|_|_|_|_|_|_|_|
|_|_|_|X|_|_|_|
|_|_|O|X|_|_|_|
|X|O|X|O|_|_|_|
|O|O|O|O|X|X|_|

Victoire de X en diagonale décroissante 
|_|_|_|_|_|_|_|  
|_|_|_|_|_|_|_|
|_|_|X|_|_|_|_|
|_|_|O|X|_|_|_|
|X|O|X|O|X|_|_|
|O|X|O|O|O|X|_|

2. Pour une position donnée, combien de directions doivent être vérifiées pour une victoire ?
8 positions à vérifier (haut, bas, gauche, droite, et les 4 diagonales)
3. Pour chacune de ces directions, quel est l'algorithme pour vérifier l'alignement de 4 pions ?


4. Décrire l'algorithme sans le coder (pseudo-code)

fonction win_game (player,board,row,col,drow,dcol):
    count1 = 0
    current_row, current_col = row,col
    While in board and board[row][col] == player: 
        row += drow
        col += dcol
        count1 ++
    
    count2 = 0
    row = current_row
    col = current_col
    While in board and board[row][col] == player:
        row -= drow
        col -= dcol
        count2 ++
    
    count = count1 + count2
    return count >= 4
        
    


## Partie 2 

# Tache 2.1

1. Quels sont les noms des deux agents dans l'environnement ?
2. Que représente la variable action dans le code proposé par la documentation ? Quel est son type ?
3. Que fait env.agent_iter() et env.step(action) ?
4. Quelles informations sont retournées par env.last() ?
5. Quelle est la structure de l'observation retournée ?
6. Qu'est-ce qu'un "action mask" et pourquoi est-il important ?