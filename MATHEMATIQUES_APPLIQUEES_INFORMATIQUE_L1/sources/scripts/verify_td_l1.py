# -*- coding: utf-8 -*-
"""Verification de TOUTES les valeurs numeriques des TD et corriges MAI L1-L2.
Chaque assertion imprime OK ; le script s'arrete a la premiere erreur."""
import math, sys

def ok(label, cond=True):
    if not cond:
        print('ECHEC :', label)
        sys.exit(1)
    print('OK  ', label)

# ---------- Chapitre 1 : ensembles ----------
A = set(range(2, 11)); ok('1.1 |A| = 9', len(A) == 9)
B = set('licence'); ok('1.1 B = {l,i,c,e,n}, |B| = 5', B == set('licen') and len(B) == 5)
ok('1.1 |AxB| = 45', len(A) * len(B) == 45)

U = set(range(1, 9)); A2 = {1, 2, 3, 4}; B2 = {3, 4, 5, 6}
ok('1.2 A u B', A2 | B2 == {1, 2, 3, 4, 5, 6})
ok('1.2 A n B', A2 & B2 == {3, 4})
ok('1.2 barA', U - A2 == {5, 6, 7, 8})
ok('1.2 barB', U - B2 == {1, 2, 7, 8})
ok('1.2 barA n barB = bar(AuB) = {7,8}', (U - A2) & (U - B2) == U - (A2 | B2) == {7, 8})
ok('1.2 bar(AnB) = barA u barB = {1,2,5,6,7,8}',
   U - (A2 & B2) == (U - A2) | (U - B2) == {1, 2, 5, 6, 7, 8})

ok('1.3 zones 33/24/72/18', 48 - 15 == 33 and 39 - 15 == 24 and 33 + 15 + 24 == 72 and 90 - 72 == 18)
ok('1.3 formule 48+39-15 = 72', 48 + 39 - 15 == 72)

Pseul = 34 - 12 - 9 + 4; Jseul = 27 - 12 - 7 + 4; Sseul = 22 - 9 - 7 + 4
union = Pseul + Jseul + Sseul + (12 - 4) + (9 - 4) + (7 - 4) + 4
ok('1.4 regions 17/12/10/8/5/3', (Pseul, Jseul, Sseul) == (17, 12, 10) and (12 - 4, 9 - 4, 7 - 4) == (8, 5, 3))
ok('1.4 union = 59, aucun = 11, somme = 70', union == 59 and 70 - 59 == 11 and union + 11 == 70)

U4 = set(range(1, 5)); A4 = {1, 2}; B4 = {2, 3}
ok('1.5 E = B', (A4 & B4) | ((U4 - A4) & B4) == B4 == {2, 3})
ok('1.5 F = A', (A4 | B4) & (A4 | (U4 - B4)) == A4 == {1, 2})

# ---------- Chapitre 2 : logique ----------
V = [(p, q) for p in (0, 1) for q in (0, 1)]  # ordre binaire 00,01,10,11
NOT = lambda a: 1 - a
AND = lambda a, b: a & b
OR = lambda a, b: a | b
IMP = lambda a, b: 0 if (a == 1 and b == 0) else 1

# exercice 2 : quatre colonnes attendues
att_npq = [0, 1, 0, 0]; att_pvnq = [1, 0, 1, 1]
att_npq2 = [1, 1, 1, 0]; att_npvnq = [1, 1, 1, 0]
ok('2.2 colonne NOT P AND Q', [AND(NOT(p), q) for p, q in V] == att_npq)
ok('2.2 colonne P OR NOT Q', [OR(p, NOT(q)) for p, q in V] == att_pvnq)
ok('2.2 De Morgan 1 (tables egales)', [NOT(AND(p, q)) for p, q in V] == [OR(NOT(p), NOT(q)) for p, q in V] == att_npq2)

# exercice 3
ok('2.3 De Morgan 2', [NOT(OR(p, q)) for p, q in V] == [AND(NOT(p), NOT(q)) for p, q in V] == [1, 0, 0, 0])
ok('2.3 P->Q = NOT P OR Q', [IMP(p, q) for p, q in V] == [OR(NOT(p), q) for p, q in V] == [1, 1, 0, 1])
ok('2.3 contra = imp ; reciproque differente',
   [IMP(NOT(q), NOT(p)) for p, q in V] == [IMP(p, q) for p, q in V] == [1, 1, 0, 1]
   and [IMP(q, p) for p, q in V] == [1, 0, 1, 1])
ok('2.3 Q4 negation S AND NOT E', [AND(1, NOT(0))] == [1] and IMP(1, 0) == 0)

# exercice 4 : simplifications booleennes sur 8 lignes
T = list(itertools.product((0, 1), repeat=3)) if False else [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
X = [OR(AND(a, b), AND(a, OR(b, c))) for a, b, c in T]
Xs = [AND(a, OR(b, c)) for a, b, c in T]
Y = [AND(OR(a, b), OR(a, c)) for a, b, c in T]
Ys = [OR(a, AND(b, c)) for a, b, c in T]
Z = [AND(a, OR(a, b)) for a, b, c in T]
As = [a for a, b, c in T]
ok('2.4 X = A(B+C) sur 8 lignes', X == Xs)
ok('2.4 Y = A+BC sur 8 lignes', Y == Ys)
ok('2.4 Z = A sur 8 lignes', Z == As)
ok('2.4 colonnes affichees X/Y/Z', X == [0,0,0,0,0,1,1,1] and Y == [0,0,0,1,1,1,1,1] and Z == [0,0,0,0,1,1,1,1])

# exercice 5
P = [0, 1, 1, 0, 0, 1, 1, 1]; Q = [1, 1, 1, 1, 0, 0, 0, 1]
ok('2.5 P AND Q = 01100001', ''.join(map(str, [AND(a, b) for a, b in zip(P, Q)])) == '01100001')
ok('2.5 P OR Q = 11110111', ''.join(map(str, [OR(a, b) for a, b in zip(P, Q)])) == '11110111')
ok('2.5 P XOR Q = 10010110', ''.join(map(str, [a ^ b for a, b in zip(P, Q)])) == '10010110')
M, K = 0b1011, 0b0110
ok('2.5 C = M xor K = 1101 ; C xor K = M', bin(M ^ K)[2:] == '1101' and (M ^ K) ^ K == M == 0b1011)
ok('2.5 S = (A AND B) OR (NOT A AND B) = B',
   [OR(AND(a, b), AND(NOT(a), b)) for a in (0, 1) for b in (0, 1)] == [0, 1, 0, 1])

# ---------- Chapitre 3 : numeration ----------
ok('3.1 110101 = 53 ; 127,4_8 = 87,5 ; 2E,8_16 = 46,5',
   int('110101', 2) == 53 and 1*64 + 2*8 + 7 + 4/8 == 87.5 and 2*16 + 14 + 8/16 == 46.5)
ok('3.2 2026 -> 11111101010 / 3752_8 / 7EA_16',
   bin(2026)[2:] == '11111101010' and oct(2026)[2:] == '3752' and hex(2026)[2:].upper() == '7EA')
ok('3.2 77 -> 1001101', bin(77)[2:] == '1001101')
ok('3.3 175_8 = 125 = 1111101', int('175', 8) == 125 == int('1111101', 2))
ok('3.3 A24_16 = 2596 = 101000100100', int('A24', 16) == 2596 == int('101000100100', 2))
ok('3.3 1111101101 = 1005 = 1755_8 = 3ED_16',
   int('1111101101', 2) == 1005 == int('1755', 8) == int('3ED', 16))
ok('3.4 247+31 = 278 = 100010110', int('11110111', 2) == 247 and int('11111', 2) == 31
   and 247 + 31 == 278 == int('100010110', 2))
ok('3.4 278-43 = 235 = 11101011', int('101011', 2) == 43 and 278 - 43 == 235 == int('11101011', 2))
ok('3.4 3A7+19B = 542_16 = 1346', int('3A7', 16) == 935 and int('19B', 16) == 411
   and 935 + 411 == 1346 == int('542', 16))
ok('3.5 2^8 = 256 ; 2^24 = 16 777 216', 2**8 == 256 and 2**24 == 16777216)
ok('3.5 ecart 4Go vs 4Gio = 294 967 296', 4 * 2**30 - 4 * 10**9 == 294967296)
ok('3.5 C=67 -> 01000011 ; T=84 -> 01010100',
   bin(67)[2:].zfill(8) == '01000011' and bin(84)[2:].zfill(8) == '01010100')
ok('3.6 64e9/2^30 = 59,6', round(64e9 / 2**30, 1) == 59.6)
ok('3.6 1000 codes -> 10 bits ; 2C_16 = 44 = 101100',
   2**9 == 512 and 2**10 == 1024 and int('2C', 16) == 44 == int('101100', 2))

# ---------- Chapitre 4 : memoire ----------
ok('4.1 45 = 00101101 ; -45 -> 11010011 ; lu 211 -> -45',
   bin(45)[2:].zfill(8) == '00101101'
   and bin((~45 & 0xFF) + 1)[2:] == '11010011'
   and int('11010011', 2) == 211 and 211 - 256 == -45)
ok('4.1 -1 -> 11111111', bin((~1 & 0xFF) + 1)[2:] == '11111111')
ok('4.2 90 = 01011010', bin(90)[2:].zfill(8) == '01011010')
s = (0b11010011 + 0b01011010) & 0xFF
ok('4.2 somme 8 bits = 00101101 = 45 ; decimal -45+90 = 45', s == 0b00101101 == 45 and -45 + 90 == 45)
ok('4.3 75 = 01001011 ; 65 = 01000001 ; somme = 10001100 = 140 -> -116',
   bin(75)[2:].zfill(8) == '01001011' and bin(65)[2:].zfill(8) == '01000001'
   and (75 + 65) & 0xFF == 0b10001100 == 140 and 140 - 256 == -116)
ok('4.4 2^20 = 1 048 576 = 1024 kio', 2**20 == 1048576 and 1048576 / 1024 == 1024)
fb = 1280 * 720 * 3
ok('4.4 framebuffer 2 764 800 octets = 2,8 Mo', fb == 2764800 and round(fb / 1e6, 1) == 2.8)
ok('4.4 128 Go -> 119,2 Gio', round(128e9 / 2**30, 1) == 119.2)

# ---------- Chapitre 5 : angles ----------
ok('5.1 45->pi/4 ; 210->7pi/6 ; 300->5pi/3',
   (45, 210, 300) == tuple(round(d * 180 / math.pi, 6) for d in (math.pi/4, 7*math.pi/6, 5*math.pi/3))
   or all(abs(g * math.pi / 180 - r) < 1e-12 for g, r in
          ((45, math.pi/4), (210, 7*math.pi/6), (300, 5*math.pi/3))))
ok('5.1 5pi/4 -> 225 ; 11pi/6 -> 330 ; pi/9 -> 20',
   all(abs(r * 180 / math.pi - g) < 1e-9 for r, g in
       ((5*math.pi/4, 225), (11*math.pi/6, 330), (math.pi/9, 20))))
ok('5.2 horloge 8h20 : 250 - 120 = 130', abs((8 + 1/3) * 30 - 250) < 1e-9 and 20 * 6 == 120 and 250 - 120 == 130)
ok('5.3 echelle : 6,5^2 - 2,5^2 = 36 -> 6 m', 6.5**2 - 2.5**2 == 36 and math.sqrt(36) == 6)
h = 25 * math.tan(math.radians(30))
ok('5.3 tour : 25 x tan30 = 14,4 m', abs(h - 14.43) < 0.02 and round(h, 1) == 14.4)
ok('5.4 u+v ; ||u|| = 5 ; ||v|| = 5,10', math.sqrt(4**2 + 3**2) == 5 and round(math.sqrt(26), 2) == 5.10)
ok('5.4 2u-v = (7,-11) ; norme 13,04', math.sqrt(7**2 + 11**2) == math.sqrt(170)
   and round(math.sqrt(170), 2) == 13.04)
ok('5.4 AB = (5,-12) ; distance 13', math.sqrt(5**2 + 12**2) == 13)

# ---------- Chapitre 6 : images ----------
Mpr = [[2, 0], [0, 3]]; Mr = [[0, -1], [1, 0]]; p = (5, 2)
mul = lambda M, v: (M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1])
mmul = lambda X, Y: [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
ok('6.1 Ap = (10,6) ; Rp = (-2,5)', mul(Mpr, p) == (10, 6) and mul(Mr, p) == (-2, 5))
ok('6.1 A(Rp) = (-4,15)', mul(Mpr, mul(Mr, p)) == (-4, 15))
ok('6.1 A x R = [[0,-2],[3,0]] ; (A x R)p = (-4,15)',
   mmul(Mpr, Mr) == [[0, -2], [3, 0]] and mul(mmul(Mpr, Mr), p) == (-4, 15))
ok('6.2 4032 x 3024 = 12 192 768 = 12,2 Mpx ; rapport 4/3',
   4032 * 3024 == 12192768 and round(12192768 / 1e6, 1) == 12.2 and 4032 / 3024 == 4/3)
L = 4032 * 2.54 / 300; H = 3024 * 2.54 / 300
ok('6.2 impression 34,1 x 25,6 cm > A4 paysage 29,7 x 21',
   round(L, 1) == 34.1 and round(H, 1) == 25.6 and (L > 29.7 and H > 21))
def hx(n):
    q, r = divmod(n, 16)
    return ('0123456789ABCDEF'[q] + '0123456789ABCDEF'[r])
ok('6.3 (66,135,245) -> #4287F5', (hx(66), hx(135), hx(245)) == ('42', '87', 'F5'))
ok('6.3 #1B5E20 -> (27, 94, 32)', (int('1B', 16), int('5E', 16), int('20', 16)) == (27, 94, 32))
ok('6.3 2^24 = 16 777 216 ; gris 2^8 = 256', 2**24 == 16777216 and 2**8 == 256)
ok('6.4 poids 1920x1080x24/8 = 6 220 800 = 6,2 Mo', 1920 * 1080 * 3 == 6220800
   and round(6220800 / 1e6, 1) == 6.2)
ok('6.4 JPEG x10 -> 0,6 Mo', round(6.2208 / 10, 1) == 0.6)
ok('6.4 scan 2480 x 3508 = 8 699 840 ; N&B /8 = 1 087 480 = 1,1 Mo ; gris 8,7 Mo',
   2480 * 3508 == 8699840 and 8699840 // 8 == 1087480
   and round(1087480 / 1e6, 1) == 1.1 and round(8699840 / 1e6, 1) == 8.7)

# ---------- Cours : valeurs reprises et corrigees ----------
ok('cours 6 : 4000x3000 -> 33,9 x 25,4 cm ; A3 42 x 29,7 ok, A4 paysage 29,7 x 21 non',
   round(4000 * 2.54 / 300, 1) == 33.9 and round(3000 * 2.54 / 300, 1) == 25.4
   and (33.9 > 29.7 and 25.4 > 21) and (33.9 < 42 and 25.4 < 29.7))
ok('cours 6 : 150 dpi -> 67,7 x 50,8 cm', round(4000 * 2.54 / 150, 1) == 67.7 and round(3000 * 2.54 / 150, 1) == 50.8)

print('\nTOUTES LES VALEURS SONT VERIFIEES.')
