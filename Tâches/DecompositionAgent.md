# Partie 3

## Tâche 3.1

Un agent doit choisir quelle colonne jouer. Décomposez cela en sous-tâches :

1. Analyse des entrées : Quelles informations l'agent reçoit-il ?
L'agent reçoit l'état de la partie : où sont ses jetons à lui et ceux de son adversaire.
2. Détection des coups valides : Comment déterminez-vous quelles colonnes sont jouables ?
Il faut que la colonne ne soit pas pleine.
3. Sélection du coup : Quel algorithme utiliserez-vous pour choisir un coup ?
4. Sortie : Que doit retourner l'agent ?
Le numéro de la colonne dans laquelle il souhaite ajouter son jeton.

## Tâche 3.2

A votre avis, quels seraients les algorithmes à implémenter dans les agents (différentes stratégies de jeu), par ordre de complexité croissante :

**Niveau 0** (Agent le plus simple possible):
Placement aléatoire du jeton.

**Niveau 1** (Légèrement plus intelligent - éviter les coups invalides):
Placement aléatoire du jeton parmis les colonnes où il est valide de jouer (colonnes pas pleines).

**Niveau 2** (Chercher des opportunités immédiates):
Si on ne peut pas gagner au prochain coup, position aléatoire -> pour chaque colonne valide, simuler le coup et vérifier s'il y a une victoire.

**Niveau 3** (Jeu défensif):
Vérifier si l'adversaire peut gagner au prochain coup, si oui le bloquer, sinon stratégie de victoire immédiate.

**Niveau 4** (Positionnement stratégique):
Evalue plusieurs coups possibles et choisit celui avec un meilleur score.

**Niveau 5+** (Algorithmes avancés):

## Tâche 3.3 : Définir l'interface de l'agent

Dans la suite, l'objectif est d'implémenter des agents selon les stratégies décrites ci-dessus. Chaque agent doit ainsi choisir une action en fonction de l'état du jeu (c-à-d la position des jetons). L'idée est d'implémenter une classe Agent par stratégie.

Quel serait le squelette de cette classe (attributs, méthodes, etc.) ?

```python
class Agent:
    def __init__(self, name, symbol):
       """
        Initialize the agent.
        :param name: Name or type of the agent (e.g., 'Random', 'Defensive')
        :param symbol: Player's symbol ('X' or 'O')
        """
        self.name = name
        self.symbol = symbol

    def choose_action(self, board):
        """
        Main method to choose the next move.
        Must be implemented by child classes according to strategy.
        :param board: 2D list representing the current board state
        :return: column (int) where the agent wants to play
        """

    def valid_action(self, board):
        """
        Returns a list of columns that are valid to play.
        """

    def simulate_action(self, board, column, symbol):
        """
        Returns a copy of the board after making a move.
        Does not modify the original board.
        """

    def check_victory(self, board, symbol):
        """
        Checks if the given symbol has won on the board.
        """
```

On pourrait créer des classes filles avec une méthode choose_action modifiée en fonction du niveau de l'agent.
