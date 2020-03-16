#! /usr/bin/python

import random, sys, os, time

if (len(sys.argv) != 2):
	print("Enter a valid gamemode.")
	print("Available gamemodes:\n")
	print("Random")
	sys.exit()

XWINS = 1
OWINS = 2
DRAW = 3
marks = [" "] * 9
GAMEMODE = sys.argv[1]

def checkBoardFull():
	for mark in marks:
		if mark == " ":
			return 0
	return 1

def checkBoardRows():
	i = 0
	for i in range(0, 7, 3):
		if marks[i] == marks[i + 1] == marks[i + 2]:
			if marks[i] == "X":
				return XWINS
			elif marks[i] == "O":
				return OWINS
	return 0

def checkBoardCols():
	i = 0
	for i in range(3):
		if marks[i] == marks[i + 3] == marks[i + 6]:
			if marks[i] == "X":
				return XWINS
			elif marks[i] == "O":
				return OWINS
	return 0

def checkBoardDiag():
	if marks[0] == marks[4] == marks[8]:
			if marks[0] == "X":
				return XWINS
			elif marks[0] == "O":
				return OWINS
	if marks[2] == marks[4] == marks[6]:
			if marks[2] == "X":
				return XWINS
			elif marks[2] == "O":
				return OWINS
	return 0

def checkGameEnded():
	gameState = checkBoardRows()
	if gameState:
		return gameState
	gameState = checkBoardCols()
	if gameState:
		return gameState
	gameState = checkBoardDiag()
	if gameState:
		return gameState
	if checkBoardFull():
		return DRAW
	
def printWinner(gameState):
	os.system("clear")
	print("Gamemode: " + sys.argv[1])
	printBoard()
	if gameState == XWINS:
		print("X wins!")
	elif gameState == OWINS:
		print("O wins!")
	else:
		print("It's a draw.")
		print(gameState)
	sys.exit()

def printBoard():
	print(" " + marks[6] +  " | " + marks[7] + " | " + marks[8] + " ")
	print("-----------")
	print(" " + marks[3] +  " | " + marks[4] + " | " + marks[5] + " ")
	print("-----------")
	print(" " + marks[0] +  " | " + marks[1] + " | " + marks[2] + " ")

def printBoardGui():
	os.system("clear")
	print("Gamemode: " + sys.argv[1])
	print(" " + marks[6] +  " | " + marks[7] + " | " + marks[8] + " ")
	print("-----------")
	print(" " + marks[3] +  " | " + marks[4] + " | " + marks[5] + " ")
	print("-----------")
	print(" " + marks[0] +  " | " + marks[1] + " | " + marks[2] + " ")
	if playerTurn:
		print("It's your turn.")
	else:
		print("Cpu is thinking...")

def checkMoveValidPlayer(pos):
	if pos > 9 or pos < 0:
		print("Move is not between 1 and 9.")
	elif marks[pos] != " ":
		print("Space is already occupied.")
	else:
		return 1
	return 0

def checkMoveValidCpu(pos):
	if marks[pos] != " ":
		return 0
	return 1

def handlePlayerTurn():
	while 1:
		pos = int(input()) - 1
		if checkMoveValidPlayer(pos):
			marks[pos] = playerMark
			return

def handleCpuTurn():
	time.sleep(1)
	while 1:
		pos = random.randint(0, 8)
		if checkMoveValidCpu(pos):
			marks[pos] = cpuMark
			return

playerTurn = random.choice([True, False]) # 1 for player turn
										# 0 for cpu turn
if (playerTurn):
	playerMark = "X"
	cpuMark = "O"
else:
	playerMark = "O"
	cpuMark = "X"

while 1:
	printBoardGui()
	gameState = checkGameEnded()
	if gameState:
		printWinner(gameState)
	if playerTurn:
		handlePlayerTurn()
	else:
		handleCpuTurn()
	playerTurn = not playerTurn
