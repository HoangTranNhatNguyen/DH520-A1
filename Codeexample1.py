print(""" You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a bear eating a giant cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your legs off. Ouch!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss of Voldemort's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    crazy = input("> ")

    if crazy == "1" or crazy == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good Job!")
    else:
        print("The inanity rots your eyes into a pool of muck.")
        print("Good Job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
