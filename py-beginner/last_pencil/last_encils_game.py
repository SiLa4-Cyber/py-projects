import random

possibles = ["1", "2", "3"]
players = ["John", "Jack"]

print("How many pencils would you like to use:")
while True:
    pencils = input()
    if not pencils.isdigit():
        print("The number of pencils should be numeric")
    elif int(pencils) < 1:
        print("The number of pencils should be positive")
    else:
        pencils = int(pencils)
        break

print("Who will be the first (John, Jack):")
while True:
    name = input()
    if name not in players:
        print("Choose between 'John' and 'Jack'")
        continue
    break

print(pencils * "|")
while pencils > 0:

    if name == players[0]:

        print(players[0] + "'s turn!")
        choice = input()

        while choice == "0" or choice.isdigit() is False or int(choice) > 3 or int(choice) > pencils:
            if choice == "0" or choice.isdigit() is False:
                print("Possible values: '1', '2' or '3'")
                choice = input()
            elif int(choice) > 3:
                if int(choice) > 3 and int(choice) > pencils:
                    print("Too many pencils were taken")
                    print("Possible values: '1', '2' or '3'")
                    choice = input()
                elif 3 < int(choice) < pencils:
                    print("Too many pencils were taken")
                    print("Possible values: '1', '2' or '3'")
                    choice = input()
                elif int(choice) > 3 and int(choice) == pencils:
                    print("Too many pencils were taken")
                    print("Possible values: '1', '2' or '3'")
                    choice = input()
            elif int(choice) > pencils:
                print("Too many pencils were taken")
                choice = input()
        pencils -= int(choice)
        print(pencils * "|")
        name = players[1]
    else:
        print(players[1] + "'s turn:")
        if pencils == 1:
            choice = 1
        elif pencils % 4 == 0:
            choice = 3
        elif pencils % 2 != 0:
            choice = 2
        elif pencils % 2 == 0:
            choice = 1
        else:
            choice = random.randint(1, 3)

        pencils -= int(choice)
        print(choice)
        print(pencils * "|")
        name = players[0]

if name == players[0]:
    print(players[0], "won!")
else:
    print(players[1], "won!")
