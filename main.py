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
    valid_indices = map(lambda num:str(num), range(1,grid_dimension + 1)) # creates a list of characters from 1 to grid_dimension + 1

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

    return (int(x),int(y))

if __name__== "__main__":
    print("Welcome to tic-tac-toe with variations!\n")
    # TODO: Description of the game
    print("Note: Enter the word 'exit' whenever an input field appears to exit the game\n")
    user_input_dimension() # Takes in the dimensions of the grid to play the game
    init_grid()
    