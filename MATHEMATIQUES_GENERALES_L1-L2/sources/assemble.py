# -*- coding: utf-8 -*-
"""Assemblage des documents Mathematiques Generales (cours + TD + corriges).
Usage : python3 assemble.py [nom_de_document]   (sans argument : tous)
Source : mg_l1/parts/00_preamble.tex + mg_l1/docs/<doc>/*.tex tries.
Sortie : mg_l1/build/<doc>.tex
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = ['cours_mg', 'td_mg', 'corriges_mg']

def groupes_insecables(text):
    """Empeche la coupure entre un contenu centre et sa legende (captionof) :
    tout bloc center contenant une captionof est emballe dans une minipage."""
    def wrap(m):
        body = m.group(1)
        if '\\captionof' in body:
            return ('\\begin{center}\n\\begin{minipage}{\\textwidth}\n'
                    + body + '\\end{minipage}\n\\end{center}')
        return m.group(0)
    return re.sub(r'\\begin\{center\}\n(.*?)\\end\{center\}', wrap, text, flags=re.S)

def convert_floating_figs(text):
    out = []
    depth_boxes = 0
    lines = text.split('\n')
    i = 0
    box_starts = ('\\begin{exemple}', '\\begin{definition}', '\\begin{propriete}',
                  '\\begin{theoreme}', '\\begin{formule}', '\\begin{methode}',
                  '\\begin{remarque}', '\\begin{attention}', '\\begin{exercice}',
                  '\\begin{corrige}')
    box_ends = ('\\end{exemple}', '\\end{definition}', '\\end{propriete}',
                '\\end{theoreme}', '\\end{formule}', '\\end{methode}',
                '\\end{remarque}', '\\end{attention}', '\\end{exercice}',
                '\\end{corrige}')
    while i < len(lines):
        ln = lines[i]
        stripped = ln.strip()
        if any(stripped.startswith(b) for b in box_starts):
            depth_boxes += 1
        elif any(stripped.startswith(b) for b in box_ends):
            depth_boxes = max(0, depth_boxes - 1)
        if depth_boxes > 0 and stripped.startswith('\\begin{figure}'):
            j = i
            while j < len(lines) and not lines[j].strip().startswith('\\end{figure}'):
                j += 1
            block = '\n'.join(lines[i:j+1])
            block = block.replace('\\begin{figure}[h]', '\\begin{center}', 1)
            block = block.replace('\\begin{figure}', '\\begin{center}', 1)
            block = block.replace('\\centering', '', 1)
            block = block.replace('\\end{figure}', '\\end{center}', 1)
            block = re.sub(r'\\caption\{', r'\\captionof{figure}{', block, count=1)
            out.append(block)
            i = j + 1
            continue
        out.append(ln)
        i = i + 1
    return '\n'.join(out)

def assemble(doc):
    docdir = os.path.join(BASE, 'docs', doc)
    preambule = os.path.join(BASE, 'parts', '00_preamble.tex')
    files = [preambule]
    for name in sorted(os.listdir(docdir)):
        if name.endswith('.tex'):
            files.append(os.path.join(docdir, name))
    parts = []
    for p in files:
        s = open(p, encoding='utf-8').read()
        if os.path.basename(p) != os.path.basename(preambule):
            s = convert_floating_figs(s)
            s = groupes_insecables(s)
        parts.append(s)
    outpath = os.path.join(BASE, 'build', doc + '.tex')
    open(outpath, 'w', encoding='utf-8').write('\n'.join(parts))
    print('assemble ->', outpath, '(%d lignes)' % outpath.count('\n'))

if __name__ == '__main__':
    targets = [sys.argv[1]] if len(sys.argv) > 1 else DOCS
    for d in targets:
        assemble(d)
