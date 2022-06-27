import random

def monetysim(outcome,gameSize,repick, banana):
    # 1 = won, 2 = lost 3 = unknown
    #gameSize = 3, number of doors
    montey = [1] * gameSize #initate all doors to goat // 1 == goat, 2 == car, 3 == exposed goat

    #init random door to car
    winner = random.randint(0, gameSize-1)
    montey[winner]=2

    choice = random.randint(0, gameSize-1) #randomly choose a door
    
    #randomly open a non car door, if banana then you accidenly open any door, if car is opened, then you lose 
    exposed = random.randint(0, gameSize-1)
    if(banana == True):
        while(choice==exposed):#can't slip and open door picked by player 
            exposed = random.randint(0, gameSize-1)

        if(exposed == winner): # if you accidently opened car, you lose
            outcome = 2
            return outcome
    else: #There is no banana, then make sure door opened will not be car or chosen door
        while(exposed == winner or choice==exposed ):#already opened, not the car, 
            exposed = random.randint(0, gameSize-1)
    
    montey[exposed]=3 #open door 

    #choose another door again if repick == True
    if(repick==True):
        oldChoice = choice
        choice = random.randint(0, gameSize-1)
        while(montey[choice]==3 or choice == oldChoice):
            choice = random.randint(0, gameSize-1)

    if (montey[choice] == 2): #winner
        outcome = 1
        return outcome

    if(montey[choice]==1): #loser
        outcome=2
        return outcome

def testing(testSize,doors,repick,banana):
    wins = 0
    losses = 0
    result = 0
    for x in range(testSize):
        result = monetysim(result, doors,repick,banana)
        if(result==1):
            wins= wins + 1
        else:
            losses = losses + 1
        result = 0

    print(doors," doors, ",testSize,"loops, repicking door = ",repick,", banana = ",banana,": WIN PERCENTAGE IS ", (wins/testSize)*100,"% || LOSS PERCENTAGE IS ", (losses/testSize)*100,"%")
    print("_______________________________________________________________________________________________________________________________________________")

# 3 DOOR TESTING
    #repicking door without banana
print("")
print(" 3 DOOR TESTING !")
print("")
testing(10,3,True,False)
testing(100,3,True,False)
testing(1000,3,True,False)
testing(10000,3,True,False)
testing(100000,3,True,False)
testing(1000000,3,True,False)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door without banana
testing(10,3,False,False)
testing(100,3,False,False)
testing(1000,3,False,False)
testing(10000,3,False,False)
testing(100000,3,False,False)
testing(1000000,3,False,False)
print("")
print("##################################################################################################################################################")
print("")
    #repicking door with banana
testing(10,3,True,True)
testing(100,3,True,True)
testing(1000,3,True,True)
testing(10000,3,True,True)
testing(100000,3,True,True)
testing(1000000,3,True,True)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door with banana
testing(10,3,False,True)
testing(100,3,False,True)
testing(1000,3,False,True)
testing(10000,3,False,True)
testing(100000,3,False,True)
testing(1000000,3,False,True)


# 6 DOOR TESTING
    #repicking door without banana
print("")
print(" 6 DOOR TESTING !")
print("")
testing(10,6,True,False)
testing(100,6,True,False)
testing(1000,6,True,False)
testing(10000,6,True,False)
testing(100000,6,True,False)
testing(1000000,6,True,False)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door without banana
testing(10,6,False,False)
testing(100,6,False,False)
testing(1000,6,False,False)
testing(10000,6,False,False)
testing(100000,6,False,False)
testing(1000000,6,False,False)
print("")
print("##################################################################################################################################################")
print("")
    #repicking door with banana
testing(10,6,True,True)
testing(100,6,True,True)
testing(1000,6,True,True)
testing(10000,6,True,True)
testing(100000,6,True,True)
testing(1000000,6,True,True)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door with banana
testing(10,6,False,True)
testing(100,6,False,True)
testing(1000,6,False,True)
testing(10000,6,False,True)
testing(100000,6,False,True)
testing(1000000,6,False,True)

# 9 DOOR TESTING
    #repicking door without banana
print("")
print(" 9 DOOR TESTING !")
print("")
testing(10,9,True,False)
testing(100,9,True,False)
testing(1000,9,True,False)
testing(10000,9,True,False)
testing(100000,9,True,False)
testing(1000000,9,True,False)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door without banana
testing(10,9,False,False)
testing(100,9,False,False)
testing(1000,9,False,False)
testing(10000,9,False,False)
testing(100000,9,False,False)
testing(1000000,9,False,False)
print("")
print("##################################################################################################################################################")
print("")
    #repicking door with banana
testing(10,9,True,True)
testing(100,9,True,True)
testing(1000,9,True,True)
testing(10000,9,True,True)
testing(100000,9,True,True)
testing(1000000,9,True,True)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door with banana
testing(10,9,False,True)
testing(100,9,False,True)
testing(1000,9,False,True)
testing(10000,9,False,True)
testing(100000,9,False,True)
testing(1000000,9,False,True)


# 20 DOOR TESTING
    #repicking door without banana
print("")
print(" 20 DOOR TESTING !")
print("")
testing(10,20,True,False)
testing(100,20,True,False)
testing(1000,20,True,False)
testing(10000,20,True,False)
testing(100000,20,True,False)
testing(1000000,20,True,False)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door without banana
testing(10,20,False,False)
testing(100,20,False,False)
testing(1000,20,False,False)
testing(10000,20,False,False)
testing(100000,20,False,False)
testing(1000000,20,False,False)
print("")
print("##################################################################################################################################################")
print("")
    #repicking door with banana
testing(10,20,True,True)
testing(100,20,True,True)
testing(1000,20,True,True)
testing(10000,20,True,True)
testing(100000,20,True,True)
testing(1000000,20,True,True)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door with banana
testing(10,20,False,True)
testing(100,20,False,True)
testing(1000,20,False,True)
testing(10000,20,False,True)
testing(100000,20,False,True)
testing(1000000,20,False,True)


# 100 DOOR TESTING
    #repicking door without banana
print("")
print(" 100 DOOR TESTING !")
print("")
testing(10,100,True,False)
testing(100,100,True,False)
testing(1000,100,True,False)
testing(10000,100,True,False)
testing(100000,100,True,False)
testing(1000000,100,True,False)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door without banana
testing(10,100,False,False)
testing(100,100,False,False)
testing(1000,100,False,False)
testing(10000,100,False,False)
testing(100000,100,False,False)
testing(1000000,100,False,False)
print("")
print("##################################################################################################################################################")
print("")
    #repicking door with banana
testing(10,100,True,True)
testing(100,100,True,True)
testing(1000,100,True,True)
testing(10000,100,True,True)
testing(100000,100,True,True)
testing(1000000,100,True,True)
print("")
print("##################################################################################################################################################")
print("")
    #not repicking door with banana
testing(10,100,False,True)
testing(100,100,False,True)
testing(1000,100,False,True)
testing(10000,100,False,True)
testing(100000,100,False,True)
testing(1000000,100,False,True)