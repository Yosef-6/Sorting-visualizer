import pygame
import random

pygame.init()

class Visualizer:
    RESOLUTION = (0,0)
    PADDING_X = 0          
    PADDING_Y = 0
    WHITE = (255,255,255)
    RED   = (255,0,0)
    GREEN = (0,255,0)
    BLACK = (0,0,0)
    MINIMUM_BLOCK_HEIGHT = 1 
    def __init__(self,resolution = (1000,600),workingList=[1,0]):
        self.window      = pygame.display.set_mode(resolution)
        self.workingList = workingList
        self.isRunning   = True
        self.isExhausted = False
        Visualizer.RESOLUTION = resolution
        self.itemColor = []
        self.algColor  = []
        self.ALG       = [self.insertionSort,self.bubbleSort,self.selectionSort,self.radixSort]  #init your alg here
        self.algorithim = self.ALG[0](); #init with insertionsort
        self.initBlocks()
    
    def initBlocks(self):
        width,height = self.RESOLUTION
        self.cellWidth = (width - 2*Visualizer.PADDING_X)/len(self.workingList)
        self.slope =  (Visualizer.PADDING_Y-(height-Visualizer.MINIMUM_BLOCK_HEIGHT))/(max(self.workingList) - min(self.workingList))
        self.const = Visualizer.PADDING_Y - self.slope*max(self.workingList)

    def randomize(self):
        self.workingList = list(range(0,100))
        random.shuffle(self.workingList)
        self.algorithim = random.choice( self.ALG )()   
        self.algColor  = []
        self.itemColor = []
        self.initBlocks()
    # insert sort alg here








    #//////////////////////
    def insertionSort(self):
        for i,element in enumerate(self.workingList):
            currentItem = element
            j = i-1
            while j >=0 and self.workingList[j] > currentItem:
                self.workingList[j+1] = self.workingList[j]
                self.workingList[j]   = currentItem
                j = j-1
                self.itemColor = [j+1]
                self.algColor  = [j]
                yield True
                

    def bubbleSort(self):
        for _ in self.workingList:
            for  j in range (1,len(self.workingList)):
                 if self.workingList[j-1] > self.workingList[j]:
                    self.workingList[j-1] , self.workingList[j] = self.workingList[j],self.workingList[j-1]
                    self.algColor=[j,j+1]
                    yield True

    def selectionSort(self):
        for i,element in enumerate(self.workingList):
            currenrMinimum = element
            minIndex = i
            j = i+1
            self.itemColor = [i]
            while j < len(self.workingList):
                  if currenrMinimum > self.workingList[j]:
                     currenrMinimum = self.workingList[j]
                     minIndex = j
                     self.algColor=[minIndex]
                  j+=1
                  yield True

            self.workingList[i] ,self.workingList[minIndex] = self.workingList[minIndex],self.workingList[i]
    
    def radixSort(self):
        passes = len(str(max(self.workingList)))
        buckets = [[],[],[],[],[],[],[],[],[],[]]
        j = 1
        while j <= passes:
          
            for element in self.workingList:
                if len(str(element)) >= j:
             
                    buckets[int(str(element)[len(str(element))-j])].append(element)
                else:
                    buckets[0].append(element)
            k = 0
            for bucket in  buckets:
                for element in bucket:
                    self.workingList[k] = element
                    self.algColor = [k]
                    k+=1
                    yield True
            j+=1
            buckets = [[],[],[],[],[],[],[],[],[],[],[]]


    def mainEventLoop(self):
        clock = pygame.time.Clock()
        while self.isRunning  == True :
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
            self.update()
            self.render()
        pygame.quit()
 
    def renderBlocks(self):
         _,height= Visualizer.RESOLUTION
         for i,block in enumerate(self.workingList):
            y = self.slope*block+self.const
            if i in self.itemColor:
               pygame.draw.rect(self.window,Visualizer.GREEN,(i*self.cellWidth + Visualizer.PADDING_X,
               y,self.cellWidth,height - y+1))
            elif i in self.algColor:
                pygame.draw.rect(self.window,Visualizer.RED,(i*self.cellWidth + Visualizer.PADDING_X,
               y,self.cellWidth,height - y+1))
            else:
                pygame.draw.rect(self.window,Visualizer.WHITE,(i*self.cellWidth + Visualizer.PADDING_X,
               y,self.cellWidth,height - y+1))

        
    def update(self):
        if pygame.key.get_pressed()[pygame.K_r]:
            self.randomize()
            self.isExhausted = False
        if self.isExhausted != True:
           try:
              next(self.algorithim)
           except StopIteration:
              self.isExhausted = True
    def render(self):
        self.window.fill(Visualizer.BLACK)
        self.renderBlocks()
        pygame.display.update()


if __name__ =="__main__":
    workingList =   list(range(0,400))
    random.shuffle(workingList)
    visual = Visualizer((1200,600),workingList=workingList)
    visual.mainEventLoop()



   









