import pygame as pg
import math
# E = hc/λ

pi = math.pi  # 원주율
h = 6.62607015 * 10 ** -34  # Js 플랑크상수
c = 299792458  # m/s 빛의 속도
e = 1.6021773349 * 10 ** -19  # C 전자의 전하량
m = 9.10938356 * 10 ** -31  # kg 전자의 질량
μ0 = 4 * pi * 10 ** -7  # H/m 진공의 투자율
ε0 = 1 / (μ0 * c ** 2)  # F/m 진공 유전율

def lamda2RGB(lamda):
    gamma = 0.8

    if (lamda >= 380 and lamda <= 440):
        a = 0.3 + 0.7 * (lamda - 380) / (440 - 380)
        r = pow(((-(lamda - 440) / (440 - 380)) * a), gamma)
        g = 0.0
        b = pow(a, gamma)
    elif (lamda > 440 and lamda <= 490):
        r = 0.0
        g = pow(((lamda - 440) / (490 - 440)), gamma)
        b = 1.0
    elif (lamda > 490 and lamda <= 510):
        r = 0.0
        g = 1.0
        b = pow((-(lamda - 510) / (510 - 490)), gamma)
    elif (lamda > 510 and lamda <= 580):
        r = pow(((lamda - 510) / (580 - 510)), gamma)
        g = 1.0
        b = 0.0
    elif (lamda > 580 and lamda <= 645):
        r = 1.0
        g = pow((-(lamda - 645) / (645 - 580)), gamma)
        b = 0.0
    elif (lamda > 645 and lamda <= 780):
        a = 0.3 + 0.7 * (780 - lamda) / (780 - 645)
        r = pow(a, gamma)
        g = 0.0
        b = 0.0
    else:
        r = 0.0
        g = 0.0
        b = 0.0
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    return (r, g, b)

def m2nm(m):
    return m * 10 ** 9

def hydrogenSpec(n):
    a = -1 * (e**4 * m) / (8 * ε0**2 * h**2)  # J
    return a / n**2

num = 7

absordE = []
for i in range(1, num):
    for j in range(i+1, num+1):
        dif = hydrogenSpec(j) - hydrogenSpec(i)
        absordE.append(dif)


lamda = []
for E in absordE:
    lamda.append(m2nm(h * c / E))

lamda.sort()
for i in range(len(lamda)):
    print(lamda[i], end="   ")
    if i % 2 ==1:
        print()

pg.init()

size = [400, 100]
screen = pg.display.set_mode(size)

pg.display.set_caption("Hydrogen Spectrum")

done = False
de = 1
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.fill((255, 255, 255))

    for i in range(380, 780):
        x = i/de - 380
        col = lamda2RGB(i)
        pg.draw.line(screen, col, (x, 0), (x, 100))

    black = (0, 0, 0)
    for i in lamda:
        if i > 1000:
            continue
        i = int(i) - 380
        pg.draw.line(screen, black, (i, 0), (i, 100), 3)
    """
    black = (0, 0, 0)
    for i in lamda:
        i = int(i/de)
        pg.draw.line(screen, black, (i, 0), (i, 100), 1)
    """
    pg.display.flip()
pg.quit()










