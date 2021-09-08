import random

possible_col = {
    1: "white",
    2:"blue",
    3:"green",
    4:"red",
    5:"purple",
    6:"yellow",
}


col = []
user_guess = []
tries = 0


for _ in range(4):
    a = random.randint(1,6)
    col.append(possible_col[a])

def guess():
    guess_num = 4
    for x in range(guess_num):
        user = input("Guess a colour: ")
        user_guess.append(user)


def pos():
    fr = 0
    for x in range(4):
        if col[x] == user_guess[x]:
            fr+= 1
    return fr
    fr = 0
    
    
def rcol():
    r = 0
    for x in user_guess:
        if x in col:
            r+=1
    print(f"You have {r} right colours!")
    r = 0


while tries < 12:
    tries+=1
    guess()
    pos()
    rcol()
    user_guess=[]
    

    