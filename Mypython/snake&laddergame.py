player1 = 0
player2 = 0

print("\n**** Welcome to the Snake and Ladder Game *****\n")

print("Rules for playing:")
print("1. Enter any number between between 1 and 6 (both inclusive) \n2. The fun thing while playing is you will never know where the snake/ladder is present \n"
      "Note:\n There can be a tail of a snake and a start of a ladder at a point \n There can be the end of a ladder and the start of a snake at a point\n")
j = range(91,101)[::-1]
for z in range(91,101)[::-1]: print(z, end="\t")
print()
i = range(81,91)
for z in range(81,91): print(z, end="\t")
print()
h = range(71,81)[::-1]
for z in range(71,81)[::-1]: print(z, end="\t")
print()
g = range(61,71)
for z in range(61,71): print(z, end="\t")
print()
f = range(51,61)[::-1]
for z in range(51,61)[::-1]: print(z, end="\t")
print()
e = range(41,51)
for z in range(41,51): print(z, end="\t")
print()
d = range(31,41)[::-1]
for z in range(31,41)[::-1]: print(z, end="\t")
print()
c = range(21,31)
for z in range(21,31): print(z, end="\t")
print()
b = range(11,21)[::-1]
for z in range(11,21)[::-1]: print(z, end="\t")
print()
a = range(1,11)
for z in range(1,11):print(z, end="\t")
print()

def roll_dice(oldval):
    dval = int(input("Roll the dice: "))
    while dval<1 or dval>6:
        dval = int(input("Oops!! re-roll the dice, the value must be between 1 to 6: "))
    dval = dval + oldval
    return dval

def check_snake_or_ladder(n):
    # ladders = {6:28, 22:35, 27:41, 39:64, 44:59, 53:76, 81:94, 92:100}
    # snakes = {98:32, 93:73, 87:24, 63:60, 62:19, 56:53, 49:11, 35:5, 16:6}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    snakes = {98: 78, 96: 75, 94: 75, 93: 73, 87: 24, 64: 60, 67: 19, 56: 53, 49: 11, 48: 26, 16: 6}
    if ladders.keys().__contains__(n):
        print("It's a ladder, you're going up")
        n = ladders[n]
    if snakes.keys().__contains__(n):
        print("There's a snake, you've to go down")
        n = snakes[n]
    if ladders.keys().__contains__(n):
        print("It's a ladder, you're going up")
        n = ladders[n]
    return n

while player1<100 and player2<100:
    print("\nPlayer1 Turn")
    player1 = roll_dice(player1)
    player1 = check_snake_or_ladder(player1)
    print("Player1 at: {}  Player2 at: {}".format(player1, player2))

    if player1>99:
        print("(^=^) Player1 Won the game (^=^)")
        break

    print("\nPlayer2 Turn")
    player2 = roll_dice(player2)
    player2 = check_snake_or_ladder(player2)
    print("Player1 at: {}  Player2 at: {}".format(player1, player2))

    if player2 > 99:
        print("(^=^) Player2 Won the game (^=^)")
        break

