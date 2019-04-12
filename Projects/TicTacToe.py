#Made By Guy Tsarfaty
T = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

win = 0
lose = 0
flag = 0
while win == 0 and lose == 0:
    roundEnded = 1
    if T[0][0] == "X" and T[0][1] == "X" and T[0][2] == "X" or T[1][0] == "X" and T[1][1] == "X" and T[1][2] == "X" or T[2][0] == "X" and T[2][1] == "X" and T[2][2] == "X" or T[0][0] == "X" and T[1][0] == "X" and T[2][0] == "X" or T[0][1] == "X" and T[1][1] == "X" and T[2][1] == "X" or T[0][2] == "X" and T[1][2] == "X" and T[2][2] == "X" or T[0][0] == "X" and T[1][1] == "X" and T[2][2] == "X" or T[0][2] == "X" and T[1][1] == "X" and T[2][0] == "X":
        for row in T:
            print(row)
        print("Player X Won!")
        win = 1
        break
    if T[0][0] == "O" and T[0][1] == "O" and T[0][2] == "O" or T[1][0] == "O" and T[1][1] == "O" and T[1][2] == "O" or T[2][0] == "O" and T[2][1] == "O" and T[2][2] == "O" or T[0][0] == "O" and T[1][0] == "O" and T[2][0] == "O" or T[0][1] == "O" and T[1][1] == "O" and T[2][1] == "O" or T[0][2] == "O" and T[1][2] == "O" and T[2][2] == "O" or T[0][0] == "O" and T[1][1] == "O" and T[2][2] == "O" or T[0][2] == "O" and T[1][1] == "O" and T[2][0] == "O":
        for row in T:
            print(row)
        print("Player O Won!")
        win = 1
        break
    if T[0][0] != 1 and T[0][1] != 2 and T[0][2] != 3 and T[1][0] != 4 and T[1][1] != 5 and T[1][2] != 6 and T[2][0] != 7 and T[2][1] != 8 and T[2][2] != 9:
        for row in T:
            print(row)
        print("Game Over. Neither Won!")
        lose = 1
        break
    while flag == 0:
        try:
            for row in T:
                print(row)
            PlayerX = float(input("Player with X enter your number: "))
            if PlayerX == 1 and T[0][0] != "O" and T[0][0] != "X":
                T[0][0] = "X"
                flag = 1
                roundEnded = 0
            elif PlayerX == 2 and T[0][1] != "O" and T[0][1] != "X":
                T[0][1] = "X"
                flag = 1
                roundEnded = 0
            elif PlayerX == 3 and T[0][2] != "O" and T[0][2] != "X":
                T[0][2] = "X"
                flag = 1
                roundEnded = 0
            elif PlayerX == 4 and T[1][0] != "O" and T[1][0] != "X":
                T[1][0] = "X"
                flag = 1
                roundEnded = 0
            elif PlayerX == 5 and T[1][1] != "O" and T[1][1] != "X":
                T[1][1] = "X"
                flag = 1
                roundEnded = 0
            elif PlayerX == 6 and T[1][2] != "O" and T[1][2] != "X":
                T[1][2] = "X"
                flag = 1
                roundEnded = 0
            elif PlayerX == 7 and T[2][0] != "O" and T[2][0] != "X":
                T[2][0] = "X"
                flag = 1
                roundEnded = 0
            elif PlayerX == 8 and T[2][1] != "O" and T[2][1] != "X":
                T[2][1] = "X"
                flag = 1
                roundEnded = 0
            elif PlayerX == 9 and T[2][2] != "O" and T[2][2] != "X":
                T[2][2] = "X"
                flag = 1
                roundEnded = 0
            else:
                print("\nInvalid Choice!\n")
            if PlayerX == 1 and T[0][0] == "O" and T[0][0] == "X":
                print("\nInvalid Choice!\n")
            if PlayerX == 2 and T[0][1] == "O" and T[0][1] == "X":
                print("\nInvalid Choice!\n")
            if PlayerX == 3 and T[0][2] == "O" and T[0][2] == "X":
                print("\nInvalid Choice!\n")
            if PlayerX == 4 and T[1][0] == "O" and T[1][0] == "X":
                print("\nInvalid Choice!\n")
            if PlayerX == 5 and T[1][1] == "O" and T[1][1] == "X":
                print("\nInvalid Choice!\n")
            if PlayerX == 6 and T[1][2] == "O" and T[1][2] == "X":
                print("\nInvalid Choice!\n")
            if PlayerX == 7 and T[2][0] == "O" and T[2][0] == "X":
                print("\nInvalid Choice!\n")
            if PlayerX == 8 and T[2][1] == "O" and T[2][1] == "X":
                print("\nInvalid Choice!\n")
            if PlayerX == 9 and T[2][2] == "O" and T[2][2] == "X":
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
            else:
                print("\nInvalid Choice!\n")
            if PlayerO == 1 and T[0][0] == "X" and T[0][0] == "O":
                print("\nInvalid Choice!\n")
            if PlayerO == 2 and T[0][1] == "X" and T[0][1] == "O":
                print("\nInvalid Choice!\n")
            if PlayerO == 3 and T[0][2] == "X" and T[0][2] == "O":
                print("\nInvalid Choice!\n")
            if PlayerO == 4 and T[1][0] == "X" and T[1][0] == "O":
                print("\nInvalid Choice!\n")
            if PlayerO == 5 and T[1][1] == "X" and T[1][1] == "O":
                print("\nInvalid Choice!\n")
            if PlayerO == 6 and T[1][2] == "X" and T[1][2] == "O":
                print("\nInvalid Choice!\n")
            if PlayerO == 7 and T[2][0] == "X" and T[2][0] == "O":
                print("\nInvalid Choice!\n")
            if PlayerO == 8 and T[2][1] == "X" and T[2][1] == "O":
                print("\nInvalid Choice!\n")
            if PlayerO == 9 and T[2][2] == "X" and T[2][2] == "O":
                print("\nInvalid Choice!\n")
        except ValueError:
            print("\nInvalid Choice!\n")