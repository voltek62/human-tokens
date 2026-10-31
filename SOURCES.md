# Dossier de sources : les « 150 tokens de réflexion par seconde »

Relevé le 31 octobre 2026.

## 1. D'où vient le chiffre

**Le podcast.** Silicon Carne, « Black Mirror dans votre cerveau, c'est pour bientôt ? », 28 octobre 2026, 38 min, avec Carlos Diaz (animateur), Anji Ismail et Saturnin Pugnet. https://www.youtube.com/watch?v=pLN4maID1DY. Passage à 32:49, transcription :

> « On peut réfléchir à notre civilisation comme des tokens de réflexion. Chaque personne réfléchit à 150 tokens de réflexion par seconde, en gros. On peut imaginer ça et on peut calculer depuis le début de l'humanité combien de tokens de réflexion l'humanité a créé. [...] il nous a fallu 100 milliards de tokens pour développer le feu. Il nous a fallu un trillion pour développer la voiture. [...] en 2036, sur cette trajectoire, tous les ans, les IA dans le monde vont générer autant de tokens de pensée que l'humanité dans son ensemble depuis le début des temps. [...] en 2038, toutes les semaines [...] en 2040, ce sera tous les jours. »

L'incise « c'est une façon très mathématique, c'est une vision très développeur du truc » est de Carlos Diaz, pas de Pugnet.

**Le post LinkedIn.** Le chiffre apparaît d'abord dans un post LinkedIn de Saturnin Pugnet (vers juin-juillet 2026, repris dans le fil d'activité d'Avery Krieger). Formulation, d'après l'extrait indexé : « let's assume humans think at about 150 tokens of thought per second ». C'est une hypothèse posée, sans source.

**Le manifeste.** *Phase Lock*, Saturnin Pugnet, v1.0 du 2 octobre 2026, v1.3 du 23 octobre 2026, https://phaselock.satpugnet.com. Le texte ne contient ni « 150 tokens », ni « tokens of thought », ni les totaux pour le feu et la voiture. Ce qu'il contient :

- Partie I, section 03 : « speech runs at about 150 words per minute, typing at 50, reading at maybe 250, inner thought is harder to measure but probably runs at 1,000 to 4,000 words per minute equivalent ». Sans note de bas de page. **Le 150 du manifeste est donc 150 mots par minute de parole.**
- Partie II, section 09, graphique « The scale mismatch » : « Conscious thought, one lifetime ≈ 5 × 10⁹ tokens ». Sur une vie de 80 ans (2,5 × 10⁹ secondes), cela fait **2 tokens par seconde**.
- Partie III, section 16, graphique « Out-Thought », lignes de référence : toute la pensée humaine depuis le début des temps ≈ 6 × 10²⁰ tokens, croisée « ≈ 2036 » ; une année de pensée humaine ≈ 5 × 10¹⁷ ; une année de parole humaine ≈ 5 × 10¹⁶ ; une année d'écriture humaine ≈ 2 × 10¹⁵ ; tous les livres jamais écrits ≈ 10¹³. Légende : « On the current trajectory it will generate more thought than all humanity combined around 2030. And by the mid-2030s, a single year of AI output will exceed humanity's entire intellectual output since the dawn of time. » Note 27 : « Estimates based on OpenAI, Google, and words-per-day studies. »
- Partie III, section 18 : sortie consciente de l'esprit « ~10 bits / sec » contre intake sensoriel « ~10⁹ bits/sec ».

## 2. Ce qu'impliquent ses propres chiffres

| Donnée du manifeste | Calcul | Débit par personne |
|---|---|---|
| 5 × 10¹⁷ tokens de pensée par an, 8 × 10⁹ humains | 5e17 / (8e9 × 3,15e7 s) | **2,0 tok/s** |
| 5 × 10¹⁶ tokens de parole par an | 5e16 / (8e9 × 3,15e7 s) | 0,2 tok/s en moyenne sur 24 h, cohérent avec ≈ 16 000 mots par jour (Mehl et al. 2007) |
| 6 × 10²⁰ tokens depuis le début des temps, 117 × 10⁹ humains nés (PRB), ≈ 30 ans de vie moyenne historique, 16 h d'éveil | 6e20 / (117e9 × 30 × 365 × 16 × 3600) | **≈ 8 tok/s** |
| 5 × 10⁹ tokens de pensée consciente par vie | 5e9 / (80 × 3,15e7 s) | **2,0 tok/s** |

À 150 tok/s pendant 16 h par jour, une seule personne produit 8,6 millions de tokens par jour et 3,2 milliards par an. « 100 milliards de tokens pour développer le feu » représenterait alors 32 années-personne de réflexion : ces ordres de grandeur dits à l'oral ne sont pas cohérents avec les totaux du manifeste, qui supposent des centaines de milliers d'années et des milliards d'individus. Il faut les lire comme des illustrations, pas comme des estimations.

Le 150 du podcast est aussi, à peu de chose près, la vitesse de sortie d'un grand modèle de langage en 2026 (voir § 4).

## 3. Mesures humaines publiées

Conversion : 1 mot français ≈ 1,5 token sur o200k (voir § 5). 1 mot anglais ≈ 1,2 token.

| Mesure | Valeur | En tokens/s (ratio 1,5) | Source |
|---|---|---|---|
| Débit informationnel d'un humain, toutes tâches | ≈ 10 bits/s | 2 à 3 tok/s, à ≈ 4 bits d'information par token (≈ 1 bit par caractère, Shannon 1951) | Zheng J., Meister M., « The unbearable slowness of being: Why do we live at 10 bits/s? », *Neuron* 113, 2025, https://doi.org/10.1016/j.neuron.2024.11.008 ; préprint https://arxiv.org/abs/2408.10234 |
| Lecture silencieuse, adultes, non-fiction | 238 mots/min (190 études, 18 573 participants) | 6,0 | Brysbaert M., « How many words do we read per minute? A review and meta-analysis of reading rate », *Journal of Memory and Language* 109, 2019, https://doi.org/10.1016/j.jml.2019.104047 |
| Lecture à voix haute | 183 mots/min | 4,6 | idem |
| Parole en conversation (anglais) | ≈ 150 mots/min | 3,75 | National Center for Voice and Speech, repris par https://virtualspeech.com/blog/average-speaking-rate-words-per-minute |
| Frappe au clavier | 52 mots/min (168 960 participants, volontaires, donc un peu surestimé) | 1,3 | Dhakal V., Feit A. M., Kristensson P. O., Oulasvirta A., « Observations on Typing from 136 Million Keystrokes », CHI 2018, https://doi.org/10.1145/3173574.3174220 |
| Parole intérieure, équivalent étendu | > 4 000 mots/min (compte « étendu » : les ellipses de la pensée développées en phrases complètes) | ≈ 100 | Korba R. J., « The Rate of Inner Speech », *Perceptual and Motor Skills* 71(3), 1990, https://doi.org/10.2466/pms.1990.71.3.1043 |
| Entropie de l'anglais écrit | 0,6 à 1,3 bit par caractère ; ≈ 1,2 bit/car. en réplication | sert à convertir les bits en tokens | Shannon C. E., « Prediction and Entropy of Printed English », 1951 ; réplication https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7514546/ |
| Humains nés depuis 190 000 av. J.-C. | ≈ 117 milliards | sert au calcul du § 2 | Population Reference Bureau, https://www.prb.org/news/how-many-people-have-ever-lived-on-earth/ |

Lecture : la seule mesure humaine qui approche 150 tok/s est l'équivalent *étendu* de la parole intérieure selon Korba, un compte reconstruit après coup, pas un débit observé. Toutes les mesures directes de débit (lire, parler, taper, et le plafond informationnel de 10 bits/s) tombent entre 1 et 6 tokens par seconde. L'écart avec 150 est d'un facteur 25 à 100.

## 4. Vitesse de sortie des modèles (tokens/s, 2026)

| Modèle | tok/s | Source |
|---|---|---|
| Claude Fable 5.1 | ≈ 68 | relevé de septembre 2026, https://ciad.cz/en/comparisons/ai-model-speed-tested-tokens-per-second-and-latency-september-2026/ |
| Gemini 3.1 Pro Preview | 134 (médiane de sa classe de prix : 82) | https://artificialanalysis.ai/models/gemini-3-1-pro-preview |
| Gemini 3.5 Flash | > 280 | https://artificialanalysis.ai/articles/gemini-3-5-flash-everything-you-need-to-know |
| Gemini 3.5 Flash-Lite | 461 | https://artificialanalysis.ai/providers/google |
| Groq, Cerebras (modèles ouverts) | 2 000 et plus | relevés 2026 |

## 5. Tokens par mot

| Langue, tokenizer | tokens/mot | Source |
|---|---|---|
| Anglais, o200k | 1,16 à 1,2 | https://textkit.tech/blog/tokens-per-word-tokenizer-comparison-2026 |
| Français, o200k | 1,4 à 1,5 | https://www.nihardaily.com/posts/llm-token-cost-by-language-we-measured-14-of-them |
| Français, cl100k | ≈ 1,7 à 2 | https://community.openai.com/t/explosion-in-the-number-of-tokens-words-generated/317702 |

Le test compte les passages avec le vrai tokenizer o200k (bibliothèque gpt-tokenizer 2.9.0) et n'utilise le ratio 1,5 que pour convertir les références publiées en mots par minute.

## 6. Ce que ça change au raisonnement de Pugnet

Rien à la conclusion, tout au chiffre. Si l'humain réfléchit à 3 tok/s plutôt que 150, le stock de pensée humaine depuis le début des temps est 50 fois plus petit que ses 6 × 10²⁰, et la date où une année d'IA le dépasse recule d'environ un an et demi sur sa propre courbe (un facteur 50 à ≈ 3 par an). Le point qui tient : le débit d'un humain est fixe, à 3 ou à 150, et celui des machines change d'ordre de grandeur tous les deux ans.

## 7. Les quarante-cinq problèmes de raisonnement et leurs réponses

Quatre sont tirés au sort à chaque série. Les quarante premiers relèvent de l'arithmétique courante, les cinq derniers demandent un raisonnement d'une étape de plus. Réponses vérifiées par calcul le 31 octobre 2026.

| # | Problème (résumé) | Réponse |
|---|---|---|
| 1 | Un cahier à 3 €, 7 cahiers | 21 |
| 2 | 24 œufs, 9 utilisés | 15 |
| 3 | 1 h 50 en minutes | 110 |
| 4 | 3 pizzas de 8 parts | 24 |
| 5 | 80 km/h pendant 3 h | 240 |
| 6 | 40 € soldé de 25 % | 30 |
| 7 | 17 + 28 | 45 |
| 8 | Deux heures et demie en minutes | 150 |
| 9 | 30 élèves, 40 % de filles | 12 |
| 10 | Rectangle 6 × 4, aire | 24 |
| 11 | 5 kg en portions de 250 g | 20 |
| 12 | Thomas 12 ans, sœur le double, dans 3 ans | 27 |
| 13 | 12 personnes × 2 bouteilles | 24 |
| 14 | 6 L/100 km, 350 km | 21 |
| 15 | Moitié de 86 | 43 |
| 16 | Monnaie sur 10 € pour 2,80 €, en centimes | 720 |
| 17 | 100 − 37 | 63 |
| 18 | 4 volées de 12 marches | 48 |
| 19 | Jours dans 6 semaines | 42 |
| 20 | 180 pages à 30 par soir | 6 |
| 21 | Carré de périmètre 36, côté | 9 |
| 22 | 15 L/min, baignoire 180 L | 12 |
| 23 | 60 € + 10 % | 66 |
| 24 | 9 × 7 | 63 |
| 25 | 45 € partagés en 3 | 15 |
| 26 | Minutes entre 9 h 40 et 10 h 15 | 35 |
| 27 | 5 boîtes de 12 crayons, 20 donnés | 40 |
| 28 | 4 allers-retours de 15 km | 120 |
| 29 | 400 m en 80 s, m/s | 5 |
| 30 | Quart de 200 | 50 |
| 31 | 350 g à 25 g la tartine | 14 |
| 32 | Somme des faces d'un dé | 21 |
| 33 | 3 étages de 45 places, 110 voitures | 25 |
| 34 | Triangle 5, 7, 9, périmètre | 21 |
| 35 | De −3 °C à 8 °C, hausse | 11 |
| 36 | 3 km × 5 jours × 4 semaines | 60 |
| 37 | Tickets à 2,50 € avec 20 € | 8 |
| 38 | Double plus 5 = 29 | 12 |
| 39 | 200 g pour 8, pour 12 | 300 |
| 40 | 24 km en 1 h 30, km/h | 16 |
| 41 | Livre + marque-page 12,50 €, écart 12 €, marque-page en centimes | 25 |
| 42 | 3 imprimantes, 3 affiches, 3 min → 30 et 30 | 3 |
| 43 | Nénuphar qui double, étang couvert le jour 30, un quart le jour | 28 |
| 44 | Poignées de main entre 8 personnes | 28 |
| 45 | 60 km à 30 km/h puis 60 km à 60 km/h, vitesse moyenne | 40 |

Le « raisonnement écrit » dont on compte les tokens est, pour chaque problème, une à trois phrases dans la langue du test (voir `PUZZLES` dans `src/page.html`). C'est un équivalent, pas une mesure de ce qui se passe dans la tête.

## 8. Ratios tokens par mot utilisés par langue

| Langue | tokens/mot | caractères/token (repli) |
|---|---|---|
| Anglais | 1,2 | 4,2 |
| Espagnol | 1,35 | 4,0 |
| Français | 1,5 | 3,9 |
