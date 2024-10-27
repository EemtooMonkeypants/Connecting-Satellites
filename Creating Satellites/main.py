import pgzrun
from random import randint
from time import time
lines = []
WIDTH = 800
HEIGHT = 600
TITLE = 'Satellites'
numberofsatellites = 8
satellites = []
nextsatellite = 0
starttime = 0
totaltime = 0
def createSatellite():
    global starttime
    for i in range(numberofsatellites):
        sat = Actor('satellite')
        sat.pos = randint(50, WIDTH-50),randint(50, HEIGHT-50)
        satellites.append(sat)
    starttime = time()

def draw():
    global totaltime
    screen.blit('bg', (0,0))
    number = 1
    for count in satellites:
        screen.draw.text(str(number),(count.pos[0], count.pos[1]+20))
        count.draw()
        number +=1
    
    for count in lines:
        screen.draw.line(count[0], count[1], 'white')

    if nextsatellite < numberofsatellites:
        totaltime = time() - starttime
        screen.draw.text(str(round(totaltime,1)),(10,10), fontsize = 30)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10), fontsize = 30)

def update():
    pass

def on_mouse_down(pos):

    global nextsatellite, lines
    if nextsatellite < numberofsatellites:

        if satellites[nextsatellite].collidepoint(pos):
            if nextsatellite: 
                lines.append((satellites[nextsatellite-1].pos, satellites[nextsatellite].pos))
            nextsatellite +=1
        else:
            lines=[]
            nextsatellite = 0
createSatellite()
pgzrun.go()