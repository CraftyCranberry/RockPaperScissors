import random

choices = ['Rock','Paper','Scissor']
user = ''

def AI():
    output = choices[random.randint(0,2)]
    return output

def isWin(user, comp):
    if(user == 0 and comp == 'Scissor') or (user == 1 and comp == 'Rock') or (user == 2 and comp == 'Paper'):
        win = True
        return win
    else:
        return False

while True:
    print()
    print('Please enter Rock(1), Paper(2), Scissor(3)')
    while True:
        try:
            userInput = int(input())
            if userInput < 0 or userInput > 3:
                print('Invalid entry, try again')
                continue
            else:
                break

        except ValueError:
            print('Invalid entry, try again')
            continue
    userInput -= 1
    user = choices[userInput]
    comp = AI()
    print()
    print("You choose " + user)
    print("Computer choose " + str(comp))
    print()
    if user == comp:
        print("It's a tie!")
    elif isWin(userInput, comp) is True:
        print("You Win")
    elif isWin(userInput, comp) is False:
        print("You Loose")
