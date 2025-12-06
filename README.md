# CoMa-Power-4

Implémentation en Python d'agents qui jouent au Puissance 4 pour [ML Arena](https://ml-arena.com/).

Utilisation de la librairie [Pettingzoo](https://pettingzoo.farama.org/environments/classic/connect_four/).

Nous avons soumi deux agents :

- CoMa pour SmartAgent
- CoMa+ pour MinimaxAgent


## Partie 1 : Règles du Puissance 4

### Tâche 1.1 : Analyse des règles du jeu

1. Quelles sont les dimensions d'un plateau de Puissance 4 ?

Les dimensions d'un plateau sont 6x7, soit 6 lignes et 7 colonnes.

2. Comment un joueur gagne-t-il la partie ?  

Un joueur gagne la partie s'il fait une suite de 4 jetons en ligne, en colonne ou diagonale.

3. Que se passe-t-il si le plateau est complètement rempli sans gagnant ?  

Si le plateau est complètement rempli sans gagnant, il y a match nul, il n'y a pas de gagnant.

4. Un joueur peut-il placer un pion dans une colonne qui est déjà pleine ?

Il n'est pas possible pour un joueur de placer un pion dans une colonne qui est déjà pleine.

5. Quels sont les résultats possibles d'une partie ?

Les résultats possible d'une partie sont victoire du joueur 1, victoire du joueur 2, égalité.

### Tâche 1.2 : Analyse des conditions de victoire  

1. Dessinez un diagramme montrant les quatre motifs de victoire différents

Victoire de X en diagonale croissante

| Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| — | — | — | — | — | — | — |
| — | — | — | — | — | — | — |
| — | — | — | X | X | — | — |
| — | — | O | X | O | — | — |
| — | — | X | O | O | — | — |
| — | X | O | X | O | — | — |  

<br>
Victoire de O en diagonale décroissante

| Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| — | — | — | — | — | — | — |<br>
| — | — | — | — | — | — | — |<br>
| — | O | — | — | — | — | — |<br>
| — | X | O | X | O | — | — |<br>
| — | X | X | O | O | — | — |<br>
| — | X | O | X | O | — | — |<br>

<br>
Victoire de X en colonne:

| Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| — | — | — | X | — | — | — |<br>
| — | — | — | X | — | — | — |<br>
| — | — | O | X | — | — | — |<br>
| — | O | O | X | — | — | — |<br>
| — | O | X | O | — | — | — |<br>
| — | X | O | X | O | — | — |<br>

<br>
Victoire de O en ligne

| Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| — | — | — | — | — | — | — |<br>
| — | — | — | — | — | — | — |<br>
| — | — | X | X | — | — | — |<br>
| — | O | X | X | — | — | — |<br>
| — | O | X | O | — | — | — |<br>
| X | X | O | O | O | O | — |<br>

<br>
<br>
<br>

2. Pour une position donnée, combien de directions doivent être vérifiées pour une victoire ?

Pour une position données, 8 directions doivent être vérifiées pour une victoire (haut, bas, gauche, droite, et les 4 diagonales). 

3. Pour chacune de ces directions, quel est l'algorithme pour vérifier l'alignement de 4 pions ? Décrire l'algorithme sans le coder (pseudo-code)

A partir de la dernière action, il faut compter le nombre de pions successifs du joueur actuel dans chaque direction et vérifier si ce nombre est supérieur ou égal à 4.

<br>

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

## Partie 2 : Comprendre PettingZoo

### Tâche 2.1 : Lire la documentation

1. Quels sont les noms des deux agents dans l'environnement ?

Dans l'environnement, les noms des deux joueurs sont `player_0` et  `player_1`.

2. Que représente la variable `action` dans le code proposé par la documentation ? Quel est son type ?

La variable `action` représent le numéro de la colonne dans laquelle le joueur veut placer son jeton, son type est int (entier).

3. Que fait `env.agent_iter()` et `env.step(action)` ?

`env.agent_iter()` détermine quel agent est censé jouer et `env.step(action)` exécute l'action donnée.

4. Quelles informations sont retournées par `env.last()` ?

`env.last()` retourne les informations du jeu de l'agent qui vient de jouer, à savoir, `observation`, `reward`, `terminated`, `troncated`et `info`.

5. Quelle est la structure de l'observation retournée ?

observation (dict), reward (float), termination (bool), truncation (bool), info = env.last() (dict)

6. Qu'est-ce qu'un "action mask" et pourquoi est-il important ?

C'est un tableau de booléens de taille 7 reprensentant les 7 colonnes du jeu. Si la ième colonne est True alors le joueur peut jouer cette action, si elle est False, il ne peut pas.
L'action mask est important car il empèche l'agent de joueur un mouvement illégal.

### Tâche 2.2 : Analyse de l'espace d'observation

1. Quelle est la forme du tableau d'observation ?

Le tableau est de la forme (6,7,2).

2. Que représente chaque dimension ?

Le vecteur de taille 6 représente le nombre de lignes.
Le vecteur de taille 7 représente le nombre de colonnes.
Le vecteur de taille 2 sert à indiquer si la case est remplie et par quel joueur.

3. Quelles sont les valeurs possibles dans le tableau d'observation ?

Dans chaque case du tableau, les valeurs possibles sont [0,1], [1,0], [0,0].
