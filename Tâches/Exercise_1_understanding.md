# Exercice 1

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
