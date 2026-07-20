# Module GAITE : simulation robotique (GALBOT G1, IsaacLab)

Ce dossier n'a pas de notebook autonome pour l'instant : le stack GALBOT (`ioailab`) repose sur **IsaacLab / Isaac Sim**, qui necessite un GPU NVIDIA local et une installation lourde (conteneurs Docker, drivers CUDA specifiques). Ce n'est pas reproductible dans un notebook classique ni dans un environnement sandbox sans GPU dedie, donc a traiter separement des notebooks 01-05.

## Ce que couvre le stack GALBOT ioailab

D'apres le repo officiel (https://github.com/galbot-ioai/ioailab) :
- configuration du robot G1 (bras, mains, base) pour IsaacLab
- registre de taches type IsaacLab (`GalbotG1-PickCube-v0`, PickToShelf, SortToShelf, taches composees)
- agents d'action (ex: `CuroboPlannerAgent` pour la planification de mouvement avec cuRobo)
- pipeline de donnees en 4 etapes, executees comme des processus separes :
  1. `01_collect.py` : collecte de demonstrations (teleoperation ou planificateur de mouvement)
  2. `02_mimic.py` : expansion du dataset (data augmentation de trajectoires)
  3. `03_train.py` : entrainement d'une politique (ex: `robomimic_diffusion`, un modele de diffusion pour l'imitation learning)
  4. `04_eval.py` : evaluation du checkpoint entraine
- une baseline vision "traditionnelle" avec YOLO (detection/segmentation) et FoundationPose (estimation de pose 6D d'objets)

## Pourquoi c'est utile de le comprendre malgre l'absence de notebook ici

Le concept central (collecter des demonstrations -> entrainer une politique qui imite ces demonstrations -> evaluer) est **exactement le meme principe que le notebook `04_imitation_learning_robotique`**, juste applique a un vrai bras robotique en simulation 3D au lieu d'une grille 2D. Faire le notebook 04 en profondeur donne deja les bons reflexes theoriques (behavioral cloning, compounding error, DAgger) avant de toucher a IsaacLab.

Le modele de politique utilise ici (`robomimic_diffusion`) va plus loin que notre BC simple : c'est un modele de diffusion qui apprend une distribution d'actions possibles plutot qu'une seule action deterministe, utile quand plusieurs trajectoires sont valides pour la meme observation.

## Pour s'entrainer en pratique

1. Verifier l'acces materiel (GPU NVIDIA, drivers CUDA) necessaire pour IsaacLab avant l'evenement, ce n'est pas quelque chose a decouvrir sur place
2. Suivre `docs/tutorial.md` du repo `ioailab` une fois clone
3. Le simulateur en ligne https://simulation.galbot.com/login peut permettre une premiere prise en main sans installation locale, a verifier ce qu'il expose exactement (login requis)

## A faire (TODO pour ce repo)

- [ ] Confirmer si un GPU sera disponible pour les candidats avant/pendant l'evenement
- [ ] Si oui, ajouter un notebook `06b_isaaclab_pickcube_demo.ipynb` qui reproduit le quickstart du README `ioailab` (`make build`, `make shell-gui`, collecte + entrainement sur `GalbotG1-PickCube-v0`)
- [ ] Documenter ici les differences observees entre le comportement du simulateur et le vrai robot, si testes sur place a Astana
