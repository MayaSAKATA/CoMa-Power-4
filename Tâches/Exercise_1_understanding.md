# Activité 1 : Comprendre le Puissance 4 et le framework Python PettingZoo

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

`env.last()` retourne les informations du jeu de l'agent qui vient de jouer, à savoir, `obersavation`, `reward`, `terminated`, `troncated`et `info`.

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

## Partie 3 : Décomposition du problème

### Tâche 3.1 : Décomposer l'implémentation de l'agent

Un agent doit choisir quelle colonne jouer.

1. Analyse des entrées : Quelles informations l'agent reçoit-il ?

L'agent reçoit l'état de la partie : où sont les différents jetons ansi que le masque d'action : les colonnes dans lesquelles il a le droit de jouer.

2. Détection des coups valides : Comment déterminez-vous quelles colonnes sont jouables ?

Les colonnes qui sont jouables sont celles qui ne sont pas pleines. Nous les determinons grace au masque d'action qui est une liste de taille 7 remplie de 0 et de 1 selon si la colonne est pleine ou non.

3. Sélection du coup : Quel algorithme utiliserez-vous pour choisir un coup ?

Commencer par placement aléatoire du coup, puis utiliser des algorithmes de jeux connus (minimax par exemple).

4. Sortie : Que doit retourner l'agent ?

L'agent doit retourner le numéro de la colonne dans laquelle il souhaite ajouter son jeton.

### Tâche 3.2 : Conception d'algorithme - Progression

A votre avis, quels seraients les algorithmes à implémenter dans les agents (différentes stratégies de jeu), par ordre de complexité croissante :

**Niveau 0** (Agent le plus simple possible):<br>
Placement aléatoire du jeton.

**Niveau 1** (Légèrement plus intelligent - éviter les coups invalides):<br> 
Placement aléatoire du jeton parmis les colonnes où il est valide de jouer (colonnes pas pleines).

**Niveau 2** (Chercher des opportunités immédiates):<br>
A chaque tour, vérifier si on peut gagner au prochain tour, si ce n'est pas le cas, placement du jeton de façon aléatoire.
Pour chaque colonne valide, simuler le coup et vérifier s'il y a une victoire.

**Niveau 3** (Jeu défensif):<br> 
Vérifier si l'adversaire peut gagner au prochain coup, si oui le bloquer, sinon stratégie de victoire immédiate.

**Niveau 4** (Positionnement stratégique):<br> 
Utilise une stratégie de victoire immédiate ou de defense immédiate et continue les lignes de jetons commencé, en privilégiant les colonnes du milieu.

**Niveau 5+** (Algorithmes avancés): <br>
Evalue plusieurs coups possibles et choisit celui avec un meilleur score.

### Tâche 3.3 : Définir l'interface de l'agent

Dans la suite, l'objectif est d'implémenter des agents selon les stratégies décrites ci-dessus. Chaque agent doit ainsi choisir une action en fonction de l'état du jeu (c-à-d la position des jetons). L'idée est d'implémenter une classe `Agent` par stratégie.

Quel serait le squelette de cette classe (attributs, méthodes, etc.) ?

```python
class Agent:
    """
    Random agent
    """

    def __init__(self, board, name, symbol):
       """
        Initialize the agent.

        :parameters :
            board: 3D list representing the current board state
            Name: Name or type of the agent (e.g., 'Random', 'Defensive')
            symbol: Player's symbol ('X' or 'O')

        """

        self.name = name
        self.symbol = symbol

    def choose_action(self, board):
        """
        Main method to choose the next move.
        Must be implemented by child classes according to strategy.
        Parameters:
            board: 3D list representing the current board state
        Returns: 
            column (int) where the agent wants to play
        """

    def valid_action(self, board):
        """
        Defines the possible actions

        Parameters: 
            board: 3D list representing the current board state

        Returns:
            a list of bool to show columns that are valid to play.
        """

    def simulate_action(self, board, column, symbol):
        """
        Simulates an action in the game on a given column. Does not modify the original board.

        Parameters: 
            board: 3D list representing the current board state
            column: column in which the action is simulated
            symbol: current players's symbol

        Returns: 
            a copy of the board after making a move.
        """

    def check_victory(self, board, symbol):
        """
        Checks if the given symbol has won on the board.

        Parameters: 
            board: 3D list representing the current board state
            symbol: current player's symbol

        Returns: 
            bool: 1 if there is a victory for the player, 0 otherwise
        """
```
