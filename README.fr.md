# Combien de tokens de réflexion par seconde ?

*English version: [README.md](README.md)*

Un test en une page, sans serveur, pour mesurer son propre débit de « tokens de réflexion » et le comparer aux **150 tokens par seconde** que Saturnin Pugnet attribue à chaque humain, aux mesures scientifiques publiées, et à la vitesse de sortie des modèles de langage.

**Faire le test :** https://voltek62.github.io/human-tokens/

Tout se passe dans le navigateur. Rien n'est enregistré ni transmis. Interface et contenus en **français, anglais et espagnol**. La langue du navigateur est utilisée par défaut ; `#fr`, `#en` ou `#es` dans l'adresse force une langue pour un lien partagé, et le sélecteur en haut de page mémorise votre choix.

## Pourquoi

Dans le podcast Silicon Carne du 28 octobre 2026 (à 32:49), Saturnin Pugnet, membre fondateur de World avec Sam Altman, pose qu'« en gros, chaque personne réfléchit à 150 tokens de réflexion par seconde ». Il en déduit qu'en 2036 les IA produiront chaque année autant de tokens de pensée que l'humanité depuis le début des temps.

Ce chiffre est une hypothèse de travail, pas une mesure. Son manifeste *Phase Lock* ne le contient pas et ses propres totaux reviennent plutôt à 2 tokens par seconde et par personne. Le dossier complet est dans [SOURCES.md](SOURCES.md).

Plutôt que de débattre du bon chiffre, ce projet donne à chacun le moyen de mesurer le sien.

## Les quatre épreuves

| Épreuve | Ce qu'elle mesure | Référence publiée |
|---|---|---|
| Lecture silencieuse | Débit d'entrée du texte. Un texte tiré au sort parmi quatre (la danse des abeilles, le code Morse, la mesure du mètre, la machine d'Anticythère), avec deux questions de compréhension. | 238 mots/min (Brysbaert 2019) |
| Lecture à voix haute | Vitesse de la parole | 150 à 183 mots/min |
| Frappe | Débit de sortie au clavier | 52 mots/min (Dhakal et al. 2018) |
| Raisonnement | Quatre problèmes tirés au sort dans une banque de quarante-cinq (arithmétique courante, plus cinq de niveau moyen), réponses vérifiées par calcul. Pour chaque problème résolu, on compte les tokens du raisonnement écrit qu'un modèle produirait, divisés par votre temps. Les réponses fausses ne comptent pas. | 10 bits/s (Zheng & Meister 2025) |

Les passages sont comptés avec le tokenizer o200k (GPT-4o et suivants) via [gpt-tokenizer](https://github.com/niieani/gpt-tokenizer) quand il se charge, sinon avec une estimation par caractères. Les références en mots par minute sont converties avec le ratio tokens/mot de la langue choisie : 1,2 en anglais, 1,35 en espagnol, 1,5 en français (mesures sur o200k).

Le tableau de bord donne une lecture qualitative (médiane, point fort, goulot, écart avec un modèle à 100 tok/s) et trois textes de partage prêts à copier : LinkedIn, X / Bluesky / Threads, et une ligne.

## Structure

```
src/head.html   titre, polices, chargement du tokenizer
src/page.html   styles, contenu, script : textes de lecture, banque de problèmes, interface en trois langues
build.py        assemble index.html
index.html      page complète, servie par GitHub Pages
SOURCES.md      dossier de sources, calculs, réponses des problèmes
```

Modifier `src/`, puis :

```sh
python3 build.py
```

## Contribuer

Les idées bienvenues : d'autres langues (ajouter une entrée dans `LANGS`, `UI`, `READ`, `SPEAK`, `TYPE` et chaque problème), une épreuve d'écoute, d'autres textes ou problèmes, une meilleure calibration du raisonnement. Ouvrez une issue ou une pull request.

## Licence

MIT. Les textes des passages sont originaux et sous la même licence.
