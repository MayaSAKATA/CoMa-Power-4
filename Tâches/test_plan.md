# Exercice 4 : Concevoir et implémenter des tests

## Partie 1 : Concevoir votre plan de test 

### Tâche 4.1 

Listez les différentes catégories de tests :

**Tests fonctionnels  : L'agent fonctionne-t-il correctement ?**

 Sélection de coup valide : Créer des états de plateau spécifiques et vérifier que l'agent choisit des coups légaux

 Respect du masque d'action : Créer des états de plateau et un mask d'actions et vérifier que l'agent choisit des coups legaux

 Gestion de la fin de partie 

**Tests de performance : Est-il rapide et efficace ?**

 Temps par coup : chronométrer avec time.time()

 Utilisation de la mémoire : pas de dépassement de la limite imposée

**Tests stratégiques : Joue-t-il bien ?**

 Gagne contre un agent aléatoire : doit gagner 80% des matchs contre RandomAgent

 Bloque les menaces évidentes : créer des états de plateau et voir s'il bloque des les menaces évidentes

Critère de succès :

L'agent doit gagner > 80% contre RandomAgent

### Tâche 4.2 : Conception de cas de test 

```
État du plateau :
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
X X X . . . .  <- Ligne du bas, 3 alignés
```
Attendu : L'agent joue la colonne 3 pour gagner.

```
État du plateau :
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
O O O . . . .  <- L'adversaire a 3 alignés
```

Attendu : L'agent joue la colonne 3 pour bloquer

```
État du plateau :
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
X X . X X . .  <- L'agent a 2 + 2 alignés
```
Attendu : L'agent joue la colonne 3 pour gagner

```
État du plateau :
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .
. . . . . . .  
O O . O O . .  <- L'adversaire a 2 + 2 alignés
```
Attendu : L'agent joue la colonne 3 pour bloquer

```
État du plateau :
. . . . . . .
. . . . . . .
. . . . . . .
O X . . . . .
O X . . . . .  <- L'adversaire (O) a 3 alignés
O X . . . . .  <- L'agent (X) a 3 alignés
```
Attendu : L'agent joue la colonne 1 pour gagner, et non pas colonne 0 pour bloquer
