# Repo de preparation IOAI 2026 - delegation Burkina Faso

Notebooks d'entrainement pour les candidats, construits directement a partir des ressources officielles de l'IOAI 2026 (Astana, Kazakhstan). Chaque notebook est autonome, tourne sans GPU, et se termine par un exercice chrono a faire en condition proche de l'epreuve.

## Comment utiliser ce repo

1. Cloner ou telecharger le dossier
2. Ouvrir les notebooks dans l'ordre (01 -> 05), chaque section a un exemple qui tourne + un exercice a faire immediatement apres
3. Ne pas juste lire : executer, casser, corriger. C'est le seul moyen d'assimiler vite (voir la section "strategie" du notebook 01)

## Contenu

| Dossier | Sujet | Aligne sur |
|---|---|---|
| `01_pytorch_fondamentaux/` | Tensors, autograd, nn.Module, boucle d'entrainement, memotechniques | Base necessaire a tous les autres notebooks |
| `02_ml_classique/` | Regression, kNN, arbres, ensemble learning, bias-variance, cross-validation, k-means, PCA | Theorie ML classique du syllabus |
| `03_transfer_learning_finetuning/` | Fine-tuning sans oubli catastrophique, replay, gel de couches | Home Task 1 officiel ("Operation Night Watch") |
| `04_imitation_learning_robotique/` | Behavioral cloning, compounding error, piste DAgger | Home Task 2 officiel ("Robot Delivery Academy") |
| `05_llm_raisonnement_20q/` | Entropie, gain d'information, strategie de questions optimales | Home Task 3 officiel ("The Analytical Language of John Wilkins") |
| `06_gaite_robotique_simulation/` | Reperage du stack robotique GALBOT (IsaacLab) pour le contest GAITE | GAITE Contest (piste separee, materiel lourd) |

## Ressources officielles a connaitre par coeur

**Site et regles**
- Syllabus officiel 2026 : https://ioai-official.org/republic-of-kazakhstan/syllabus-2026/
- Regles du concours + annexe technique (PDF) : https://ioai-official.org/wp-content/uploads/2026/06/IOAI2026-Contest-Rules-and-Tehnical-Appendix.pdf
- Le concours 2026 comprend 3 volets : **Individual Contest**, **Team Challenge**, et **GAITE Contest** (robotique)

**At-Home Round (taches preparatoires officielles)**
- Les 3 taches sur GitHub : https://github.com/IOAI-official/IOAI-2026
- Tache 1 sur Kaggle : https://www.kaggle.com/competitions/ioai-2026-home-task-1
- Tache 2 sur Kaggle : https://www.kaggle.com/competitions/ioai-2026-home-task-2
- Exemple de tache sur Yandex Contest : https://new.contest.yandex.ru/contests/93047
- Discord #HomeTasks : https://discordapp.com/channels/1271542282142748774/1520997400364454090
- Feedback & Appeals (reserve aux team leaders) : https://forms.gle/d4pwTY1mAwXeqbweA

**GAITE (piste robotique)**
- Stack robotique GALBOT (IsaacLab, simulateur G1) : https://github.com/galbot-ioai/ioailab
- Simulateur en ligne : https://simulation.galbot.com/login

## Notes pour les formateurs

Ces notebooks sont volontairement simplifies par rapport aux taches officielles (donnees synthetiques, pas de GPU requis, execution en quelques secondes) pour permettre de comprendre le mecanisme central de chaque tache rapidement. Une fois le mecanisme maitrise sur ces versions reduites, les candidats doivent absolument s'entrainer sur les vraies taches (GitHub / Kaggle) qui ajoutent la complexite reelle (vraies donnees audio/image, vrais LLM, vraie grille 8x8 avec obstacles).

A completer au fur et a mesure : ce repo est concu pour grandir, ajouter un notebook par nouvelle notion abordee en formation.
