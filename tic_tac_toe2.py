square = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def draw_board():
    print " --- --- --- "
    print "| %s | %s | %s |" % (square[1], square[2], square[3])
    print " --- --- --- "
    print "| %s | %s | %s |" % (square[4], square[5], square[6])
    print " --- --- --- "
    print "| %s | %s | %s |" % (square[7], square[8], square[9])
    print " --- --- --- "

# Initialize game, draw board with squares, set play count to 9
draw_board()
print "Let's play Tic Tac Toe!"
play_count = 9

# Start game
while play_count > 0:
    # Check for a winner after every cycle
    def check_winner():
        if (square[1] == "x" and square[2]== "x" and square[3] == "x") or (square[4] == "x" and square[5] == "x" and square[6] == "x") or (square[7] == "x" and square[8] == "x" and square[9] == "x") or (square[1] == "x" and square[4] == "x" and square[7] == "x") or (square[3] == "x" and square[6] == "x" and square[9] == "x") or (square[1] == "x" and square[5] == "x" and square[9] == "x") or (square[3] == "x" and square[5] == "x" and square[7] == "x"):
            print "Player 1 wins!"
            global play_count
            play_count = -1
        if (square[1] == "o" and square[2]== "o" and square[3] == "o") or (square[4] == "o" and square[5] == "o" and square[6] == "o") or (square[7] == "o" and square[8] == "o" and square[9] == "o") or (square[1] == "o" and square[4] == "o" and square[7] == "o") or (square[3] == "o" and square[6] == "o" and square[9] == "o") or (square[1] == "o" and square[5] == "o" and square[9] == "o") or (square[3] == "o" and square[5] == "o" and square[7] == "o"):
            print "Player 2 wins!"
            global play_count
            play_count = -1

    # If play_count is even, it's player 1's turn
    if play_count %2 != 0:
        try:
            player_1 = int(raw_input("Player 1, enter a number: "))
        # If player 2 enters a non-number, ask them to try again
        except ValueError:
            player_1 = int(raw_input("That's not a number, enter a number: "))
        # Loop through each number option, if it matches the guess, change the square to an x
        for i in range(1, 10):
            if player_1 == i:
                square[i] = "x"
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
        # Loop through each number square, if it matches the square, change the square to an o
        for i in range(1, 10):
            if player_2 == i:
                square[i] = "o"
                break
        # Decrease play count, check for a winner and draw the updated board
        play_count -= 1
        check_winner()
        draw_board()

    # Check for stalemate - if play count gets to 0 and there hasn't been a winner, stalemate
    if play_count == 0:
        print "Sorry stalemate! No one won."
