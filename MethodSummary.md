##La question du projet

Avec seulement ce qu’on sait d’un joueur au 1er juillet, peut-on prédire si sa valeur va doubler et atteindre 5 M€ dans l’année qui suit ?

C’est de l’apprentissage supervisé (cours 1) : on montre au modèle des milliers d’exemples passés dont on connaît la réponse, il apprend le profil type, puis on le teste sur des cas qu’il n’a jamais vus.

Le chemin complet
Données brutes ─► Tableau X, y ─► Découpage ─► Modèles ─► Réglages ─► Test final ─► Interprétation
 
              
##	Étape	Ce qu’on fait	Exemple concret	Cours
1	Données Récupérer et comprendre les fichiers	1,9 million de matchs, 656 000 valeurs	Cours 2 : Pandas
2	Tableau X, y 	Une ligne par joueur et saison	Saka, été 2020 : 18 ans, +2 134 minutes, … → breakout ?	Cours 1 : features et target
3	Découpage	Train 2013–2021, validation 2022–2023, test 2024	Le modèle n’a jamais vu 2024	Cours 2 : train/validation/test
4	Référence	Une règle simple et une régression logistique	« Moins de 23 ans et minutes en hausse → breakout »	Cours 2 : régression, descente de gradient
5	Modèles	Arbre, random forest, boosting (+ k-NN, MLP si le temps)	500 petits arbres qui votent	Cours 3 : arbres, bagging, boosting
6	Réglages	Choisir la complexité sur la validation	Profondeur 3 ou 10 ? 100 ou 500 arbres ?	Cours 2 et 3 : overfitting, biais-variance
7	Test final	Évaluer une seule fois sur 2024	Sur 100 joueurs signalés, combien ont vraiment explosé ?	Cours 3 : précision, recall, F1
8	Interprétation	Qu’est-ce qui annonce une explosion ?	Âge et hausse des minutes en tête ?	Cours 3 : feature importance
Où on en est : l’étape 2

Le tableau qu’on construit, c’est exactement ce que les modèles du cours reçoivent : X (les colonnes connues au 1er juillet) et y (breakout 0 ou 1).

	Âge	Part des minutes	Hausse de minutes	Buts+passes /90	Valeur	Rang du club	y
Joueur A	20	0,75	+1 800	0,55	4 M€	3ᵉ	1
Joueur B	29	0,90	−100	0,40	15 M€	1ᵉʳ	0

Chaque colonne de X doit répondre « oui » à la question : le savait-on au 1er juillet ? Sinon, c’est du data leakage, et le modèle « triche ».

La méthode qu’on va utiliser (étapes 3 à 8)

1. Une comparaison, pas un seul modèle. On teste plusieurs méthodes du cours sur le même tableau, et on garde celle qui marche le mieux sur des saisons jamais vues. C’est l’objectif 1 du syllabus : choisir une méthode et justifier ce choix.

2. La méthode principale attendue : le boosting. Parce que :

l’explosion dépend de combinaisons (jeune et joue plus), ce que captent les arbres ;
les breakouts sont rares (≈ 2 %), et le boosting se concentre sur les cas difficiles.

3. La référence. Si le boosting ne bat pas une règle simple ou une régression logistique, sa complexité ne sert à rien. C’est un résultat honnête à présenter quoi qu’il arrive.

4. L’évaluation. Pas d’accuracy : un modèle qui dit toujours « non » aurait 98 % de réussite. On utilise :

la précision : parmi les joueurs signalés, combien explosent vraiment ?
le recall : parmi les vraies pépites, combien ont été trouvées ?
Ce que tu peux lire de ton côté, dans l’ordre
Quand	Quoi lire	Pour comprendre
Cette semaine	Cours 2, partie 8 : overfitting, train/validation/test, cross-validation	Pourquoi on découpe comme ça
Cette semaine	Cours 3, partie 3 : matrice de confusion, précision, recall, F1	Comment on va noter les modèles
Semaine 3	Cours 3, parties 5 et 6 : arbres, entropie, bagging, AdaBoost	Comment marchent tes modèles principaux
Semaine 3	Cours 2, parties 3–4 : fonction de coût, descente de gradient	Comment s’entraîne la régression logistique
Optionnel	Cours 4 : MLP	Si tu ajoutes un réseau de neurones