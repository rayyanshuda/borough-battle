import random

#this is the list and all smaller lists have values for each village (sample: [number of soldiers in village, "Village name", "whether or not it's a base"]
player = [[0, "Leaf Village"],
          [0, "Sand Village"],
          [0, "Cloud Village"],
          [0, "Stone Village"],
          [0, "Mist Village"]
          ]
#list for computer, same template as player list
comp = [[0, "Leaf Village"],
        [0, "Sand Village"],
        [0, "Cloud Village"],
        [0, "Stone Village"],
        [0, "Mist Village"]
        ]

#player adding 10 soldiers to the villages
def playerAddSoldiers():
    try:
        print("Where do you want to position the Kages and Second-in-Commands?  \n")
        print("Villages: Leaf Village, Sand Village, Cloud Village, Stone Village, Mist Village \n")
        a = int(input("How many do you want to add to Leaf Village? "))
        b = int(input("How many do you want to add to Sand Village? "))
        c = int(input("How many do you want to add to Cloud Village? "))
        x = int(input("How many do you want to add to Stone Village? "))
        y = int(input("How many do you want to add to Mist Village? "))
            #check if the number of soldiers in each village adds up to 10, if doesn't, print invalid input and run function again
        if a + b + c + x + y != 10:
            print() #creating space in terminal for readability 
            print("Invalid Input: Need to Add Exactly 10 Units \n")
            if (a + b + c + x + y) > 10:
                remain = (a + b + c + x + y) - 10
                print("Sum of Inputs Was", remain, "More Than 10")
            elif (a + b + c + x + y) < 10:
                remain = 10 - (a + b + c + x + y)
                print("Sum of Inputs Was", remain, "Less Than 10")
            print()
            playerAddSoldiers()
            #if sum of inputs is 10, replace the first index of each smaller list in the player list as the variables
        else:
            player[0][0] = a
            player[1][0] = b
            player[2][0] = c
            player[3][0] = x
            player[4][0] = y
    except:
        print("Invalid Input: Please Input Integers \n")
        playerAddSoldiers()

#these are the computer's placement of first 10 soldiers in the villages
def compAddSoldiers():
    first = random.randint(0, 10)
    remaining = 10 - first
    second = random.randint(0, remaining)
    remaining = 10 - (first + second)
    third = random.randint(0, remaining)
    remaining = 10 - (first + second + third)
    fourth = random.randint(0, remaining)
    remaining = 10 - (first + second + third + fourth)
    fifth = remaining

    comp[0][0] = first
    comp[1][0] = second
    comp[2][0] = third
    comp[3][0] = fourth
    comp[4][0] = fifth


def baseBoro():
    #choosing base, check if input equals to the given options. If does, add the word "BASE" to the end of the smaller list. If doesn't, print invalid input, run program
    #when checking if won at base, check if player[i][-1] == "BASE", double the points
    #**note: can't check player[i][2] == "BASE" because if there isn't anything at the second index, then probably will give me error
    global d
    global playerBase
    d = input("What do you want your base village to be? Leaf, Sand, Cloud, Stone, Mist? \n").upper()
    if d == "LEAF":
        player[0].append("BASE")
        playerBase = player[0][1]
    elif d == "SAND":
        player[1].append("BASE")
        playerBase = player[1][1]
    elif d == "CLOUD":
        player[2].append("BASE")
        playerBase = player[2][1]
    elif d == "STONE":
        player[3].append("BASE")
        playerBase = player[3][1]
    elif d == "MIST":
        player[4].append("BASE")
        playerBase = player[4][1]
    else:
        print()
        print("Invalid Input: Please Input One of the Given Options \n")
        print()
        #re-run program
        baseBoro()
    #computer choosing base: choose number between 0-4, and that is the index
    def compBase():
        global d
        global computerBase
        h = random.randint(0,4)
        while comp[h][1] == playerBase:
            h = random.randint(0,4)
        comp[h].append("BASE")
        computerBase = comp[h][1]
        
    compBase()


#code for adding more soldiers
def moreSoldiers():
    global rounds
    global b
    rounds = random.randint(10, 25)
    #need 'b' when using cheat because 'b' will be the total rounds, so to find the rounds played: b - rounds
    b = rounds
    #need another function in case user input isn't valid, so it just reruns asking the question instead of choosing a new number between 10-25
    def soldierAdd():
        global rounds
        global b
        global computerBase
        global playerBase
        while rounds > 0:
            #user adding more soldiers
            addSoldier = input("Where do you want to add another soldier? Leaf, Sand, Cloud, Stone, Mist? \n").upper()
            if addSoldier != "NINJA":
                if addSoldier == "LEAF":
                    player[0][0] = player[0][0] + 1
                elif addSoldier == "SAND":
                    player[1][0] = player[1][0] + 1
                elif addSoldier == "CLOUD":
                    player[2][0] = player[2][0] + 1
                elif addSoldier == "STONE":
                    player[3][0] = player[3][0] + 1
                elif addSoldier == "MIST":
                    player[4][0] = player[4][0] + 1
                else:
                    print("Invalid Input: Please Input One of the Given Options \n")
                    soldierAdd()
                #computer adding more soldiers, but need to stop at round 1, so the soldiers are the same amount
                if rounds >= 1:
                    v = random.randint(0, 4)
                    comp[v][0] = comp[v][0] + 1
                    print()
                    print("Our intel says the Ten Tails sent a clone to", comp[v][1], "\n")
                    print()
                    rounds = rounds - 1
            elif addSoldier == "NINJA": #if input is ninja, then display the cheat
                print("")
                print("Through a risky endeavor, our ninjas return with valuable information \n")
                #printing my soldiers (each index at a time)
                print("Your Soldiers: \n")
                
                print("Leaf Village:", player[0][0], "soldiers")
                
                print("Sand Village:", player[1][0], "soldiers")
                
                print("Cloud Village:", player[2][0], "soldiers")
                
                print("Stone Village:", player[3][0], "soldiers")
                
                print("Mist Village:", player[4][0], "soldiers \n")

                print("Your base is", playerBase, "\n")
                
                #printing enemy soldiers (each index at a time)
                print("Ten Tails Clones: \n")
                
                print("Leaf Village:", comp[0][0], "clones")
                
                print("Sand Village:", comp[1][0], "clones")
                
                print("Cloud Village:", comp[2][0], "clones")
                
                print("Stone Village:", comp[3][0], "clones")
                
                print("Mist Village:", comp[4][0], "clones \n")

                print("Ten Tail's base is", computerBase, "\n")

                #calculate for the rounds played, and rounds left (which is just variable 'rounds' because that changes)
                roundsPlayed = b - rounds
                roundsLeft = rounds
                print(roundsPlayed, "rounds have been played")
                print(roundsLeft, "rounds left")
                print()
            
    soldierAdd()
def results():
    i = 0
    pPoints = 0 #player points
    cPoints = 0 #computer points
    pVillageWins = 0 #number of player wins at each village
    cVillageWins = 0 #number of computer wins at each village
    while i < 5: #5 because I want it to stop at the 4th index
        print(player[i][1]) #printing what village the points are being calculated for
        if player[i][0] == comp[i][0]: #if tied no one gets points
            print("No Points Scored \n")
        elif player[i][0] == 0: #if you have 0 soldiers, enemy gets same number of points as soldiers in their base
            cVillageWins = cVillageWins + 1
            compPoints = comp[i][0] #compPoints is temporary variable to check whether or not it's base to be doubled
            if comp[i][-1] == "BASE": #checking if that village is their base
                print("No! Ten Tails won at his base! Points are doubled.")
                compPoints = compPoints * 2
            cPoints = cPoints + compPoints
            if compPoints == 1:
                print("Ten Tails Wins [", compPoints, "Point ] \n")
            else:
                print("Ten Tails Wins [", compPoints, "Points ] \n")
        elif comp[i][0] == 0: #if enemy have 0 soldiers, you gets same number of points as soldiers in your base
            pVillageWins = pVillageWins + 1
            playerPoints = player[i][0] #playerPoints is temporary variable to check whether or not it's base to be doubled
            if player[i][-1] == "BASE": #checking if that village is your base
                print("You won at base! Points are doubled.")
                playerPoints = player[i][0]
                playerPoints = playerPoints * 2
            pPoints = pPoints + playerPoints
            if playerPoints == 1:
                print("You Win! [", playerPoints, "Point ] \n")
            else:
                print("You Win! [", playerPoints, "Points ] \n")
        elif player[i][0] > comp[i][0]:
            pVillageWins = pVillageWins + 1
            playerPoints = player[i][0] // comp[i][0]
            if player[i][-1] == "BASE":
                print("You won at base! Points are doubled.")
                playerPoints = playerPoints * 2
            pPoints = pPoints + playerPoints
            if playerPoints == 1:
                print("You Win! [", playerPoints, "Point ] \n")
            else:
                print("You Win! [", playerPoints, "Points ] \n")
        elif comp[i][0] > player[i][0]:
            cVillageWins = cVillageWins + 1
            compPoints = comp[i][0] // player[i][0]
            if comp[i][-1] == "BASE":
                print("No! Ten Tails won at his base! Points are doubled.")
                compPoints = compPoints * 2
            cPoints = cPoints + compPoints
            if compPoints == 1:
                print("Ten Tails Wins [", compPoints, "Point ] \n")
            else:
                print("Ten Tails Wins [", compPoints, "Points ] \n")
        i = i + 1
    if pPoints == 1:
        print("You:", pPoints, "Point") #printing your points if only one point
    else:
        print("You:", pPoints, "Points") #printing your points
    if cPoints == 1:
        print("Ten Tails:", cPoints, "Point \n") #printing enemy points if only one point
    else:
        print("Ten Tails:", cPoints, "Points \n") #printing enemy points
    if pPoints > cPoints:
        print("Ten Tails is Defeated. You Win!")
    elif cPoints > pPoints:
        print("Oh No! Ten Tails Wins!")
    else:
        #if points are tied, calculate for more villages won
        print("Points are tied!")
        if pVillageWins == 1:
            print("You have won at 1 village")
        else:
            print("You have won at", pVillageWins, "villages")
        if cVillageWins == 1:
            print("Ten Tails has won at 1 Village")
        else:
            print("Ten Tails has won at", cVillageWins, "villages")
        if pVillageWins > cVillageWins:
            print("You won more villages: You Win!")
        elif cVillageWins > pVillageWins:
            print("Ten Tails has won more villages: Ten Tails Wins!")
        else:
            print("You have been defeated. Ten Tails Wins!")

#intro storyline
print("Great Hokage! I apologize for the informalities but this is urgent. ")
print("The Ten Tails is attacking the villages again")
print("Being the one uniting the 5 villages 20 seconds ago, the citizens' hope resides in you to command us!")
print("We wouldn't disturb you if it wasn't a serious danger")
print("The Ten Tails is creating clones and attacking all five villages at once")
print("The 5 Kages and their second-in-commands are ready to be deployed. \n")

playerAddSoldiers()
compAddSoldiers()
print()
print("We need to choose a base village now where we can keep you safe. \n")
print("We can defeat Ten Tails if you can accumulate more points in our villages")
print("Points are rewarded based on the ratio of our soldiers to Ten Tail clones in each village.")
print("Winning at base raises morale of the soldiers and gives double the points")
print("But beware Great Hokage! If the Ten Tails has more clones than our soldiers in his base, his points are doubled for that village! \n")
#choose base village
baseBoro()
print()
print("I guess the Ten Tails was too lazy to attack on a Monday. We have time to deploy more soldiers! ")
print("Unfortunately, communications is malfunctioning, so we can only send a message to headquarters to deploy one soldier at a time. \n")
print("Hint: Type in 'Ninja' to view secret information by our ninjas \n")
moreSoldiers()
print()
print()
print("EMERGENCY: Ten Tails has started attacking! Let's review the results. \n")
results()
