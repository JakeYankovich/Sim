import pygame
import random
pygame.init()

#pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.


size = 25
gWidth = 650
gHeight = 450


screen = pygame.display.set_mode( [500, 500] )

#             0                                                     1                                                    2       3       4                 5                    6                   7                   8                           9       10
#           [x position ,                               y position,                               size,size, hunger, behavior, matebar, partner, chosen food, cellid, strave countdown]

cell1 = [random.randint(0,640), random.randint(0,450), 10, 10, 31, "hungry", 0, -1, -1, 0, 200]
cell2 = [random.randint(0,640), random.randint(0,450), 10, 10,31, "hungry", 0, -1, -1, 1, 200]
cellid = 2
cells = [cell1, cell2]
'''
numfood = 3
foods = []
for i in range(numfood):
    foods.append([random.randint(0,640), random.randint(0,450), 10, 10])'''
food1 = [random.randint(0,640), random.randint(0,450), 10, 10]
food2 = [random.randint(0,640), random.randint(0,450), 10, 10]
food3 = [random.randint(0,640), random.randint(0,450), 10, 10]
foods = [food1, food2, food3]

win = pygame.display.set_mode((gWidth, gHeight))

pygame.display.set_caption("Cells Game")


myfont = pygame.font.SysFont('Comic Sans MS', 30) #text test



totalArea = gWidth * gHeight

gameSpeed = 50 #lower is faster

run = True

#behavior = "hungry"
#hunger = 31
#print(cell[5])
while run:
    pygame.time.delay(gameSpeed)
    
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #keys = pygame.key.get_pressed()
    
    #maybe impliment a system for cell only finding nearby food?
    # if (food [0] - cell[0]) < 200
    for cell in cells:
        if cell[10] > 0:
            for i in range(len(foods)):
                if (abs(cell[0] - foods[i][0]) < 7) and (abs(cell[1] - foods[i][1]) < 7): # EAT FOOD
                    print("Cell", cell[9], "ate food :)")
                    foods[i] = [random.randint(0,640), random.randint(0,450), 10, 10]
                    cell[5] = "bored"
                    cell[4] = 0 #not hungry
                    cell[8] = -1 #un-choose food
                    cell[10] = 200
                    print("cell", cell[9], "is", cell[5])
            
            if cell[5] == "hungry":                                                                                         # hungry
                while cell[8] == -1: #if no valid chosefood
                    ifood = random.randint(0,(len(foods)-1)) #choose a random food
                    if ifood != -1:
                        chosefood = foods[ ifood ]
                        print("cell", cell[9],  "chose food number", ifood)
                        cell[8] = ifood
                chosefood = foods[cell[8]]
                xdirection = (cell[0] - chosefood[0]) 
                ydirection = (cell[1]  -  chosefood[1])
                #print(xdirection, "= xdirection")
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    print("cell#",cell[9], "at", cell[0], cell[1], "is trying to find food#")
                    print(cell[8], "at", chosefood[0], chosefood[1])
                if xdirection < -5:
                    cell[0] = cell[0] + 5
                    #print("Moving right")
                elif xdirection > 5:
                    cell[0] = cell[0] -5
                    #print("Moving left")
                if ydirection < -5:
                    cell[1] = cell[1] + 5
                elif ydirection > 5:
                    cell[1] = cell[1] -5
                #print("Cell is", behavior, "and located at", cell[0],",",cell[1])
                #print("food is at", food[0],",", food[1])
                cell[10] = cell[10] - 1
                
            if cell[5] == "bored":                                                                                                      # bored
                #print(cell[6])
                #print(cell[6])
                cell[10] = cell[10] -1
                if cell[6] >= 63:  #exit bored loop if hungry
                    cell[5] = "mating"
                    print("cell", cell[9], "is", cell[5])
                    #print(R, G, B)
                cell[6] = cell[6] + 1 # becoming ready to mate
                
                #print(hunger)
                cell[0] = cell[0] + (random.randint(-1,1))*5 #moving random direction
                cell[1] = cell[1] + (random.randint(-1,1))*5
                if cell[0] < 0: #Checking if new random position is within boundaries
                    cell[0] = 5
                    #print(cell[9] , "hit a wall :(")
                elif cell[0] > 645:
                    cell[0] = 645
                    #print(cell[9] , "hit a wall :(")
                if cell[1] < 0:
                    cell[1] = 5
                    #print(cell[9] , "hit a wall :(")
                elif cell[1] > 445:
                    cell[1] = 445
                    #print(cell[9] , "hit a wall :(")
                
            
            if cell[5] == "mating":                                                                                                                 # mating  
                cell[6] = cell[6] -1
                if cell[6] <=0: #if no longer interested
                    print("cell", cell[9], "is no longer interested in mating")
                    cell[5] = "hungry"
                while cell[7] == -1: #if no valid partner,
                    cell[6] = cell[6] -1
                    ipart = random.randint(0,(len(cells)-1)) #choose a random partner
                    partner = cells[ ipart ]
                    if partner[9] != cell[9] and partner[10] > 0: #make sure partner is not self
                        cell[7] = ipart #if valid partner, assign partner officially
                        print("cell", cell[9], "has chosen partner", cell[7])
                    else: cell[7] = -1
                        
                if cell[9] != partner[9] and partner[10] > 0:
                    xdirection = (cell[0] - partner[0]) 
                    ydirection = (cell[1]  -  partner[1])
                    if xdirection < -5:
                        cell[0] = cell[0] + 5
                    elif xdirection > 5:
                        cell[0] = cell[0] -5
                    if ydirection < -5:
                        cell[1] = cell[1] + 5
                    elif ydirection > 5:
                        cell[1] = cell[1] -5
                    cell[10] = cell[10] - 1
                    if (abs(cell[0] - partner[0]) < 6) and (abs(cell[1] - partner[1]) < 6) :  #cell met valid partner!
                        #print("mated???? ---------------")
                        newcell = [cell[0], cell[1], 10, 10,31, "hungry", 0, -1,-1,cellid, 200]
                        cellid = cellid + 1
                        print(cell[9], "mated with", partner[9], "and created", newcell[9])
                        cells.append(  newcell )
                        cell[5] = "hungry"
                        cell[7] = -1
                
            
            '''if cell[6] == 0:  #exit bored loop if hungry
                cell[5] = "hungry"
                cell[7] = -1 #no partner
                print("cell", cell[9], "is", cell[5])'''
            #cell[10] = cell[10] - 1
        elif cell[10] == 0:
            print("cell", cell[9], "is dead")
            cell[10] = -1
        
    living = 0
    for cell in cells:
        if cell[10] > 0:
            living = living + 1
    text = "living cells: " + str(living)
    textsurface = myfont.render(text, False, (100, 100, 100))
    screen.blit(textsurface,(0,0))
    
    
    for cell in cells: #draw cells
        if cell[10] > 0:
            R = 150 - 3*cell[4] + cell[6]*2
            if R < 0: R = 0
            elif R > 255: R = 255
            G =  150 + 3*cell[4]
            if G < 0: G = 0
            elif G > 255: G = 255
            B = 120 + 4*cell[4] + (cell[6]/2)
            if B < 0: B = 0
            elif B > 255: B = 255
        else:
            #print("CELL STARVED")
            R = 50
            B = 15
            G = 15
        pygame.draw.rect(win, (R, G, B), (cell[0], cell[1], cell[2], cell[3]))
        
        #draw food
    for food in foods:
        pygame.draw.rect(win, (130, 255, 160), (food[0], food[1], food[2], food[3]))
    

    
    pygame.display.update()

pygame.quit()