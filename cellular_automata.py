import numpy as np
import random


def createMap(_w,_h,Density=0.5):
    newMap = np.zeros((_w,_h))
    for x in range(_w):
        for y in range(_h):
            ran = random.random()
            if ran < Density:
                newMap[x,y] = 1
            else:
                pass
    return newMap


def inRange(w,h,x,y):       
    return True if ((x > (w-1) or x < 0) or (y > (h-1) or y < 0)) else False


def getFriends(Map,x,y):
    Friends = 0
    w,h = Map.shape
    for _x in range(-1,2):
        for _y in range(-1,2):
            nX = x+_x
            nY = y+_y
            
            if nX == x and nY == y:
                pass
            elif inRange(w,h,nX,nY):
                Friends +=1
            elif Map[nX,nY] == 1:
                Friends += 1
            elif Map[nX,nY] == 0:
                pass


    return Friends


def step(Map,Alive=4):
    newMap = np.zeros(Map.shape)
    _w, _h = Map.shape
    for x in range(_w):
        for y in range(_h):
            _Friends = getFriends(Map,x, y)
            #print(_Friends)
            if _Friends > Alive:
                newMap[x,y] = 1
            elif _Friends <= Alive:
                newMap[x,y] = 0
    return newMap

def Simulation(size,steps=2,density=.5,alive=4) -> np.ndarray:  
    w,h = size

    Map = createMap(int(w),int(h),density)

    for _ in range(steps):
        Map = step(Map,alive)

    return Map
        
