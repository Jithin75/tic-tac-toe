grid_dimension = 3 # Dimension of the tic-tac-toe grid (defaults to 3)
grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] # The tic-tac-toe grid (defaults to a 3x3 grid)

def exit_game():
    '''
    Exits the game after printing a message
    '''

    print("\nThank You for playing!")
    exit(0)

def init_grid():
    '''
    Initializes an empty grid
    '''

    if grid_dimension == 3:
        return
    else:
        global grid
        grid = []
        for i in range(grid_dimension): # Appends the below list grid_dimension times
            grid.append([' ']*grid_dimension) # Appends a list of empty strings and length grid_dimension

def display_grid():
    '''
    Displays the grid in a readable manner
    '''

    # TODO: Printing the grid with indices in a readable way for the user using the global grid variable

    for row in grid:
        print(row)

def game_status():
    '''
    Checks if the Game has been won, drawn, or still in progress
    '''

    is_draw = True

    # Check each row for wins and if ' ' exist then the game cannot be a draw
    for row in grid:
        row_values = set(row)
        if ' ' in row_values:
            is_draw = False
        elif len(row_values) == 1:
            return 'W'

    # Check for if the game has been drawn
    if is_draw:
        return 'D'

    # Check each column for wins
    for i in range(grid_dimension):
        column = [row[i] for row in grid]
        column_values = set(column)
        if (len(column_values) == 1) and (' ' not in column_values):
            return 'W'

    # Check both the diagonals for wins
    diag1 = [grid[i][j] for i in range(grid_dimension) for j in range(grid_dimension) if i == j]
    diag1_values = set(diag1)
    if (len(diag1_values) == 1) and (' ' not in diag1_values):
            return 'W'

    diag2 = [grid[i][j] for i in range(grid_dimension) for j in range(grid_dimension) if (i + j) == (grid_dimension - 1)]
    diag2_values = set(diag2)
    if (len(diag2_values) == 1) and (' ' not in diag2_values):
            return 'W'

    # Game is still in progress
    return 'N'

def user_input_dimension():
    '''
    Validates the user input and update the grid dimensions of the game
    '''

    c = 'invalid'
    n = 'invalid'
    invalid_digit = True
    invalid_choice = True

    while invalid_choice:
        c = input("Do you want to play on the standard (3x3) grid or a custom grid [s (standard), c (custom)]: ")
        if c.lower() == "exit":
            exit_game()
        if c not in ['s','c']:
            print("Invalid Choice! Please either enter s or c")
            continue
        else:
            break
    
    if c == 's':
        return
    
    while invalid_digit:
        n = input("Input the dimension of the grid you would like to play in (>= 3): ")
        if n.lower() == "exit":
            exit_game()
        if not n.isdigit():
            print("Invalid Choice! Please enter a valid positive integer")
            continue
        if int(n) < 3:
            print("Dimension is too small! Please enter a value greater or equal to 3")
            continue
        else:

            global grid_dimension 
            grid_dimension = int(n)
            break


def user_input_indices():
    '''
    Validates the user input and returns a set of indices corresponding to the grid
    '''

    x = 'invalid'
    y = 'invalid'
    valid_x_index = True
    valid_y_index = True
    indices_available = True
    valid_indices = list(map(lambda num:str(num), range(1,grid_dimension + 1))) # creates a list of characters from 1 to grid_dimension + 1

    while indices_available:

        while valid_x_index: 
            x = input("Please enter the row index of where you would like to make your move (1-{}): ".format(grid_dimension))
            if x.lower() == "exit":
                exit_game()
            if x not in valid_indices:
                print("Invalid entry! Please enter a valid integer between 1 and {}".format(grid_dimension))
                continue
            else:
                break

        while valid_y_index: 
            y = input("Please enter the column index of where you would like to make your move (1-{}): ".format(grid_dimension))
            if y.lower() == "exit":
                exit_game()
            if y not in valid_indices:
                print("Invalid entry! Please enter a valid integer between 1 and {}".format(grid_dimension))
                continue
            else:
                break
        
        if grid[int(x) - 1][int(y) - 1] == ' ':
            break
        else:
            print("The above chosen position is already occupied, please enter a valid position that is available")

    return (int(x) - 1,int(y) - 1)

if __name__== "__main__":

    # TODO: Allow game replays

    # WELCOME AND INITIAL SETUP FOR THE GAME
    print("{:^{}}".format("\nWelcome to tic-tac-toe with variations!\n", 150))
    print("Game Logic and Design: Jithin Krishna")
    print("Game UI and HCI factor: Nitesh Duraivel")
    # TODO: Description of the game 
    print("Note: Enter the word 'exit' whenever an input field appears to exit the game\n")
    user_input_dimension() # Takes in the dimensions of the grid to play the game
    init_grid() # Initialize an empty grid
    print("The grid used to play the game is given below, please use the co-ordinates as show to indicate the position of your move.")
    display_grid() # Prints the tic-tac-toe grid to show the user for reference

    # GAME LOGIC
    game_over = False
    X_move = True

    while not game_over:
        if X_move: # Player X's turn
            print("\nPlayer X's turn")
            print("Please enter the co-ordinates of where you would like to place the 'X' on the above grid")
            indices = user_input_indices()
            grid[indices[0]][indices[1]] = 'X'
            status = game_status()
            if status == 'W': # X won the game
                game_over = True
                display_grid() # TODO: Provide a better output message (Example: print the streak showing the victory)
                print("\nX has won the game!") 
                pass
            elif status == 'D': # Game has been drawn 
                game_over = True
                display_grid()
                print("\nThe game has been drawn") # TODO: If possible make the output message more meaningful
                pass
            else: # Game can continue
                display_grid()
                pass
            X_move = False
        else: # Player Y's turn
            print("\nPlayer O's turn")
            print("Please enter the co-ordinates of where you would like to place the 'O' on the above grid")
            indices = user_input_indices()
            grid[indices[0]][indices[1]] = 'O'
            status = game_status()
            if status == 'W': # X won the game
                game_over = True
                display_grid() # TODO: Provide a better output message (Example: print the streak showing the victory)
                print("\nO has won the game!") 
                pass
            elif status == 'D': # Game has been drawn 
                game_over = True
                display_grid()
                print("\nThe game has been drawn") # TODO: If possible make the output message more meaningful
                pass
            else: # Game can continue
                display_grid()
                pass
            X_move = True
            pass
    
    # GAME EXIT
    exit_game()

# TODO: Improve the UI to make it more easier and engaging, the above display functions and print statements are a
#            placeholder for testing and will shall be changed later 
