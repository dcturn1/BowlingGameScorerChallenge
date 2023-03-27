#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################################
#Title: bowlingGame.py
#Author: Douglas T.
#Creation Date: 03/25/2023
#Description: The terminal based version of Score a Bowling Game App.
#
#Changelog:
#Name:          Date:       Change:
# Douglas T.    03/25/2023  Initial version
#########################################################################################

import os
import sys

#A dictionary that holds the values given for each shot. The key represents the
#frame while the value list represents the shots.
frames = {1: [0,0], 2: [0,0], 3: [0,0], 4: [0,0], 5: [0,0], 6: [0,0], 7: [0,0], 8: [0,0], 9: [0,0], 10: [0,0,0]}
#A dictionary that holds the scores for each of the frames.  The key represents
#the frame while the value represents the score.
frameTotals = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

#Description: Takes user input and performs a series of checks to ensure the
#   value is appropriate
#Inputs: currentShot: the current shot in the frame
#        currentFrame: the current frame
#Output: The user entered value for the current shot.
def getInput(currentShot, currentFrame):
    correctInput = False
    value = ''
    while correctInput == False:
        inData = input()
        if  inData == "0" or inData == "1" or inData == "2" or inData == "3" or inData == "4" or inData == "5" or inData == "6" or inData == "7" or inData == "8" or inData == "9":
            value = int(inData)
            if currentShot == 2 and (value + (frames[currentFrame])[0]) >= 10:
                print("Total pins down per frame cannot be greater than 10, and should be a spare.")
            else:
                correctInput = True
        elif inData == "/":
            if currentShot != 1:
                value = inData
                correctInput = True
            else:
                print("Invalid entry: Cannot have a spare on the first shot of a frame.")
        elif inData == "X" or inData == "x":
            if currentShot != 2 or (currentFrame == 10 and (frames[10])[currentShot - 2] == "X"):
                value = inData.upper()
                correctInput = True
            else:
                print("Invalid entry: Cannot have a strike on the second shot of a frame.")
        else:
            print("Invalid entry")
    return(value)

#Description: A helper function used for calculating the score of frames
#that contain a spare.
#Inputs: frame: the number of the frame being calculated.
#Output: Returns the score for the frame.
def calcSpare(frame):
    value = 0
    if (frames[frame + 1])[0] == "X":
        value = 20
    else:
        value = (frames[frame + 1])[0] + 10

    return(value)

#Description: A helper function used for calculating the score of frames that
#that contain a strike.
#Inputs: frame: the number of the frame being calculated.
#Output: Returns the score for the desired frame.
def calcStrike(frame):
    value = 0
    if frame == 9:
        shotOne = (frames[frame + 1])[0]
        shotTwo = (frames[frame + 1])[1]
        if shotOne == "X":
            shotOne = 10
        if shotTwo == "X":
            shotTwo = 10
        if shotTwo == "/":
            shotOne = 10
            shotTwo = 0
        value = shotOne + shotTwo + 10
    elif "X" in frames[frame + 1]:
        if "X" in frames[frame + 2]:
            value = 30
        else:
            value = 20 + (frames[frame + 2])[0]
    elif "/" in frames[frame + 1]:
        value = 20
    else:
        value = sum(frames[frame + 1]) + 10

    return(value)

#Description: Iterates through the frames, updating the scores held in
#frameTotals
#Inputs: curentFrame: the number of the current frame.
#Output: Updates the scores held in frameTotals
def updateTotals(currentFrame):
    for i in range(1, currentFrame + 1):
        if i == 1:
            if "X" in frames[i]:
                frameTotals[i] = calcStrike(i)
            elif "/" in frames[i]:
                frameTotals[i] = calcSpare(i)
            else:
                frameTotals[i] = sum(frames[i])
        elif i == 10:
            shots = [10 if x == "X" else x for x in frames[i]]
            if "/" in shots:
                frameTotals[i] = frameTotals[i - 1] + 10 + shots[2]
            else:
                frameTotals[i] =  frameTotals[i - 1] + sum(shots)
        else:
            if "X" in frames[i]:
                frameTotals[i] = calcStrike(i) + frameTotals[i - 1]
            elif "/" in frames[i]:
                frameTotals[i] = calcSpare(i) + frameTotals[i - 1]
            else:
                frameTotals[i] = frameTotals[i - 1] + sum(frames[i])

#Description: Restarts the entire program
#Inputs: None
#Output: None
def restartEverything():
    os.execl(sys.executable, sys.executable, *sys.argv)

if __name__ == "__main__":

    for currentFrame in list(frames):
        if currentFrame == 10:
            shotMax = 2
            currentShot = 1
            while currentShot <= shotMax:
                shotValue = getInput(currentShot, currentFrame)
                (frames[currentFrame])[currentShot - 1] = shotValue
                if currentShot == 1 and shotValue == "X":
                    shotMax += 1
                if currentShot == 2 and shotValue == "/":
                    shotMax += 1
                currentShot += 1
                updateTotals(currentFrame)
                print(frames)
                print("\n")
                print(frameTotals)
                print("\n")
        else:
            shotMax = 2
            currentShot = 1
            while currentShot <= shotMax:
                shotValue = getInput(currentShot, currentFrame)
                (frames[currentFrame])[currentShot - 1] = shotValue
                if shotValue == "X":
                    (frames[currentFrame])[currentShot] = 0
                    currentShot += 1
                currentShot += 1
                updateTotals(currentFrame)
                print(frames)
                print("\n")
                print(frameTotals)
                print("\n")
