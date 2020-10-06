import random
print("Welcome to the Oracle. Ask me any yes or no question. When you have found your answers, type 'done'.\n")
while True:
    inp = input("What is your question?\n")
    inp = inp.lower()
    if inp in ("done", "done.", "exit", "quit"):
        print("Thank you for consulting the Oracle. See you next time.")
        quit()
    x = random.randint(1,20)
    if x == 1:
        print("It is certain.\n")
    elif x == 2:
        print("It is decidedly so.\n")
    elif x == 3:
        print("Without a doubt.\n")
    elif x == 4:
        print("Yes - definitely.\n")
    elif x == 5:
        print("You may rely on it.\n")
    elif x == 6:
        print("As I see it, yes.\n")
    elif x == 7:
        print("Most likely.\n")
    elif x == 8:
        print("Outlook good.\n")
    elif x == 9:
        print("Yes.\n")
    elif x == 10:
        print("Signs point to yes.\n")
    elif x == 11:
        print("Reply hazy, try again.\n")
    elif x == 12:
        print("Ask again later.\n")
    elif x == 13:
        print("Better not tell you now.\n")
    elif x == 14:
        print("Cannot predict now.\n")
    elif x == 15:
        print("Concentrate and ask again.\n")
    elif x == 16:
        print("Don't count on it.\n")
    elif x == 17:
        print("My reply is no.\n")
    elif x == 18:
        print("My sources say no.\n")
    elif x == 19:
        print("Outlook not so good.\n")
    elif x == 20:
        print("Very doubtful.\n")
