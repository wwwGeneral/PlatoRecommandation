# Suggestions de choses à faire...

## Interrogations proposées par N. Borie

Ayant fini de générer les méta données associées aux 93 exercices
opérables pour le C dans PLaTon, voici une liste de questions,
potentiellement profondes, pour lesquelles la recommandation
algorithmique peut apporter des éléments de réponses.


Il y a aussi des descriptions d'expériences qui vous permettrons de
rassembler des preuves objectives du bon fonctionnement de votre
moteur de recommandations.

  
### Challenge 1 : générer des parcours d'apprentissage pour les élèves fictifs

En modélisant des élèves virtuels de niveaux différents : des élèves
forts qui réussissent presque tout, des élèves moyens et des élèves
faibles qui échouent un grand nombre d'exercices.

* Générer des parcours complets :
    - niveau de maîtrise initiaux dans chaque notion égaux à zéro
	- liste ordonnées d'exercices + note obtenues à chaque exercice
	- niveau de maîtrise finaux dans chaque notion maximal possible
	
Dans l'idée, on aimerait voir le système de recommandation qui va
moins vite vers les nouvelles notions quand l'élève est plus
faible. Ceci serait un argument preuve de bon fonctionnement de votre
système de recommandation.

* Générer des parcours précis :
  - Prendre un étudiant déjà fort sur une ou plusieurs notions et
    générer le parcours pour apprendre le reste des notions.
	  
Dans l'idée, on aimerait voir qu'un élève déjà expérimenté sur une ou
plusieurs notions ne se voient pas recommander des exercices portant
sur des notions qu'il a déjà valider. Ceci serait un argument preuve
de bon fonctionnement de votre système de recommandation.

  - Prendre un étudiant avec un passif vierge (zéro dans toutes les
    notions) et tentez de rusher une ou plusieurs notions
    spécifiques. Établir ainsi un parcours d'apprentissage minimal
    vers une ou plusieurs notions spécifiées.

Dans l'idée, on aimerait voir par exemple : "comment apprendre malloc
au plus vite ?". A partir d'un étudiant vierge, on voudrait voir la
suite d'exercices minimale qui permet d'apprendre malloc rapidement
mais sans avoir de saut de difficulté énorme d'un exercice à un
autre. Si votre moteur de recommandation est bien fait, on devrait
voir un parcours pas trop brutal mais allant rapidement vers
l'objectif en terme de notion. Ceci serait un argument preuve
de bon fonctionnement de votre système de recommandation.

  - Générer des parcours avec nombre d'exercice fini déterminer à
    l'avance.
	
Dans l'idée, vous reprenez un trio d'élèves fictifs (bon, moyen,
mauvais) et vous leur recommander chacun 50 exercices parmi les 93
disponibles pour le C. Vous partez systématiquement d'élèves vierge en
terme de notions (tout à zéro). Suivant la force des élèves, vous
comparez les niveaux atteints pour chacun d'entre eux après 50
exercices. On espère voir des niveaux de maîtrise plus important pour
le bon étudiant fictifs et des niveaux plus faibles pour le
mauvais. Ceci serait un argument preuve de bon fonctionnement de votre
système de recommandation.


### Challenge 2 : extractions des dépendances entre notions

Un grand nombres d'exercices n'ont aucun pré-requis. Ce dont les
exercices d'entrées sur la plateforme pour le C. De manière générale,
certaines notions sont plutôt basiques et d'autre plutôt avancées.

* Est-il possible d'extraire dans les méta-données un graphe dont les
  sommets sont les notions et les flèches seront les dépendances
  d'apprentissage ? Si notion1 est relié via une flèche à notion2,
  cela signifiera que la notion1 est plutôt un pré-requis de la
  notion2. Est-il possible de pondérer les arrêtes avec un entier qui
  représente la force de cette dépendance ? (L'entier peut-il être le
  nombre d'exercice considérant notion1 comme un pré-requis de notion2 ?)

Ceci n'est pas un objectif prioritaire mais plus on objectif
d'approfondissement.


### Challenge 3 : identifier les manques de la bases de données


Toujours en utilisant des élèves fictifs, voir un grands nombres
d'élèves fictifs, tentez de proposer une expérience algorithmique pour
voir quelles sont les notions les moins représentées. En gros, vous
proposez un programme python de simulation qui tente de renseigner les
enseignants pour leur dire : "C'est dans telle et telle notion qu'il
faudrait rajouter des exercices.". 

Ceci n'est pas un objectif prioritaire mais plus on objectif
d'approfondissement.
