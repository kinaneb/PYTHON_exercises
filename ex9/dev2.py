from random import randint
def play():
    print("choose a number between 1 and 100")
    n = int(input())
    min_r = 1
    max_r = 100
    for i in range(10):
        r = randint(min_r, max_r)
        print("you number is: ", r, " ?")
        answer = input()
        if(answer == '-'):
            min_r = r
        elif(answer == '+'):
            max_r = r
        elif(answer == '='):
            return True

    return False
if __name__ == "__main__":
    if(play()):
        print("I win")
    else:
        print("I lose")
