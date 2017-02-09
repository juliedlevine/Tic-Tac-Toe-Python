square_1 = 1
square_2 = 2
square_3 = 3
square_4 = 4
square_5 = 5
square_6 = 6
square_7 = 7
square_8 = 8
square_9 = 9

def draw_board():
    print " --- --- --- "
    print "| %s | %s | %s |" % (square_1, square_2, square_3)
    print " --- --- --- "
    print "| %s | %s | %s |" % (square_4, square_5, square_6)
    print " --- --- --- "
    print "| %s | %s | %s |" % (square_7, square_8, square_9)
    print " --- --- --- "
draw_board()

print "Let's play Tic Tac Toe!"
play_count = 9

while play_count > 0:
    def check_winner():
        if (square_1 == "x" and square_2 == "x" and square_3 == "x") or (square_4 == "x" and square_5 == "x" and square_6 == "x") or (square_7 == "x" and square_8 == "x" and square_9 == "x") or (square_1 == "x" and square_4 == "x" and square_7 == "x") or (square_3 == "x" and square_6 == "x" and square_9 == "x") or (square_1 == "x" and square_5 == "x" and square_9 == "x") or (square_3 == "x" and square_5 == "x" and square_7 == "x"):
            print "Player 1 wins!"
            global play_count
            play_count = 0
        if (square_1 == "o" and square_2 == "o" and square_3 == "o") or (square_4 == "o" and square_5 == "o" and square_6 == "o") or (square_7 == "o" and square_8 == "o" and square_9 == "o") or (square_1 == "o" and square_4 == "o" and square_7 == "o") or (square_3 == "o" and square_6 == "o" and square_9 == "o") or (square_1 == "o" and square_5 == "o" and square_9 == "o") or (square_3 == "o" and square_5 == "o" and square_7 == "o"):
            print "Player 2 wins!"
            global play_count
            play_count = 0

    if play_count %2 != 0:
        try:
            player_1 = int(raw_input("Player 1, enter a number: "))
        except ValueError:
            player_1 = int(raw_input("That's not a number, enter a number: "))
        for i in range(1, 10):
            if player_1 == 1:
                square_1 = "x"
                break
            elif player_1 == 2:
                square_2 = "x"
                break
            elif player_1 == 3:
                square_3 = "x"
                break
            elif player_1 == 4:
                square_4 = "x"
                break
            elif player_1 == 5:
                square_5 = "x"
                break
            elif player_1 == 6:
                square_6 = "x"
                break
            elif player_1 == 7:
                square_7 = "x"
                break
            elif player_1 == 8:
                square_8 = "x"
                break
            elif player_1 == 9:
                square_9 = "x"
                break
        play_count -= 1
        check_winner()
        draw_board()

    elif play_count %2 == 0:
        try:
            player_2 = int(raw_input("Player 2, enter a number: "))
        except ValueError:
            player_2 = int(raw_input("That's not a number, enter a number: "))
        for i in range(1, 10):
            if player_2 == 1:
                square_1 = "o"
                break
            elif player_2 == 2:
                square_2 = "o"
                break
            elif player_2 == 3:
                square_3 = "o"
                break
            elif player_2 == 4:
                square_4 = "o"
                break
            elif player_2 == 5:
                square_5 = "o"
                break
            elif player_2 == 6:
                square_6 = "o"
                break
            elif player_2 == 7:
                square_7 = "o"
                break
            elif player_2 == 8:
                square_8 = "o"
                break
            elif player_2 == 9:
                square_9 = "o"
                break
        play_count -= 1
        check_winner()
        draw_board()

    if play_count == 0:
        print "Sorry stalemate! No one won."
