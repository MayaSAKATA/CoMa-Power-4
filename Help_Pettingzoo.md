# Aide bibliothèque pettingzoo.classic

`action_mask`: actions autorisées

`agent_iter()` : Donne l’ordre de jeu des agents

`env.reset()` : Recommence une partie
`env.last()` : Infos du joueur courant (renvoie ce que l’agent courant « voit »)
`env.step(action)`: Joue un coup
`env.legal_actions(agent)` : Colonnes disponibles
`env.agent_iter()` : Boucle des agents
`env.state()` : Plateau global
`env.observation_space`, `action_space` : Définitions RL standard

`terminaison/truncation` : Fin de partie
