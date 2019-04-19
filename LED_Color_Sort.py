import board
import adafruit_dotstar as dotstar
    #print led[i]
dots = dotstar.DotStar(board.SCK, board.MOSI, 30, brightness=0.5,auto_write=True)

import random
#led = [(y,0,0) for y in range(random.sample(range(100), 30))]
led = [(y,0,0) for y in range(10,250,8)]

#led = [(y,0,0) for y in range(10,250,8)]

store = []
for i in range(30):
  store.append(random.choice(led))

for i in range(30):
    dots[i] = (50,store[i][0],255-store[i][0])

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp


selectionSort(store)

for i in range(30):
    dots[i] = (50,store[i][0],255-store[i][0])













