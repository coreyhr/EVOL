##Random Stuff
def clear():
    print("\n" * 4)
def fs():
    print("<>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <>< <><")
import time
name = ("")
###
def intro():
    options = ["yes","no","tert","I am a real frog"]
    play = ("")
    print("Welcome to ^^^Evolution: The game^^^ \n (we recommend playing in full screen mode, however you can best do that)\n")
    while play not in options:
        play = input("Want to play? (yes/no) ").lower().strip()
    if play == options [0]:
        name = str(input("What is your name?"))
        intro2()
    elif play == options [1]:
        outro()
    elif play == options [2]:
        turt1()
    elif play == options [3]:
        amphi()


def intro2():
    name = ""
    print("\nWell that doesn't matter now.")
    options = ["quit","1","2"]
    user_c = ""
#    print("Well that doesn't matter now. You are evolution.\n")
    print("You must understand that you now are evolution.")

    print("The very force itself. You'll be making simple choices throughout this game. \nBut they will have severe implications. So strap in. \n ")
    print("Oh, I guess I should also tell you, if you want to quit just type 'quit'.")
    print("So let's set the scene. \n <>< <>< <>< \n <>< <>< <>< \n <>< <>< <><")
    print("Its wet. Quite wet. You are looking over these little fish. ")
    print ("Your fish keep getting eaten by bigger fish. ")
    print("And those other fish keep getting bigger and hungrier.")
    print("So now you have to make a choice. ")
    print("Don't mess up. Natural Selection does not favor the weak. \n")
    print("So do you want to stay and fight or have your fish flee towards shallow waters.")
    print("|Press 1 to stand your ground. |Press 2 to flee.")
###
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###DON'T TOUCH
###
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        death1()
    elif user_c == options [2]:
        fish1()
def fish1():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print ("\nAhh. Good choice. Your fish have fled in toward the coast. You can see the sand below you. ")
    print("But these waters are still deadly. ")
    print ("And your fish are quite weak. They sure aren't adapted to this new environment. ")
    print ("So now you have a real choice to make. \n")
    print ("Should your fish develop camoflage for this new habitat?")
    print ("Should your fish flee further into the tidal zones?")
    print ("Or should your fish focus on finding a better way to forage?")
    print ("|Press 1 for camo. |Press 2 to flee futher. |Press 3 to evolve foraging adaptations.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###DON'T TOUCH
###
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        fish2()
    elif user_c == options [2]:
        tide1()
    elif user_c == options [3]:
        death2()
def fish2():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
###Type in What you want it to say here. Use time.sleep(s) to set time gaps.
### \n will make a new line.
    fs()
    print ("\nAh-ha! You are so sneaky.")
    print ("But the previous issues still stand. Your fish are getting out-competed.\n")
    print ("So should we focus on developing locomotion physiology. ")
    print ("Should your fish evolve better foraging adaptations? ")
    print("Or should your fish flee into those tidal zones? ")
    print("|Press 1 to evolve locomotion. |Press 2 to evolve foraging. |Press 3 to enter tide pools.")

###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###DON'T TOUCH
###
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        ptide1()
    elif user_c == options [2]:
        death11()
    elif user_c == options [3]:
        tide1()
def ptide1():
    fs()
    options = ["quit","1","2"]
###Dont Change Below
    user_c = ""
###
###Type in What you want it to say here. Use time.sleep(s) to set time gaps.
### \n will make a new line.
    print ("\nI see we are getting somewhere now. ")
    print ("But your fish are getting hungry. And there isn't much food around. \nAnd that's not to say your fish could eat it. \n")
    print ("So should we focus on developing foraging adaptations. ")
    print("Or should your fish look for food in the tidal zones? ")
    print("|Press 1 to evolve foraging. |Press 2 to enter tide pools.")

###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###DON'T TOUCH
###
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        death5()
    elif user_c == options [2]:
        tide1b()
def ptide2():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
###Type in What you want it to say here. Use time.sleep(s) to set time gaps.
### \n will make a new line.
    fs()
    print ("\nYour fish fish sure seem fit to their environment. ")
    print ("But your fish are getting hungry. It's because there isn't much food around at all. \n")
    print ("So should your fish look for food further out at sea? ")
    print("Should your fish look for food in the tidal zones? ")
    print("Or should your fish stay where they are and hope food will soon come? ")
    print("|Press 1 to go back out to sea. |Press 2 to enter tide pools. |Press 3 to wait. ")

###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###DON'T TOUCH
###
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        death7()
    elif user_c == options [2]:
        ptide2b()
    elif user_c == options [3]:
        death6()
def tide1b():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print ("\nWelcome to the tidepools! Your little band of fish are chillin' at the entrance. ")
    print("This place sure looks pleasant! AND THERE IS FOOD!!! So now everything is all good!")
    print ("So what should you work on now?\n")
    print ("Should your fish work on their foraging adaptations now? \nShould they work further on their locomotion adaptations? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve foraging. |Press 2 to evolve locomotion. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tide2b()
    elif user_c == options [2]:
        tide3b()
    elif user_c == options [3]:
        death3()
def tide1():
    options = ["quit","1","2","3","4"]
###Dont Change Below
    user_c = ""
###
    fs()
    print ("Welcome to the tidepools! Your little band of fish are chillin' at the entrance.")
    print("This place sure looks pleasant! So now everything is all good! \nBut there are thinks to be done still! \nYour fish are hungry, slow, hot, and still at risk from the fish out at sea. ")
    print ("So what should you work on now?\n")
    print ("Should your fish work on their foraging adaptations now? \nShould they work on their locomotion adaptations? \n Should they work on developing a resistance to the harsh sunlight. \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve foraging. |Press 2 to evolve locomotion. \n|Press 3 to develop resistance to the sun. |Press 4 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tidef()
    elif user_c == options [2]:
        tidel()
    elif user_c == options [3]:
        tider()
    elif user_c == options [4]:
        death3()
def tidef():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("You can eat so good now! But your fish are slow and can't run from predators! \nTo make matters worse they are eating all of the available food. \nIt's also pretty hot in these shallows. \n")
    print ("So, should your fish work further on their locomotion adaptations? \nShould they evolve sun resistance? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve locomotion. |Press 2 to sun resistance. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tidefl()
    elif user_c == options [2]:
        tidefr()
    elif user_c == options [3]:
        death3()
def tidefr():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("Your fish are feeling the thermo-equilibrium now! Ain't that special. \nBut what is there to do now? \nYour slow fat little fish are eating all of the nearby food.")
    print ("So, should your fish work further on their locomotion adaptations? \nShould they evolve cannabilism? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve locomotion. |Press 2 to evolve cannibalism. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathtide()
    elif user_c == options [2]:
        death9()
    elif user_c == options [3]:
        death12()
def tidefl():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("Your fish have evolved these weird muscled arm fin things. It's pretty freaking nasty. \nSo good job. \nBut your fish are still really hot. And they are eating everything in sight. \n")
    print ("So, should your fish evolve heat resistance. \nShould they turn to cannibalismbilism to solve the food issue? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve heat resistance. |Press 2 to cannibalize. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathtide()
    elif user_c == options [2]:
        death9()
    elif user_c == options [3]:
        death3()
def tider():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("Your fish aren't hot anymore. So I guess that's good. \nBut your fish are slow and can't run from predators! \nTo make matters worse they are super hungry and terrible at eating the nearby food. \n")
    print ("So, should your fish work further on their locomotion adaptations? \nShould they evolve foraging mouth parts? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve locomotion. |Press 2 to evolve foraging. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tiderl()
    elif user_c == options [2]:
        tiderf()
    elif user_c == options [3]:
        death3()
def tiderl():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("We are getting somewhere now. Your fish have these weird arm things they use to move around and they do not fear the sun. \nThey are pretty hungry though and have eaten almost all of the nearby food by now.")
    print ("So, should your fish evolve foraging now? \nShould they evolve cannibalism? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve foraging. |Press 2 to evolve cannibalism. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathtide()
    elif user_c == options [2]:
        death9()
    elif user_c == options [3]:
        amphi()
def tiderf():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("Your fish are feeling nice and cool. The sun no longer fears them. \nBut your may eat all the food in their habitat. \nSo what should your slow, fat, little fish they do now? \n")
    print ("So, should your fish work further on their locomotion adaptations? \nShould they evolve cannibalism? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve locomotion. |Press 2 to evolve cannibalism. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathtide()
    elif user_c == options [2]:
        death9()
    elif user_c == options [3]:
        death12()
def tidel():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("Ew! Your fish have these weird arm things instead of fins. But they are good for pushing the fish around in the weeds and shallows. \nBut your fish are still hot and hungry. \n")
    print ("So, should your fish work on their foraging adaptations? \nShould they evolve sun resistance? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve foraging. |Press 2 to evolve sun resistance. |Press 3 to go further into the tide zones.")
    ###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tidelf()
    elif user_c == options [2]:
        tidelr()
    elif user_c == options [3]:
        death3()
def tidelr():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("We are getting somewhere now. Your fish are sure feeling the thermo-equilibrium now! How spiffy is that. \nThey are pretty hungry though and have eaten almost all of the nearby food by now.")
    print ("So, should your fish work further on foraging adapations? \nShould they evolve cannibalism? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve foraging. |Press 2 to evolve cannibalism. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathtide()
    elif user_c == options [2]:
        death9()
    elif user_c == options [3]:
        amphi()
def tidelf():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("Nice! Your fish are really good at eating the nearby vegetation. Like really, really good. That can't be sustainable. \nThere isn't much food nearby anymore.\nThe fish are also pretty hot. \n")
    print ("So, should your fish evolve heat resistance. \nShould they turn to cannibalism to solve the food issue? \nOr should they move further into the tide pools.")
    print("|Press 1 to heat resistance. |Press 2 to cannibalize. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathtide()
    elif user_c == options [2]:
        death9()
    elif user_c == options [3]:
        death3()
def tide2b():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print ("\nWow that is nice! Your fish can eat all they want now. \nThey are growing big and strong. \nMaybe a little too big. \nSize comes with complications you know. \n")
    print ("So, should your fish work further on their locomotion adaptations? \nShould they evolve to get smaller? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve locomotion. |Press 2 to evolve foraging. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tide2bb()
    elif user_c == options [2]:
        death8()
    elif user_c == options [3]:
        death3()
def tide3b():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print ("\nYour fish are quite adept at moving through the shallow weeds and pools. \nThey almost use their fins like little arms to push and pull themselves about. \nHow cute. But kinda weird. \nAnyways, your fish friends are getting a bit hungry and the sunlight in such shallow water is getting hot.\n")
    print ("So, should your fish work on their foraging adaptations? \nShould they develop resistance to the harsh sun. \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve foraging. |Press 2 to evolve sun resistance. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tide3ff()
    elif user_c == options [2]:
        tide3rr()
    elif user_c == options [3]:
        death3()
def tide3rr():
    options = ["quit","1","2","3","4"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("Your fish don't feel nearly as hot. But they sure are hungry. \nAnd to make matters worse, they are eating all of the remaining food they can find. That doesn't sound sustainable. \nThey see alot of food further into the tide pools. \n")
    print ("So, should the fish move into the tide pools? \nShould they sit and wait for food to come to them? \nShould they go back out to sea and search for food there? \nOr should they resort to canabilism.")
    print("|Press 1 to go inwards. |Press 2 to wait. \n|Press 3 to go back to sea. |Press 4 for cannibalism")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        amphi()
    elif user_c == options [2]:
        death6()
    elif user_c == options [3]:
        death11()
    elif user_c == options [4]:
        death9()
def tide3ff():
    options = ["quit","1","2","3","4"]
###Dont Change Below
    user_c = ""
###
    fs()
    print ("\nYour fish can move around great and are good at looking for food. \nBut your fish are eating all of the food! \nThere's definitley more food inland or back out in the big oceans. \n")
    print ("So, go inland into the pools? \nShould they develop resistance to the harsh sun. \nShould they go out into the ocean again? \nOr should they turn to canabilism?")
    print("|Press 1 to go inwards. |Press 2 to evolve sun resistance. \n|Press 3 to go back to the oceans. |Press 4 to turn to cannabilism.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        death3()
    elif user_c == options [2]:
        tidea()
    elif user_c == options [3]:
        death11()
    elif user_c == options [4]:
        death9()
def tidea():
    options = ["quit","1","2","3","4"]
###Dont Change Below
    user_c = ""
###
    fs()
    print("Wowza, your fish hardly even look like fish anymore. But they are eating all of the available food! \nLike there is no more food left. You have to do something.\n")
    print ("So, should they go inland into the pools? \nShould they develop filter feeding. \nShould they go out into the ocean again? \nOr should they turn to canabilism?")
    print("|Press 1 to go inwards. |Press 2 to evolve filter feeding. \n|Press 3 to go back to the oceans. |Press 4 to turn to cannabilism.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
###Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        amphi()
    elif user_c == options [2]:
        death10()
    elif user_c == options [3]:
        death11()
    elif user_c == options [4]:
        death9()
def tide2bb():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print ("\nYour fish can eat all they want now. \nThey are growing big and strong. \nMaybe a little too big. \nSize comes with complications you know. \n")
    print ("So, should your fish work on their locomotion adaptations? \nShould they evolve to get smaller? \nOr should they move further into the tide pools.")
    print("|Press 1 to evolve locomotion. |Press 2 to get smaller. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
##Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tide3bb()
    elif user_c == options [2]:
        death8()
    elif user_c == options [3]:
        death3()
def tide3bb():
    options = ["quit","1","2","3"]
###Dont Change Below
    user_c = ""
###
    fs()
    print ("\nYour fish are looking quite fit to their environment. They barely even look like fish anymore. \nThe biggest issue is they are eating all of the available food. \nIt's also a bit hot too. \n")
    print ("So should your fish develop a resistance to the sunlight? Should they turn to cannabilism? Or should they look for food further into the pools?")
    print("|Press 1 to evolve sunlight resistance. |Press 2 to evolve cannabilism. |Press 3 to go further into the tide zones.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
##Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tide4bb()
    elif user_c == options [2]:
        death9()
    elif user_c == options [3]:
        amphi()
def tide4bb():
    options = ["quit","1","2","3","4"]
###Dont Change Below
    user_c = ""
###
    fs()
    print ("\nYour fish are super super hungry.\nBut really that's the only issue. So how should we find food. \n\nShould we go further into the tidepools? \n Should the fish turn to cannabilism? \nShould the fish develop filter feeding? \nShould the fish go back out to sea? \n|Press 1 to go further inland. |Press 2 to resort to cannabilism. \n|Press 3 to filter feed. |Press 4 to go out to sea.")
###DON'T TOUCH
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
##Add or remove terms so that the orange equals the number of choices.
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        amphi()
    elif user_c == options [2]:
        death9()
    elif user_c == options [3]:
        death10()
    elif user_c == options [4]:
        death7()
def turt1():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Well look at that! You made a turtle. That's quite a step up from a fish. \nAlso if you wanna just jump straight here, type 'tert' when it asks if you want to play a game. \nBut let's get back to it. You have turtle choices to make now. \n")
    print ("So, should your turtles evolve feeding adaptations? \nShould they evolve flatter shells? \nShould evolve thicker shells? \nShould they travel out into the ocean? \nOr should they travel out of the water.")
    print("|Press 1 to evolve bite power. |Press 2 to evolve flatter shells. |Press 3 to evolve thicker shells. \n|Press 4 to go to sea. |Press 5 to leave the water.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        fturt()
    elif user_c == options [2]:
        flsh()
    elif user_c == options [3]:
        wsh()
    elif user_c == options [4]:
        deatho()
    elif user_c == options [5]:
        deathl()
def fturt():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Oh man! Your turtles are really thriving. They eat anything in their path. Their limited brains can hold them back no longer! \nBut now  you've got to choose the kind of turtle you want to make. \nBut don't mess up. That's still an option. \n")
    print ("So, should your turtles evolve a form of poison defense? \nShould they focus on evolving new ways to attract mates? \nShould they evolve larger fins? \nShould they travel out into the ocean? \nOr should they travel out of the water.")
    print("|Press 1 to evolve poison. |Press 2 to evolve sexual selection. |Press 3 to really bite. \n|Press 4 to go to sea. |Press 5 to leave the water.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathpt()
    elif user_c == options [2]:
        sst()
    elif user_c == options [3]:
        presnap()
    elif user_c == options [4]:
        deatho()
    elif user_c == options [5]:
        deathl()
def flsh():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Yes! Flat and hydro-dynamic is the way. \nYour turtles are thriving. They are quite adept in the water and are fast enough to catch any small creatures in the water.  \nSo where do your turtles go from here? \n")
    print ("Should your turtles further their biting adaptations? \nShould they focus on hiding from predators? \nShould evolve super sharp claws? \nShould they travel out into the ocean? \nOr should they travel out of the water.")
    print("|Press 1 to evolve bite power. |Press 2 to evolve hiding abilities. |Press 3 to sharp claws. \n|Press 4 to go to sea. |Press 5 to leave the water.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathbt()
    elif user_c == options [2]:
        ht()
    elif user_c == options [3]:
        deathct()
    elif user_c == options [4]:
        oturt()
    elif user_c == options [5]:
        deathl()
def wsh():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Your shell is really something. You're like a tank. A turtle tank. \nBut you've gotta figure something out. It's hard for your little turtles to get food. \nGranted nothing could hurt your turtles, but what should they do? \n")
    print ("So, should your turtles evolve bite power? \nShould they wider fins? \nShould they travel out into the ocean? \nOr should they travel out of the water.")
    print("|Press 1 to evolve bite power. |Press 2 to evolve wider fins. |Press 3 to go to sea. |Press 4 to leave the water.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathff()
    elif user_c == options [2]:
        deathsink()
    elif user_c == options [3]:
        deatho()
    elif user_c == options [4]:
        pretort()
def pretort():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Your turtles have now become land turtles. The walking tanks of the land. \nSo now you have to decide what these creatures should eat. \nBecause God knows nothing could eat them.\n")
    print ("So, should your turtles feed on vegetables? \nShould they evolve to feed on humans? \nShould evolve to feed on fish? \nOr should they evolve to eat anything and everthing.")
    print("|Press 1 to choose vegetables. |Press 2 to choose humans. |Press 3 to choose fish. |Press 4 eat anything.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        tort()
    elif user_c == options [2]:
        deathhuman()
    elif user_c == options [3]:
        deathcanteat()
    elif user_c == options [4]:
        deathtrash()
def sst():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Well before we move on. You have to choose how your turtles should evolve. \nThey need to woo the other gender. So by which mechanism should your turtles evolve sexual selection?")
    print ("So, should your turtles use chemical based signalling? \nShould they use color-based signalling? \nOr should they evolve vocal signalling?")
    print("|Press 1 to evolve to get smelly. |Press 2 to get colorful. |Press 3 to get noisy. ")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathsmell()
    elif user_c == options [2]:
        painted()
    elif user_c == options [3]:
        deathnoise()
def ht():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Alright alright alright. So you wanna be weak. I like it. \nYou have to choose how your turtles should hide though. \nSo what do you think?")
    print ("Should your turtles develop highly sophisticated camoflage? \nShould they hide under the sand? \nOr should they hide by evolving a way to reduce their scent?")
    print("|Press 1 to camoflage. |Press 2 to hide under the sand. |Press 3 to get less stinky. ")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathcamo()
    elif user_c == options [2]:
        softshell()
    elif user_c == options [3]:
        deathstink()
def oturt():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("You bravely enter the wild wild oceans. This place seems familiar. It's like you've been here before. \nBut many issues have arisin since your turtles entered the water. \nThe food is tough to catch. Your turtles can't really hold their breath. And they get lost often. \nBut first thing is first; what should they eat?")
    print ("So, should your turtles evolve to feed on ocean plant life? \nShould they evolve to eat fish? \nShould evolve to eat sea jellies and other cniderians? \nShould they travel out into the ocean? \nOr should they travel out of the water.")
    print("|Press 1 to eat vegetation. |Press 2 to eat fish. |Press 3 to sea jellies. |Press 4 to filter feed.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        pgt()
    elif user_c == options [2]:
        deathfish()
    elif user_c == options [3]:
        plt()
    elif user_c == options [4]:
        deathfilter()
def pgt():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Righteous! Grab shell dude. Your turtles take to the seaweed and find that they LOVE IT! \nSo now its time to decide where to live. So pick carefully! \n")
    print ("Should your turtles live in the coral reefs? \nShould your turtles travel the open seas? \nOr should your turtles live on the coastal seas, diving deep for untouched food?")
    print("|Press 1 to live in the reefs. |Press 2 to travel the open seas. |Press 3 to eat that deep food. ")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        greenturt()
    elif user_c == options [2]:
        deathseas()
    elif user_c == options [3]:
        deathdeep()
def amphi():
    options = ["quit","1","2","3"]
    user_c = ""
    fs()
    print("Congratulations! You have successfully made an amphibian! \nThis is a big step for you evolution. I am proud. \nTo skip that stupid fish stuff, just type 'I'm a real frog' when asked if you want to play the game. \nBut back to it. Congrats! You have made it to the inner tide pools. \nLet's skip forwards a million years or so. Cuz it's a text-based game and we can do that. \nSo now you're spawn are this weird little amphibian thing. \nAs generic of an amphibian as you can picture. And they live in freshwater ponds near the ocean.  \n")
    print("So now you have a choice to make. Do you want to focus on evolving your swimming abilities. Or do you want to evolve hind legs? Or do you want to send it and go straight onto land.")
    print("|Press 1 to evolve swimming. |Press 2 to evolve hind legs? |PRess 3 go out all out.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathamphswim()
    elif user_c == options [2]:
        amph2()
    elif user_c == options [3]:
        caec()
def caec():

    fs()
    print("Congratulations! You've made a caecilian. Which is pretty unfortunate really. \nBut we plan on adding a bit of caeclian diversity to this as well! \nAnyways! You won the game! If you consider making a big worm a win.")
def amph2():
    options = ["quit","1","2","3","4"]
    user_c = ""
    fs()
    print("With your forlegs and hindlegs you can easily swim around in the water as well as travel out onto land. \nLand brings a whole new variety of dangers and opportunities. Or so they tell me. \nSo here are the choices. \n")
    print("Should your amphibians hold tight in the ponds they have come to love and focus on evolving sexual selection signals? \nShould your amphibians move further inland? I hear there are ponds there too. Or should your amphibians take to the nearby trees?" )
    print("|Press 1 to hold tight. |Press 2 to move inland |Press 3 go to the trees. |Press 4 to develop lazor vision.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        frog()
    elif user_c == options [2]:
        amph3()
    elif user_c == options [3]:
        deathtrees()
    elif user_c == options [4]:
        deathlazors()
def frog():
    fs()
    print("Hey congrats! This would be the path leading to frog diversity if we weren't so lazy. \nBut this means you win the game for now! But I want you to know this is the easiest way to win. \nSo take that as you will. But thanks for playing. \nHopefully in a week or two we will add in the frog diversity expansion. \n")
def amph3():
    options = ["quit","1","2","3"]
    user_c = ""
    fs()
    print("Your strong hind legs have carried your creatures safely to the inlands pools \nBut be warned. Staying out of water is hard for your little guys. \nAnd like always, there is bad news. The resources in the ponds aren't very plentiful. \n")
    print("Should your amphibians develop less water permiable skin to look for food onland? Should your amphibians stay in the ponds and hope conditins improve? Or should your amphibians develop claws to take down larger prey? \n")
    print("|Press 1 to evolve thick skin. |Press 2 to stick around? |Press 3 develop claws.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        d1()
    elif user_c == options [2]:
        deathwait()
    elif user_c == options [3]:
        wolverine()
def wolverine():
    fs()
    print("Yo! You have created a whack species! Let me introduce to you the wolverine frog! \n That's really quite nifty. You've created a cool species! Props to you. \nThis means you win the game, in a cool way too! \n")
def d1():
    options = ["quit","1","2","3"]
    user_c = ""
    fs()
    print("With your new species you can gather resources away from water! \nThings are looking really good. Almost like an easy branchpoint because this project was bigger than we thought? \n")
    print("So do your land amphibian-things want to take to the trees? Do your things want to stick to ambush predation? Or do you want to develop a type of armor to protect yourself from the new dangers? \n")
    print("|Press 1 to climb. |Press 2 to ambush? |Press 3 armor up.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        climb()
    elif user_c == options [2]:
        ambush()
    elif user_c == options [3]:
        turt1()
def climb():
    fs()
    print("Congrats! Your creatures have made it to the trees! For now that means you have made an Anole! That's like the second best way to win this game. \nStick around for a whole ANOLE expansion pack coming up in the coming years/months/days. \nBut hey, pat yourself on the back. You guided some stupid fish into a pretty neat creature!")
def ambush():
    fs()
    print("Congrats! You've made a pre-snake thing! Stick around in the coming days or whatever for the snake expansion pack! \nWe will have cobra's, king-snakes, constrictors, garters and others! \nCome back soon. But this does mean you win for now. So that's cool if you care about that.")
def deathwait():
    fs()

    print("You fool! Never choose to wait! \nExcept for that one time when you should! \n ***GAME OVER***\n")
def deathamphswim():
    fs()
    print("NO NO NO! You just escaped the plagues of the water. Why go backwards! \n ***GAME OVER***\n")
def deathlazors():
    fs()
    print("Well that was stupid. \nYour creatures attempt to develop natural lazors. \nBut instead all of the options were futile. \nYes, we shouldn't have made it an options. \nBut you REALLY shouldn't have picked it. \n***GAME OVER***")
def deathtrees():
    fs()
    print("Your frog-salamandar things attempt to climb the trees! \nAnd suprisingly it seems to be going fairly well. \nBut all of your frogs are drying out! Infact they are drying out so fast that you lost. \n***GAME OVER***")
def plt():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Oh interesting choice. Sea Jellies are not very filling. \nSo how in the world are you gonna make this work. It's not gonna be easy. ")
    print ("Should your turtles evolve to eat a whole bunch of Sea Jellies, like 23/7 levels of eating. \nShould they evolve means of efficiently digesting the Jellies? \nShould they travel north towards where there are alot more Sea Jellies?")
    print("|Press 1 to evolve crazy feeding habits. |Press 2 to digest better. |Press 3 to go north.")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        pplt()
    elif user_c == options [2]:
        deathdigest()
    elif user_c == options [3]:
        deathcold()
def pplt():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("You feeding machines. Your turtles are unstoppable.  \nExcept they were stopped. By a lack of Sea Jellies. \nHow will you fix this problem?  The turtles are running out of food. \n")
    print ("Should your turtles travel south to where food is more abundant? \nShould they travel north to where Sea Jellies are more abundant? \nOr should the turtles try to eat the fish around? ")
    print("|Press 1 to travel south. |Press 2 to travel north. |Press 3 to eat fish. ")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
            done()
    elif user_c == options [1]:
        deathnofood()
    elif user_c == options [2]:
        ppplt()
    elif user_c == options [3]:
        deathnotenough()
def ppplt():
    options = ["quit","1","2","3","4","5"]
    user_c = ""
    fs()
    print("Oh good! The Jellies are back. And they are everywhere.  \nExcept its really cold here. And the Jellies are most abundant in pretty deep waters. \nSo last choice, how are your turtles gonna fix these issues? ")
    print ("Should your turtles evolve a lot of blubber and insulatory based adaptations? \nShould they evolve to dive really really deep? \nOr should they just get really really big, and hope everything works out. ")
    print("|Press 1 to fight the cold. |Press 2 to dive really really deep. |Press 3 to get big baby. ")
    while user_c not in options:
        user_c = input("Choose a number: ").lower().strip()
    if user_c == "quit":
        done()
    elif user_c == options [1]:
        deathblub()
    elif user_c == options [2]:
        deathdeep()
    elif user_c == options [3]:
        leather()
###
def deatho():
    fs()
    print("\nNO NO NO! Your turtle's were not adapted to go back into the ocean! \nThey all go out into the ocean and die because they can't swim and can't catch fish and can't find mates. \nAll in all it was a rough time for those turtles. \n***GAME OVER***\n")
def deathl():
    fs()
    print("\nIt was a good idea! But your turtles weren't ready to move onto land! \nThey didn't have the legs and thick shell to support themselves. \nOn land, they all collapse and painfully fry in the sun. \n***GAME OVER***\n")
def deathpt():
    fs()
    print("\nYou must not have been paying attention! \nTurtles can't be poisonous. Atleast I really hope so. \nAnd even if they can, you didn't succeed in making those turtles. \nYour turtles died from a mislocation of resources. Poison is expensive. And you have a shell. \n*** GAME OVER***")
def deathbt():
    fs()
    print("\nYou had good ideas thus far. But this one didn't work out for your turtles. \nYour turtles are fast and nimble and don't need a strong bite strength to get big food! \nAnd when your turtles would try to take on big foods the big food would beat them up and then sometimes eat them. \nQuite sad. Quite sad. \n***GAME OVER*** \n")
def deathct():
    fs()
    print("\nWhat would those do? You crazy. \n***GAME OVER*** \n")
def deathff():
    fs()
    print("\nYou are so slow that even though you can bite through anything you can't seem to catch anything. \nThis means all of your turtles slowly starve. \n***GAME OVER*** \n")
def deathsink():
    fs()
    print("\nYour wider fins don't seem to help your turtles! As they keep getting bigger they get heavier. \nSlowly your turtles one by one sink to the bottoms of random ponds. \nAs they sink, you think you can hear them think 'I though we got widerfins for this'. \n***GAME OVER***")
def deathsmell():
    fs()
    print("\nYour turtles have evolved these great smells for the female turtles to notice them. \nBut the female turtles can't smell very well. \nAnd in the ponds they have a tough time finding the males!\nYour turtles slowly reproduce less and less every year. \n***GAME OVER***\n")
def deathnoise():
    fs()
    print("\nAll the nearby predators turn their attention to the turtles when they attempt their mating calls. \nThe shells can't protect the turtles from everything! \nMaybe be more sneaky next time. \n***GAME OVER***\n")
def deathcamo():
    fs()
    print("\nYour turtles try to develop a highly developed camo system. \nBut the shell and variation in the ponds you live in just made the entire thing a mess. \nThe predators didn't get you. But your turtles spend too much wasted time and energy on this camo! \n***GAME OVER***\n")
def deathstink():
    fs()
    print("\nYou didn't really stink to begin win! \nYour turtles stagnate into non-existance. \n***GAME OVER***\n")
def deathfish():
    fs()
    print("\nYour turtles are way too slow to catch fish! They keep trying and trying but just can't. \nA quite frugile way to go. \n***GAME OVER***\n")
def deathfilter():
    fs()
    print("\nNope. Bad choice. \n***GAME OVER***\n")
def deathseas():
    fs()
    print("\n \n***GAME OVER***\n")
def deathdeep():
    fs()
    print("\nYour turtles travel out into the barren open seas! \nThe seas are so wide and open. They can't find a thing. \nAnd your turtles all lose each other! \nThey either die alone or from hunger. \n***GAME OVER***\n")
def deathcold():
    fs()
    print("\n \n***GAME OVER***\n")
def deathdigest():
    fs()
    print("\nWell you tried your luck! But your turtles couldn't find a way to develop efficient enough digestion. \nSometimes it just be like that in evolution. \n***GAME OVER***\n")
def deathblub():
    fs()
    print("\nYou manage to successfully fight the cold near the surface waters. \nBut your turtles are never able to find enough sea jellies to sustain themselves! \nEventually they all slowly grow too weak to deal with the cold. \n***GAME OVER***\n")
def deathnofood():
    fs()
    print("\nYour turtles travel to the southern warm water! \nAnd turns out that even though there are alot of fish and other organisms around... \nThere don't seem to be any large schools of sea jellies. \nAnd as much as your turtles look, they can never find enough food. ***GAME OVER***\n")
def deathnotenough():
    fs()
    print("\nYour turtles turn to eating fish! But your newfound size doesn't allow for your turtles to easily catch fish! \nYour turtles slowly starve as they strain to catch damselfish. \n***GAME OVER***\n")
def deathhuman():
    fs()
    print("\nWell it's really too bad humans haven't evolved yet. If they had, you'd probably rule this world. \n***GAME OVER*** \n")
def deathcanteat():
    fs()
    print("\nAs much as your little tortoises try to catch a fish, they just can't do it. \nThey are too stocky. And would drown if they fully entered the water. \n***GAME OVER***")
def deathtrash():
    fs()
    print("\nYour turtle attempts to eat everything in its path! There is so much food! \nIt's really a great time for your little tortoises. Except they all ate poisoned vegetation. \n***GAME OVER***")
###
def death12():
    fs()
    print("\nYour fish move into the tide pool. \nThe water is really shallow and there are rocks and weeds everywhere. \nEventually all of your fish get stuck! They can't flop their way to freedom. \n***GAME OVER***")
def death1():
    fs()
    print("\nOH NO. THIS OCEAN BELONGS TO THE SHARKS. NOT YOU. \n")
    print("***GAME OVER***")
def death2 ():
    fs()
    print("\nYOU FOOL! The sharks were hot on your heels.")
    print("And as you stopped to feed. They stopped to feed on you.")
    print("***GAME OVER***\n")
def done():
    print("\nThe real evolution wouldn't quit. You are weak.\n")
def death3():
    fs()
    print("\nYour fish go further into the tidal zone. But what's that? \nIT'S HIGH NOON. THE WATER'S EVAPORATING. \n Soon, all the water dries up. The fish all slowly dry to death.\nBet you didn't see that one coming. \nGotta think from all angles. \n***GAME OVER***\n")
def death4():
    fs()
    print("\nYay! Your fish can eat now. Too bad they can't move around very well in the tidepools.\nThey all seem to get stuck! \nOh and now the sun is drying up all the water. \nWell shoot. All your fish died. \n ***THE END***.\n")
def death5():
    fs()
    print("\nYour fish search day and night for food. They know they could eat it now. \nBut there is too much life in the sea. \nThere is no food to be found. Your fish die slowly and painfully. \n***GAME OVER***\n")
def death6():
    fs()
    print("\nNO NO NO. Never wait! This is selection of the fittest. \nYou sure aren't fit. I'm not even going to explain why you lost. \n***GAME OVER***\n")
def death7():
    fs()
    print("\nOh you poor poor fool. That's where the sharks are! \nYou might have developed new camoflage for the shallows. But not here. \nOh No. They see you. \n***GAME OVER*** \n")
def death8():
    fs()
    print("\nYour fish start getting smaller and smaller. \nThis worked out for a while. So take pride in the small moments of peace you provided. \nBut there where other fish following your example. \nAnd as your fish got smaller. These fish got bigger and hungrier. \nIn short, they ate your fish friends. \n***GAME OVER***\n  ")
def death9():
    fs()
    print("\nWell, they all ate each other. \n ***GAME OVER***\n")
def death10():
    fs()
    print("\nYour fish try to filter feed. But they are such large and active organisms that they could never get enough food! \nThat means they all die. \n***GAME OVER***\n")
def death11():
    fs()
    print("\nYour fish begin to feed. It seems to be going well for a while. \nHowever your camoflage doens't protect your fish enough when they go to feed. \nAnd the oceanic predators are developing advanced senses. \nAnywho. They ate all your fish. Quite painfully and violently. What a shame. \n***GAME OVER***\n")
def outro():
    fs()
    print("\nWhy pull up the program then?\n")
def deathtide():
    fs()
    print("\nYour fish have been doing things right! How great for them. Except I should tell you now. You haven't been fast enough. \nOther fish were following in your footsteps. \nThey colonized innertide pools first and will go on to become HERPS! \nMaybe next time don't work on foraging until you are safe. *hint *hint. \n***GAME OVER\n")

#Main Function
intro()
