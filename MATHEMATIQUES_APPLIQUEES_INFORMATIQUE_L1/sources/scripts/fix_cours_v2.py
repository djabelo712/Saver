# -*- coding: utf-8 -*-
"""Corrections du cours MAI L1-L2 (retour utilisateur) :
1. suppression des tirets cadratins (le << tiret AI >>) dans tout le texte ;
2. ajout de l'ensemble des decimaux D (tableau + texte + figure 1.1) ;
3. refonte des figures 1.1, 1.2, 1.3, 1.4 (chevauchements) ;
4. refonte des figures de portes logiques 2.1 (circuit faux : C manquant)
   et 2.2 (silhouettes OU/XOR incorrectes) ;
5. refonte des figures 5.1 (cercle trigo) et 5.2 (vecteur) ;
6. ajustement de la figure 6.1 (titre du panneau bitmap) ;
7. panneau 3 de la page de garde : Probabilites -> Ensembles ;
8. macro \D dans le preambule.
Chaque remplacement est verifie (nombre d'occurrences = 1).
"""
import sys

BASE = '/home/z/my-project/mai_l1/'
D = BASE + 'docs/cours_l1/'

def applique(path, paires):
    with open(path, encoding='utf-8') as f:
        s = f.read()
    for old, new in paires:
        n = s.count(old)
        if n != 1:
            print('ECHEC (%d occurrences) dans %s :\n  %r' % (n, path, old[:90]))
            sys.exit(1)
        s = s.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)
    print('OK  %-28s (%2d remplacements)' % (path.split('/')[-1], len(paires)))

# ============================================================
# 1. PREAMBULE : macro D + panneau 3 de la page de garde
# ============================================================
pream = BASE + 'parts/00_preamble.tex'
applique(pream, [
    (r"\newcommand{\R}{\mathbb{R}}",
     r"\newcommand{\R}{\mathbb{R}}" + "\n" + r"\newcommand{\D}{\mathbb{D}}"),
    (r"""% panneau 3 : evenements et probabilites
\fill[white, draw=rogris!45, line width=0.7pt, rounded corners=2.5mm]
  (14.0,-13.8) rectangle (19.2,-20.05);
\fill[rogold] (14.28,-14.05) rectangle (18.92,-14.11);
\node[text=rogris, font=\footnotesize\scshape] at (16.6,-19.68)
  {\textls[110]{Probabilités}};
\begin{scope}[shift={(16.6,-16.55)}, scale=1.0]
  \draw[rogris!70, line width=0.9pt, rounded corners=1.4mm, fill=white]
    (-1.15,-1.1) rectangle (1.15,1.1);
  \fill[roor] (-0.55,0.55) circle (0.13);
  \fill[roor] (0.55,0.55) circle (0.13);
  \fill[roor] (0,0) circle (0.13);
  \fill[roor] (-0.55,-0.55) circle (0.13);
  \fill[roor] (0.55,-0.55) circle (0.13);
  \node[font=\scriptsize, text=rogris] at (0,-1.6) {$P(\text{face } 5) = 1/6$};
\end{scope}""",
     r"""% panneau 3 : ensembles et diagramme de Venn
\fill[white, draw=rogris!45, line width=0.7pt, rounded corners=2.5mm]
  (14.0,-13.8) rectangle (19.2,-20.05);
\fill[rogold] (14.28,-14.05) rectangle (18.92,-14.11);
\node[text=rogris, font=\footnotesize\scshape] at (16.6,-19.68)
  {\textls[110]{Ensembles}};
\begin{scope}[shift={(16.6,-16.7)}, scale=1.0]
  \draw[rogris!60, line width=0.6pt, fill=rogrisf!40]
    (-1.5,-1.05) rectangle (1.5,1.15);
  \draw[robleu, line width=1pt, fill=robleuf, fill opacity=0.65]
    (-0.62,0.05) ellipse (0.8 and 0.58);
  \draw[roteal, line width=1pt, fill=rotealf, fill opacity=0.65]
    (0.62,0.05) ellipse (0.8 and 0.58);
  \node[font=\scriptsize, text=rogris] at (0,-1.6)
    {$A \cup B$, $A \cap B$ et $\overline{A}$};
\end{scope}"""),
])

# ============================================================
# 2. FRONTMATTER : tirets des titres
# ============================================================
applique(D + '10_frontmatter.tex', [
    ("pdftitle={Mathématiques Appliquées à l'Informatique — Licence 1 & 2 : support de cours}",
     "pdftitle={Mathématiques Appliquées à l'Informatique (Licence 1 & 2) : support de cours}"),
    (r"\renewcommand{\DocTitre}{Mathématiques Appliquées à l'Informatique — Licence 1 \& 2}",
     r"\renewcommand{\DocTitre}{Mathématiques Appliquées à l'Informatique (Licence 1 \& 2)}"),
    (r"\renewcommand{\DocKicker}{Institut Supérieur CPTEC --- Support de cours}",
     r"\renewcommand{\DocKicker}{Institut Supérieur CPTEC \textbullet{} Support de cours}"),
    (r"\renewcommand{\DocDescription}{Support de cours de l'étudiant --- six chapitres avec exemples résolus}",
     r"\renewcommand{\DocDescription}{Support de cours de l'étudiant : six chapitres avec exemples résolus}"),
])

# ============================================================
# 3. CHAPITRE 1 : tirets + decimaux + figures 1.1 a 1.4
# ============================================================
applique(D + '20_ch01.tex', [
    # --- tirets ---
    ("les trois opérations fondamentales — union, intersection, complémentaire — et leurs propriétés",
     "les trois opérations fondamentales (union, intersection, complémentaire) et leurs propriétés"),
    ("une combinaison d'appartenances — dans $A$ mais ni dans $B$ ni dans $C$, dans $A$ et $B$ mais pas dans $C$, et ainsi de suite — et le comptage",
     "une combinaison d'appartenances (dans $A$ mais ni dans $B$ ni dans $C$, dans $A$ et $B$ mais pas dans $C$, et ainsi de suite), et le comptage"),
    ("deux choix successifs — un identifiant et un mot de passe, une ligne et une colonne d'une feuille de calcul, un utilisateur et une machine d'un réseau.",
     "deux choix successifs : un identifiant et un mot de passe, une ligne et une colonne d'une feuille de calcul, un utilisateur et une machine d'un réseau."),
    ("étudié au chapitre 3 — compter les codages, c'est compter les sous-ensembles.",
     "étudié au chapitre 3 : compter les codages, c'est compter les sous-ensembles."),
    ("des petits ensembles concrets — deux sous-ensembles de $\\{1, 2, 3, 4\\}$ suffisent — puis calculer",
     "des petits ensembles concrets (deux sous-ensembles de $\\{1, 2, 3, 4\\}$ suffisent), puis calculer"),
    ("Les trois opérations — union $A \\cup B$, intersection $A \\cap B$, complémentaire $\\overline{A}$ — se lisent",
     "Les trois opérations (union $A \\cup B$, intersection $A \\cap B$, complémentaire $\\overline{A}$) se lisent"),
    # --- decimaux : tableau ---
    (r"$\Q$ & nombres rationnels, quotients d'entiers & $-7$ ; $\dfrac{2}{3}$ ; $0{,}75$\\",
     r"$\D$ & nombres décimaux, écriture finie après la virgule & $-7$ ; $0{,}75$ ; $2{,}5$\\" + "\n" +
     r"\rowcolor{rogrisf!50}$\Q$ & nombres rationnels, quotients d'entiers & $-7$ ; $\dfrac{2}{3}$ ; $0{,}75$\\"),
    (r"\rowcolor{rogrisf!50}$\R$ & nombres réels, rationnels et irrationnels & $\sqrt{2}$ ; $\pi$ ; $0{,}75$\\",
     r"$\R$ & nombres réels, rationnels et irrationnels & $\sqrt{2}$ ; $\pi$ ; $0{,}75$\\"),
    # --- decimaux : texte ---
    ("tout entier naturel est un entier relatif, tout entier relatif est un rationnel, tout rationnel est un réel. La figure~\\ref{ch1:fig:nombres} illustre cet emboîtement.",
     "tout entier naturel est un entier relatif, tout entier relatif est un décimal, tout décimal est un rationnel, tout rationnel est un réel. Les décimaux $\\D$ sont les nombres dont l'écriture s'arrête après la virgule, comme $0{,}75$ ou $2{,}5$ : chacun s'écrit comme un quotient d'entiers par une puissance de 10, et la fraction $\\tfrac{1}{3}$, dont les décimales se répètent sans fin, n'en fait pas partie. La figure~\\ref{ch1:fig:nombres} illustre cet emboîtement."),
    ("Rangeons les nombres $-7$, $\\dfrac{2}{3}$, $0$, $\\sqrt{2}$, $15$ dans les bons ensembles. Les nombres $-7$, $0$ et $15$ sont des entiers relatifs, donc ils appartiennent à $\\Z$ et aussi à $\\N$ pour $0$ et $15$ ; le nombre $\\dfrac{2}{3}$ est rationnel sans être entier ; le nombre $\\sqrt{2}$ est réel mais irrationnel, car aucun quotient d'entiers ne vaut exactement $\\sqrt{2}$. On a donc $0, 15 \\in \\N$ ; $-7 \\in \\Z$ ; $\\dfrac{2}{3} \\in \\Q$ ; $\\sqrt{2} \\in \\R$ mais $\\sqrt{2} \\notin \\Q$.",
     "Rangeons les nombres $-7$, $\\dfrac{2}{3}$, $0{,}75$, $0$, $\\sqrt{2}$, $15$ dans les bons ensembles. Les nombres $-7$, $0$ et $15$ sont des entiers relatifs, donc ils appartiennent à $\\Z$ et aussi à $\\N$ pour $0$ et $15$ ; le nombre $0{,}75$ est décimal, car $0{,}75 = \\tfrac{75}{100}$ ; le nombre $\\dfrac{2}{3}$ est rationnel sans être décimal, ses décimales se répétant sans fin ; le nombre $\\sqrt{2}$ est réel mais irrationnel, car aucun quotient d'entiers ne vaut exactement $\\sqrt{2}$. On a donc $0, 15 \\in \\N$ ; $-7 \\in \\Z$ ; $0{,}75 \\in \\D$ ; $\\dfrac{2}{3} \\in \\Q$ ; $\\sqrt{2} \\in \\R$ mais $\\sqrt{2} \\notin \\Q$."),
    # --- figure 1.1 : emboitement N C Z C D C Q C R ---
    (r"""\begin{center}
\begin{tikzpicture}[scale=0.9]
  \draw[rogris!70, line width=0.8pt, fill=rogrisf!30, rounded corners=2mm] (0,0) rectangle (11.6,4.6);
  \node[anchor=north west, text=rogris, font=\footnotesize\bfseries] at (0.15,4.5) {$\R$ réels};
  \draw[robleu, line width=0.8pt, fill=robleuf, rounded corners=2mm] (0.5,0.4) rectangle (9.6,3.4);
  \node[anchor=north west, text=robleu, font=\footnotesize\bfseries] at (0.65,3.3) {$\Q$ rationnels};
  \draw[roteal, line width=0.8pt, fill=rotealf, rounded corners=2mm] (0.9,0.7) rectangle (7.2,2.4);
  \node[anchor=north west, text=roteal, font=\footnotesize\bfseries] at (1.05,2.3) {$\Z$ entiers relatifs};
  \draw[rogold, line width=0.8pt, fill=rogoldf, rounded corners=2mm] (1.3,1.0) rectangle (4.6,2.1);
  \node[text=rogold, font=\footnotesize\bfseries] at (2.95,1.55) {$\N$ naturels};
  \node[font=\footnotesize, text=rogris] at (10.4,2.6) {$\sqrt{2}$};
  \node[font=\footnotesize, text=rogris] at (10.4,1.5) {$\pi$};
  \node[font=\footnotesize, text=rogris] at (8.4,1.4) {$\dfrac{2}{3}$};
  \node[font=\footnotesize, text=rogris] at (5.9,1.5) {$-7$};
  \node[font=\footnotesize, text=rogris] at (2.95,0.35) {$0$, $1$, $17$, $256$};
\end{tikzpicture}
\captionof{figure}{Les ensembles de nombres s'emboîtent : $\N \subset \Z \subset \Q \subset \R$}
\label{ch1:fig:nombres}
\end{center}""",
     r"""\begin{center}
\begin{tikzpicture}[scale=0.92]
  % --- R : reels (bande du haut : etiquettes et exemples) ---
  \draw[rogris!70, line width=0.8pt, fill=rogrisf!30, rounded corners=2mm]
    (0,0) rectangle (14.2,6.0);
  \node[anchor=west, text=rogris, font=\footnotesize\bfseries] at (0.35,5.5) {$\R$ réels};
  \node[anchor=east, text=rogris, font=\footnotesize] at (13.85,5.5) {$\sqrt{2}$ \quad $\pi$};
  % --- Q : rationnels ---
  \draw[robleu, line width=0.8pt, fill=robleuf, rounded corners=2mm]
    (0.55,0.35) rectangle (12.2,5.0);
  \node[anchor=west, text=robleu, font=\footnotesize\bfseries] at (0.9,4.55) {$\Q$ rationnels};
  \node[anchor=east, text=rogris, font=\footnotesize] at (11.85,4.55) {$\dfrac{2}{3}$};
  % --- D : decimaux ---
  \draw[roor, line width=0.8pt, fill=roorf, rounded corners=2mm]
    (1.1,0.7) rectangle (10.2,4.05);
  \node[anchor=west, text=roor, font=\footnotesize\bfseries] at (1.45,3.6) {$\D$ décimaux};
  \node[anchor=east, text=rogris, font=\footnotesize] at (9.85,3.6) {$0{,}75$ \quad $2{,}5$};
  % --- Z : entiers relatifs ---
  \draw[roteal, line width=0.8pt, fill=rotealf, rounded corners=2mm]
    (1.65,1.05) rectangle (8.2,3.15);
  \node[anchor=west, text=roteal, font=\footnotesize\bfseries] at (2.0,2.7) {$\Z$ entiers relatifs};
  \node[anchor=east, text=rogris, font=\footnotesize] at (7.85,2.7) {$-7$};
  % --- N : entiers naturels ---
  \draw[rogold, line width=0.8pt, fill=rogoldf, rounded corners=2mm]
    (2.2,1.4) rectangle (7.0,2.25);
  \node[anchor=west, text=rogold, font=\footnotesize\bfseries] at (2.5,1.82) {$\N$ naturels};
  \node[anchor=east, text=rogris, font=\footnotesize] at (6.7,1.82) {$0$ ; $17$ ; $256$};
\end{tikzpicture}
\captionof{figure}{Les ensembles de nombres s'emboîtent : $\N \subset \Z \subset \D \subset \Q \subset \R$}
\label{ch1:fig:nombres}
\end{center}"""),
    # --- figure 1.2 : Venn a deux ensembles ---
    (r"""\begin{center}
\begin{tikzpicture}[scale=0.72]
  \draw[rogris!60, line width=0.6pt, fill=rogrisf!40] (0,0) rectangle (10,4.6);
  \node[text=rogris, font=\footnotesize] at (0.55,4.25) {$U$};
  \draw[robleu, line width=1pt, fill=robleuf, fill opacity=0.55] (3.7,2.3) ellipse (2.3 and 1.65);
  \draw[roteal, line width=1pt, fill=rotealf, fill opacity=0.55] (6.3,2.3) ellipse (2.3 and 1.65);
  \node[text=robleu, font=\bfseries] at (2.9,3.35) {$A$};
  \node[text=roteal, font=\bfseries] at (7.1,3.35) {$B$};
  \node[font=\footnotesize, text=rogris] at (2.95,2.3) {$A \cap \overline{B}$};
  \node[font=\footnotesize, text=rogris] at (5.0,2.3) {$A \cap B$};
  \node[font=\footnotesize, text=rogris] at (7.05,2.3) {$\overline{A} \cap B$};
  \node[font=\footnotesize, text=rogris] at (1.35,1.0) {$\overline{A \cup B}$};
  \node[font=\footnotesize, text=rogris] at (8.7,1.0) {$\overline{A \cup B}$};
  \node[font=\footnotesize, text=rogris] at (5.0,0.55) {$\overline{A} \cap \overline{B} = \overline{A \cup B}$};
\end{tikzpicture}
\captionof{figure}{Diagramme de Venn de deux ensembles sécants : chaque région a un nom}
\label{ch1:fig:venn}
\end{center}""",
     r"""\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[rogris!60, line width=0.6pt, fill=rogrisf!40] (0,0) rectangle (11.2,5.4);
  \node[text=rogris, font=\footnotesize] at (0.55,4.95) {$U$};
  \draw[robleu, line width=1pt, fill=robleuf, fill opacity=0.55] (4.0,2.7) ellipse (2.6 and 1.9);
  \draw[roteal, line width=1pt, fill=rotealf, fill opacity=0.55] (7.2,2.7) ellipse (2.6 and 1.9);
  \node[text=robleu, font=\bfseries] at (2.6,4.1) {$A$};
  \node[text=roteal, font=\bfseries] at (8.6,4.1) {$B$};
  \node[font=\footnotesize, text=rogris] at (3.1,2.7) {$A \cap \overline{B}$};
  \node[font=\footnotesize, text=rogris] at (5.6,2.7) {$A \cap B$};
  \node[font=\footnotesize, text=rogris] at (8.1,2.7) {$\overline{A} \cap B$};
  \node[font=\footnotesize, text=rogris] at (1.75,0.55) {$\overline{A \cup B}$};
  \node[font=\footnotesize, text=rogris] at (9.45,0.55) {$\overline{A \cup B}$};
\end{tikzpicture}
\captionof{figure}{Diagramme de Venn de deux ensembles sécants : chaque région porte un nom, et $\overline{A} \cap \overline{B} = \overline{A \cup B}$}
\label{ch1:fig:venn}
\end{center}"""),
    # --- figure 1.3 : repartition des 120 etudiants ---
    (r"""\begin{center}
\begin{tikzpicture}[scale=0.72]
  \draw[rogris!60, line width=0.6pt, fill=rogrisf!40] (0,0) rectangle (10,4.6);
  \node[text=rogris, font=\footnotesize] at (0.55,4.25) {$U = 120$};
  \draw[robleu, line width=1pt, fill=robleuf, fill opacity=0.55] (3.7,2.3) ellipse (2.3 and 1.65);
  \draw[roteal, line width=1pt, fill=rotealf, fill opacity=0.55] (6.3,2.3) ellipse (2.3 and 1.65);
  \node[text=robleu, font=\bfseries] at (2.9,3.5) {$P$};
  \node[text=roteal, font=\bfseries] at (7.1,3.5) {$R$};
  \node[font=\footnotesize, text=rogris] at (2.95,2.3) {$40$};
  \node[font=\bfseries, text=roor] at (5.0,2.3) {$25$};
  \node[font=\footnotesize, text=rogris] at (7.05,2.3) {$25$};
  \node[font=\footnotesize, text=rogris] at (5.0,0.6) {$30$};
\end{tikzpicture}
\captionof{figure}{Répartition des 120 étudiants : 90 suivent au moins un des deux modules}
\label{ch1:fig:cptec}
\end{center}""",
     r"""\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[rogris!60, line width=0.6pt, fill=rogrisf!40] (0,0) rectangle (11.2,5.4);
  \node[text=rogris, font=\footnotesize] at (0.55,4.95) {$U = 120$};
  \draw[robleu, line width=1pt, fill=robleuf, fill opacity=0.55] (4.0,2.7) ellipse (2.6 and 1.9);
  \draw[roteal, line width=1pt, fill=rotealf, fill opacity=0.55] (7.2,2.7) ellipse (2.6 and 1.9);
  \node[text=robleu, font=\bfseries] at (2.6,4.1) {$P$};
  \node[text=roteal, font=\bfseries] at (8.6,4.1) {$R$};
  \node[font=\footnotesize, text=rogris] at (3.1,2.7) {$40$};
  \node[font=\bfseries, text=roor] at (5.6,2.7) {$25$};
  \node[font=\footnotesize, text=rogris] at (8.1,2.7) {$25$};
  \node[font=\footnotesize, text=rogris] at (5.6,0.5) {$30$};
\end{tikzpicture}
\captionof{figure}{Répartition des 120 étudiants : 90 suivent au moins un des deux modules}
\label{ch1:fig:cptec}
\end{center}"""),
    # --- figure 1.4 : Venn a trois ensembles ---
    (r"""\begin{center}
\begin{tikzpicture}[scale=0.78]
  \draw[rogris!60, line width=0.6pt, fill=rogrisf!40] (0,0) rectangle (9.6,5.4);
  \node[text=rogris, font=\footnotesize] at (0.5,5.05) {$U$};
  \draw[robleu, line width=1pt, fill=robleuf, fill opacity=0.5] (3.4,2.9) ellipse (2.15 and 1.75);
  \draw[roteal, line width=1pt, fill=rotealf, fill opacity=0.5] (6.2,2.9) ellipse (2.15 and 1.75);
  \draw[rogold, line width=1pt, fill=rogoldf, fill opacity=0.5] (4.8,1.7) ellipse (2.15 and 1.75);
  \node[text=robleu, font=\bfseries] at (2.35,3.9) {$A$};
  \node[text=roteal, font=\bfseries] at (7.25,3.9) {$B$};
  \node[text=rogold, font=\bfseries] at (4.8,0.62) {$C$};
  \node[font=\scriptsize, text=rogris] at (3.5,3.35) {1};
  \node[font=\scriptsize, text=rogris] at (4.8,3.35) {2};
  \node[font=\scriptsize, text=rogris] at (6.1,3.35) {3};
  \node[font=\scriptsize, text=rogris] at (3.85,2.5) {4};
  \node[font=\scriptsize, text=rogris] at (5.75,2.5) {5};
  \node[font=\scriptsize, text=rogris] at (6.45,1.65) {6};
  \node[font=\scriptsize, text=rogris] at (4.8,1.35) {7};
  \node[font=\scriptsize, text=rogris] at (1.35,1.0) {8};
\end{tikzpicture}
\captionof{figure}{Trois ensembles sécants : huit régions numérotées, dont le noyau $A \cap B \cap C$ (région 7)}
\label{ch1:fig:venn3}
\end{center}""",
     r"""\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[rogris!60, line width=0.6pt, fill=rogrisf!40] (0,0) rectangle (10.4,5.8);
  \node[text=rogris, font=\footnotesize] at (0.5,5.35) {$U$};
  \draw[robleu, line width=1pt, fill=robleuf, fill opacity=0.5] (3.9,3.3) ellipse (2.3 and 1.7);
  \draw[roteal, line width=1pt, fill=rotealf, fill opacity=0.5] (6.5,3.3) ellipse (2.3 and 1.7);
  \draw[rogold, line width=1pt, fill=rogoldf, fill opacity=0.5] (5.2,2.1) ellipse (2.3 and 1.7);
  \node[text=robleu, font=\bfseries] at (2.5,4.55) {$A$};
  \node[text=roteal, font=\bfseries] at (7.9,4.55) {$B$};
  \node[text=rogold, font=\bfseries] at (5.2,0.68) {$C$};
  \node[font=\scriptsize, text=rogris] at (3.3,4.1) {1};
  \node[font=\scriptsize, text=rogris] at (5.2,4.35) {2};
  \node[font=\scriptsize, text=rogris] at (7.1,4.1) {3};
  \node[font=\scriptsize, text=rogris] at (3.6,2.55) {4};
  \node[font=\scriptsize, text=rogris] at (6.8,2.55) {5};
  \node[font=\scriptsize, text=rogris] at (4.0,1.0) {6};
  \node[font=\bfseries, text=rogris] at (5.2,2.9) {7};
  \node[font=\scriptsize, text=rogris] at (1.2,0.9) {8};
\end{tikzpicture}
\captionof{figure}{Trois ensembles sécants : huit régions numérotées, dont le noyau $A \cap B \cap C$ (région 7)}
\label{ch1:fig:venn3}
\end{center}"""),
])

# ============================================================
# 4. CHAPITRE 2 : tirets + circuit corrige + silhouettes
# ============================================================
applique(D + '21_ch02.tex', [
    ("est vraie dès que l'une l'est — le « ou » de l'informatique est inclusif.",
     "est vraie dès que l'une l'est : le « ou » de l'informatique est inclusif."),
    ("dix lettres donnent 1024 lignes — c'est pourquoi les méthodes algébriques",
     "dix lettres donnent 1024 lignes : c'est pourquoi les méthodes algébriques"),
    ("dont la réciproque $Q \\rightarrow P$ — « s'il accède au réseau, c'est qu'il a payé » — n'est pas automatiquement vraie",
     "dont la réciproque $Q \\rightarrow P$ (« s'il accède au réseau, c'est qu'il a payé ») n'est pas automatiquement vraie"),
    ("trois produits de deux entrées seulement — un circuit plus petit pour la même fonction.",
     "trois produits de deux entrées seulement, soit un circuit plus petit pour la même fonction."),
    ("c'est une \\emph{tautologie} — c'est le principe du tiers exclu",
     "c'est une \\emph{tautologie} : c'est le principe du tiers exclu"),
    ("La vraie négation est $P \\land \\lnot Q$ — j'ai le baccalauréat \\emph{et} je ne suis pas inscrit —, tandis que",
     "La vraie négation est $P \\land \\lnot Q$ (j'ai le baccalauréat \\emph{et} je ne suis pas inscrit), tandis que"),
    ("les théorèmes du tableau~\\ref{ch2:tab:theoremes} — absorption, simplification, De Morgan — réduisent expressions et circuits.",
     "les théorèmes du tableau~\\ref{ch2:tab:theoremes} (absorption, simplification, De Morgan) réduisent expressions et circuits."),
    # --- figure 2.1 : circuit corrige (C manquait, B cablé deux fois) ---
    (r"""\begin{center}
\begin{tikzpicture}[line width=0.9pt, scale=1.0]
  % inverseur
  \node[left] at (-0.6,2.6) {$B$};
  \draw (-0.6,2.6) -- (0.3,2.6);
  \draw (0.3,2.35) -- (0.3,2.85) -- (0.75,2.85) -- (0.75,2.35) -- cycle;
  \draw (0.9,2.6) circle (0.15);
  \draw (1.05,2.6) -- (2.2,2.6);
  \node[font=\scriptsize, text=rogris] at (1.55,2.82) {$\overline{B}$};
  \draw (2.2,2.6) -- (2.2,2.15) -- (2.75,2.15);
  \draw (2.2,2.6) -- (2.2,3.05) -- (2.75,3.05);
  % porte ET du haut
  \draw (2.75,2.15) -- (2.75,3.05) arc[start angle=90, end angle=-90, radius=0.45] -- (2.75,2.15);
  \draw (3.2,2.6) -- (3.9,2.6);
  \node[font=\scriptsize, text=rogris] at (3.55,2.82) {$\overline{B} \cdot C$};
  % porte ET du bas : A.B
  \draw (2.75,0.35) -- (2.75,1.25) arc[start angle=90, end angle=-90, radius=0.45] -- (2.75,0.35);
  \node[left] at (-0.6,1.15) {$A$};
  \draw (-0.6,1.15) -- (3.0,1.15);
  \draw (-0.6,0.45) -- (2.75,0.45);
  \node[left] at (-0.6,0.45) {$B$};
  \draw (2.75,0.45) -- (2.75,0.8);
  \draw (3.2,0.8) -- (3.9,0.8);
  \node[font=\scriptsize, text=rogris] at (3.55,1.02) {$A \cdot B$};
  % porte OU finale
  \draw (3.9,0.8) -- (3.9,1.45) .. controls (4.35,1.35) and (4.35,0.9) .. (3.9,0.8);
  \draw (3.9,2.6) -- (3.9,1.95) .. controls (4.35,2.05) and (4.35,2.5) .. (3.9,2.6);
  \draw (3.9,1.95) .. controls (4.6,1.9) and (4.6,1.35) .. (3.9,1.45);
  \draw (4.62,1.7) -- (5.4,1.7);
  \node[right] at (5.45,1.7) {$F$};
\end{tikzpicture}
\captionof{figure}{Circuit réalisant $F = A \cdot B + \overline{B} \cdot C$ : deux ET, un OU et un inverseur}
\label{ch2:fig:circuit}
\end{center}""",
     r"""\begin{center}
\begin{tikzpicture}[line width=0.9pt]
  % --- entree B et inverseur ---
  \node[anchor=east] at (-0.7,3.2) {$B$};
  \draw (-0.65,3.2) -- (0.3,3.2);
  \draw (0.3,2.95) -- (0.3,3.45) -- (0.75,3.45) -- (0.75,2.95) -- cycle;
  \draw (0.9,3.2) circle (0.15);
  \draw (1.05,3.2) -- (2.75,3.2);
  \node[font=\scriptsize, text=rogris, anchor=south] at (1.9,3.26) {$\overline{B}$};
  % --- entree C ---
  \node[anchor=east] at (-0.7,2.6) {$C$};
  \draw (-0.65,2.6) -- (2.75,2.6);
  % --- porte ET du haut : NON B . C ---
  \draw (2.75,2.6) -- (2.75,3.2) -- (3.35,3.2)
        arc[start angle=90, end angle=-90, radius=0.3] -- (2.75,2.6);
  \draw (3.65,2.9) -- (4.45,2.9);
  \node[font=\scriptsize, text=rogris, anchor=south] at (4.22,2.98) {$\overline{B} \cdot C$};
  % --- entrees A et B ---
  \node[anchor=east] at (-0.7,1.3) {$A$};
  \draw (-0.65,1.3) -- (2.75,1.3);
  \node[anchor=east] at (-0.7,0.7) {$B$};
  \draw (-0.65,0.7) -- (2.75,0.7);
  % --- porte ET du bas : A . B ---
  \draw (2.75,0.7) -- (2.75,1.3) -- (3.35,1.3)
        arc[start angle=90, end angle=-90, radius=0.3] -- (2.75,0.7);
  \draw (3.65,1.0) -- (4.45,1.0);
  \node[font=\scriptsize, text=rogris, anchor=south] at (4.25,1.08) {$A \cdot B$};
  % --- porte OU finale ---
  \draw (4.45,2.9) .. controls (4.73,2.55) and (4.73,1.35) .. (4.45,1.0);
  \draw (4.45,2.9) .. controls (5.15,2.75) and (5.45,2.15) .. (5.5,1.95);
  \draw (4.45,1.0) .. controls (5.15,1.15) and (5.45,1.75) .. (5.5,1.95);
  \draw (5.5,1.95) -- (6.1,1.95);
  \node[anchor=west] at (6.15,1.95) {$F$};
\end{tikzpicture}
\captionof{figure}{Circuit réalisant $F = A \cdot B + \overline{B} \cdot C$ : un inverseur, deux ET et un OU}
\label{ch2:fig:circuit}
\end{center}"""),
    # --- figure 2.2 : six silhouettes redessinees ---
    (r"""\begin{center}
\begin{tikzpicture}[line width=0.8pt, scale=0.86, every node/.style={font=\scriptsize}]
  % AND
  \draw (0,0) -- (0.7,0) -- (0.7,1.0) arc[start angle=90, end angle=-90, radius=0.5] -- (0,0);
  \draw (1.2,0.5) -- (1.9,0.5); \node[above] at (1.5,0.6) {ET};
  \node[left] at (-0.05,0.7) {A}; \node[left] at (-0.05,0.3) {B};
  % OR
  \begin{scope}[xshift=3.0cm]
    \draw (0,0) -- (0,1.0); \draw (0,1.0) .. controls (0.75,0.9) and (0.75,0.1) .. (0,0);
    \draw (0.62,0.5) -- (1.4,0.5); \node[above] at (0.85,0.6) {OU};
  \end{scope}
  % NOT
  \begin{scope}[xshift=6.0cm]
    \draw (0,0.25) -- (0,0.75) -- (0.65,0.5) -- cycle; \draw (0.79,0.5) circle (0.14);
    \draw (0.93,0.5) -- (1.5,0.5); \node[above] at (0.55,0.75) {NON};
  \end{scope}
  % NAND
  \begin{scope}[xshift=9.0cm]
    \draw (0,0) -- (0.7,0) -- (0.7,1.0) arc[start angle=90, end angle=-90, radius=0.5] -- (0,0);
    \draw (1.2,0.5) circle (0.14); \draw (1.34,0.5) -- (1.8,0.5);
    \node[above] at (0.55,1.05) {NON-ET};
  \end{scope}
  % NOR
  \begin{scope}[xshift=12.0cm]
    \draw (0,0) -- (0,1.0); \draw (0,1.0) .. controls (0.75,0.9) and (0.75,0.1) .. (0,0);
    \draw (0.75,0.5) circle (0.14); \draw (0.89,0.5) -- (1.4,0.5);
    \node[above] at (0.5,1.05) {NON-OU};
  \end{scope}
  % XOR
  \begin{scope}[xshift=15.0cm]
    \draw (0.22,0) -- (0.22,1.0); \draw (0,0) -- (0,1.0);
    \draw (0,1.0) .. controls (0.75,0.9) and (0.75,0.1) .. (0,0);
    \draw (0.85,0.5) -- (1.6,0.5); \node[above] at (0.75,1.05) {OU EXCLUSIF};
  \end{scope}
\end{tikzpicture}
\captionof{figure}{Les six silhouettes de portes : le cercle en sortie marque l'inversion}
\label{ch2:fig:portes}
\end{center}""",
     r"""\begin{center}
\begin{tikzpicture}[line width=0.8pt, scale=0.86, every node/.style={font=\scriptsize}]
  % ET
  \begin{scope}
    \draw (0,0) -- (0.7,0) -- (0.7,1.0) arc[start angle=90, end angle=-90, radius=0.5] -- (0,0);
    \draw (-0.45,0.7) -- (0,0.7); \draw (-0.45,0.3) -- (0,0.3);
    \draw (1.2,0.5) -- (1.85,0.5);
    \node[anchor=south] at (0.6,1.18) {ET};
  \end{scope}
  % OU
  \begin{scope}[xshift=3.0cm]
    \draw (0,0) .. controls (0.28,0.32) and (0.28,0.68) .. (0,1.0);
    \draw (0,1.0) .. controls (0.62,0.95) and (0.95,0.78) .. (1.12,0.5);
    \draw (0,0) .. controls (0.62,0.05) and (0.95,0.22) .. (1.12,0.5);
    \draw (1.12,0.5) -- (1.85,0.5);
    \node[anchor=south] at (0.55,1.18) {OU};
  \end{scope}
  % NON
  \begin{scope}[xshift=6.0cm]
    \draw (0,0.25) -- (0,0.75) -- (0.65,0.5) -- cycle;
    \draw (0.79,0.5) circle (0.14);
    \draw (0.93,0.5) -- (1.85,0.5);
    \node[anchor=south] at (0.42,0.92) {NON};
  \end{scope}
  % NON-ET
  \begin{scope}[xshift=9.0cm]
    \draw (0,0) -- (0.7,0) -- (0.7,1.0) arc[start angle=90, end angle=-90, radius=0.5] -- (0,0);
    \draw (-0.45,0.7) -- (0,0.7); \draw (-0.45,0.3) -- (0,0.3);
    \draw (1.2,0.5) circle (0.14); \draw (1.34,0.5) -- (1.85,0.5);
    \node[anchor=south] at (0.6,1.18) {NON-ET};
  \end{scope}
  % NON-OU
  \begin{scope}[xshift=12.0cm]
    \draw (0,0) .. controls (0.28,0.32) and (0.28,0.68) .. (0,1.0);
    \draw (0,1.0) .. controls (0.62,0.95) and (0.95,0.78) .. (1.12,0.5);
    \draw (0,0) .. controls (0.62,0.05) and (0.95,0.22) .. (1.12,0.5);
    \draw (1.12,0.5) circle (0.14); \draw (1.26,0.5) -- (1.85,0.5);
    \node[anchor=south] at (0.55,1.18) {NON-OU};
  \end{scope}
  % OU EXCLUSIF
  \begin{scope}[xshift=15.0cm]
    \draw (0,0) .. controls (0.28,0.32) and (0.28,0.68) .. (0,1.0);
    \draw (0.22,0) .. controls (0.50,0.32) and (0.50,0.68) .. (0.22,1.0);
    \draw (0.22,1.0) .. controls (0.84,0.95) and (1.17,0.78) .. (1.34,0.5);
    \draw (0.22,0) .. controls (0.84,0.05) and (1.17,0.22) .. (1.34,0.5);
    \draw (1.34,0.5) -- (1.95,0.5);
    \node[anchor=south] at (0.78,1.18) {OU EXCLUSIF};
  \end{scope}
\end{tikzpicture}
\captionof{figure}{Les six silhouettes de portes : le cercle en sortie marque l'inversion}
\label{ch2:fig:portes}
\end{center}"""),
])

# ============================================================
# 5. CHAPITRE 3 : tirets
# ============================================================
applique(D + '22_ch03.tex', [
    ("que deux états stables — le courant passe ou ne passe pas —, auxquels on associe",
     "que deux états stables (le courant passe ou ne passe pas), auxquels on associe"),
    ("$1+1=10$ — j'écris 0 et je reporte 1.",
     "$1+1=10$ : j'écris 0 et je reporte 1."),
])

# ============================================================
# 6. CHAPITRE 4 : tirets
# ============================================================
applique(D + '23_ch04.tex', [
    ("tout ce qu'un programme manipule — compteurs, salaires, coordonnées d'un pixel — y prend",
     "tout ce qu'un programme manipule (compteurs, salaires, coordonnées d'un pixel) y prend"),
    ("Une solution plus intuitive existe — réserver un bit de signe et coder la valeur absolue sur les bits restants, dite \\emph{grandeur signée} — mais elle a deux défauts",
     "Une solution plus intuitive existe, dite \\emph{grandeur signée} (réserver un bit de signe et coder la valeur absolue sur les bits restants), mais elle a deux défauts"),
    ("Ne pas confondre le \\emph{complément à un} — la simple inversion des bits — et le \\emph{complément à deux}",
     "Ne pas confondre le \\emph{complément à un} (la simple inversion des bits) et le \\emph{complément à deux}"),
    ("Le nombre $0{,}1$ n'a pas d'écriture binaire finie — de même que $\\tfrac{1}{3}$ n'a pas d'écriture décimale finie — et la machine",
     "Le nombre $0{,}1$ n'a pas d'écriture binaire finie, de même que $\\tfrac{1}{3}$ n'a pas d'écriture décimale finie, et la machine"),
    ("on compare des flottants avec une tolérance — déclarer le résultat correct si $|x - 0{,}3| < 10^{-9}$ — et on ne code jamais",
     "on compare des flottants avec une tolérance (déclarer le résultat correct si $|x - 0{,}3| < 10^{-9}$), et on ne code jamais"),
    ("une moyenne, un prix, une coordonnée sont des réels — ou des entiers de plus petite unité (centimes, centièmes de point) ;",
     "une moyenne, un prix, une coordonnée sont des réels, ou des entiers de plus petite unité (centimes, centièmes de point) ;"),
    ("soit — mieux pour des notes réglementées — en entier de centièmes",
     "soit, mieux pour des notes réglementées, en entier de centièmes"),
    ("La mémoire d'affichage — le \\emph{framebuffer} — doit donc contenir",
     "La mémoire d'affichage, le \\emph{framebuffer}, doit donc contenir"),
])

# ============================================================
# 7. CHAPITRE 5 : tirets + figures 5.1 et 5.2
# ============================================================
applique(D + '24_ch05.tex', [
    ("fixe les deux unités de mesure — le degré et le radian — et leur conversion",
     "fixe les deux unités de mesure (le degré et le radian) et leur conversion"),
    ("Le triangle rectangle de côtés $3$, $4$ et $5$ — car $3^{2} + 4^{2} = 9 + 16 = 25 = 5^{2}$ — est le plus célèbre",
     "Le triangle rectangle de côtés $3$, $4$ et $5$ (car $3^{2} + 4^{2} = 9 + 16 = 25 = 5^{2}$) est le plus célèbre"),
    ("La même lecture du tableau~\\ref{ch5:tab:trigo} — adjacent, opposé, hypoténuse — résout",
     "La même lecture du tableau~\\ref{ch5:tab:trigo} (adjacent, opposé, hypoténuse) résout"),
    ("correspond à un arc de longueur $s = r \\times \\alpha$ — la longueur se lit directement",
     "correspond à un arc de longueur $s = r \\times \\alpha$ : la longueur se lit directement"),
    ("Ce calcul — différence de coordonnées, puis Pythagore — est celui",
     "Ce calcul (différence de coordonnées, puis Pythagore) est celui"),
    ("relient les côtés (tableau~\\ref{ch5:tab:trigo}) — la diagonale d'un écran 16:9",
     "relient les côtés (tableau~\\ref{ch5:tab:trigo}) : la diagonale d'un écran 16:9"),
    # --- figure 5.1 : cercle trigonometrique refait ---
    (r"""\begin{center}
\begin{tikzpicture}[scale=1.1]
  \draw[rogris!60, line width=0.6pt] (-1.6,-1.6) rectangle (1.9,1.9);
  \draw[->, rogris, line width=0.6pt] (-1.5,0) -- (1.8,0) node[right, font=\footnotesize] {$x$};
  \draw[->, rogris, line width=0.6pt] (0,-1.5) -- (0,1.8) node[above, font=\footnotesize] {$y$};
  \draw[robleu, line width=1pt] (1,0) arc[start angle=0, end angle=120, radius=1];
  \fill[roor] (1,0) circle (0.05) node[below right, font=\footnotesize] {$1$};
  \fill[roor] (0,1) circle (0.05) node[above right, font=\footnotesize] {$\pi/2$};
  \fill[roor] (-0.5,0.866) circle (0.05) node[above left, font=\footnotesize] {$2\pi/3$};
  \node[font=\footnotesize, text=rogris] at (0.5,-0.25) {$\dfrac{\pi}{6}$};
  \node[font=\footnotesize, text=rogris] at (-0.28,0.28) {$\dfrac{\pi}{4}$};
  \node[font=\footnotesize, text=rogris] at (-0.62,-0.24) {$\pi$};
  \draw[robleu, line width=0.9pt] (0,0) -- (0.866,-0.5);
  \node[font=\footnotesize, text=robleu] at (1.05,-0.55) {$\dfrac{5\pi}{3}$};
  \node[font=\footnotesize, text=rogris, align=center] at (0.95,1.55) {tour complet $= 2\pi$ rad $= 360°$};
\end{tikzpicture}
\captionof{figure}{Le cercle trigonométrique : un tour vaut $2\pi$ radians}
\label{ch5:fig:cercle}
\end{center}""",
     r"""\begin{center}
\begin{tikzpicture}[scale=1.3]
  \draw[->, rogris, line width=0.6pt] (-1.7,0) -- (1.9,0)
        node[anchor=north east, font=\footnotesize] {$x$};
  \draw[->, rogris, line width=0.6pt] (0,-1.7) -- (0,1.9)
        node[anchor=north east, font=\footnotesize] {$y$};
  \draw[robleu, line width=1.1pt] (1,0) arc[start angle=0, end angle=360, radius=1];
  % points remarquables sur les axes
  \fill[roor] (1,0) circle (0.045);
  \node[font=\footnotesize, text=rogris, anchor=north west] at (1.04,-0.08) {$0$};
  \fill[roor] (0,1) circle (0.045);
  \node[font=\footnotesize, text=rogris, anchor=south east] at (-0.04,1.08) {$\dfrac{\pi}{2}$};
  \fill[roor] (-1,0) circle (0.045);
  \node[font=\footnotesize, text=rogris, anchor=south east] at (-1.08,0.12) {$\pi$};
  \fill[roor] (0,-1) circle (0.045);
  \node[font=\footnotesize, text=rogris, anchor=north west] at (-0.04,-1.1) {$\dfrac{3\pi}{2}$};
  % angle remarquable pi/3 avec son rayon
  \draw[rogold, line width=1pt] (0,0) -- (0.5,0.866);
  \fill[rogold] (0.5,0.866) circle (0.045);
  \node[font=\footnotesize, text=rogold, anchor=south west] at (0.55,0.92) {$\dfrac{\pi}{3}$};
  \draw[rogold, line width=0.7pt] (0.42,0) arc[start angle=0, end angle=60, radius=0.42];
  % legende sous la figure
  \node[font=\footnotesize, text=rogris, align=center] at (0.1,-2.2)
    {un tour complet vaut $2\pi$ rad $= 360°$};
\end{tikzpicture}
\captionof{figure}{Le cercle trigonométrique de rayon 1 : les angles remarquables se lisent en radians}
\label{ch5:fig:cercle}
\end{center}"""),
    # --- figure 5.2 : vecteur refait ---
    (r"""\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[rogris!60, line width=0.6pt] (-0.7,-0.7) rectangle (4.4,4.4);
  \draw[->, rogris, line width=0.6pt] (-0.6,0) -- (4.2,0) node[right, font=\footnotesize] {$x$};
  \draw[->, rogris, line width=0.6pt] (0,-0.6) -- (0,4.2) node[above, font=\footnotesize] {$y$};
  \draw[->, robleu, line width=1.1pt] (0,0) -- (3,4) node[right, font=\footnotesize, text=robleu] {$\vec{u}$};
  \draw[roteal, line width=0.6pt, dashed] (3,0) -- (3,4);
  \draw[roteal, line width=0.6pt, dashed] (0,4) -- (3,4);
  \node[font=\footnotesize, text=rogris] at (1.5,-0.3) {$x = 3$};
  \node[font=\footnotesize, text=rogris] at (-0.45,2) {$y = 4$};
  \node[font=\footnotesize, text=robleu] at (1.9,2.5) {$\|\vec{u}\| = 5$};
\end{tikzpicture}
\captionof{figure}{Le vecteur $\vec{u} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ : ses coordonnées et sa norme}
\label{ch5:fig:vecteur}
\end{center}""",
     r"""\begin{center}
\begin{tikzpicture}[scale=0.95]
  \draw[->, rogris, line width=0.6pt] (-0.9,0) -- (4.4,0)
        node[anchor=north east, font=\footnotesize] {$x$};
  \draw[->, rogris, line width=0.6pt] (0,-0.9) -- (0,4.8)
        node[anchor=north east, font=\footnotesize] {$y$};
  % graduations
  \draw[rogris, line width=0.5pt] (3,0.08) -- (3,-0.08);
  \draw[rogris, line width=0.5pt] (0.08,4) -- (-0.08,4);
  % lignes de rappel pointillees
  \draw[roteal, line width=0.6pt, dashed] (3,0) -- (3,4) -- (0,4);
  % le vecteur
  \draw[->, robleu, line width=1.2pt] (0,0) -- (3,4);
  \node[text=robleu, font=\footnotesize\bfseries, anchor=west] at (3.14,4.1) {$\vec{u}$};
  % coordonnees
  \node[font=\footnotesize, text=rogris, anchor=north] at (3,-0.16) {$3$};
  \node[font=\footnotesize, text=rogris, anchor=east] at (-0.14,4) {$4$};
  \node[font=\scriptsize, text=roteal, anchor=west] at (3.25,1.9) {$\Delta x = 3$};
  \node[font=\scriptsize, text=roteal, anchor=south] at (1.5,4.1) {$\Delta y = 4$};
  % norme, a l'ecart du trace
  \node[font=\footnotesize, text=robleu, anchor=east] at (1.3,2.5) {$\|\vec{u}\| = 5$};
\end{tikzpicture}
\captionof{figure}{Le vecteur $\vec{u} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ : ses coordonnées et sa norme}
\label{ch5:fig:vecteur}
\end{center}"""),
])

# ============================================================
# 8. CHAPITRE 6 : tirets + figure 6.1
# ============================================================
applique(D + '25_ch06.tex', [
    ("en tant qu'objets de calcul — dimensions, somme, produit — puis les applique",
     "en tant qu'objets de calcul (dimensions, somme, produit), puis les applique"),
    ("des équations — segments, cercles, courbes de Bézier, aires remplies — dont le logiciel",
     "des équations (segments, cercles, courbes de Bézier, aires remplies) dont le logiciel"),
    ("Les traitements d'image — luminosité, contraste, filtre de netteté — réécrivent",
     "Les traitements d'image (luminosité, contraste, filtre de netteté) réécrivent"),
    ("La synthèse additive des écrans — ajouter de la lumière, du noir vers le blanc — s'oppose",
     "La synthèse additive des écrans, qui ajoute de la lumière du noir vers le blanc, s'oppose"),
    ("Les formats compressés — JPEG pour les photos, PNG pour les graphiques — réduisent",
     "Les formats compressés (JPEG pour les photos, PNG pour les graphiques) réduisent"),
    ("SVG & dessins vectoriels & sans objet (équations) & ---\\\\",
     "SVG & dessins vectoriels & sans objet (équations) & non applicable\\\\"),
    ("$\\dfrac{8\\,700\\,000}{8} \\approx 1{,}1$ Mo — la raison pour laquelle",
     "$\\dfrac{8\\,700\\,000}{8} \\approx 1{,}1$ Mo : la raison pour laquelle"),
    ("Ajouter un quatrième canal — l'opacité, notée alpha, dans le codage RGBA — porterait",
     "Ajouter un quatrième canal (l'opacité, notée alpha, dans le codage RGBA) porterait"),
    ("C'est cette arithmétique — bits, octets, débit — qui explique",
     "C'est cette arithmétique (bits, octets, débit) qui explique"),
    ("applique les transformations de base — échelle $\\begin{pmatrix} k & 0 \\\\ 0 & k \\end{pmatrix}$, rotation $\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}$ — aux pixels d'une image",
     "applique les transformations de base (échelle $\\begin{pmatrix} k & 0 \\\\ 0 & k \\end{pmatrix}$, rotation $\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}$) aux pixels d'une image"),
    # --- figure 6.1 : pixels decalles sous le titre du panneau ---
    (r"""  \draw[robleu!70, fill=robleuf] (0.8,0.6) rectangle (1.6,1.4);
  \draw[robleu!70, fill=robleuf] (1.6,0.6) rectangle (2.4,1.4);
  \draw[robleu!70, fill=robleuf] (0.8,1.4) rectangle (1.6,2.2);
  \draw[robleu, fill=robleuf] (1.6,1.4) rectangle (2.4,2.2);
  \draw[robleu!70, fill=robleuf] (1.6,2.2) rectangle (2.4,3.0);
  \draw[robleu!70, fill=robleuf] (2.4,1.4) rectangle (3.2,2.2);
  \draw[robleu, fill=robleuf] (2.4,2.2) rectangle (3.2,3.0);
  \draw[robleu!70, fill=robleuf] (2.4,3.0) rectangle (3.2,3.8);
  \draw[robleu, fill=robleuf] (3.2,2.2) rectangle (4.0,3.0);
  \node[font=\scriptsize, text=rogris, align=center] at (2.6,0.28) {les carrés deviennent visibles};""",
     r"""  \draw[robleu!70, fill=robleuf] (1.2,0.5) rectangle (1.9,1.2);
  \draw[robleu!70, fill=robleuf] (1.9,0.5) rectangle (2.6,1.2);
  \draw[robleu!70, fill=robleuf] (1.2,1.2) rectangle (1.9,1.9);
  \draw[robleu, fill=robleuf] (1.9,1.2) rectangle (2.6,1.9);
  \draw[robleu!70, fill=robleuf] (1.9,1.9) rectangle (2.6,2.6);
  \draw[robleu!70, fill=robleuf] (2.6,1.2) rectangle (3.3,1.9);
  \draw[robleu, fill=robleuf] (2.6,1.9) rectangle (3.3,2.6);
  \draw[robleu!70, fill=robleuf] (2.6,2.6) rectangle (3.3,3.3);
  \draw[robleu, fill=robleuf] (3.3,1.9) rectangle (4.0,2.6);
  \node[font=\scriptsize, text=rogris, align=center] at (2.6,0.22) {les carrés deviennent visibles};"""),
])

print('\nToutes les corrections appliquées.')
