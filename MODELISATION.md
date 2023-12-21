
## Modélisation du problème

Soient $\text{Children}$ l'ensemble des enfants, $\text{Candy}$ l'ensemble des bonbons

Le problème peut être modéliser comme étant un problème CSP défini comme suit :
- **Variables** :
	- $X = (x_{e, b})_{e \in \text{Children}, b \in \text{Candy}}$ est la matrice des nombres de bonbon $b$ qu'on donne à l'enfant $e$
- **Domaines** :
	- Le domaine étant $\mathbb{M}_{m \times n}(\mathbb{N})$ l'ensemble des combinaisons de nombre de bonbon donné aux enfant
- **Contraintes** :
	- Chaque enfant doit recevoir au moins un bonbon de sa liste préférée.
   $$1 \le x_{e,b} \le \max(b)$$
	-  La distribution doit être aussi équitable que possible. $$\forall e_1, e_2 \in \text{Children},  \sum_{k} {x_{e_1, k}} = \sum_{k} {x_{e_2, k}}$$
	- Les bonbons disponibles sont limités en quantité.
	$$\forall b \in \text{Candy}, \sum_{} {x_{e, b}} \le \max(b)$$
	- maximisant la satisfaction générale (à méditer)
   $$\forall X = (x_{e, k}^{'}) \in \mathbb{M}\_{m \times n}(\mathbb{N}), \forall e_i \in \text{Children},  \sum_{k} {x_{e_i, k}} = \max\{ \sum_{k} {x^{'}_{e, k}} \}$$
