# Annales Corrigées — Université de Kara

**Auteurs** : DJABON Ounimborbitibou & BOUTCHOKA Malaki  
**Version** : V4 corrigée — Juin 2026  
**Niveaux** : Licence 1, Licence 2, Licence 3 (Parcours MPC)

## Structure du dossier

```
ANNALES_CORRIGEES/
├── preambule_commun.tex       ← Préambule LaTeX commun (ne pas modifier)
├── page_de_garde_modele.tex   ← Modèle de page de garde
├── README.md                   ← Ce fichier
├── L1/                         ← 11 UEs + main + page de garde
│   ├── main_L1.tex / .pdf     ← Document complet L1 (230 pages)
│   ├── Atomistique_L1.tex / .pdf
│   ├── Algebre_Lineaire_L1.tex / .pdf
│   ├── Analyse_Vectorielle_L1.tex / .pdf
│   ├── Calcul_Differentiel_L1.tex / .pdf
│   ├── Calcul_Integral_L1.tex / .pdf
│   ├── Electrocinetique_L1.tex / .pdf
│   ├── Electrostatique_L1.tex / .pdf     ← Avec schémas TikZ vectoriels
│   ├── Logique_L1.tex / .pdf             ← 25 exercices (+10 ajoutés)
│   ├── MPM_L1.tex / .pdf                 ← Mécanique du Point Matériel
│   ├── Programmation_C_L1.tex / .pdf
│   ├── Optique_Geometrique_L1.tex / .pdf
│   ├── page_garde_L1.tex / .pdf
│   ├── images/                           ← 129 images L1
│   └── transitions/                      ← Pages de transition entre UEs
├── L2/                         ← 12 UEs + main
│   ├── main_L2.tex / .pdf     ← Document complet L2 (225 pages)
│   └── ... (12 UEs)
└── L3/                         ← 13 UEs + main
    ├── main_L3.tex / .pdf     ← Document complet L3 (351 pages)
    └── ... (13 UEs)
```

## Statistiques finales

| Niveau | Pages | Images | Exercices | Overflows critiques |
|--------|-------|--------|-----------|---------------------|
| L1     | 230   | 68     | 190       | 0                   |
| L2     | 225   | 83     | 151       | 0                   |
| L3     | 351   | 107    | 267       | 0                   |
| **TOTAL** | **806** | **258** | **608** | **0** |

## Comment compiler

Pour compiler un fichier UE individuel :
```bash
cd L1  # ou L2, L3
tectonic Atomistique_L1.tex
```

Pour compiler le document complet d'un niveau :
```bash
cd L1  # ou L2, L3
tectonic main_L1.tex
```

**Pré-requis** : Tectonic (https://tectonic-typesetting.github.io/)

## Améliorations apportées (V4)

### Bug typographique "œ" corrigé
- Tous les caractères unicode "œ" remplacés par `\oe{}` (commande LaTeX robuste)
- "Comme toute \oe{}uvre humaine..." s'affiche désormais correctement

### Pages de transition
- Tous les titres longs (>25 caractères) divisés sur 2 lignes
- Fontsizes adaptées (36 → 30 → 26 → 22 selon la longueur)
- Plus aucun débordement sur les pages de transition

### Exercices
- **608 exercices** au total (vs 548 en V3)
- Tous les exercices sont numérotés séquentiellement de 1 à N
- Plus aucun "Exercice -" sans numéro
- Plus aucun trou dans la numérotation

### Images
- **258 images** intégrées dans les PDFs finaux
- Schémas physiques recréés en TikZ pour Électrostatique L1
- Images extraites des anciens PDFs et réintégrées

### Symboles typographiques
- **0 symbole AI unicode** (em-dash —, en-dash –, flèches, grecques)
- Tous remplacés par les commandes LaTeX standard

### Débordements de marge
- **0 overflow critique** (>5pt) — tous les overflows restants sont <5pt (cosmétiques)
- Équations longues passées en mode display
- Tableaux passés en `tabularx{\textwidth}`

### Qualité typographique
- Notations vectorielles uniformisées (`\vect{}` partout)
- Démonstrations mathématiques standardisées
- Caractères spéciaux en mode math gérés via `\text{}` (I_{\text{enlacé}} etc.)

## Signalement d'erreurs

Comme toute \oe{}uvre humaine n'est jamais parfaite, prière de signaler toute erreur ou imprécision constatée dans ce document aux auteurs.
