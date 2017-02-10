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

# Initialize game, draw board with squares, set play count to 9
draw_board()
print "Let's play Tic Tac Toe!"
play_count = 9

# Start game
while play_count > 0:
    # Check for a winner after every cycle
    def check_winner():
        if (square_1 == "x" and square_2 == "x" and square_3 == "x") or (square_4 == "x" and square_5 == "x" and square_6 == "x") or (square_7 == "x" and square_8 == "x" and square_9 == "x") or (square_1 == "x" and square_4 == "x" and square_7 == "x") or (square_3 == "x" and square_6 == "x" and square_9 == "x") or (square_1 == "x" and square_5 == "x" and square_9 == "x") or (square_3 == "x" and square_5 == "x" and square_7 == "x"):
            print "Player 1 wins!"
            global play_count
            play_count = 0
        if (square_1 == "o" and square_2 == "o" and square_3 == "o") or (square_4 == "o" and square_5 == "o" and square_6 == "o") or (square_7 == "o" and square_8 == "o" and square_9 == "o") or (square_1 == "o" and square_4 == "o" and square_7 == "o") or (square_3 == "o" and square_6 == "o" and square_9 == "o") or (square_1 == "o" and square_5 == "o" and square_9 == "o") or (square_3 == "o" and square_5 == "o" and square_7 == "o"):
            print "Player 2 wins!"
            global play_count
            play_count = 0

    # If play_count is even, it's player 1's turn
    if play_count %2 != 0:
        try:
            player_1 = int(raw_input("Player 1, enter a number: "))
        # If player 2 enters a non-number, ask them to try again
        except ValueError:
            player_1 = int(raw_input("That's not a number, enter a number: "))
        # Loop through each number option, if it matches the square, change the square to an x
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
        # Decrease play count, check for a winner and draw the updated board
        play_count -= 1
        check_winner()
        draw_board()

    # If play_count is odd, it's player 2's turn
    elif play_count %2 == 0:
        try:
            player_2 = int(raw_input("Player 2, enter a number: "))
        # If player 2 enters a non-number, ask them to try again
        except ValueError:
            player_2 = int(raw_input("That's not a number, enter a number: "))
        # Loop through each number option, if it matches the square, change the square to an o
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
        # Decrease play count, check for a winner and draw the updated board
        play_count -= 1
        check_winner()
        draw_board()

    # Check for stalemate - if play count gets to 0 and there hasn't been a winner, stalemate
    if play_count == 0:
        print "Sorry stalemate! No one won."
