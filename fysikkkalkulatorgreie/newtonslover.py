import math

def newtons_foerste_lov(m, a):
    F = m * a
    return F

def newtons_andre_lov(F, m):
    a = F / m
    return a

def newtons_tredje_lov(F1, F2):
    if F1 == -F2:
      return True
    else:
      return False

def kinetisk_energi(m, v):
    Ek = 0.5 * m * v**2
    return Ek

def potensiell_energi(m, h, g = 9.81):
    Ep = m * g * h
    return Ep

def arbeid(F, d):
    W = F * d
    return W

def effekt(W, t):
    P = W / t
    return P
