# CoMa-Power-4

## Partie 1

### Tâche 1.1

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

### Tâche 1.2

1. Dessinez un diagramme montrant les quatre motifs de victoire différents

Victoire de X en diagonale croissante

| — | — | — | — | — | — | — |<br>
| — | — | — | — | — | — | — |<br>
| — | — | — | X | X | — | — |<br>
| — | — | O | X | O | — | — |<br>
| — | — | X | O | O | — | — |<br>
| — | X | O | X | O | — | — |<br>

Victoire de X en colonne

| — | — | — | X | — | — | — |<br>
| — | — | — | X | — | — | — |<br>
| — | — | O | X | — | — | — |<br>
| — | O | O | X | — | — | — |<br>
| — | O | X | O | — | — | — |<br>
| — | X | O | X | O | — | — |<br>

Victoire de O en ligne

| — | — | — | — | — | — | — |<br>
| — | — | — | — | — | — | — |<br>
| — | — | X | X | — | — | — |<br>
| — | O | X | X | — | — | — |<br>
| — | O | X | O | — | — | — |<br>
| X | X | O | O | O | O | — |<br>

Victoire de O en diagonale décroissante 

| — | — | — | — | — | — | — |<br>
| — | — | — | — | — | — | — |<br>
| — | O | — | — | — | — | — |<br>
| — | X | O | X | O | — | — |<br>
| — | X | X | O | O | — | — |<br>
| — | X | O | X | O | — | — |<br>
2. Pour une position donnée, combien de directions doivent être vérifiées pour une victoire ?
8 positions à vérifier (haut, bas, gauche, droite, et les 4 diagonales)
3. Pour chacune de ces directions, quel est l'algorithme pour vérifier l'alignement de 4 pions ?
A partir de la dernière action, il faut compter le nombre de pions successifs du dernier joueur dans chaque direction et vérifier si ce nombre est supérieur à 4.
4. Décrire l'algorithme sans le coder (pseudo-code)
```
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
```

## Partie 2

### Tâche 2.1

1. Quels sont les noms des deux agents dans l'environnement ? 'player_0', 'player_1'
2. Que représente la variable action dans le code proposé par la documentation ? Quel est son type ?  numéro (int) de la colonne dans laquelle le joueur veut placer son jeton
3. Que fait env.agent_iter() et env.step(action) ? env.agent_iter() détermine quel agent est censé jouer et env.step(action) exécute l'action donnée
4. Quelles informations sont retournées par env.last() ? retourne les informations du jeu de l'agent qui vient de jouer
5. Quelle est la structure de l'observation retournée ? observation (dict), reward (float), termination (bool), truncation (bool), info = env.last() (dict)
6. Qu'est-ce qu'un "action mask" et pourquoi est-il important ? Tableau de taille 7 (puisque 7 colonnes) avec des 1 là où le joueur a le droit de jouer (0 signifie colonne pleine) -> important car permet de filtrer les actions interdites

### Tâche 2.2

1. Quelle est la forme du tableau d'observation ?
Le tableau est de la forme (6,7,2).
2. Que représente chaque dimension ?
le vecteur de taille 6 représente le nombre de lignes
le vecteur de taille 7 représente le nombre de colonnes
le vecteur de taille 2 sert à indiquer si la case est remplie et par quel joueur
3. Quelles sont les valeurs possibles dans le tableau d'observation ?
dans chaque case du tableau, les valeurs possibles sont [0,1], [1,0], [0,0]
