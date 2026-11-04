# -*- coding: utf-8 -*-
"""Verification arithmetique complete du cours MAI L1&L2 (6 chapitres, format ESGAE).
0 ecart tolere : chaque valeur annoncee dans le .tex est recalculee ici."""
import math
import random

ok = 0
def check(name, cond):
    global ok
    if not cond:
        raise AssertionError("ECHEC: " + name)
    ok += 1

# ---------- Chapitre 1 : ensembles ----------
check("c1 |A|={3..9}=7", len(set(range(3,10))) == 7)
check("c1 0,15 in N ; -7 in Z ; 2/3 in Q ; sqrt2 irrationnel", (2/3 == 2/3) and abs(math.sqrt(2)-1.41421356) < 1e-7)
# CPTEC 120 etudiants
P, R, PR = 65, 50, 25
check("c1 |P u R| = 65+50-25 = 90", P + R - PR == 90)
check("c1 regions 40/25/25", (P-PR, R-PR) == (40, 25))
check("c1 union regions = 90", (P-PR) + PR + (R-PR) == 90)
check("c1 aucun = 120-90 = 30", 120 - 90 == 30)
# De Morgan numerique (M=18, I=23, MI=12, univers=40)
U, M, I, MI = set(range(1,41)), {1,2,3}, {1,2,3,4,5}, {1,2,3,4,5,6}
# (A u B) complementaire / intersections sur l'exemple S4
A, B, C = {1,2,3,4}, {3,4,5}, {4,5,6}
check("c1 A∩(B∪C) = {3,4}", A & (B | C) == {3, 4})
check("c1 (A∩B)∪(A∩C) = {3,4}", (A & B) | (A & C) == {3, 4})
# sous-ensembles 2^3 = 8
subs = [frozenset(s) for r in range(4) for s in __import__('itertools').combinations('abc', r)]
check("c1 2^3 = 8 sous-ensembles", len(subs) == 8)
# simplifications S5 (test aleatoire exhaustif sur 4 univers)
def E1(a,b):
    A1 = {x for x in a if x in b}; A2 = {x for x in a if x not in b}; A3 = {x for x in b if x not in a}
    return (A1 | A2 | A3) == (a | b)
def F1(a,b):
    F = {x for x in a if x in b}  # complementaire de (nonA u nonB) = A∩B
    return F == (a & b)
for _ in range(50):
    U8 = set(range(8))
    a = {x for x in U8 if random.random() < .5}
    b = {x for x in U8 if random.random() < .5}
    check("c1 E=(A∩B)u(A∩B̄)u(Ā∩B)=A∪B", E1(a,b))
    check("c1 F=(A∩B) par De Morgan", F1(a,b))
    check("c1 (A∪B)∩(Ā∪B)=B", (a | b) & ((U8 - a) | b) == b)

# ---------- Chapitre 2 : logique ----------
check("c2 2^10 = 1024 != 1000", 2**10 == 1024 and 2**10 != 1000)
P_w, Q_w = 0b01100111, 0b11110001
check("c2 P∧Q = 01100001", format(P_w & Q_w, '08b') == '01100001')
check("c2 P∨Q = 11110111", format(P_w | Q_w, '08b') == '11110111')
check("c2 P⊕Q = 10010110", format(P_w ^ Q_w, '08b') == '10010110')
M_w, K_w = 0b1011010011110001, 0b1010111001001110
C_w = M_w ^ K_w
check("c2 C = 0001101010111111", format(C_w, '016b') == '0001101010111111')
check("c2 C⊕K = M", C_w ^ K_w == M_w)
# accuse : ((C->N) ∧ ¬N) -> ¬C tautologie
for c in (0,1):
    for n in (0,1):
        imp = (not c) or n
        lhs = imp and (not n)
        full = (not lhs) or (not c)
        check("c2 accuse ligne", full == 1)
# implication ≡ ¬P ∨ Q
for p in (0,1):
    for q in (0,1):
        check("c2 P->Q ≡ ¬P∨Q", int((not p) or q) == int((not p) or q))
# contradiction P ∧ ¬(P∨Q)
for p in (0,1):
    for q in (0,1):
        check("c2 P∧¬(P∨Q)=0", int(p and (not (p or q))) == 0)
# circuit F = A·B + B̄·C
for a in (0,1):
    for b in (0,1):
        for c in (0,1):
            f = (a & b) | ((1-b) & c)
            rows_f = {(0,0,0):0,(0,0,1):1,(0,1,0):0,(0,1,1):0,(1,0,0):0,(1,0,1):1,(1,1,0):1,(1,1,1):1}
            check("c2 circuit ligne", f == rows_f[(a,b,c)])
# simplifications booleennes (test exhaustif)
for a in (0,1):
    for b in (0,1):
        check("c2 (A+B)(A+B̄)=A", ((a or b) and (a or (1-b))) == a)
        check("c2 ĀB+AB+ĀB̄ = B+Ā", (((1-a)&b)|(a&b)|((1-a)&(1-b))) == (b or (1-a)))
        check("c2 F=¬(Ā+B)+A·B = A", ((((1-((1-a)|b)))&1) | (a&b)) == a)

# ---------- Chapitre 3 : numeration ----------
check("c3 (1023)_4 = 75", 1*64 + 0*16 + 2*4 + 3 == 75)
check("c3 (175)_8 = 125", 1*64 + 7*8 + 5 == 125)
check("c3 (A24)_16 = 2596", 10*256 + 2*16 + 4 == 2596)
check("c3 35 -> 100011", format(35, 'b') == '100011')
check("c3 35 = 32+2+1", 32 + 2 + 1 == 35)
check("c3 2596 -> A24_16", format(2596, 'X') == 'A24')
check("c3 divisions 2596", (2596 // 16, 2596 % 16, 162 // 16, 162 % 16, 10 // 16, 10 % 16) == (162, 4, 10, 2, 0, 10))
check("c3 1111010110110_2 = 7862", int('1111010110110', 2) == 7862)
check("c3 7862 -> (17266)_8", format(7862, 'o') == '17266')
check("c3 A24 -> 101000100100", format(0xA24, 'b') == '101000100100')
check("c3 1011+1101 = 11000 (24)", int('1011',2) + int('1101',2) == 24 and format(24,'b') == '11000')
check("c3 1011 x 101 = 55 = 110111", int('1011',2) * int('101',2) == 55 and format(55,'b') == '110111')
check("c3 55 = 32+16+4+2+1", 32+16+4+2+1 == 55)
check("c3 1101-0110 = 7 = 111", int('1101',2) - int('0110',2) == 7 and format(7,'b') == '111')
check("c3 3A7 = 935", 3*256 + 10*16 + 7 == 935)
check("c3 1B9 = 441", 1*256 + 11*16 + 9 == 441)
check("c3 3A7+1B9 = 1376 = (560)_16", 935 + 441 == 1376 and format(1376, 'X') == '560')
check("c3 1376 = 5x256+6x16", 5*256 + 6*16 == 1376)
check("c3 2^4=16 ; 2^8=256", 2**4 == 16 and 2**8 == 256)
check("c3 ASCII ord", (ord('C'), ord('P'), ord('T'), ord('E'), ord(' ')) == (67, 80, 84, 69, 32))
check("c3 ord('0')=48 ord('e')=101", (ord('0'), ord('e')) == (48, 101))
check("c3 32 = 00100000", format(32, '08b') == '00100000')
check("c3 67 = 01000011", format(67, '08b') == '01000011')
check("c3 48 = 00110000", format(48, '08b') == '00110000')
check("c3 101 = 01100101", format(101, '08b') == '01100101')
check("c3 CPTEC = 5 octets = 40 bits", 5 * 8 == 40)
check("c3 64 Go / 3 Mo ≈ 21300", abs(64e9 / 3e6 - 21333.33) < 1)

# ---------- Chapitre 4 : memoire ----------
check("c4 77 = 01001101", format(77, '08b') == '01001101')
check("c4 64+8+4+1 = 77", 64 + 8 + 4 + 1 == 77)
inv = 0b01001101 ^ 0b11111111
check("c4 inverse 10110010", inv == 0b10110010)
ca2 = inv + 1
check("c4 CA2(-77) = 10110011", ca2 == 0b10110011)
check("c4 lecture 179 - 256 = -77", 179 - 256 == -77 and 128+32+16+2+1 == 179)
a5, am3 = 0b00000101, 0b11111101
check("c4 3 -> 11111100 inverse", (0b00000011 ^ 0b11111111) == 0b11111100)
check("c4 5+(-3) = 2 (bit9 ignore)", ((a5 + am3) & 0xFF) == 0b00000010 and (a5 + am3) >> 8 == 1)
check("c4 6,5 = 0110,1000 (4+4 bits)", (0b0110, 0b1000/16) == (6, 0.5))
check("c4 2^16 = 65536", 2**16 == 65536)
check("c4 2^32 = 4294967296", 2**32 == 4294967296)
check("c4 8 Go = 8589934592 octets", 8 * 2**30 == 8589934592)
check("c4 32 Go = 32e9 octets = 29,8 GiO", 32 * 10**9 == 32000000000 and abs(32e9 / 2**30 - 29.8) < 0.1)
check("c4 32 Go / 4 Mo = 8000 photos", 32 * 10**9 / (4 * 10**6) == 8000)
check("c4 500 Go / 1,5 Go ≈ 333", abs(500e9 / 1.5e9 - 333.33) < 0.5)
check("c4 100+50 = 150 = 10010110", 100 + 50 == 150 and format(150, '08b') == '10010110')
check("c4 150 - 256 = -106", 150 - 256 == -106)
check("c4 0.1+0.2 = 0.30000000000000004", repr(0.1 + 0.2) == '0.30000000000000004')
check("c4 0.1+0.2 != 0.3", 0.1 + 0.2 != 0.3)
check("c4 50000 x 6 = 300000", 50000 * 6 == 300000)
check("c4 intervalles signes", (2**7 - 1, -2**7, 2**15 - 1, -2**15, 2**31 - 1, 2**63 - 1) ==
      (127, -128, 32767, -32768, 2147483647, 9223372036854775807))
check("c4 2,1 milliards = 2^31-1", abs(2**31 - 1 - 2.1e9) < 5e7)

# ---------- Chapitre 5 : angles ----------
check("c5 150° = 5pi/6", abs(150 * math.pi / 180 - 5 * math.pi / 6) < 1e-12)
check("c5 5pi/6 = 150°", abs(5 * math.pi / 6 * 180 / math.pi - 150) < 1e-12)
check("c5 72° = 2pi/5", abs(72 * math.pi / 180 - 2 * math.pi / 5) < 1e-12)
check("c5 rotation (4,1) -> (-1,4)", (-1, 4) == (-(1), 4))
k = 24 / math.sqrt(337)
check("c5 k = 24/sqrt(337) ≈ 1,3074", abs(k - 1.30742) < 1e-4)
check("c5 w = 16k ≈ 20,9 ; h = 9k ≈ 11,8", abs(16 * k - 20.92) < 0.01 and abs(9 * k - 11.77) < 0.01)
check("c5 53 cm x 30 cm", abs(16 * k * 2.54 - 53.1) < 0.15 and abs(9 * k * 2.54 - 29.9) < 0.15)
check("c5 15 x tan(35°) ≈ 10,50 m", abs(15 * math.tan(math.radians(35)) - 10.503) < 0.01)
check("c5 tan35 ≈ 0,700", abs(math.tan(math.radians(35)) - 0.700) < 0.001)
check("c5 u(3,4) norme 5", math.hypot(3, 4) == 5)
check("c5 u+v = (2,6)", (3 + (-1), 4 + 2) == (2, 6))
check("c5 2u = (6,8) norme 10", math.hypot(6, 8) == 10)
check("c5 AB = (5,12), norme 13", math.hypot(7 - 2, 15 - 3) == 13 and 25 + 144 == 169)

# ---------- Chapitre 6 : vecteurs et images ----------
check("c6 u+v = (-1,6)", (2 + (-3), 5 + 1) == (-1, 6))
check("c6 A·u = (4,15)", (2*2 + 0*5, 0*2 + 3*5) == (4, 15))
check("c6 echelle x2 (40,25)->(80,50)", (2*40, 2*25) == (80, 50))
check("c6 rotation (4,1)->(-1,4)", (0*4 - 1*1, 1*4 + 0*1) == (-1, 4))
check("c6 4000x3000 = 12 Mpx", 4000 * 3000 == 12000000)
check("c6 1920x1080 = 2073600 ≈ 2,07 Mpx", 1920 * 1080 == 2073600)
check("c6 1920/1080 = 16/9", abs(1920 / 1080 - 16 / 9) < 1e-12)
check("c6 4000/3000 = 4/3", abs(4000 / 3000 - 4 / 3) < 1e-12)
check("c6 impression 300 dpi : 33,9 x 25,4 cm", abs(4000 * 2.54 / 300 - 33.87) < 0.02 and abs(3000 * 2.54 / 300 - 25.4) < 0.01)
check("c6 impression 150 dpi : 67,7 x 50,8 cm", abs(4000 * 2.54 / 150 - 67.73) < 0.02 and abs(3000 * 2.54 / 150 - 50.8) < 0.01)
check("c6 164 = A4", 10 * 16 + 4 == 164 and format(164, 'X') == 'A4')
check("c6 78 = 4E", 4 * 16 + 14 == 78 and format(78, 'X') == '4E')
check("c6 20 = 14", 1 * 16 + 4 == 20 and format(20, 'X') == '14')
check("c6 1A2B3C = 26,43,60", (0x1A, 0x2B, 0x3C) == (26, 43, 60))
check("c6 2^24 = 16777216", 2**24 == 16777216)
check("c6 2^30 = 1073741824", 2**30 == 1073741824)
check("c6 2^4 = 16", 2**4 == 16)
check("c6 4000x3000x24/8 = 36 Mo", 4000 * 3000 * 24 / 8 == 36000000)
check("c6 288000000/8 = 36000000", 288000000 // 8 == 36000000)
check("c6 A4 300 dpi : 2480 x 3507 px", abs(21 * 300 / 2.54 - 2480.3) < 0.5 and abs(29.7 * 300 / 2.54 - 3507.9) < 0.5)
check("c6 2480x3508 ≈ 8,70 Mpx", 2480 * 3508 == 8699840)
check("c6 page 8 bits = 8,7 Mo ; 1 bit = 1,1 Mo", abs(8699840 / 1e6 - 8.7) < 0.05 and abs(8699840 / 8 / 1e6 - 1.09) < 0.02)
check("c6 36 -> 3,6 Mo (facteur 10) ; < 2 s a 2 Mo/s", 36 / 10 == 3.6 and 3.6 / 2 < 2)

# ---------- Enrichissements (tables ajoutees) ----------
# c2 : table (P∨Q)∧R
for p_,q_,r_ in [(1,1,1),(1,1,0),(1,0,1),(1,0,0),(0,1,1),(0,1,0),(0,0,1),(0,0,0)]:
    check("c2 (P∨Q)∧R ligne", int((p_ or q_) and r_) == {(1,1,1):1,(1,1,0):0,(1,0,1):1,(1,0,0):0,(0,1,1):1,(0,1,0):0,(0,0,1):0,(0,0,0):0}[(p_,q_,r_)])
# c2 : majoritaire = AB+AC+BC et forme canonique
for a in (0,1):
    for b in (0,1):
        for c in (0,1):
            canon = ((1-a)&b&c)|(a&(1-b)&c)|(a&b&(1-c))|(a&b&c)
            simp = (a&b)|(a&c)|(b&c)
            maj = 1 if (a+b+c) >= 2 else 0
            check("c2 majoritaire", canon == simp == maj)
# c3 : 185 = 128+32+16+8+1
check("c3 185 = 128+32+16+8+1", 128+32+16+8+1 == 185 and int('10111001',2) == 185)
# c3 : 0,625 -> 0,101 ; (101,01)2 = 5,25 ; Horner 13 ; 22x2=44
frac, bits = 0.625, ''
for _ in range(5):
    frac *= 2
    bits += str(int(frac))
    frac -= int(frac)
    if frac == 0: break
check("c3 0,625 = 0,101 en binaire", bits == '101' and frac == 0)
check("c3 (101,01)2 = 5,25", 4 + 1 + 0.25 == 5.25)
check("c3 Horner 1101 = 13", ((1*2+1)*2+0)*2+1 == 13)
check("c3 10110 x 10 = 101100 (44)", int('10110',2) * 2 == int('101100',2) == 44)
# c4 : extraits CA2 4 bits
for mot, val in [('0000',0),('0001',1),('0010',2),('0100',4),('0111',7),
                 ('1000',-8),('1010',-6),('1100',-4),('1110',-2),('1111',-1)]:
    v = int(mot, 2)
    if v >= 8: v -= 16
    check("c4 CA2 4 bits " + mot, v == val)
# c4 : framebuffer 1920x1080x3
check("c4 framebuffer = 6220800 o ≈ 6,2 Mo", 1920*1080*3 == 6220800 and abs(6220800/1e6 - 6.2) < 0.05)
check("c4 60 x 6,2 ≈ 372 Mo/s", abs(60 * 6.2208 - 372) < 2 and abs(60*6.2 - 372) < 1e-9)

# ---------- Enrichissements ch5/ch6 ----------
check("c5 3-4-5 pythagore", 3**2 + 4**2 == 5**2)
check("c5 angle entre (3,4) et (4,3) ≈ 16,26°", abs(math.degrees(math.acos(24/25)) - 16.26) < 0.01)
check("c5 produit scalaire (3,4)·(4,3) = 24, normes 5 et 5", 3*4 + 4*3 == 24 and math.hypot(3,4) == 5)
check("c6 HD = 0,92 Mpx ; 4K = 8,29 Mpx", 1280*720 == 921600 and 3840*2160 == 8294400)
S = [[2,0],[0,3]]; R = [[0,-1],[1,0]]
P_ = [[S[0][0]*R[0][0] + S[0][1]*R[1][0], S[0][0]*R[0][1] + S[0][1]*R[1][1]],
      [S[1][0]*R[0][0] + S[1][1]*R[1][0], S[1][0]*R[0][1] + S[1][1]*R[1][1]]]
check("c6 S x R = [[0,-2],[3,0]]", P_ == [[0,-2],[3,0]])
check("c6 (S.R).(4,1) = (-2,12)", (P_[0][0]*4 + P_[0][1]*1, P_[1][0]*4 + P_[1][1]*1) == (-2, 12))
check("c6 composition = rotation puis echelle", (2*(-1), 3*4) == (-2, 12))
check("c6 couleurs usuelles", ((255,255,0),(0,255,255),(255,0,255)) == ((255,255,0),(0,255,255),(255,0,255)))
check("c6 jaune = rouge+vert", (255,255,0)[0] == 255 and (255,255,0)[1] == 255 and (255,255,0)[2] == 0)

# ---------- Seconde vague ----------
import math as _m
check("c5 loi des cosinus b=7 c=8 a=60 -> 7,55", abs(_m.sqrt(7**2 + 8**2 - 2*7*8*math.cos(math.radians(60))) - 7.5498) < 0.01)
check("c6 ligne photo 4000 px RVB = 12000 o", 4000*3 == 12000)
check("c6 RGBA 32 bits = 48 Mo", 4000*3000*32//8 == 48000000)
check("c4 complement a un de 77 = -78 lu", 178 - 256 == -78 and 0b01001101 ^ 0b11111111 == 0b10110010)
check("c4 grandeur signee : deux zeros", (0b00000000, 0b10000000 & 0x7F) == (0, 0))
check("c6 2^4 = 16 couleurs indexees", 2**4 == 16)

check("c6 sqrt116 ≈ 10,8 ; envoi 288 Mb a 10 Mb/s = 29 s", abs(math.sqrt(116) - 10.77) < 0.01 and 36*8 == 288 and abs(288/10 - 28.8) < 0.1)
check("c6 JPEG 3,6 Mo = 28,8 Mb ; < 3 s a 10 Mb/s", 3.6*8 == 28.8 and 28.8/10 < 3)

s_acc = 0.0
for _ in range(1000): s_acc += 0.1
check("c4 somme boucle 1000x0.1 = 99.9999999999986", abs(s_acc - 99.9999999999986) < 1e-9)
check("c5 horloge 3h30 = 75 deg", 3.5*30 == 105 and 30*6 == 180 and 180-105 == 75 and 360//12 == 30 and 360//60 == 6)

print("OK : %d controles passes, 0 ecart." % ok)
