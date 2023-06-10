import random
import time

actions = ["1", "2", "3", "0"]

entertainment = [["You played a fighting game", " and did really well!", " and got messed up."],
                 ["You played Dark Souls", " and made a lot of progress!", " and lost all your souls."],
                 ["You played an FPS", " and your aim was on point!", " and spent most your time dead."],
                 ["You binged a Netflix show", " and it was heartwarming!", " and it was gut wrenching."],
                 ["You binged an old sitcom", " and it really took your mind off things!", " and it was really dull."],
                 ["You decided to listen to some music", " and found some real jams!",
                  " but couldn't find anything interesting"],
                 ["You Picked up a book", " and read for hours on end!", " but couldn't focus at all."],
                 ["You tried cooking something new", " and it was delicious!",
                  " but you almost lit your house on fire."],
                 ["You got on a voice chat with some pals", " and you all played games for hours!",
                  " and you had a nasty argument."],
                 ["You booted up your old PS2", " and had a nice trip down memory lane!",
                  " but it just didn't feel the same."],
                 ["You played some Kenshi", " and saw that your characters are getting super strong!",
                  " and then your favorite character died."],
                 ["You launched your IDE", " and made a lot of progress on your project!",
                  " but a bug had you stumped for hours."]]

eventtext = ["Your phone's screen is cracked and unresponsive. You should get it fixed.",
             "You find a wallet. Inside is a lot of money and family photos. You pocket it.",
             "You found some money on the sidewalk",
             "A stranger thought you were a beggar and gave you some change.",
             "You ran out of smokes today.",
             "You felt the urge to buy a stupid anime figurine, so you did.",
             "You find some money in your pocket! Hooray!",
             "Your fridge has broken down.",
             "You lost your wallet.",
             "After getting off the bus you reached into your pocket for you phone, but it wasn't there.",
             "A friend called you to go out and you got totally smashed.",
             "You're all out of mayo. Can't have that!",
             "Your front door's lock is broken! The locksmith will charge extra at night you know...",
             "There's mosquitoes everywhere! You invest in some bug spray.",
             "Your shoes are all worn out. Time to get new ones.",
             "The electric company called for an old bill you completely forgot about...",
             "Some sewage pipes burst... again. The building manager came to collect... again.",
             "You watched a nice film to calm your nerves...",
             "Everything you eat tastes like ashes.",
             "You didn't even get out of bed today.",
             "You wanted to read a book, but dropped it after the first chapter",
             "You remembered your old partner and cried while cooking some awful meal.",
             "You had some chocolate and a coke. Briefly, things didn't seem that bad.",
             "Maybe you should learn guitar? Nah... too much effort...",
             "You thought about calling them again today, but didn't even try to reach for you phone.",
             "You woke up with a limp arm and wondered if it would ever come back. It did.",
             "You daydreamed about your funeral again.",
             "You could've sworn the button looked like it was mocking you yesterday.",
             "The news was more depressing than usual.",
             "Today was unremarkable... again.",
             "You spotted a hedgehog on your way to the park. It was cute.",
             "An old friend reached out today to see how you're doing. You felt good."]

depdep = [random.randint(10, 15), random.randint(-10, 5), random.randint(-15, -10), random.randint(5, 15),
          random.randint(5, 10), random.randint(-15, -5), random.randint(-20, -10), random.randint(15, 25),
          random.randint(10, 25), random.randint(25, 30), random.randint(-30, -20), random.randint(0, 5),
          random.randint(25, 30), random.randint(0, 5), random.randint(-5, 5), random.randint(20, 25),
          random.randint(5, 15), random.randint(-15, -5), 0, random.randint(5, 15), random.randint(0, 10),
          random.randint(5, 15), random.randint(25, 30), random.randint(-25, -20), random.randint(-5, 5),
          random.randint(-10, 0), random.randint(20, 25), random.randint(25, 30), random.randint(5, 10),
          random.randint(0, 5), random.randint(-35, -20), random.randint(-40, -35)]

monmon = [random.randint(-250, -60), random.randint(300, 800), random.randint(2, 11), random.randint(3, 12),
          random.randint(-25, -15), random.randint(-250, -50), random.randint(2, 20), random.randint(-300, -100),
          random.randint(-500, -200), random.randint(-450, -150), random.randint(-30, -10), random.randint(-12, -6),
          random.randint(-100, -20), random.randint(-25, -8), random.randint(-123, -64), random.randint(-250, -100),
          random.randint(-87, -14)]

malenames = ["Ethan", "Caleb", "Lucas", "Gabriel", "Owen", "Adrian", "Xavier", "Leo", "Sebastian", "Julian",
             "Nathan", "Cole", "Evan", "Isaac", "Blake", "Dominic", "Max", "Ryan", "Elijah", "Henry", "Milo",
             "Finn", "Jasper", "Elliot", "Dylan", "Zachary", "Oscar", "Aaron", "Miles", "Harrison"]

femalenames = ["Ava", "Emma", "Olivia", "Sophia", "Isabella", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn",
               "Abigail", "Emily", "Elizabeth", "Sofia", "Ella", "Scarlett", "Victoria", "Luna", "Chloe",
               "Grace", "Penelope", "Layla", "Riley", "Zoe", "Nora", "Stella", "Anna", "Aurora", "Lucy", "Nova"]

neutralnames = ["Alex", "Taylor", "Jordan", "Rhys", "Charlie", "Avery", "Jamie", "Riley", "Sam", "Bailey", "Blake",
                "Dakota", "Hayden", "Peyton", "Jesse", "Phoenix", "Rowan", "Emerson", "Finley", "Harley", "Morgan",
                "Reese", "Skyler", "Sage", "Parker", "River", "Ellis", "Quinn", "Marley", "Sawyer"]

jobs = [" Graphic Designer, but just wanted to paint naked people", " Photographer and loved it",
        " Fashion Designer... and had a coke habit", " Musician, but didn't play their favourite genre",
        "n Animator, and an Insomniac", " Film Director. Even had a short film reviewed by a big newspaper",
        " Writer, was about to get a book published too", "n Interior Designer, but had a side hustle going",
        " Video Game Developer and suicidal", "n Illustrator", " Bartender and pretty happy",
        " Software Developer, balding, stressed, and gaining weight", "n Event Planner for lame people",
        " Photographer with a secret stash of unsavoury content",
        " Customer Service Representative who hated their job",
        " Sales Representative who loved their job", " Broke College Student. You did them a favour",
        " Plumber with a bad case of asscrack syndrome and two kids", " very hasty and selfish Bus driver",
        " First Grade Teacher who despised children", "n Antisocial Social Worker", " Therapist with BPD",
        " Sadomasochistic Catholic Youth Minister", " Unemployed and massively in debt",
        " 16 year old sugar baby who lied about their age", " Homeless person you saw on your way to the supermarket",
        " Carpenter with a loving stepfather.\nThough some say they saw him a few hours later",
        " Severely Underpaid Sound Engineer", " Poet, who had recently fallen madly in love",
        "n Up-and-Coming Gothic Jewelery Designer you had a crush on.\nYou hope soon the button takes you",
        " Hardcore Marvel Fan. It's not a HUGE shame", "n Overworked Supermarket Clerk",
        "n Aspiring Fashion Model with 5 roommates", "n Estranged Childhood Friend of yours."
        "\nApparently they had just gotten married", "n Old Classmate and VERY young parent",
        " Victim, trying to support their sick parents with, like, 5 jobs",
        " Twitter Furry Artist. They were making good money, but it wasn't worth it",
        " Freelance Software Dev who only knew LUA for some reason", " your DM for three sessions of a failed campaign",
        " Bear of an art student with an unfaithful streak.\nThey kicked you in the face in a moshpit that one time",
        " that one punk you spotted at all those DIY punk shows", " your Dope Dealer. You are devastated.",
        " your online gaming buddy. They'll never come online again", " your hometown neighbour's downs kid",
        " Public Servant and a Hardcore Conspiracy Theorist", "n Alcoholic Motorcyclist",
        " Heroin Addict with a surprisingly stable Medical Engineering gig"]
########################################################################################################################


class Player:
    def __init__(self, name, money, food, bills, health, taxhealth, depression):
        self.name = name
        self.number = 0
        self.money = money
        self.food = food
        self.bills = bills
        self.health = health
        self.taxhealth = taxhealth
        self.depression = depression


class Friend:
    def __init__(self, name, job):
        self.number = 0
        self.name = name
        self.job = job


class Event:
    def __init__(self, text, money, dep):
        self.text = text
        self.money = money
        self.dep = dep


class GameState:
    def __init__(self):
        self.thelist = []
        self.friends = []
        self.events = []
        self.entertainment = []
        self.deathcounter = 0
        self.frienddeathcounter = 0
        self.day = 0
        self.playernumber = 0

    def generatefriends(self):
        for i in range(len(jobs)):
            sexnum = random.randint(0, 2)
            if sexnum == 0:
                x = random.randint(1, len(malenames)) - 1
                name = malenames[x]
                malenames.pop(x)
            elif sexnum == 1:
                x = random.randint(1, len(femalenames)) - 1
                name = femalenames[x]
                femalenames.pop(x)
            else:
                x = random.randint(1, len(neutralnames)) - 1
                name = neutralnames[x]
                neutralnames.pop(x)
            x = random.randint(1, len(jobs)) - 1
            job = jobs[x]
            jobs.pop(x)

            self.friends.append(Friend(name, job))

    def generateevents(self):

        for i in range(len(eventtext)):
            if i < len(monmon):
                self.events.append(Event(eventtext[i], monmon[i], depdep[i]))
            else:
                self.events.append(Event((eventtext[i]), 0, depdep[i]))

    def generateentertainment(self):

        for i in range(len(entertainment)):
            self.entertainment.append(entertainment[i])

    def generatelists(self, size):
        self.generateevents()
        self.generatefriends()
        self.generateentertainment()
        self.thelist = []
        for i in range(size):
            self.thelist.append(i)
        i = 0

        flag = True
        self.playernumber = -1
        while flag:
            x = random.choice(self.thelist)
            if x in self.thelist:
                self.playernumber = x
                flag = False

        friendlist = []
        while i < len(self.friends):
            x = random.choice(self.thelist)
            if x in self.thelist and x != self.playernumber and x not in friendlist:
                self.friends[i].number = x
                friendlist.append(x)
                i = i + 1
        self.friends.append(Friend("Karyofyllia", " Computer Science Student"))
        self.friends.append(Friend("Bill", " Software Developer and making bank"))
        return self


class ActionHandler:
    def __init__(self, action1, action2):
        self.action1 = action1
        self.action2 = action2

    def action(self, player, gamestate):

        if player.depression > 100:
            player.depression = 100
        elif player.depression < 0:
            player.depression = 0

        print("\n1. Press the Button              Day", end=" ")
        for i in range(3 - len(str(gamestate.day))):
            print(" ", end="")
        print(gamestate.day, "          Money:", player.money,
              "\n2. Do not press the Button                    ", "     Food:", player.food,
              "\n3. Entertain yourself                      ", "Mental State:", 100 - player.depression,
              "\n0. Quit                                       ", "    Bills:", player.bills)
        action = input()
        while action not in actions:
            print("INVALID OPTION")
            print("\n1. Press the Button              Day", end=" ")
            for i in range(3 - len(str(gamestate.day))):
                print(" ", end="")
            print(gamestate.day, "          Money:", player.money,
                  "\n2. Do not press the Button                    ", "     Food:", player.food,
                  "\n3. Entertain yourself                      ", "Mental State:", 100 - player.depression,
                  "\n0. Quit                                       ", "    Bills:", player.bills)
            action = input()
        victory = False
        playing = True

        if action == "0":
            print("Goodbye...\n")
            playing = False
        elif action == "1":
            gamestate, player = buttonpress(gamestate, player)
            if player.number == -2:
                playing = playerdeath(player)
            self.action1 += 1
        elif action == "3":
            gamestate, player = entertainself(gamestate, player)
        else:
            print("A day passes.")
            self.action2 += 1
        if not gamestate.thelist:
            print("Only you survive.\n")
            playing = False
            victory = True
        depgain = random.randint(0, 10)
        player.depression += depgain
        if player.depression > 100:
            player.depression = 100
            print("You don't know much longer you can take this...")
            player.health -= 1
        elif player.depression < 0:
            player.depression = 0
        time.sleep(0.5)
        return player, gamestate, playing, victory


def gameintro(name):

    print("Hello", end="")
    time.sleep(0.2)
    for i in range(3):
        time.sleep(0.2)
        print(".", end="")
    time.sleep(0.4)
    print(" ", end="")
    for i in range(len(name)):
        time.sleep(0.2)
        print(name[i], end="")
    for i in range(3):
        time.sleep(0.2)
        print(".", end="")
    time.sleep(0.5)
    print("\n\n")

    introtext = "Before you lies a button, its unassuming surface concealing a chilling power. A game of\n" \
                "choices and consequences awaits you, where life and death hang in the balance. With each\n" \
                "press, an irreversible ripple effect will unfold, intertwining lives and shaping destinies.\n" \
                "            \n" \
                "In this realm of introspection there are no clear answers, only the weight of responsibility\n" \
                "that accompanies your every choice. Will empathy guide your decisions, or will curiosity\n" \
                "succumb to the allure of control? Brace yourself for an odyssey where the pressing of a\n" \
                "single button holds the power to shape lives and determine fates. Choose wisely, for the\n" \
                "journey begins now.\n"

    print(introtext)
    time.sleep(1)
    print("You must survive 150 days.")
    time.sleep(1)

    response = 0
    while response != "Y" and response != "y" and response != "N" and response != "n":
        response = input("\nDo you accept? Y/N: ")
        print("\n\n")

    return response


def randomevent(gamestate, player):
    if not gamestate.events:
        gamestate.generateevents()
    x = random.choice(gamestate.events)
    print(x.text)
    print("Balance change: ", x.money)
    player.money += x.money
    player.depression += x.dep
    gamestate.events.remove(x)
    return gamestate, player


def entertainself(gamestate, player):
    if not gamestate.entertainment:
        gamestate.generateentertainment()
    x = random.choice(gamestate.entertainment)
    print(x[0], end="")
    if random.randint(0, 100) < 80:
        player.depression -= random.randint(20, 40)
        print(x[1])
    else:
        player.depression += random.randint(10, 25)
        print(x[2])
    gamestate.entertainment.remove(x)
    return gamestate, player


def buttonpress(gamestate, player):
    print("One Perishes...")
    x = random.choice(gamestate.thelist)

    if x == player.number:
        player.number = -2
    else:
        i = 0
        flag = True
        while i < len(gamestate.friends) and flag:
            if x == gamestate.friends[i].number:
                flag = False
            else:
                i = i + 1
        if not flag:
            print("... your friend " + gamestate.friends[i].name + ".\n")
            print("They were a" + gamestate.friends[i].job + "...")
            gamestate.friends.pop(i)
            gamestate.frienddeathcounter += 1
            player.depression += 10
        else:
            gamestate.thelist.remove(x)
        gain = random.randint(50, 500)
        player.depression += random.randint(15, 30)
        player.money += gain
        print("Money gained: ", gain, "")
        gamestate.deathcounter += 1
    return gamestate, player


def playerdeath(player):
    print(player.name + " is dead...\n")
    return False


def playertax(player):
    print(player.name + " did not pay their taxes in time...\n")
    return False


def finances(player):
    playing = True
    player.food -= random.randint(5, 15)
    player.bills += random.randint(5, 25)
    flag1 = flag2 = False
    if player.food < 25:
        player.food = 0
        player.health -= 1
        print("You are starving")
        flag1 = True
    if player.bills > 150:
        print("Your bills are stacking up")
        flag2 = True

    if flag1 or flag2:
        if flag1 and not flag2:
            if player.money > (100 - player.food) * 3:
                print("You buy food.")
                player.money -= (100 - player.food) * 3
                player.food = 100
                player.health = 4
            else:
                print("You cannot afford food...")
                player.health -= 1
        elif not flag1 and flag2:
            if player.money > player.bills:
                print("You pay your bills.")
                player.money -= player.bills
                player.bills = 0
                player.taxhealth = 5
            else:
                print("You cannot afford to pay your bills...")
                player.taxhealth -= 1
        else:
            if player.money > (100 - player.food) * 3 + player.bills:
                print("You buy food and pay your bills")
                player.money -= (100 - player.food) * 3 + player.bills
                player.bills = 0
                player.food = 100
                player.health = 4
                player.taxhealth = 5
            else:
                print("You cannot afford anything...")
                player.health -= 1
                player.taxhealth -= 1
    if player.health <= 0:
        playing = playerdeath(player)
    elif player.taxhealth <= 0:
        playing = playertax(player)
    return player, playing


def gameloop(gamestate, player):
    handler = ActionHandler(0, 0)
    victory = False
    playing = True
    while playing:
        if random.randint(0, 100) > 45:
            gamestate, player = randomevent(gamestate, player)
        player, gamestate, playing, victory = handler.action(player, gamestate)

        if playing:
            player, playing = finances(player)
        if gamestate.day >= 150:
            playing = False
            victory = True
        gamestate.day += 1
        time.sleep(0.3)

    return victory, gamestate


def main():
    name = input("What is your name?\n")
    response = gameintro(name)
    size = 100

    if response == "y":
        player = Player(name, 1000, 100, 0, 4, 4, 15)
        gamestate = GameState()
        gamestate.generatelists(size)
        end = gameloop(gamestate, player)
        if end[0]:
            print(player.name + " survives. Deaths: ", end[1].deathcounter, " of which ",
                  end[1].frienddeathcounter, " were friends. ")
        else:
            print("\nGAME OVER.\n")
    else:
        print("Goodbye.\n")
    return 0


main()
