import sys
import pygame
import time
import random
import os
import Questions

study_questions = Questions()

doBeginning = True
doTrials = True
doEmotions = True
doNumerical = True
doDemographics = True
doReligion = True
doSpir1 = True
doSpir2 = True
doPers = True

class Participant:
    def __init__(self):
        self.condition = 0
        self.conditions = ['not set', 'not set']
        self.pics = []
        self.order = []
        self.times = []
        self.ID = 0

participant = Participant()

class Pics:
    def __init__(self):
        self.path = os.getcwd()
        #path = os.path.abspath(os.path.dirname(__file__))
        

        self.high_rel_pics = []
        for x in range(0,6):
            self.high_rel_pics.append(pygame.image.load(self.path + '\\High Awe Religious\\' + str(x+1) + '.jpg'))

        self.low_rel_pics = []
        for x in range(0,6):
            self.low_rel_pics.append(pygame.image.load(self.path + '\\Low Awe Religious\\' + str(x+1) + '.jpg'))

        self.high_non_pics = []
        for x in range(0,6):
            self.high_non_pics.append(pygame.image.load(self.path + '\\High Awe Non\\' + str(x+1) + '.jpg'))

        self.low_non_pics = []
        for x in range(0,6):
            self.low_non_pics.append(pygame.image.load(self.path + '\\Low Awe Non\\' + str(x+1) + '.jpg'))

        self.timeInstructions = pygame.image.load(self.path + '\\timeInstructions.bmp')
        self.timeConclusion = pygame.image.load(self.path + '\\timeConclusion.bmp')
        self.afterpractice = pygame.image.load(self.path + '\\afterpractice.bmp')

        self.numerical = []
        self.numerical.append(pygame.image.load(self.path + '\\slides\\1hints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\2nohints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\3hints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\4nohints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\5hints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\6nohints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\7hints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\8nohints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\9hints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\10nohints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\11hints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\12nohints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\13hints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\14nohints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\15hints.bmp'))
        self.numerical.append(pygame.image.load(self.path + '\\slides\\16nohints.bmp'))

        self.numInstructions = pygame.image.load(self.path + '\\slides\\instructions.bmp')
        self.numIndication = pygame.image.load(self.path + '\\slides\\indication.bmp')
        self.numConclusion = pygame.image.load(self.path + '\\slides\\conclusion.bmp')

pics = Pics()

class Timer:
    def __init__(self):

        self.set = 0
        self.elapsed = 0


timer = Timer()

class MenuButton:
    def __init__(self, pos, text):
        self.pos = pos
        self.text = text

        self.status = 'unclicked'
        
    def checkHover(self,mousePos):

        if mousePos[0] >= self.pos[0] and mousePos[0] <= self.pos[0] + 100 and mousePos[1]>=self.pos[1] and mousePos[1] <= self.pos[1] + 50:
            if self.status == 'unclicked':
                self.status = 'hover'
        elif self.status == 'hover':
            self.status = 'unclicked'
            

    def checkClick(self,leftClick):
        self.newClick = False
        if self.status == 'hover' and leftClick == True:
            self.status = 'clicked'
            self.newClick = True

    def blit(self):

        #sys.stdout.write(self.status)
        #sys.stdout.flush()

        pos = self.pos

        if self.status == 'unclicked':
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]],[pos[0]+100,pos[1]],2)
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]],[pos[0],pos[1]+50],2)
            pygame.draw.line(screen,[0,0,0],[pos[0]+100,pos[1]],[pos[0]+100,pos[1]+50],2)
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]+50],[pos[0]+100,pos[1]+50],2)

        else:
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]],[pos[0]+100,pos[1]],15)
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]],[pos[0],pos[1]+50],15)
            pygame.draw.line(screen,[0,0,0],[pos[0]+100,pos[1]],[pos[0]+100,pos[1]+50],15)
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]+50],[pos[0]+100,pos[1]+50],15)
            
        survText = font.render(self.text, 0, (0,0,0), (255,255,255))
        screen.blit(survText,[self.pos[0] + 10, self.pos[1] + 15]) 


class ContinueButton:
    def __init__(self,pos):

        self.pos = pos

        self.status = 'unclicked'

    def checkHover(self,mousePos):

        if mousePos[0] >= self.pos[0] and mousePos[0] <= self.pos[0] + 100 and mousePos[1]>=self.pos[1] and mousePos[1] <= self.pos[1] + 50:
            self.status = 'hover'
        else:
            self.status = 'unclicked'

    def checkClick(self,leftClick):

        if self.status == 'hover' and leftClick == True:
            self.status = 'clicked'

    def blit(self):

        pos = self.pos

        if self.status == 'unclicked':
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]],[pos[0]+100,pos[1]],10)
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]],[pos[0],pos[1]+50],10)
            pygame.draw.line(screen,[0,0,0],[pos[0]+100,pos[1]],[pos[0]+100,pos[1]+50],10)
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]+50],[pos[0]+100,pos[1]+50],10)

        else:
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]],[pos[0]+100,pos[1]],15)
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]],[pos[0],pos[1]+50],15)
            pygame.draw.line(screen,[0,0,0],[pos[0]+100,pos[1]],[pos[0]+100,pos[1]+50],15)
            pygame.draw.line(screen,[0,0,0],[pos[0],pos[1]+50],[pos[0]+100,pos[1]+50],15)
            
        survText = font.render('Continue', 0, (0,0,0), (255,255,255))
        screen.blit(survText,[self.pos[0] + 10, self.pos[1] + 15]) 
        
    

class Button:
    def __init__(self, questionID, pos):

        self.pos = pos
        self.questionID = questionID

        self.hoverButton = pygame.image.load(pics.path + '\\hoverButton.bmp')
        self.unclickedButton = pygame.image.load(pics.path + '\\unclickedButton.bmp')
        self.clickedButton = pygame.image.load(pics.path + '\\clickedButton.bmp')

        self.status = 'unclicked'
        self.current = self.unclickedButton
        self.newClick = False

    def checkHover(self, mousePos):

        if mousePos[0] >= self.pos[0] and mousePos[0] <= self.pos[0] + 20 and mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + 20:
            if self.status == 'unclicked':
                self.status = 'hover'
                self.current = self.hoverButton
        elif self.status == 'hover':
            self.status = 'unclicked'
            self.current = self.unclickedButton

    def checkClick(self, leftClick):
        self.newClick = False
        if self.status == 'hover' and leftClick == True:
            self.status = 'clicked'
            self.current = self.clickedButton
            self.newClick = True

    def blit(self):

        screen.blit(self.current,self.pos)

        

class ButtonRow:

    def __init__(self, num, ypos, questionID):
        self.num = num
        self.questionID = questionID
        self.buttons = []

        
        if self.num == 1:
            rowLength = 20
            spacing = 20
        else:
            rowLength = 269.6
            spacing = (rowLength - 20)/(self.num - 1)
        
        self.startX = (1250 - rowLength)/2.0


        for x in range(0,num):
            self.buttons.append(Button(questionID,[self.startX + spacing*x,ypos]))

    def displayRow(self):
        for x in range(0,self.num):
            self.buttons[x].checkHover(pos)
            self.buttons[x].checkClick(leftDown)
            if self.buttons[x].newClick == True:
                for y in range(0,self.num):
                    self.buttons[y].status = 'unclicked'
                    self.buttons[y].current = self.buttons[y].unclickedButton
                self.buttons[x].status = 'clicked'
                self.buttons[x].current = self.buttons[x].clickedButton
            self.buttons[x].blit()

    def getAnswers(self):

        ans = 0

        for x in range(0,self.num):
            if self.buttons[x].status == 'clicked':
                ans = x + 1

        return str(ans)

class ButtonCol:

    def __init__(self, num, xpos, ypos, questionID):
        self.num = num
        self.questionID = questionID
        self.buttons = []
        for x in range(0,num):
            self.buttons.append(Button(questionID,[xpos,ypos + 30*x]))

    def displayCol(self):
        for x in range(0,self.num):
            self.buttons[x].checkHover(pos)
            self.buttons[x].checkClick(leftDown)
            if self.buttons[x].newClick == True:
                for y in range(0,self.num):
                    self.buttons[y].status = 'unclicked'
                    self.buttons[y].current = self.buttons[y].unclickedButton
                self.buttons[x].status = 'clicked'
                self.buttons[x].current = self.buttons[x].clickedButton
            self.buttons[x].blit()

    def getAnswers(self):

        ans = -1

        for x in range(0,self.num):
            if self.buttons[x].status == 'clicked':
                ans = x

        return ans

class TextBox:
    def __init__(self,greyText,xpos,ypos,width, fontType):
        self.greyText = greyText
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.font = fontType

        self.text = ''
        self.status = 'unclicked'
        self.focus = False
        self.lineTime = 0
        self.showLine = False
        self.cursorPos = 0 #index of character after line

        if self.font == 'small':
            self.letterLength = 12
        elif self.font == 'big':
            self.letterLength = 17

    def updateText(self, key, keyPressed, leftDown, mousePos):
        
        changeFocus = False

        if self.text == '':
            self.cursorPos = 0

        if self.status == 'unclicked':
            self.focus = False
        if self.focus and keyPressed:
            
            if key == pygame.K_BACKSPACE:
                if not (self.text == ''):
                    self.text = self.text[0:self.cursorPos-1] + self.text[self.cursorPos:]
                    self.cursorPos-=1
            elif key == pygame.K_LEFT:
                if self.cursorPos > 0:
                    self.cursorPos -= 1
            elif key == pygame.K_RIGHT:
                if self.cursorPos < len(self.text):
                    self.cursorPos += 1
            else:
                self.cursorPos+=1
                if key >= 256:
                    character = chr(key - 208)
                else:
                    character = chr(key)
                self.text = self.text[0:self.cursorPos-1] + str(character) + self.text[self.cursorPos-1:]

        elif self.status == 'unclicked':
            self.text = ''

        if leftDown:

            boxLength = len(self.text)*self.letterLength
            if mousePos[1] < self.ypos and mousePos[1] > self.ypos - 20 and mousePos[0] > self.xpos and mousePos[0] < self.xpos + boxLength + 100:
                self.focus = True

                changeFocus = True
                self.cursorPos = (mousePos[0]-self.xpos)//self.letterLength ##integer division, ie a = bc + d, then a//b = c
                if self.cursorPos >= len(self.text):
                    self.cursorPos = len(self.text)

                sys.stdout.write(str(self.cursorPos)+'\n')

        return changeFocus

    def blit(self):

        #sys.stdout.write(str(self.ypos) + '\t' + self.status + '\t' + str(self.focus) + '\n')


        if self.font == 'small':
         if self.status == 'unclicked':
            screen.blit(smallfont.render(self.greyText, 0, (175,175,175), (255,255,255)),[self.xpos,self.ypos-20])
         elif self.status == 'clicked' or self.focus:
            screen.blit(monofont.render(self.text, 0, (0,0,0), (255,255,255)),[self.xpos,self.ypos-20])
        elif self.font == 'big':
         if self.status == 'unclicked':
            screen.blit(bigfont.render(self.greyText, 0, (175,175,175), (255,255,255)),[self.xpos,self.ypos-25])
         elif self.status == 'clicked' or self.focus:
            screen.blit(bigmonofont.render(self.text, 0, (0,0,0), (255,255,255)),[self.xpos,self.ypos-25])

        #underline
        pygame.draw.line(screen,[0,0,0],[self.xpos,self.ypos],[self.xpos + self.width ,self.ypos],1)

        boxLength = len(self.text)*self.letterLength

        #overline
        #pygame.draw.line(screen, [0,0,0], [self.xpos, self.ypos - 20], [self.xpos + boxLength, self.ypos - 20],1)

        if self.focus:
            #pygame.draw.line(screen, [0,0,0], [(self.xpos + self.cursorPos*self.letterLength), self.ypos -20], [(self.xpos + self.cursorPos*self.letterLength), self.ypos],1)

            elapsed = time.time() - self.lineTime

            if elapsed < 0.5:
                pygame.draw.line(screen, [0,0,0], [(self.xpos + self.cursorPos*self.letterLength), self.ypos -20], [(self.xpos + self.cursorPos*self.letterLength), self.ypos-1],1)
            elif elapsed > 1:
                self.lineTime = time.time()
            else:
                pygame.draw.line(screen, [255,255,255], [(self.xpos + self.cursorPos*self.letterLength), self.ypos -20], [(self.xpos + self.cursorPos*self.letterLength), self.ypos-1],1)

                
class SurveyAnswers:
    def __init__(self):
        self.answers = []


surveyAnswers = SurveyAnswers()

surveyTitles = ['Emotion Survey', 'Demographics', 'Religiousness Survey', 'Spirituality Survey Pt1', 'Spirituality Survey Pt2', 'Personality Survey']
answerHeadings = [['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8'], ['D1', 'D2', 'D3', 'D4'], ['R1', 'R2'], ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'],
                ['S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15'], ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']]


def writeSurveyData(num):
    surveyData.write(surveyTitles[num] + '\n')
    for y in range(0,len(surveyAnswers.answers[num])):
        surveyData.write(answerHeadings[num][y] + '\t' + surveyAnswers.answers[num][y] + '\n')
    surveyData.write('\n')

    for y in range(0,len(surveyAnswers.answers[num])):
        surveyData2.write(answerHeadings[num][y] + '\t' + surveyAnswers.answers[num][y] + '\n')

def onExit():
    sys.exit()



#READ ORDER AND TIME FILE

def readOrderTime(section):

    if section == 1:
        ordertimeFile = open('time-estimation task.txt', 'r')
    else:
        ordertimeFile = open('time-estimation task (101-132).txt', 'r')

    lines = ordertimeFile.readlines()


    linesArray = []
    for line in lines[1:]:
        line = line.split()
        for x in range(0, len(line)):
            line[x] = int(line[x])
        linesArray.append(line)




    orderTimesConditionsConfiguration = [] # [list of ints length 6, list of ints length 10, int, int]
    count = 0
    orders = []
    times = []
    configuration = 0
    condition = 0


    for line in linesArray:
        times.append(line[4])

        configuration = line[1]
        condition = line[2]

        if count != 0 and count != 1 and count != 8 and count != 9:
            orders.append(line[5])

        count += 1

        if count == 10:
            orderTimesConditionsConfiguration.append([orders, times, condition, configuration])
            orders = []
            times = []
            count = 0

    if section == 1:
        return orderTimesConditionsConfiguration
    else:
        templist = []
        for x in range(0,100):
            templist.append(x)
        return templist + orderTimesConditionsConfiguration

pygame.init()

screen = pygame.display.set_mode([1250,850], pygame.FULLSCREEN)

#Beginning Screen


lowButton = MenuButton([100,100],'low')
highButton = MenuButton([300,100],'high')
nonrelButton = MenuButton([100,300],'non')
relButton = MenuButton([300,300],'rel')
randomButton = MenuButton([600,600], 'random')

font = pygame.font.SysFont('timesnewroman',20)
smallfont = pygame.font.SysFont('timesnewroman', 18)
monofont = pygame.font.SysFont('monospace', 20)
bigfont = pygame.font.SysFont('timesnewroman', 28)
bigmonofont = pygame.font.SysFont('monospace', 28)

contButton = ContinueButton([575,400])
askPartNum = TextBox('', 830, 275, 200, 'small')
askPartID = TextBox('', 533, 270, 200, 'small')

exists = False
notext = False
notANum = False
while doBeginning:


    leftDown = False
    key = 0
    keyDown = False

    pos = pygame.mouse.get_pos()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            wait = 0
            onExit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                onExit
            else:
                key = event.key
                keyDown = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            leftDown = True
            
    screen.fill([255,255,255])
    # lowButton.checkHover(pos)
    # lowButton.checkClick(leftDown)
    
    
    # highButton.checkHover(pos)
    # highButton.checkClick(leftDown)
    
    
    # nonrelButton.checkHover(pos)
    # nonrelButton.checkClick(leftDown)
    
    
    # relButton.checkHover(pos)
    # relButton.checkClick(leftDown)

    # if lowButton.newClick == True:
    #     highButton.status = 'unclicked'
    #     sys.stdout.write('here')
    #     sys.stdout.flush()
    # if highButton.newClick == True:
    #     lowButton.status = 'unclicked'

    # if relButton.newClick == True:
    #     nonrelButton.status = 'unclicked'
    # if nonrelButton.newClick == True:
    #     relButton.status = 'unclicked'
        
    
    # randomButton.checkHover(pos)
    # randomButton.checkClick(leftDown)

    # if randomButton.newClick == True:
    #     randomButton.status = 'unclicked'
    #     aweType = random.randint(0,1)

    #     if aweType == 0:
    #         highButton.status = 'unclicked'
    #         lowButton.status = 'clicked'
    #     else:
    #         lowButton.status = 'unclicked'
    #         highButton.status = 'clicked'

    #     relType = random.randint(0,1)
    #     if relType == 0:
    #         relButton.status = 'clicked'
    #         nonrelButton.status = 'unclicked'
    #     else:
    #         relButton.status = 'unclicked'
    #         nonrelButton.status = 'clicked'
    
    #lowButton.blit()
    #highButton.blit()
    #nonrelButton.blit()
    #relButton.blit()
    #randomButton.blit()

    contButton.checkHover(pos)
    contButton.checkClick(leftDown)
    contButton.blit()

    askPartNum.status = 'clicked'
    askPartID.status = 'clicked'


    # changeFocusNum = askPartNum.updateText(key, keyDown, leftDown, pos)
    # changeFocusID = askPartID.updateText(key, keyDown, leftDown, pos)

    # if changeFocusNum:
    #     askPartNum.focus = True
    #     askPartID.focus = False

    # if changeFocusID:
    #     askPartNum.focus = False
    #     askPartID.focus = True 


    # askPartNum.blit()
    askPartID.status = 'clicked'
    askPartID.focus = True
    askPartID.updateText(key, keyDown, leftDown, pos)
    askPartID.blit()




    if contButton.status == 'clicked':
        ID = askPartID.text

        try:
            if ID != '':
                int(ID)
                notANum = False        
        except:
            notANum = True
            notext = False
            exists = False

        if ID == '':
            notext = True
            exists = False
        elif notANum != True:
            notext = False
            if os.path.exists(pics.path + '\\Data\\Participant ' + ID):
                exists = True
                contButton.status == 'unclicked'
            else:
                os.mkdir('Data\\Participant ' + ID)
                doBeginning = False


    if exists:
        screen.blit(font.render('Participant ' + ID + ' exists already', 0, (0,0,0),(255,255,255)),[525,500])
    elif notext:
        screen.blit(font.render('No participant selected', 0, (0,0,0),(255,255,255)),[525,500])
    elif notANum:
        screen.blit(font.render('Participant must be a number!', 0, (0,0,0),(255,255,255)),[525,500])
    

    #screen.blit(font.render('Pick Conditions', 0, (0,0,0), (255,255,255)),[150,20])
    screen.blit(font.render('Enter participant ID: ', 0, (0,0,0), (255,255,255)), [360, 250])
    pygame.display.flip()

participant.ID = int(askPartID.text)
if participant.ID < 100:
    orderTimesConditionsConfiguration = readOrderTime(1)
else:
    orderTimesConditionsConfiguration = readOrderTime(2)

participant.condition = orderTimesConditionsConfiguration[participant.ID -1][2]
participant.configuration = orderTimesConditionsConfiguration[participant.ID -1][3]

participant.conditions = []

if participant.condition == 1:
    participant.conditions = ['High', 'Religious']
    participant.pics = pics.high_rel_pics
elif participant.condition == 2:
    participant.conditions = ['High', 'Non-Religious']
    participant.pics = pics.high_non_pics
elif participant.condition == 3:
    participant.conditions = ['Low', 'Religious']
    participant.pics = pics.low_rel_pics
elif participant.condition == 4:
    participant.conditions = ['Low', 'Non-Religious']
    participant.pics = pics.low_non_pics


participant.order = orderTimesConditionsConfiguration[participant.ID - 1][0]
participant.times = orderTimesConditionsConfiguration[participant.ID - 1][1]
surveyData = open('Data\\Participant ' + str(participant.ID) + '\\Participant ' + str(participant.ID) + ' survey data.txt', 'w')
surveyData.write('Participant\tAwe\tPrime\n')
surveyData.write(str(participant.ID) + '\t' + participant.conditions[0] + '\t' + participant.conditions[1] + '\n')
surveyData2 = open('Data\\Participant ' + str(participant.ID) + '\\Participant ' + str(participant.ID) + ' survey data2.txt', 'w')
surveyData2.write('Participant\t' + str(participant.ID) + '\nAwe\t' + participant.conditions[0] + '\nPrime\t' + participant.conditions[1] + '\n')


#TRIALS

def runTrial(pic, showTime):

    hit = False

    #cross

    startTime = time.time()
    elapsed = 0
    screen.fill([255,255,255])
    pygame.draw.line(screen,[0,0,0],[575,425],[675,425],3)
    pygame.draw.line(screen,[0,0,0],[625,375],[625,475],3)
    pygame.display.flip()
    while elapsed <= 0.5:
        elapsed = time.time()- startTime

    #white
    startTime = time.time()
    elapsed = 0
    screen.fill([255,255,255])
    pygame.display.flip()
    while elapsed <= 1.5:
        elapsed = time.time() - startTime

    #pic
    startTime = time.time()
    elapsed = 0
    screen.fill([255,255,255])
    if pic == 0 or pic == 1 or pic == 8 or pic == 9:
        pygame.draw.rect(screen,[50,50,50], [25,25,1200,800], 0)
        pygame.draw.line(screen, [0,0,0],[50,50],[1200,800], 10)
        pygame.draw.line(screen, [0,0,0],[50,800],[1200,50], 10)
    else:
        print pic
        screen.blit(participant.pics[participant.order[pic-2] - 1], (25,25))
    pygame.display.flip()
    while elapsed <= showTime:       
        elapsed = time.time() - startTime

    #cross
    #clear event queue
    pygame.event.get()
    reactionTime = 'None'
    startTime = time.time()
    beginReaction = startTime
    elapsed = 0
    screen.fill([255,255,255])
    pygame.draw.line(screen,[0,0,0],[575,425],[675,425],3)
    pygame.draw.line(screen,[0,0,0],[625,375],[625,475],3)
    pygame.display.flip()
    while elapsed <= 0.5:       
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                onExit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                reactionTime = time.time() - beginReaction
                hit = True
        elapsed = time.time() - startTime

    #white
    startTime = time.time()
    elapsed = 0
    screen.fill([255,255,255])
    pygame.display.flip()
    while elapsed <= 1.5:
        if not hit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    onExit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    reactionTime = time.time() - beginReaction
                    hit = True
        elapsed = time.time() - startTime

    #outline
    startTime = time.time()
    wait = True
    pygame.draw.rect(screen,[50,50,50], [25,25,1200,800], 0)
    pygame.display.flip()
    pygame.event.get()
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                onExit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                hitTime = time.time() - startTime
                wait = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                onExit()
    
    return reactionTime, hitTime


#instructions/practice
pygame.mouse.set_visible(False)
if doTrials:
    doInstructions = True

    leftDown = False
    screen.fill([255,255,255])

    while doInstructions:

       for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            doInstructions = False
            onExit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            doInstructions = False

       screen.blit(pics.timeInstructions,(145,65))
       pygame.display.flip()

    doInstructions = True
    while doInstructions:
        r, h = runTrial(0,1.5)
        ask = True

        while ask:
            screen.fill([255,255,255])

            #screen.blit(font.render('Reaction time: ' + str(r) + '          Hit time: ' + str(h), 0, (0,0,0), (255,255,255)), (400, 300))

            screen.blit(pics.afterpractice,(145,65))

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    ask = False
                    onExit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                    ask = False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                    ask = False
                    doInstructions = False

            pygame.display.flip()


#real Trials                   
if doTrials:

    timeEstFile = open(pics.path + '\\Data\\Participant ' + str(participant.ID) + '\\Participant ' + str(participant.ID) + ' time estimation.txt', 'w')
    timeEstFile.write('Participant\tAwe\tPrime\tConfiguration\n')
    timeEstFile.write(str(participant.ID) + '\t' + participant.conditions[0] + '\t' + participant.conditions[1] + '\t' + str(participant.configuration) + '\n')
    timeEstFile.write('Trial\tPic ID\tDisplay Time\tReaction\tGuess\n')

    for x in range(0,10):

        showTime = participant.times[x]

        rT,hT = runTrial(x,showTime)

        if x == 0 or x == 1 or x == 8 or x == 9:
            picID = '0'
        else:
            picID = str(participant.order[x-2])

        timeEstFile.write(str(x+1) + '\t' + picID + '\t' + str(showTime) + '\t' + str(rT) + '\t' + str(hT) + '\n')


    doConc = True

    while doConc:


       for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            doConc = False
            onExit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            doConc = False


       screen.blit(pics.timeConclusion, (145,65))


       pygame.display.flip()



    

#Emotion Survey
                

emotions = ['Angry', 'Awe', 'Sad', 'Happy', 'Calm', 'Bored', 'Excited', 'Afraid']


questions = []

for x in range(0,8):
    questions.append(ButtonRow(7,100 + 100*x,emotions[x]))

contButton = ContinueButton([1000,700])

pygame.mouse.set_visible(True)

while doEmotions:

    leftDown = False

    pos = pygame.mouse.get_pos()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            doEmotions = False
            onExit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            leftDown = True

        
            
    screen.fill([255,255,255])

    text = font.render('Please rate the extent to which you currently feel each of the emotions below.',0,(0,0,0),(255,255,255))
    screen.blit(text, (150,20))

    for x in range(0,len(emotions)):

        startX = questions[x].startX
        
        text = font.render(emotions[x], 0, (0,0,0), (255,255,255))
        
        screen.blit(text, (startX - 50,70 + 100*x))

        notatall = smallfont.render('not at all', 0, (0,0,0), (255,255,255))
        screen.blit(notatall, (startX - 25,130 + 100*x))

        verymuch = smallfont.render('very much', 0, (0,0,0), (255,255,255))
        screen.blit(verymuch, (startX + 225,130 + 100*x))        
        #sys.stdout.write(emotions[x] + "\n")
        #sys.stdout.flush()



    for question in questions:
        question.displayRow()
            

    contButton.checkHover(pos)
    contButton.checkClick(leftDown)
    contButton.blit()

    if contButton.status == 'clicked':
        doEmotions = False
        ans = []
        for question in questions:
            ans.append(question.getAnswers())

        surveyAnswers.answers.append(ans)
        writeSurveyData(len(surveyAnswers.answers)-1)
    
    pygame.display.flip()



#Numerical estimation

def numEst(slide):
    screen.fill([255,255,255])

    pygame.mouse.set_visible(False)

    startTime = time.time()
    elapsed = 0
    while elapsed <= 4:
        screen.blit(slide, (145,65))
        pygame.display.flip()
        elapsed = time.time() - startTime

    screen.fill([255,255,255])
    pygame.display.flip()
    guess = ''
    wait = True
    pygame.event.clear()

    textbox = TextBox('', 525,400,200, 'big')

    pygame.mouse.set_visible(True)

    while wait:
        keyDown = False
        leftDown = False
        key = 0

        screen.fill([255,255,255])
        screen.blit(pics.numIndication,(145,65))

        textbox.status = 'clicked'
        textbox.focus = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                wait = False
                onExit()

            elif event.type == pygame.KEYDOWN:
                key = event.key
                keyDown = True
                if event.key == pygame.K_SPACE:
                    wait = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                leftDown = True


        if wait:
            textbox.updateText(key, keyDown, leftDown, pygame.mouse.get_pos())
            textbox.blit()

        pygame.display.flip()

    return textbox.text

if doNumerical:
    doInstructions = True

    screen.fill([255,255,255])

    while doInstructions:


       for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            doInstructions = False
            onExit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            doInstructions = False


       screen.blit(pics.numInstructions, (145,65))


       pygame.display.flip()

if doNumerical == True:

    numEstFile = open('Data\\Participant ' + str(participant.ID) + '\\Participant ' + str(participant.ID) + ' numerical estimation.txt', 'w')
    numEstFile.write('Participant\tAwe\tPrime\n')
    numEstFile.write(str(participant.ID) + '\t' + participant.conditions[0] + '\t' + participant.conditions[1] + '\n')
    numEstFile.write('Trial\tGuess\n')

    count = 0
    for pic in pics.numerical:

        count += 1

        guess = numEst(pic)
        numEstFile.write(str(count) + '\t' + str(guess) + '\n')


        doInstructions = True

    screen.fill([255,255,255])

    doConc = True

    while doConc:


       for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            doConc = False
            onExit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            doConc = False


       screen.blit(pics.numConclusion, (145,65))


       pygame.display.flip()



#Demographics
cols = []

buttonPos = 400

cols.append(ButtonCol(3,buttonPos,80,'Gender'))
cols.append(ButtonCol(8,buttonPos,200,'Race'))
cols.append(ButtonCol(8,buttonPos,470,'Religion'))
cols.append(ButtonCol(2,buttonPos,750,'Citizenship'))

contButton = ContinueButton([1000,700])

textBoxes = []
textBoxes.append(TextBox('Specify or leave blank', buttonPos + 100,160,200, 'small'))
textBoxes.append(TextBox('Specify or leave blank', buttonPos + 100,430,200, 'small'))
textBoxes.append(TextBox('Specify or leave blank', buttonPos + 100,700,200, 'small'))

while doDemographics:

    leftDown = False
    keyDown = False
    key = 0

    pos = pygame.mouse.get_pos()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            onExit()
            doDemographics = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            leftDown = True
        elif event.type == pygame.KEYDOWN:
            keyDown = True
            key = event.key
                
    screen.fill([255,255,255])
    text = font.render('Please complete the following:',0,(0,0,0),(255,255,255))
    screen.blit(text,(150,20))

    choices = []
    screen.blit(font.render('Gender:',0,(0,0,0),(255,255,255)),(70,80))

    choices.append(['Male', 'Female', 'Other'])

    for x in range(0,len(choices[0])):
        screen.blit(font.render(choices[0][x],0,(0,0,0),(255,255,255)),(buttonPos + 30, 80+30*x))
    

    screen.blit(font.render('Race:',0,(0,0,0),(255,255,255)),(70,200))
    choices.append(['Non-Hispanic White', 'Hispanic', 'Black', 'Asian (East, South & Southeast)',
                    'American Indian/Alaska Native', 'Middle Eastern', 'More than one race',
                    'Other'])
    for x in range(0, len(choices[1])):
        screen.blit(font.render(choices[1][x],0,(0,0,0),(255,255,255)),(buttonPos + 30, 200 + 30*x))


    screen.blit(font.render('What is your religious affiliation?',0,(0,0,0),(255,255,255)),(70,470))
    choices.append(['Protestant Catholic', 'Roman Catholic', 'Evangelical Christian', 'Jewish',
                    'Muslim', 'Hindu', 'Buddhist', 'Other'])
    for x in range(0,len(choices[2])):
        screen.blit(font.render(choices[2][x],0,(0,0,0),(255,255,255)),(buttonPos + 30, 470 + 30*x))

    
    screen.blit(font.render('Were you born in Canada?',0,(0,0,0),(255,255,255)),(70,750))

    choices.append(['Yes', 'No'])
    for x in range(0,len(choices[3])):
        screen.blit(font.render(choices[3][x],0,(0,0,0),(255,255,255)),(buttonPos + 30, 750 + 30*x))

    screen.blit(font.render('Yes', 0, (0,0,0), (255,255,255)), (buttonPos + 30, 750))
    screen.blit(font.render('No', 0, (0,0,0), (255,255,255)), (buttonPos + 30, 780))

    for col in cols:
        col.displayCol()

    if cols[0].buttons[2].newClick:
        textBoxes[0].focus = True
        textBoxes[1].focus = False
        textBoxes[2].focus = False
    
    if cols[0].buttons[2].status != 'hover':
        textBoxes[0].status = cols[0].buttons[2].status

    if cols[1].buttons[7].newClick:
        textBoxes[0].focus = False
        textBoxes[1].focus = True
        textBoxes[2].focus = False

    if cols[1].buttons[7].status != 'hover':
        textBoxes[1].status = cols[1].buttons[7].status

    if cols[2].buttons[7].newClick:
        textBoxes[0].focus = False
        textBoxes[1].focus = False
        textBoxes[2].focus = True
    
    if cols[2].buttons[7].status != 'hover':
        textBoxes[2].status = cols[2].buttons[7].status


    for box in textBoxes:
        changeFocus = box.updateText(key, keyDown, leftDown, pos)

        if changeFocus:
            for bbox in textBoxes:
                bbox.focus = False

            box.focus = True
        
        
    for box in textBoxes:
        box.blit()

    contButton.checkHover(pos)
    contButton.checkClick(leftDown)
    contButton.blit()

    if contButton.status == 'clicked':
        doDemographics = False
        ans = []
        counter = 0
        for col in cols:
            num = col.getAnswers()
            if num == -1:
                ans.append('0')
            else:
                if counter < 3:
                    if num == col.num - 1:
                        if textBoxes[counter].text == '':
                            ans.append('Other: unspecified')
                        else:
                            ans.append('Other: ' + textBoxes[counter].text)
                    else:
                        ans.append(choices[counter][num])
                else:
                    ans.append(choices[counter][num])
                            
            counter += 1

        surveyAnswers.answers.append(ans)
        writeSurveyData(len(surveyAnswers.answers)-1)
    
    pygame.display.flip()
        


#religiousness
questions = study_questions.religiousness


rows = []

for x in range(0,len(questions)):
    rows.append(ButtonRow(7,100 + 100*x,questions[x]))

contButton = ContinueButton([1000,700])


while doReligion:

    leftDown = False

    pos = pygame.mouse.get_pos()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            onEXit()
            doReligion = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            leftDown = True

        
            
    screen.fill([255,255,255])

    text = font.render('Please rate the extent to which you agree with each statement below.',0,(0,0,0),(255,255,255))
    screen.blit(text, (150,20))

    for x in range(0,len(questions)):
        
        startX = rows[x].startX
        text = font.render(questions[x], 0, (0,0,0), (255,255,255))
        
        screen.blit(text, (250,70 + 100*x))

        notatall = smallfont.render('not at all', 0, (0,0,0), (255,255,255))
        screen.blit(notatall, (startX - 25,130 + 100*x))

        verymuch = smallfont.render('very much', 0, (0,0,0), (255,255,255))
        screen.blit(verymuch, (startX + 225,130 + 100*x))



    for row in rows:
        row.displayRow()
            

    contButton.checkHover(pos)
    contButton.checkClick(leftDown)
    contButton.blit()

    if contButton.status == 'clicked':
        doReligion = False
        ans = []
        for row in rows:
            ans.append(row.getAnswers())

        surveyAnswers.answers.append(ans)
        writeSurveyData(len(surveyAnswers.answers)-1)

    
    pygame.display.flip()


#Spirituality Pt1

questions = study_questions.spir1


rows = []

for x in range(0,len(questions)):
    rows.append(ButtonRow(7,100 + 100*x,questions[x]))

contButton = ContinueButton([1000,700])


while doSpir1:

    leftDown = False

    pos = pygame.mouse.get_pos()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            onExit()
            doSpir1= False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            leftDown = True

        
            
    screen.fill([255,255,255])

    text = font.render('Please rate the extent to which you agree with each statement below.',0,(0,0,0),(255,255,255))
    screen.blit(text, (150,20))

    for x in range(0,len(questions)):

        startX = rows[x].startX
        
        text = font.render(questions[x], 0, (0,0,0), (255,255,255))
        
        screen.blit(text, (250,70 + 100*x))

        notatall = smallfont.render('not at all', 0, (0,0,0), (255,255,255))
        screen.blit(notatall, (startX - 25,130 + 100*x))

        verymuch = smallfont.render('very much', 0, (0,0,0), (255,255,255))
        screen.blit(verymuch, (startX + 225,130 + 100*x))



    for row in rows:
        row.displayRow()
            

    contButton.checkHover(pos)
    contButton.checkClick(leftDown)
    contButton.blit()

    if contButton.status == 'clicked':
        doSpir1 = False
        ans = []
        for row in rows:
            print "here"
            ans.append(row.getAnswers())

        surveyAnswers.answers.append(ans)
        writeSurveyData(len(surveyAnswers.answers)-1)

    
    pygame.display.flip()

#Spirituality Pt2

questions = study_questions.spir2


rows = []

for x in range(0,len(questions)):
    rows.append(ButtonRow(7,100 + 100*x,questions[x]))

contButton = ContinueButton([1000,700])


while doSpir2:

    leftDown = False

    pos = pygame.mouse.get_pos()

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            onExit()
            doSpir2= False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            leftDown = True

        
            
    screen.fill([255,255,255])

    text = font.render('Please rate the extent to which you agree with each statement below.',0,(0,0,0),(255,255,255))
    screen.blit(text, (150,20))

    for x in range(0,len(questions)):

        startX = rows[x].startX
        
        text = font.render(questions[x], 0, (0,0,0), (255,255,255))
        
        screen.blit(text, (250,70 + 100*x))

        notatall = smallfont.render('not at all', 0, (0,0,0), (255,255,255))
        screen.blit(notatall, (startX - 25,130 + 100*x))

        verymuch = smallfont.render('very much', 0, (0,0,0), (255,255,255))
        screen.blit(verymuch, (startX + 225,130 + 100*x))



    for row in rows:
        row.displayRow()
            

    contButton.checkHover(pos)
    contButton.checkClick(leftDown)
    contButton.blit()

    if contButton.status == 'clicked':
        doSpir2 = False
        ans = []
        for row in rows:
            ans.append(row.getAnswers())

        surveyAnswers.answers.append(ans)
        writeSurveyData(len(surveyAnswers.answers)-1)
    
    pygame.display.flip()

#Personality

questions = study_questions.personality


rows = []

for x in range(0,len(questions)):
    rows.append(ButtonRow(5,100 + 100*x,questions[x]))

contButton = ContinueButton([1000,700])


while doPers:

    leftDown = False

    pos = pygame.mouse.get_pos()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            onExit()
            doPers= False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            leftDown = True

        
            
    screen.fill([255,255,255])

    text = font.render('Please rate the extent to which you:',0,(0,0,0),(255,255,255))
    screen.blit(text, (150,20))

    for x in range(0,len(questions)):

        startX = rows[x].startX
        
        text = font.render(questions[x], 0, (0,0,0), (255,255,255))
        
        screen.blit(text, (250,70 + 100*x))

        notatall = smallfont.render('not at all', 0, (0,0,0), (255,255,255))
        screen.blit(notatall, (startX - 25,130 + 100*x))

        verymuch = smallfont.render('very much', 0, (0,0,0), (255,255,255))
        screen.blit(verymuch, (startX + 225,130 + 100*x))



    for row in rows:
        row.displayRow()
            

    contButton.checkHover(pos)
    contButton.checkClick(leftDown)
    contButton.blit()

    if contButton.status == 'clicked':
        doPers = False
        ans = []
        for row in rows:
            ans.append(row.getAnswers())

        surveyAnswers.answers.append(ans)
        writeSurveyData(len(surveyAnswers.answers)-1)
    
    pygame.display.flip()


screen.fill([255,255,255])
screen.blit(bigfont.render('Thank you for your participation!', 0 ,(0,0,0), (255,255,255)), [300,300])
screen.blit(bigfont.render('Please let the experimenter know that you are done.', 0, (0,0,0), (255,255,255)), [300, 500])
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            onExit()

