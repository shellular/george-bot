#imports the things
import pynput
import json
import time
import random
from pynput.keyboard import Key, Controller
kb = Controller()

#reads the keybind json file. no wayy
with open("options/binds.json") as binds_file:
    bindsJSON = json.load(binds_file)
    
    upInput = bindsJSON["up"]
    downInput = bindsJSON["down"]
    leftInput = bindsJSON["left"]
    rightInput = bindsJSON["right"]
    pInput = bindsJSON["punch"]
    kInput = bindsJSON["kick"]
    sInput = bindsJSON["slash"]
    hsInput = bindsJSON["hslash"]
    dInput = bindsJSON["dust"]
    tInput = bindsJSON["taunt"]
    
noInput = ""
jumpChance = 20
walkRightChance = 10
walkLeftChance = 10
dashLeftChance = 50
dashRightChance = 50
crouchChance = 30
pChance = 40
kChance = 20
sChance = 25
hsChance = 25
dChance = 10
tChance = 2
noChance = 0

maxHoldTime = 1
def tryLoneInput(odds, button, holdTime, hasAltMovement, altOdds, altButton):
    if random.randint(1,100) <= odds:
        kb.press(button)
    elif random.randint(1,100) <= altOdds and hasAltMovement:
        kb.press(altButton)
    global maxHoldTime
    maxHoldTime = holdTime
inputCycle = 0
print("hi, i'm george, and i like to do george things! let's play guilty gear")
while True:
    inputCycle += 1
    print("i've made input choices " + str(inputCycle) + " times!")
    time.sleep(random.uniform(0.1, maxHoldTime))
    kb.release(leftInput)
    kb.release(rightInput)
    kb.release(upInput)
    kb.release(downInput)
    kb.release(pInput)
    kb.release(kInput)
    kb.release(sInput)
    kb.release(hsInput)
    kb.release(dInput)
    kb.release(tInput)
    
    tryLoneInput(pChance, pInput, 0.1, False, noChance, noInput)   
    tryLoneInput(kChance, kInput, 0.1, False, noChance, noInput)   
    tryLoneInput(sChance, sInput, 0.1, False, noChance, noInput)   
    tryLoneInput(hsChance, hsInput, 0.1, False, noChance, noInput)   
    tryLoneInput(dChance, dInput, 0.1, False, noChance, noInput)   
    tryLoneInput(tChance, tInput, 0.1, False, noChance, noInput)

    tryLoneInput(jumpChance, upInput, 0.1, False, noChance, noInput)
    tryLoneInput(walkLeftChance, leftInput, 2, True, walkRightChance, rightInput) 
    tryLoneInput(crouchChance, downInput, 1, False, noChance, noInput)
    
    if random.randint(1,100) <= dashLeftChance:
        kb.press(leftInput)
        time.sleep(0.05)
        kb.release(leftInput)
        time.sleep(0.05)
        kb.press(leftInput)
        maxHoldTime = 2
    elif random.randint(1,100) <= dashRightChance:
        kb.press(rightInput)
        time.sleep(0.05)
        kb.release(rightInput)
        time.sleep(0.05)
        kb.press(rightInput)
        maxHoldTime = 2