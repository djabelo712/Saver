# -*- coding: utf-8 -*-
"""Verification numerique exhaustive du module Mathematiques Generales (CPTEC).
Cours (chapitres 1 a 6, incl. fonctions numeriques), TD et Corriges : chaque
valeur numerique du texte est recalculee et comparee a la valeur attendue.
0 ecart tolere."""
import math, sys

ok, ko = 0, 0
def chk(name, actual, expected, tol=0.01):
    global ok, ko
    if abs(actual - expected) <= tol:
        ok += 1
    else:
        ko += 1
        print("ECART %s : calcule %s vs attendu %s" % (name, actual, expected))

def near(a, b, tol=0.01):
    return abs(a - b) <= tol

# ============ CHAPITRE 2 (equations : cours + TD + corriges) ============
# 3.1 : 4(x+5)=3x-2 -> -22 ; produit (2x+1)(x-3) ; TD : 5(x-2)=3x+4 -> 7
chk("4(x+5)=3x-2", (-2-20)/(4-3), -22)
chk("5(x-2)=3x+4", (4+10)/(5-3), 7)
chk("(3x-2)(x+5)", 2/3, 2/3)
# 3.2 : -3x^2-x+4 (D=49, racines -4/3, 1) ; 25x^2-90x+81 (D=0, 1.8) ; 4x^2+3x+9 (D=-135)
D = (-1)**2 - 4*(-3)*4
chk("D(-3x2-x+4)", D, 49)
chk("x1", (1+math.sqrt(D))/(-6), -4/3)
chk("x2", (1-math.sqrt(D))/(-6), 1)
chk("D(25x2-90x+81)", 90**2-4*25*81, 0)
chk("x0", 90/50, 1.8)
chk("D(4x2+3x+9)", 9-144, -135)
# TD 3.2 : 2x2-5x-3 (49, 3, -1/2) ; 4x2-12x+9 (0, 3/2) ; x2+x+1 (-3)
chk("D(2x2-5x-3)", 25+24, 49)
chk("x(2x2-5x-3)+", (5+7)/4, 3)
chk("x(2x2-5x-3)-", (5-7)/4, -0.5)
chk("D(4x2-12x+9)", 144-144, 0)
chk("x0(4x2-12x+9)", 12/8, 1.5)
chk("D(x2+x+1)", 1-4, -3)
# 3.3 : -3x2+2x+1 (S=2/3, P=-1/3, racines -1/3, 1) ; X2-6X+8 (2,4) ; TD 5x2-6x+1 ; X2-2X-8 ; 2x2-7x+3
chk("S(-3x2+2x+1)", -2/-3, 2/3)
chk("P(-3x2+2x+1)", 1/-3, -1/3)
chk("racines", -2/6+0.0+(-2/6-4/6), -1/3-1)  # -1/3 et 1 : somme -1/3
chk("DX2-6X+8", 36-32, 4)
chk("rac(X2-6X+8)", (6+2)/2, 4)
chk("S(5x2-6x+1)", 6/5, 1.2)
chk("P(5x2-6x+1)", 1/5, 0.2)
chk("D(5x2-6x+1)", 36-20, 16)
chk("rac(5x2-6x+1)-", (6-4)/10, 0.2)
chk("D(X2-2X-8)", 4+32, 36)
chk("rac(X2-2X-8)", (2+6)/2, 4)
chk("P(2x2-7x+3)", 3/2, 1.5)
chk("autre rac", (3/2)/(1/2), 3)
chk("S(2x2-7x+3)", 7/2, 3.5)
# 3.4 : x4-3x2+2 (X=1,2 -> +-1, +-sqrt2) ; x4+3x2+4 (D=-7) ; TD x4-5x2+4 ; x4+x2-2
chk("D(X2-3X+2)", 9-8, 1)
chk("X1", (3+1)/2, 2)
chk("D(X2+3X+4)", 9-16, -7)
chk("D(X2-5X+4)", 25-16, 9)
chk("X(x4-5x2+4)", (5+3)/2, 4)
chk("D(X2+X-2)", 1+8, 9)
# 3.5 : -2x+6>=0 -> x<=3 ; 5x+4>0 -> -4/5 ; TD 3x-7<=0 -> 7/3 ; -4x+10>0 -> 5/2
chk("-2x+6>=0", 6/2, 3)
chk("5x+4>0", -4/5, -0.8)
chk("3x-7<=0", 7/3, 2.333333, 0.001)
chk("-4x+10>0", 10/4, 2.5)
# 3.6 : 2x2+3x-5>=0 (49, -5/2, 1) ; -x2+3x-2<0 (1, 1, 2) ; TD x2-4x-5<=0 (36, -1, 5) ; -2x2+8x-6>0
chk("D(2x2+3x-5)", 9+40, 49)
chk("rac1", (-3-7)/4, -2.5)
chk("rac2", (-3+7)/4, 1)
chk("D(-x2+3x-2)", 9-8, 1)
chk("TD rac x2-4x-5", (4-6)/2, -1)
chk("TD rac+", (4+6)/2, 5)
chk("D(x2-4x+3)", 16-12, 4)
chk("rac(x2-4x+3)", (4-2)/2, 1)

# ============ CHAPITRE 3 (fonctions numeriques : cours + TD + corriges) ============
# 3.1 : tableau de valeurs de x^2-2x-3 ; domaines de l'exemple
chk("3.1 f(-1)=0", (-1)**2 - 2*(-1) - 3, 0)
chk("3.1 f(1)=-4", 1 - 2 - 3, -4)
chk("3.1 f(4)=5", 16 - 8 - 3, 5)
chk("3.1 D_f interdits", (3)*(-3), -9)  # x^2-9 s'annule en -3 et 3
chk("3.1 D_g frontiere", 3 - 3, 0)      # 3-x >= 0 -> x <= 3
# 3.2 : cout Kara C(q)=1500q+350000
chk("3.2 m", (800000-500000)/(300-100), 1500)
chk("3.2 p", 500000 - 100*1500, 350000)
chk("3.2 C(400)=950000", 1500*400 + 350000, 950000)
chk("3.2 CM(100)", (1500*100+350000)/100, 5000)
chk("3.2 CM(400)", (1500*400+350000)/400, 2375)
# 3.3 : limites de l'exemple (4 calculs)
chk("3.3 lim(2x+1) en 3", 2*3+1, 7)
chk("3.3 h(1.999)=3.999", (1.999**2-4)/(1.999-2), 3.999)
chk("3.3 h(2.001)=4.001", (2.001**2-4)/(2.001-2), 4.001)
chk("3.3 lim quotient deg2", (3*10**8 - 5*10**4 + 1)/(2*10**8 + 10**4), 1.5, 0.01)
# 3.4 : derivees de l'exemple + tangente x^2 en 3
chk("3.4 f'(3)=12*(3*3-5)^3", 4*3*(3*3-5)**3, 768)
chk("3.4 taux x^2 en 3 h=0.1", ((3.1**2) - 9)/0.1, 6.1)
chk("3.4 tangente y(4)=15", 6*4-9, 15)
# 3.5 : etude de x^3-3x+1
chk("3.5 f(-1)=3", (-1)**3 - 3*(-1) + 1, 3)
chk("3.5 f(1)=-1", 1 - 3 + 1, -1)
# 3.6 : profit anacarde
chk("3.6 pi(100)=180000", 10000*100 - 50*100**2 - 320000, 180000)
chk("3.6 R'(100)=8000", 12000 - 40*100, 8000)
chk("3.6 C'(100)=8000", 2000 + 60*100, 8000)
chk("3.6 p(100)=10000", 12000 - 20*100, 10000)
chk("3.6 CM(100)=8200", (320000 + 2000*100 + 30*100**2)/100, 8200)
chk("3.6 points morts q=40", 10000*40 - 50*40**2 - 320000, 0)
chk("3.6 points morts q=160", 10000*160 - 50*160**2 - 320000, 0)
# TD 3.1 : domaines (interdits +2/-2 ; frontiere 2.5)
chk("TD3 ex1 f interdits", 2*(-2), -4)
chk("TD3 ex1 g frontiere", 5 - 2*2.5, 0)
# TD 3.3 : prime P(x)=100x+4000
chk("TD3 ex3 p", 4000, 4000)
chk("TD3 ex3 m", (9000-4000)/50, 100)
chk("TD3 ex3 P(80)", 100*80+4000, 12000)
chk("TD3 ex3 P(x)=10000", (10000-4000)/100, 60)
# TD 3.4 : exp/ln
chk("TD3 ex4 ln12", math.log(12), 2.4849, 0.0001)
chk("TD3 ex4 e^3", math.exp(3), 20.0855, 0.0001)
chk("TD3 ex4 e^(2ln3)=9", math.exp(2*math.log(3)), 9, 0.001)
chk("TD3 ex4 ln16", math.log(8)+math.log(2), 2.7726, 0.0001)
# TD 3.5 : limites (10 ; 5 ; 4 ; 0.25)
chk("TD3 ex5 lim1", (4.9999**2-25)/(4.9999-5), 10, 0.001)
chk("TD3 ex5 lim2", (5*10**8+3*10**4)/(10**8-1), 5, 0.001)
chk("TD3 ex5 lim3", (1.0001**2+2*1.0001-3)/(1.0001-1), 4, 0.001)
chk("TD3 ex5 lim4", (math.sqrt(0.0001+4)-2)/0.0001, 0.25, 0.0001)
# TD 3.6 : derivees (controle par taux h=0.001 en x=1) + tangente -2x+2
chk("TD3 ex6 u'(1)~3e", ((1.001**2)*math.exp(1.001) - math.exp(1))/0.001, 3*math.exp(1), 0.01)
chk("TD3 ex6 v'(1)=7/9", (3*1.001-1)/(1.001+2)**2 - (3-1)/(3**2), 7/9 - 7/9, 0.01)
chk("TD3 ex6 tangente y(2)", -2*2+2, -2)
# TD 3.7 : g=x^3-6x^2+9x+1
g = lambda x: x**3 - 6*x**2 + 9*x + 1
chk("TD3 ex7 g(1)=5", g(1), 5)
chk("TD3 ex7 g(3)=1", g(3), 1)
chk("TD3 ex7 g(4)=5", g(4), 5)
chk("TD3 ex7 factorisation", (2-1)**2*(2-4), -2)  # (x-1)^2(x-4) en x=2
# TD 3.8 : profit atelier couture
chk("TD3 ex8 pi(100)=70000", 1600*100 - 8*100**2 - 10000, 70000)
chk("TD3 ex8 R'(100)=1400", 1800 - 4*100, 1400)
chk("TD3 ex8 C'(100)=1400", 200 + 12*100, 1400)
chk("TD3 ex8 p(100)=1600", 1800 - 2*100, 1600)
chk("TD3 ex8 CM(100)=900", (10000 + 200*100 + 6*100**2)/100, 900)
chk("TD3 ex8 marge 700", 1600 - 900, 700)

# ============ CHAPITRE 4 (systemes et PL : cours + TD + corriges) ============
# systeme commun {2x+y=8 ; x-2y=-1} -> (3,2) ; D=-5, Dx=-15, Dy=-10
chk("D cours", 2*(-2)-1*1, -5)
chk("Dx cours", 8*(-2)-(-1)*1, -15)
chk("Dy cours", 2*(-1)-8*1, -10)
chk("x cours", -15/-5, 3)
chk("y cours", -10/-5, 2)
# Gauss cours {x-2y+5z=10 ; 2x-3y+8z=16 ; -3x+y-2z=-1} -> (-1,2,3)
L2 = [2-2*1, -3-2*(-2), 8-2*5, 16-2*10]
chk("L2'", L2[1], 1); chk("L2'z", L2[2], -2); chk("L2'c", L2[3], -4)
L3 = [-3+3*1, 1+3*(-2), -2+3*5, -1+3*10]
chk("L3'y", L3[1], -5); chk("L3'z", L3[2], 13); chk("L3'c", L3[3], 29)
chk("z", 9/3, 3)
chk("y", -4+2*3, 2)
chk("x", 10+2*2-5*3, -1)
# TD 4.1 {3x+2y=13 ; x-y=1} -> (3,2)
chk("TD41 y", (13-3)/5, 2)
chk("TD41 x", 2+1, 3)
# TD 4.2 {2x+3y=12 ; 4x-y=10} D=-14, Dx=-42, Dy=-28 -> (3,2) ; S1/S2
chk("TD42 D", 2*(-1)-3*4, -14)
chk("TD42 Dx", 12*(-1)-3*10, -42)
chk("TD42 Dy", 2*10-12*4, -28)
chk("TD42 x", -42/-14, 3)
chk("TD42 y", -28/-14, 2)
chk("S1 D", 2*3-1*6, 0)
chk("S1 Dx", 5*3-1*15, 0)
chk("S2 Dx", 5*3-1*8, 7)
# TD 4.3 {x+y+z=6 ; 2x-y+z=3 ; x+2y-z=2} -> (1,2,3)
chk("TD43 -3y-z", -3*2-3, -9)  # L2-2L1 : -3y-z=-9
chk("TD43 z", 21/7, 3)
chk("TD43 y", -4+2*3, 2)
chk("TD43 x", 6-2-3, 1)
# TD 4.4 domaine : sommets (0,0),(2,0),(10/3,8/3),(0,6)
chk("TD44 inter x", 10/3, 3.333333, 0.001)
chk("TD44 inter y", 2*(10/3)-4, 8/3)
chk("TD44 (2,0) contrainte1", 2+0, 2)
# TD 4.5 menuiserie : (18,8), Z=77000 ; sommets Z : 0, 75000, 77000, 68000
chk("TD45 E y", (34-18)/2, 8)  # x+2y=34 avec x=18 -> y=8 ; 2x+3y=60 -> y=8
chk("TD45 E", 2*18+3*8, 60)
chk("TD45 E2", 18+2*8, 34)
chk("Z(18,8)", 2500*18+4000*8, 77000)
chk("Z(30,0)", 2500*30, 75000)
chk("Z(0,17)", 4000*17, 68000)
chk("planches", 2*18+3*8, 60)
chk("heures", 18+2*8, 34)

# ============ CHAPITRE 5 (angles et trigo : cours + TD + corriges) ============
chk("135deg", 135/180, 0.75)  # = 3pi/4
chk("11pi/12", 11*180/12, 165)
chk("140deg", 140/20, 7)  # 7pi/9
chk("arc cours", 5*1.2, 6)
chk("h cours", 18*math.tan(math.radians(32)), 11.25, 0.05)
chk("cos120", math.cos(math.radians(120)), -0.5, 0.001)
chk("sin120", math.sin(math.radians(120)), math.sqrt(3)/2, 0.001)
chk("cos75", (math.sqrt(6)-math.sqrt(2))/4, math.cos(math.radians(75)), 0.001)
chk("sin60 dup", 2*math.sin(math.radians(30))*math.cos(math.radians(30)), math.sqrt(3)/2, 0.001)
chk("TD 210deg", 210/30, 7)  # 7pi/6
chk("TD 240deg", 240/30, 8)  # 4pi/3
chk("TD 300deg", 300/30, 10)  # 5pi/3
chk("TD 5pi/4", 5*180/4, 225)
chk("TD arc", 8*math.pi/4, 2*math.pi)
chk("TD echelle", math.sqrt(100-16), math.sqrt(84), 0.001)
chk("TD tour", 40*math.tan(math.radians(25)), 40*0.4663, 0.02)
chk("TD cos(-pi/3)", math.cos(math.radians(-60)), 0.5, 0.001)
chk("TD sin(-pi/3)", math.sin(math.radians(-60)), -math.sqrt(3)/2, 0.001)
chk("TD sin(7pi/3)", math.sin(math.radians(420-360)), math.sqrt(3)/2, 0.001)
chk("TD cosx=sqrt2/2", math.cos(math.radians(45)), math.sqrt(2)/2, 0.001)

# ============ CHAPITRE 6 (suites : cours + TD + corriges) ============
chk("u diff", 2*(1+0)-5 - (2*0-5), 2)
chk("v diff n=1", (1+1)**2 - 1**2, 3)  # 2n+3 avec n=0 -> 3
chk("cours V4 simple", 150000*(1+0.07*4), 192000)
chk("cours V10 simple", 150000*(1+0.07*10), 255000)
chk("1.07^4", 1.07**4, 1.3108, 0.0001)
chk("cours V4 compose", 150000*1.07**4, 196619, 1)
chk("1.07^10", 1.07**10, 1.9672, 0.0001)
chk("cours V10 compose", 150000*1.07**10, 295073, 1)
chk("TD interet annuel", 250000*0.06, 15000)
chk("TD V5 simple", 250000*(1+0.06*5), 325000)
chk("TD V10 simple", 250000*(1+0.06*10), 400000)
chk("1.06^5", 1.06**5, 1.338226, 0.0001)
chk("TD V5 compose", 250000*1.06**5, 334556, 1)
chk("1.06^10", 1.06**10, 1.790848, 0.0001)
chk("TD V10 compose", 250000*1.06**10, 447712, 1)
chk("TD ecart 5 ans", 334556-325000, 9556, 1)
chk("TD ecart 10 ans", 447712-400000, 47712, 1)
chk("TD annuite", 4000000/8, 500000)
chk("TD V5 amorti", 4000000-5*500000, 1500000)
chk("TD n>=6", 3000000/500000, 6)
chk("TD V6", 4000000-6*500000, 1000000)

# ============ CHAPITRE 1 (ensembles : TD + corriges) ============
chk("TD1 ex1 |A|", 12-3+1, 10)
chk("TD1 ex1 |B|", 7, 7)
chk("TD1 ex1 |AxB|", 10*7, 70)
chk("TD1 ex3 au moins un", 45+38-17, 66)
chk("TD1 ex3 aucun", 84-66, 18)
chk("TD1 ex3 zones", (45-17)+(38-17)+17, 66)
chk("TD1 ex4 noyau", 5, 5)
chk("TD1 ex4 F seul", 31-6-4-5, 16)
chk("TD1 ex4 K seul", 24-6-3-5, 10)
chk("TD1 ex4 H seul", 19-4-3-5, 7)
chk("TD1 ex4 union", 16+10+7+6+4+3+5, 51)
chk("TD1 ex4 aucun", 60-51, 9)
chk("TD1 ex4 somme 8 regions", 16+10+7+6+4+3+5+9, 60)

print("\n%s controles passes, %d ecart(s)" % (ok, ko))
sys.exit(1 if ko else 0)
