import pygame
import wordBank

def drawStart():
  pygame.init()
  white = (255,255,255)
  color = (83, 141, 78)
  yellow = (181, 159, 59)
  surface = pygame.display.set_mode((400, 300))
  background_colour = (18,18,19)
  pygame.display.set_caption('Wordle Helper')
  surface.fill(background_colour)
############################################################################################################
  pygame.draw.rect(surface, color, pygame.Rect(25, 30, 50, 50), 0, 3)
  pygame.draw.rect(surface, color, pygame.Rect(85, 30, 50, 50), 0, 3)
  pygame.draw.rect(surface, color, pygame.Rect(145, 30, 50, 50), 0, 3)
  pygame.draw.rect(surface, color, pygame.Rect(205, 30, 50, 50), 0, 3)
  pygame.draw.rect(surface, color, pygame.Rect(265, 30, 50, 50), 0, 3)
  pygame.draw.rect(surface, color, pygame.Rect(325, 30, 50, 50), 0, 3)
  pygame.draw.rect(surface, color, pygame.Rect(135, 90, 130, 35), 0, 3)
  pygame.draw.rect(surface, yellow, pygame.Rect(125, 147, 150, 55), 0, 3)
  pygame.draw.rect(surface, (65,65,65), pygame.Rect(50, 135, 300, 3), 0, 3)
  pygame.draw.rect(surface, (65,65,65), pygame.Rect(50, 210, 300, 3), 0, 3)
############################################################################################################
  Font = pygame.font.SysFont('timesnewroman', 46)
  phraseFont = pygame.font.SysFont('timesnewroman', 30)
  versionFont = pygame.font.SysFont('timesnewroman', 20)
  buttonFont = pygame.font.SysFont('radiocanada', 50)
  letterW = Font.render("W", True, white)
  letterO = Font.render("O", True, white)
  letterR = Font.render("R", True, white)
  letterD = Font.render("D", True, white)
  letterL = Font.render("L", True, white)
  letterE = Font.render("E", True, white)
  phraseHelper = phraseFont.render("Helper", True, white)
  phraseCredits = phraseFont.render("Developed by Will Cuny", True, (65, 65, 65))
  phraseVersion = versionFont.render("v 1.1.4", True, (65,65,65))
  phraseStartButt = buttonFont.render("START", True, white)
############################################################################################################
  surface.blit(letterW, (28, 30))
  surface.blit(letterO, (93, 30))
  surface.blit(letterR, (155, 30))
  surface.blit(letterD, (213, 30))
  surface.blit(letterL, (277, 30))
  surface.blit(letterE, (336, 30))
  surface.blit(phraseHelper, (159, 90))
  surface.blit(phraseCredits, (50, 220))
  surface.blit(phraseVersion, (170, 254))
  surface.blit(phraseStartButt, (143, 159))
############################################################################################################

def findGreen(letterArray, wordList):
  surface = pygame.display.set_mode((400, 300))
  background_colour = (18,18,19)
  surface.fill(background_colour)
  letterFont = pygame.font.SysFont('radiocanada', 60)
  buttonFont = pygame.font.SysFont('radiocanada', 45)
  white = (255,255,255)

  pygame.draw.rect(surface, (83, 141, 78), pygame.Rect(20, 28, 360, 50), 0, 3)
  phraseGuess = buttonFont.render(("Click Green Letters"), True, white)
  surface.blit(phraseGuess, (58, 40))
  
  x = 55
  for letter in letterArray:
    pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(x - 10, 100 - 5, 50, 50), 0, 3)
    phraseLetter = letterFont.render(letter.upper(), True, (255, 255, 255))
    if letter == "i":
      surface.blit(phraseLetter, (x + 9, 100))
    else:
      surface.blit(phraseLetter, (x, 100))
    x += 65

  doneFont = pygame.font.SysFont('radiocanada', 50)
  pygame.draw.rect(surface, (181, 159, 59), pygame.Rect(125, 190, 150, 50), 0, 3)
  phraseDone = doneFont.render("DONE", True, white)
  surface.blit(phraseDone, (150, 200))
  numclicks1 = 1
  numclicks2 = 1
  numclicks3 = 1
  numclicks4 = 1
  numclicks5 = 1
  while True:
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
############################################################################################################
        if 45 <= x <= 95 and 95 <= y <= 145 and numclicks1 % 2 != 0:
          pygame.draw.rect(surface, (83, 141, 78), pygame.Rect(45, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[0].upper(), True, (255, 255, 255))
          if letterArray[0] == "i":
            surface.blit(phraseLetter, (55 + 9, 100))
          else: 
            surface.blit(phraseLetter, (55, 100))
          numclicks1 += 1
        elif 45 <= x <= 95 and 95 <= y <= 145 and numclicks1 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(45, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[0].upper(), True, (255, 255, 255))
          if letterArray[0] == "i":
            surface.blit(phraseLetter, (55 + 9, 100))
          else:
            surface.blit(phraseLetter, (55, 100))
          numclicks1 += 1
############################################################################################################
        if 110 <= x <= 160 and 95 <= y <= 145 and numclicks2 % 2 != 0:
          pygame.draw.rect(surface, (83, 141, 78), pygame.Rect(110, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[1].upper(), True, (255, 255, 255))
          if letterArray[1] == "i":
            surface.blit(phraseLetter, (120 + 9, 100))
          else:
            surface.blit(phraseLetter, (120, 100))
          numclicks2 += 1
        elif 110 <= x <= 160 and 95 <= y <= 145 and numclicks2 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(110, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[1].upper(), True, (255, 255, 255))
          if letterArray[1] == "i":
            surface.blit(phraseLetter, (120 + 9, 100))
          else:
            surface.blit(phraseLetter, (120, 100))
          numclicks2 += 1
############################################################################################################
        if 175 <= x <= 225 and 95 <= y <= 145 and numclicks3 % 2 != 0:
          pygame.draw.rect(surface, (83, 141, 78), pygame.Rect(175, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[2].upper(), True, (255, 255, 255))
          if letterArray[2] == "i":
            surface.blit(phraseLetter, (185 + 9, 100))
          else:
            surface.blit(phraseLetter, (185, 100))
          numclicks3 += 1
        elif 175 <= x <= 225 and 95 <= y <= 145 and numclicks3 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(175, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[2].upper(), True, (255, 255, 255))
          if letterArray[2] == "i":
            surface.blit(phraseLetter, (185 + 9, 100))
          else:
            surface.blit(phraseLetter, (185, 100))
          numclicks3 += 1
############################################################################################################
        if 240 <= x <= 290 and 95 <= y <= 145 and numclicks4 % 2 != 0:
          pygame.draw.rect(surface, (83, 141, 78), pygame.Rect(240, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[3].upper(), True, (255, 255, 255))
          if letterArray[3] == "i":
            surface.blit(phraseLetter, (250 + 9, 100))
          else:
            surface.blit(phraseLetter, (250, 100))
          numclicks4 += 1
        elif 240 <= x <= 290 and 95 <= y <= 145 and numclicks4 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(240, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[3].upper(), True, (255, 255, 255))
          if letterArray[3] == "i":
            surface.blit(phraseLetter, (250 + 9, 100))
          else:
            surface.blit(phraseLetter, (250, 100))
          numclicks4 += 1
############################################################################################################
        if 305 <= x <= 355 and 95 <= y <= 145 and numclicks5 % 2 != 0:
          pygame.draw.rect(surface, (83, 141, 78), pygame.Rect(305, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[4].upper(), True, (255, 255, 255))
          if letterArray[4] == "i":
            surface.blit(phraseLetter, (315 + 9, 100))
          else:
            surface.blit(phraseLetter, (315, 100))
          numclicks5 += 1
        elif 305 <= x <= 355 and 95 <= y <= 145 and numclicks5 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(305, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[4].upper(), True, (255, 255, 255))
          if letterArray[4] == "i":
            surface.blit(phraseLetter, (315 + 9, 100))
          else:
            surface.blit(phraseLetter, (315, 100))
          numclicks5 += 1

############################################################################################################
        if 125 <= x <= 275 and 190 <= y <= 240:
          if numclicks1 % 2 == 0:
            for word in wordList.copy():
              if word[0] != letterArray[0]:
                wordList.remove(word)
                
          if numclicks2 % 2 == 0:
            for word in wordList.copy():
              if word[1] != letterArray[1]:
                wordList.remove(word)

          if numclicks3 % 2 == 0:
            for word in wordList.copy():
              if word[2] != letterArray[2]:
                wordList.remove(word)

          if numclicks4 % 2 == 0:
            for word in wordList.copy():
              if word[3] != letterArray[3]:
                wordList.remove(word)

          if numclicks5 % 2 == 0:
            for word in wordList.copy():
              if word[4] != letterArray[4]:
                wordList.remove(word)
          return letterArray, wordList
############################################################################################################

def findYellow(letterArray, wordList):
  surface = pygame.display.set_mode((400, 300))
  background_colour = (18,18,19)
  surface.fill(background_colour)
  letterFont = pygame.font.SysFont('radiocanada', 60)
  buttonFont = pygame.font.SysFont('radiocanada', 45)
  white = (255,255,255)
  pygame.draw.rect(surface, (181, 159, 59), pygame.Rect(20, 28, 360, 50), 0, 3)
  phraseGuess = buttonFont.render(("Click Yellow Letters"), True, white)
  surface.blit(phraseGuess, (55, 40))
  x = 55
  for letter in letterArray:
    pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(x - 10, 100 - 5, 50, 50), 0, 3)
    phraseLetter = letterFont.render(letter.upper(), True, (255, 255, 255))
    if letter == "i":
      surface.blit(phraseLetter, (x + 9, 100))
    else: 
      surface.blit(phraseLetter, (x, 100))
    x += 65
  doneFont = pygame.font.SysFont('radiocanada', 50)
  pygame.draw.rect(surface, (181, 159, 59), pygame.Rect(125, 190, 150, 50), 0, 3)
  phraseDone = doneFont.render("DONE", True, white)
  surface.blit(phraseDone, (150, 200))
  numclicks1 = 1
  numclicks2 = 1
  numclicks3 = 1
  numclicks4 = 1
  numclicks5 = 1
  while True:
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
############################################################################################################
        if 45 <= x <= 95 and 95 <= y <= 145 and numclicks1 % 2 != 0:
          pygame.draw.rect(surface, (181, 159, 59), pygame.Rect(45, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[0].upper(), True, (255, 255, 255))
          if letterArray[0] == "i":
            surface.blit(phraseLetter, (55 + 9, 100))
          else: 
            surface.blit(phraseLetter, (55, 100))
          numclicks1 += 1
        elif 45 <= x <= 95 and 95 <= y <= 145 and numclicks1 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(45, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[0].upper(), True, (255, 255, 255))
          if letterArray[0] == "i":
            surface.blit(phraseLetter, (55 + 9, 100))
          else:
            surface.blit(phraseLetter, (55, 100))
          numclicks1 += 1
############################################################################################################
        if 110 <= x <= 160 and 95 <= y <= 145 and numclicks2 % 2 != 0:
          pygame.draw.rect(surface, (181, 159, 59), pygame.Rect(110, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[1].upper(), True, (255, 255, 255))
          if letterArray[1] == "i":
            surface.blit(phraseLetter, (120 + 9, 100))
          else:
            surface.blit(phraseLetter, (120, 100))
          numclicks2 += 1
        elif 110 <= x <= 160 and 95 <= y <= 145 and numclicks2 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(110, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[1].upper(), True, (255, 255, 255))
          if letterArray[1] == "i":
            surface.blit(phraseLetter, (120 + 9, 100))
          else:
            surface.blit(phraseLetter, (120, 100))
          numclicks2 += 1
############################################################################################################
        if 175 <= x <= 225 and 95 <= y <= 145 and numclicks3 % 2 != 0:
          pygame.draw.rect(surface, (181, 159, 59), pygame.Rect(175, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[2].upper(), True, (255, 255, 255))
          if letterArray[2] == "i":
            surface.blit(phraseLetter, (185 + 9, 100))
          else:
            surface.blit(phraseLetter, (185, 100))
          numclicks3 += 1
        elif 175 <= x <= 225 and 95 <= y <= 145 and numclicks3 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(175, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[2].upper(), True, (255, 255, 255))
          if letterArray[2] == "i":
            surface.blit(phraseLetter, (185 + 9, 100))
          else:
            surface.blit(phraseLetter, (185, 100))
          numclicks3 += 1
############################################################################################################
        if 240 <= x <= 290 and 95 <= y <= 145 and numclicks4 % 2 != 0:
          pygame.draw.rect(surface, (181, 159, 59), pygame.Rect(240, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[3].upper(), True, (255, 255, 255))
          if letterArray[3] == "i":
            surface.blit(phraseLetter, (250 + 9, 100))
          else:
            surface.blit(phraseLetter, (250, 100))
          numclicks4 += 1
        elif 240 <= x <= 290 and 95 <= y <= 145 and numclicks4 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(240, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[3].upper(), True, (255, 255, 255))
          if letterArray[3] == "i":
            surface.blit(phraseLetter, (250 + 9, 100))
          else:
            surface.blit(phraseLetter, (250, 100))
          numclicks4 += 1
############################################################################################################
        if 305 <= x <= 355 and 95 <= y <= 145 and numclicks5 % 2 != 0:
          pygame.draw.rect(surface, (181, 159, 59), pygame.Rect(305, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[4].upper(), True, (255, 255, 255))
          if letterArray[4] == "i":
            surface.blit(phraseLetter, (315 + 9, 100))
          else:
            surface.blit(phraseLetter, (315, 100))
          numclicks5 += 1
        elif 305 <= x <= 355 and 95 <= y <= 145 and numclicks5 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(305, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[4].upper(), True, (255, 255, 255))
          if letterArray[4] == "i":
            surface.blit(phraseLetter, (315 + 9, 100))
          else:
            surface.blit(phraseLetter, (315, 100))
          numclicks5 += 1
############################################################################################################
        if 125 <= x <= 275 and 190 <= y <= 240:
          if numclicks1 % 2 == 0:
            for word in wordList.copy():
              if word[0] == letterArray[0]:
                wordList.remove(word)
              times = 0
              for letter in word:
                if letter != letterArray[0]:
                  times += 1
                if times == 5:
                  wordList.remove(word)

          if numclicks2 % 2 == 0:
            for word in wordList.copy():
              if word[1] == letterArray[1]:
                wordList.remove(word)
              times = 0
              for letter in word:
                if letter != letterArray[1]:
                  times += 1
                if times == 5:
                  wordList.remove(word)

          if numclicks3 % 2 == 0:
            for word in wordList.copy():
              if word[2] == letterArray[2]:
                wordList.remove(word)
              times = 0
              for letter in word:
                if letter != letterArray[2]:
                  times += 1
                if times == 5:
                  wordList.remove(word)

          if numclicks4 % 2 == 0:
            for word in wordList.copy():
              if word[3] == letterArray[3]:
                wordList.remove(word)
              times = 0
              for letter in word:
                if letter != letterArray[3]:
                  times += 1
                if times == 5:
                  wordList.remove(word)

          if numclicks5 % 2 == 0:
            for word in wordList.copy():
              if word[4] == letterArray[4]:
                wordList.remove(word)
              times = 0
              for letter in word:
                if letter != letterArray[4]:
                  times += 1
                if times == 5:
                  wordList.remove(word)
          return letterArray, wordList
############################################################################################################

def findGrey(letterArray, wordList):
  surface = pygame.display.set_mode((400, 300))
  background_colour = (18,18,19)
  surface.fill(background_colour)
  letterFont = pygame.font.SysFont('radiocanada', 60)
  buttonFont = pygame.font.SysFont('radiocanada', 45)
  white = (255,255,255)
  pygame.draw.rect(surface, (130, 130, 145), pygame.Rect(20, 28, 360, 50), 0, 3)
  phraseGuess = buttonFont.render(("Click Grey Letters"), True, white)
  surface.blit(phraseGuess, (65, 40))
  x = 55
  for letter in letterArray:
    pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(x - 10, 100 - 5, 50, 50), 0, 3)
    phraseLetter = letterFont.render(letter.upper(), True, (255, 255, 255))
    if letter == "i":
      surface.blit(phraseLetter, (x + 9, 100))
    else:
      surface.blit(phraseLetter, (x, 100))
    x += 65
  doneFont = pygame.font.SysFont('radiocanada', 50)
  pygame.draw.rect(surface, (181, 159, 59), pygame.Rect(125, 190, 150, 50), 0, 3)
  phraseDone = doneFont.render("DONE", True, white)
  surface.blit(phraseDone, (150, 200))
  numclicks1 = 1
  numclicks2 = 1
  numclicks3 = 1
  numclicks4 = 1
  numclicks5 = 1
  while True:
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
############################################################################################################
        if 45 <= x <= 95 and 95 <= y <= 145 and numclicks1 % 2 != 0:
          pygame.draw.rect(surface, (130, 130, 145), pygame.Rect(45, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[0].upper(), True, (255, 255, 255))
          if letterArray[0] == "i":
            surface.blit(phraseLetter, (55 + 9, 100))
          else: 
            surface.blit(phraseLetter, (55, 100))
          numclicks1 += 1
        elif 45 <= x <= 95 and 95 <= y <= 145 and numclicks1 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(45, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[0].upper(), True, (255, 255, 255))
          if letterArray[0] == "i":
            surface.blit(phraseLetter, (55 + 9, 100))
          else:
            surface.blit(phraseLetter, (55, 100))
          numclicks1 += 1
############################################################################################################
        if 110 <= x <= 160 and 95 <= y <= 145 and numclicks2 % 2 != 0:
          pygame.draw.rect(surface, (130, 130, 145), pygame.Rect(110, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[1].upper(), True, (255, 255, 255))
          if letterArray[1] == "i":
            surface.blit(phraseLetter, (120 + 9, 100))
          else:
            surface.blit(phraseLetter, (120, 100))
          numclicks2 += 1
        elif 110 <= x <= 160 and 95 <= y <= 145 and numclicks2 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(110, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[1].upper(), True, (255, 255, 255))
          if letterArray[1] == "i":
            surface.blit(phraseLetter, (120 + 9, 100))
          else:
            surface.blit(phraseLetter, (120, 100))
          numclicks2 += 1
############################################################################################################
        if 175 <= x <= 225 and 95 <= y <= 145 and numclicks3 % 2 != 0:
          pygame.draw.rect(surface, (130, 130, 145), pygame.Rect(175, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[2].upper(), True, (255, 255, 255))
          if letterArray[2] == "i":
            surface.blit(phraseLetter, (185 + 9, 100))
          else:
            surface.blit(phraseLetter, (185, 100))
          numclicks3 += 1
        elif 175 <= x <= 225 and 95 <= y <= 145 and numclicks3 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(175, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[2].upper(), True, (255, 255, 255))
          if letterArray[2] == "i":
            surface.blit(phraseLetter, (185 + 9, 100))
          else:
            surface.blit(phraseLetter, (185, 100))
          numclicks3 += 1
############################################################################################################
        if 240 <= x <= 290 and 95 <= y <= 145 and numclicks4 % 2 != 0:
          pygame.draw.rect(surface, (130, 130, 145), pygame.Rect(240, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[3].upper(), True, (255, 255, 255))
          if letterArray[3] == "i":
            surface.blit(phraseLetter, (250 + 9, 100))
          else:
            surface.blit(phraseLetter, (250, 100))
          numclicks4 += 1
        elif 240 <= x <= 290 and 95 <= y <= 145 and numclicks4 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(240, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[3].upper(), True, (255, 255, 255))
          if letterArray[3] == "i":
            surface.blit(phraseLetter, (250 + 9, 100))
          else:
            surface.blit(phraseLetter, (250, 100))
          numclicks4 += 1
############################################################################################################
        if 305 <= x <= 355 and 95 <= y <= 145 and numclicks5 % 2 != 0:
          pygame.draw.rect(surface, (130, 130, 145), pygame.Rect(305, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[4].upper(), True, (255, 255, 255))
          if letterArray[4] == "i":
            surface.blit(phraseLetter, (315 + 9, 100))
          else:
            surface.blit(phraseLetter, (315, 100))
          numclicks5 += 1
        elif 305 <= x <= 355 and 95 <= y <= 145 and numclicks5 % 2 == 0:
          pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(305, 95, 50, 50), 0, 3)
          phraseLetter = letterFont.render(letterArray[4].upper(), True, (255, 255, 255))
          if letterArray[4] == "i":
            surface.blit(phraseLetter, (315 + 9, 100))
          else:
            surface.blit(phraseLetter, (315, 100))
          numclicks5 += 1
############################################################################################################
        if 125 <= x <= 275 and 190 <= y <= 240:
          if numclicks1 % 2 == 0:
            for word in wordList.copy():
              if letterArray[0] in word:
                wordList.remove(word)

          if numclicks2 % 2 == 0:
            for word in wordList.copy():
              if letterArray[1] in word:
                wordList.remove(word)

          if numclicks3 % 2 == 0:
            for word in wordList.copy():
              if letterArray[2] in word:
                wordList.remove(word)

          if numclicks4 % 2 == 0:
            for word in wordList.copy():
              if letterArray[3] in word:
                wordList.remove(word)

          if numclicks5 % 2 == 0:
            for word in wordList.copy():
              if letterArray[4] in word:
                wordList.remove(word)

          return wordList          
############################################################################################################

def printOptions(wordList):
  surface = pygame.display.set_mode((400, 700))
  background_colour = (18,18,19)
  surface.fill(background_colour)
  letterFont = pygame.font.SysFont('radiocanada', 25)
  buttonFont = pygame.font.SysFont('radiocanada', 50)
  messageFont = pygame.font.SysFont('radiocanada', 40)
  white = (255,255,255)
  intermediate = pygame.surface.Surface((400, 30000))
  clock = pygame.time.Clock()
  scroll_y = 0
  intermediate.fill (background_colour)
  for i in range(len(wordList)):
    phraseLetter = letterFont.render(wordList[i], True, (255, 255, 255))
    intermediate.blit(phraseLetter, (25 + (i % 5) * 75, 50 + (i // 5) * 25))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if event.button == 4: 
          scroll_y = min((scroll_y + 25), 0)
        if event.button == 5:
          scroll_y = max(scroll_y - 25, -((len(wordList) // 5) * 18))
        if 50 <= x <= 350 and 640 <= y <= 690:
          return
    surface.blit(intermediate, (0, 25 + scroll_y))

    pygame.draw.rect(surface, (44,45,45), pygame.Rect(0, 630, 400, 80), 0, 3)
    pygame.draw.rect(surface, (83, 141, 78), pygame.Rect(50, 640, 300, 50), 0, 3)
    phraseGuess = buttonFont.render(("Enter Next Word"), True, white)
    surface.blit(phraseGuess, (65, 650))
    
    pygame.draw.rect(surface, (44,45,45), pygame.Rect(0, 0, 400, 60), 0, 3)
    pygame.draw.rect(surface, (84, 85, 85), pygame.Rect(50, 10, 300, 40), 0, 3)
    phraseMessage = messageFont.render(("Remaining Words: "), True, white)
    surface.blit(phraseMessage, (73, 17))

    pygame.display.flip()
    clock.tick(60)

def playScreen():
  buttonFont = pygame.font.SysFont('radiocanada', 40)
  textFont = pygame.font.SysFont('radiocanada', 60)
  white = (255,255,255)
  background_colour = (18,18,19)
  surface = pygame.display.set_mode((400, 300))
  pygame.display.set_caption('Wordle Helper')
  surface.fill(background_colour)

  clock = pygame.time.Clock()
  text = ''
  i = 0
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          letters = []
          for letter in text:
            letters.append(letter)
          return letters
        elif event.key == pygame.K_BACKSPACE:
          text = text[:-1]
          if i > 25:
            i -= 25
        else:
          i += 25
          text += event.unicode

    surface.fill(background_colour)
    pygame.draw.rect(surface, (83, 141, 78), pygame.Rect(15, 33, 370, 50), 0, 3)
    phraseGuess = buttonFont.render(("Type Guess & Press Enter:"), True, white)
    surface.blit(phraseGuess, (20, 45))

    txt_surface = textFont.render(text.upper(), True, white)
    surface.blit(txt_surface, (125, 140))
    
    pygame.display.flip()
    clock.tick(30)

def buttonClicked():
  while True:
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        if 125 <= x <= 275 and 150 <= y <= 205:
          return
        
def main():
  wordList = wordBank.defaultWords
  drawStart()
  for i in range(6):
    if i == 0:
      buttonClicked()
    letterArray = playScreen()
    letterArray, wordList = findGreen(letterArray, wordList)
    letterArray, wordList = findYellow(letterArray, wordList)
    wordList = findGrey(letterArray, wordList)
    printOptions(wordList)
    i += 1
      
if __name__=="__main__":
  main()



