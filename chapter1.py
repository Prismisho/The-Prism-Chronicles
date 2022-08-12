#Importing the module crap.
import time

#The Introduction that greets you and asks for your name.
def ChapterGreetings():
    time.sleep(3)
    print("Thank you for executing chapter1.py!")
    time.sleep(3)
    print("This is Chapter 1 of 'The Prism Chronicles'.")
    time.sleep(3)
    playername = input("What is your name?")
    time.sleep(3)
    print("Hi",playername,"!")
    time.sleep(3)
    print("Starting Chapter 1 in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(3)
    return

def Act1():
    print("Prismisho, Please add details.")
    return

ChapterGreetings()
Act1()
