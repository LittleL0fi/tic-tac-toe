board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player = "X"

for turn in range(9):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    move = int(input(player + ", pick a number: "))
    board[move - 1] = player

    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):
        print(player, "wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
# professor note: if you want me to start explaining code i come in during office hours and explain if youd like