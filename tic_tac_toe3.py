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

winning_combos = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

player_1_guesses = []
player_2_guesses = []

# Start game
while play_count > 0:
    # Check for a winner after every cycle
    def check_winner():
        if sorted(player_1_guesses) in winning_combos:
            print "Player 1 wins!"
        if sorted(player_2_guesses) in winning_combos:
            print "Player 2 wins!"
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
        player_1_guesses.append(player_1)
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
        player_2_guesses.append(player_2)

    # Check for stalemate - if play count gets to 0 and there hasn't been a winner, stalemate
    if play_count == 0:
        print "Sorry stalemate! No one won."
