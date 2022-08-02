from random import randint


def play():
    r = randint(1, 100)
    for i in range(10):
        print(i, ": 10  " + " Enter a number between 1 and 100 please")
        x = int(input())
        if(x == r):
            return True
        elif(x < r):
            print("soo small")
        else:
            print("soo big")
    return False


if __name__ == "__main__":
    if(play()):
        print("you win")
    else:
        print("game over")
