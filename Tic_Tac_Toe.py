def checkwin(xState, oState):
    # All Winning Patterns
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        # if X matches with the pattern then X won the Match
        if sum([xState[win[0]], xState[win[1]], xState[win[2]]]) == 3:
            return 1
        # if O matches with the pattern then O won the Match
        if sum([oState[win[0]], oState[win[1]], oState[win[2]]]) == 3:
            return 0
    return -1

def printboard(xState, oState):
    # Printing Board By using gameValues 's List
    zero = 'X' if xState[0] else ('O' if oState[0] else 0)
    one = 'X' if xState[1] else ('O' if oState[1] else 1)
    two = 'X' if xState[2] else ('O' if oState[2] else 2)
    three = 'X' if xState[3] else ('O' if oState[3] else 3)
    four = 'X' if xState[4] else ('O' if oState[4] else 4)
    five = 'X' if xState[5] else ('O' if oState[5] else 5)
    six = 'X' if xState[6] else ('O' if oState[6] else 6)
    seven = 'X' if xState[7] else ('O' if oState[7] else 7)
    eight = 'X' if xState[8] else ('O' if oState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"---------")
    print(f"{three} | {four} | {five}")
    print(f"---------")
    print(f"{six} | {seven} | {eight}")

xState = [0,0,0,0,0,0,0,0,0]
oState = [0,0,0,0,0,0,0,0,0]

turn = 1
turns_done = []
while True:
    printboard(xState, oState)
    # check draw
    if len(turns_done) == 9:
        print("---Game Draw---")
        break
    # Start
    if turn == 1:
        print("X's Turn")
        value = int(input("Enater the place no. & press 9 to forfite: "))
        if value in turns_done:
            print("--InValid Move--")
            print()
            print()
            print()
            continue
        if value == 9:
            print("---O WINS---")
            break
        turns_done.append(value)
        xState[value] = 1
    else:
        print("O's Turns")
        value = int(input("Enater the place no. & press 9 to forfite: "))
        if value in turns_done:
            print("--InValid Move--")
            print()
            print()
            print()
            continue
        if value == 9:
            print("---X WINS---")
            break
        turns_done.append(value)
        oState[value] = 1
    # check who won
    cwin = checkwin(xState, oState)
    if cwin != -1:
        if cwin == 1:
            print("---X WINS----")
        elif cwin == 0:
            print("---O WINS----")
        break
    # for giving chance to other player
    turn = 1 - turn
    print()
    print()
    print()
