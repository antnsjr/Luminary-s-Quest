#Anthony Stephens JR
import random
import time

def Intro():
    print("In the land of Yggradsil evil has ran wild.")
    print("Monsters claim the lives of the innocent and are becoming more powerful by each passing day.")
    print("Only the Luminary is strong enough to take down the center of all this corruption.")
    print("The Darkspawn.... It is his destiny to bring back the world to light.")
    name = input("Enter your name Luminary:")
    print("Hello", name)
    time.sleep(2)
    print("Are you prepared to stop chaos and defeat the Darkspawn?")
    decision = input("Enter Y/N:", )
    time.sleep(2)
    if decision == ("Y"):
        time.sleep(1)
        print("May your quest begin")
        time.sleep(1)
    elif decision == "N":
        time.sleep(2)
        print ("Come back when you're ready Hero...")
        time.sleep(2)
        Intro()
    else:
        print("Invalid Answer")
        Intro()
Intro()
def MainStory1():
    print ("As you start your journey, you the road splits into two.")
    time.sleep(2)
    choose = input("Do you want to take the left or right past. Enter L/R:")
    time.sleep(1)
    if choose == "L":
        print("As you walk down the path you see a group of goblins.")
        time.sleep(1)
        print("Narrator: They find you and murder you with sticks and stones but their words never hurt you.")
        time.sleep(1)
        print("Narrator: Mostly because you didn't understand them.")
        RETRY = input("Try Again? Y/N")
        if RETRY == "Y":
            MainStory1
        elif RETRY == "N":
            print("Narrator: Way to let us down", name)
        else:
            RETRY = input("Try Again? Y/N")
            print Intro()
    elif choose == "R":
        print("Narrator: The path looks safe and you run into a young man around your age.")
    else:
        print ("Error")
        time.sleep(2)
        MainStory1()
MainStory1()
def MeetingErik():
    print ("Stranger: Hey there mate! What are you doing here in a place like?")
    time.sleep(1)
    print ("Narrator: You tell them who you are and what your quest is.")
    time.sleep(1)
    print ("Stranger: HAHAHA! Seriously!)
    seriously = input("Quick what's 9 + 10?")
        if seriously = "19"
           print ("Stranger: Well, I guess you aren't a complete idiot")
        elif seriously = ("21") or ("69") or ("420")
           print ("......")
           time.sleep(1)
           print ("You died! Don't ask how though!)
    print("Erik: Well, my name's Erik and my quest was to find the Luminary.")
    time.sleep(2) 
    print("Erik: To be honest, thought he'd look older and you know not pathetic.")
    time.sleep(2)
    print("Erik: Well begger can't be chooser is what they say")
