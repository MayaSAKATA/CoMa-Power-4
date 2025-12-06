# Exercice 5 : Défis avancés

## Défi 1 : Algorithme Minimax

### Tache 5.1 : Comprendre l'algorithme

1. Pourquoi alternons-nous entre max et min ?

Le max représente le joueur voulant atteindre le plus grand score et min son adversaire qui cherche à faire descendre notre score. On alterne entre min et max pour simuler l'alternance des joueurs dans une vraie partie.

2. Que contrôle `depth` ?

Depth contrôle le nombre de coups anticipés.

3. Que se passe-t-il si la profondeur est trop grande ?

Si la profondeur est trop grande, le programme devient trop lent, il peut aussi utiliser trop de mémoire.

4. Comment l'élagage alpha-bêta réduit-il l'espace de recherche ?

L'étalage alpha-beta reduit l'espace de recherche en ignorant les branches qui n'affectent plus la décision. Si on rencontre sur une branche un resultat qui est moins bon que le resultat actuel, on arrête d'explorer cette branche car elle ne sera pas choisie quoiqu'il en soit.
