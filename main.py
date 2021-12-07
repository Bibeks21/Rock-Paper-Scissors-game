#Rock paper scissors game......
import random

def gameWin(Comp,you):
    if comp == you:
        return None

    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("comp Turn: Rock(r) Paper(p) Scissors(s)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("your Turn: Rock(r) Paper(p) Scissors(s)?")
a = gameWin(comp,you)

print(f"Computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("The game is a Tie!")
elif a:
    print("you Win!")
else:
    print("you Lose!")