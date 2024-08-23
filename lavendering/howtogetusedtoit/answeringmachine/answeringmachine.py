import os
import time
from collections import defaultdict

bpm = 161
multiplier = 2*(1/(bpm/60))
print(multiplier)
with open("lyrics.txt", "r") as f:
    wordsArr = f.read().split()
with open("timing.txt", "r") as f:
    timingArr = f.read().split()
        
lyricMap = defaultdict(list)
for i in range(len(wordsArr)):
    lyricMap[i].append(wordsArr[i])
    lyricMap[i].append(timingArr[i])

def print_at_rate(lyricMap):
    for key in lyricMap:
        if(lyricMap[key][0] == "[newline]"):
            print("")
        elif(lyricMap[key][0] == "[wipe]"):
            os.system('cls')
        elif(lyricMap[key][0] == "[wait]"):
            time.sleep(multiplier*(float(70/4)))
        else:
            print(end=' ', flush=True)
            for character in lyricMap[key][0]:
                print('\033[93m' + character, end='', flush=True)
                time.sleep(float(multiplier*(float(lyricMap[key][1])/4)/len(lyricMap[key][0])))
            print(end='', flush=True)

print_at_rate(lyricMap)

