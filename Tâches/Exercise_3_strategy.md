# Exercice 3 : Implémenter un agent basé sur des règles

## Partie 1 : Planifier votre stratégie

### Tache 3.1: Conception de la stratégie

#### Stratégie de CoMa-power-4

1. Classement des priorités : Dans quel ordre les règles doivent-elles être vérifiées ?
    * Exemple : Devriez-vous bloquer une victoire de l'adversaire avant d'essayer de gagner vous-même ?

A chaque itération, on regarde si nous pouvons gagner au prochain tour, si oui on joue pour gagner.
Ensuite, on regarde si l'adversaire peut gagner au prochain tour, si c'est le cas, on le bloque.
Si aucun des deux agents ne peut gagner au prochain tour, on priorise l'attaque en essayant de continuer un alignement de jetons ou d'en créer un.

2. Règles essentielles : Quelles sont les règles indispensables ?

    * Listez au moins 3 règles que votre agent devrait suivre

    1. Si on est dans le cas ou on peut gagner au prochain coup, jouer pour gagner.

    2. Si l'adversaire peut gagner au prochain coup, le bloquer.

    3. On attribut un score à chaque action possible selon leur pertinance.

    4. On effectue l'action qui a le plus gros score.

3. Règles souhaitables : Quelles sont les améliorations optionnelles ?

    * Listez 2-3 idées stratégiques supplémentaires

    1. Prioriser les lignes centrales pour les premiers coups.

    2. Faire une analyse du point de vue des deux agents afin de prioriser les coups qui nous avantagent et qui désavantagent l'adversaire.
