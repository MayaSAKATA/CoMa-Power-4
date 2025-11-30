# Tâche 4.1 #

## Que tester ? ##

Listez les différentes catégories de tests :

**Tests fonctionnels  : L'agent fonctionne-t-il correctement ?**

 Sélection de coup valide

 Respect du masque d'action

 Gestion de la fin de partie

**Tests de performance : Est-il rapide et efficace ?**

 Temps par coup : chronométrer avec time.time()

 Utilisation de la mémoire : 

**Tests stratégiques : Joue-t-il bien ?**

 Gagne contre un agent aléatoire : jouer 100 parties et analyser les résultats

 Bloque les menaces évidentes : créer états de plateau et voir s'il bloque des les menaces évidentes

**Critère de succès** : L'agent doit gagner > 80% contre RandomAgent

# Tâche 4.2 # 

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
. . . . . . .
O O O . . . .  <- L'adversaire a 3 alignés
X X X . . . .  <- L'agent a 3 alignés
```
Attendu : L'agent joue la colonne 3 pour gagner, et non pas colonne 1 pour bloquer
