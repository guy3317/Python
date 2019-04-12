#Made By Guy Tsarfaty
T = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

PlayerXwin = 0
PlayerOwin = 0
PlayAgain = 0
flag = 0
while PlayAgain != "n" or PlayAgain != "N":
    roundEnded = 1
    if T[0][0] == "X" and T[0][1] == "X" and T[0][2] == "X" or T[1][0] == "X" and T[1][1] == "X" and T[1][2] == "X" or T[2][0] == "X" and T[2][1] == "X" and T[2][2] == "X" or T[0][0] == "X" and T[1][0] == "X" and T[2][0] == "X" or T[0][1] == "X" and T[1][1] == "X" and T[2][1] == "X" or T[0][2] == "X" and T[1][2] == "X" and T[2][2] == "X" or T[0][0] == "X" and T[1][1] == "X" and T[2][2] == "X" or T[0][2] == "X" and T[1][1] == "X" and T[2][0] == "X":
        for row in T:
            print(row)
        PlayerXwin += 1
        print("Player X Won! Player X Total Wins:", PlayerXwin)
        while PlayAgain != "y" or PlayAgain != "Y" or PlayAgain != "n" or PlayAgain != "N":
            try:
                PlayAgain = input("Play Again? Y/N ")
                if PlayAgain == "y" or PlayAgain == "Y":
                    T = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]
                    flag = 0
                    break
                elif PlayAgain == "n" or PlayAgain == "N":
                    break
                else:
                    print("\nInvalid Choice!\n")
            except ValueError:
                print("\nInvalid Choice!\n")
    if PlayAgain == "n" or PlayAgain == "N":
        break
    if T[0][0] == "O" and T[0][1] == "O" and T[0][2] == "O" or T[1][0] == "O" and T[1][1] == "O" and T[1][2] == "O" or T[2][0] == "O" and T[2][1] == "O" and T[2][2] == "O" or T[0][0] == "O" and T[1][0] == "O" and T[2][0] == "O" or T[0][1] == "O" and T[1][1] == "O" and T[2][1] == "O" or T[0][2] == "O" and T[1][2] == "O" and T[2][2] == "O" or T[0][0] == "O" and T[1][1] == "O" and T[2][2] == "O" or T[0][2] == "O" and T[1][1] == "O" and T[2][0] == "O":
        for row in T:
            print(row)
        PlayerOwin += 1
        print("Player O Won! Player O Total Wins:", PlayerOwin)
        while PlayAgain != "y" or PlayAgain != "Y" or PlayAgain != "n" or PlayAgain != "N":
            try:
                PlayAgain = input("Play Again? Y/N ")
                if PlayAgain == "y" or PlayAgain == "Y":
                    T = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]
                    flag = 0
                    break
                elif PlayAgain == "n" or PlayAgain == "N":
                    break
                else:
                    print("\nInvalid Choice!\n")
            except ValueError:
                print("\nInvalid Choice!\n")
    if PlayAgain == "n" or PlayAgain == "N":
        break
    if T[0][0] != 1 and T[0][1] != 2 and T[0][2] != 3 and T[1][0] != 4 and T[1][1] != 5 and T[1][2] != 6 and T[2][0] != 7 and T[2][1] != 8 and T[2][2] != 9:
        for row in T:
            print(row)
        print("Game Over. Neither Won!")
        while PlayAgain != "y" or PlayAgain != "Y" or PlayAgain != "n" or PlayAgain != "N":
            try:
                PlayAgain = input("Play Again? Y/N ")
                if PlayAgain == "y" or PlayAgain == "Y":
                    T = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]
                    flag = 0
                    break
                elif PlayAgain == "n" or PlayAgain == "N":
                    break
                else:
                    print("\nInvalid Choice!\n")
            except ValueError:
                print("\nInvalid Choice!\n")
    while flag == 0:
        roundEnded = 0
        try:
            for row in T:
                print(row)
            PlayerX = float(input("Player with X enter your number: "))
            if PlayerX == 1 and T[0][0] != "O" and T[0][0] != "X":
                T[0][0] = "X"
                flag = 1
            elif PlayerX == 2 and T[0][1] != "O" and T[0][1] != "X":
                T[0][1] = "X"
                flag = 1
            elif PlayerX == 3 and T[0][2] != "O" and T[0][2] != "X":
                T[0][2] = "X"
                flag = 1
            elif PlayerX == 4 and T[1][0] != "O" and T[1][0] != "X":
                T[1][0] = "X"
                flag = 1
            elif PlayerX == 5 and T[1][1] != "O" and T[1][1] != "X":
                T[1][1] = "X"
                flag = 1
            elif PlayerX == 6 and T[1][2] != "O" and T[1][2] != "X":
                T[1][2] = "X"
                flag = 1
            elif PlayerX == 7 and T[2][0] != "O" and T[2][0] != "X":
                T[2][0] = "X"
                flag = 1
            elif PlayerX == 8 and T[2][1] != "O" and T[2][1] != "X":
                T[2][1] = "X"
                flag = 1
            elif PlayerX == 9 and T[2][2] != "O" and T[2][2] != "X":
                T[2][2] = "X"
                flag = 1
            elif PlayerX == 1 and T[0][0] == "O" or PlayerX == 1 and T[0][0] == "X" or PlayerX == 2 and T[0][1] == "O" or PlayerX == 2 and T[0][1] == "X" or PlayerX == 3 and T[0][2] == "O" or PlayerX == 3 and T[0][2] == "X" or PlayerX == 4 and T[1][0] == "O" or PlayerX == 4 and T[1][0] == "X" or PlayerX == 5 and T[1][1] == "O" or PlayerX == 5 and T[1][1] == "X" or PlayerX == 6 and T[1][2] == "O" or PlayerX == 6 and T[1][2] == "X" or PlayerX == 7 and T[2][0] == "O" or PlayerX == 7 and T[2][0] == "X" or PlayerX == 8 and T[2][1] == "O" or PlayerX == 8 and T[2][1] == "X" or PlayerX == 9 and T[2][2] == "O" or PlayerX == 9 and T[2][2] == "X":
                print("\nSlot Already Taken!\n")
            else:
                print("\nInvalid Choice!\n")
        except ValueError:
            print("\nInvalid Choice!\n")

    while flag == 1 and roundEnded == 1:
        try:
            for row in T:
                print(row)
            PlayerO = int(input("Player with O enter your number: "))
            if PlayerO == 1 and T[0][0] != "X" and T[0][0] != "O":
                T[0][0] = "O"
                flag = 0
            elif PlayerO == 2 and T[0][1] != "X" and T[0][1] != "O":
                T[0][1] = "O"
                flag = 0
            elif PlayerO == 3 and T[0][2] != "X" and T[0][2] != "O":
                T[0][2] = "O"
                flag = 0
            elif PlayerO == 4 and T[1][0] != "X" and T[1][0] != "O":
                T[1][0] = "O"
                flag = 0
            elif PlayerO == 5 and T[1][1] != "X" and T[1][1] != "O":
                T[1][1] = "O"
                flag = 0
            elif PlayerO == 6 and T[1][2] != "X" and T[1][2] != "O":
                T[1][2] = "O"
                flag = 0
            elif PlayerO == 7 and T[2][0] != "X" and T[2][0] != "O":
                T[2][0] = "O"
                flag = 0
            elif PlayerO == 8 and T[2][1] != "X" and T[2][1] != "O":
                T[2][1] = "O"
                flag = 0
            elif PlayerO == 9 and T[2][2] != "X" and T[2][2] != "O":
                T[2][2] = "O"
                flag = 0
            elif PlayerO == 1 and T[0][0] == "X" or PlayerO == 1 and T[0][0] == "O" or PlayerO == 2 and T[0][1] == "X" or PlayerO == 2 and T[0][1] == "O" or PlayerO == 3 and T[0][2] == "X" or PlayerO == 3 and T[0][2] == "O" or PlayerO == 4 and T[1][0] == "X" or PlayerO == 4 and T[1][0] == "O" or PlayerO == 5 and T[1][1] == "X" or PlayerO == 5 and T[1][1] == "O" or PlayerO == 6 and T[1][2] == "X" or PlayerO == 6 and T[1][2] == "O" or PlayerO == 7 and T[2][0] == "X" or PlayerO == 7 and T[2][0] == "O" or PlayerO == 8 and T[2][1] == "X" or PlayerO == 8 and T[2][1] == "O" or PlayerO == 9 and T[2][2] == "X" or PlayerO == 9 and T[2][2] == "O":
                print("\nSlot Already Taken!\n")
            else:
                print("\nInvalid Choice!\n")
        except ValueError:
            print("\nInvalid Choice!\n")