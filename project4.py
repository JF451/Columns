from column_logic import Columns


if __name__ == "__main__":
    #get rows amd columns from the user
    rows = int(input())
    cols = int(input())

    display_condition = input() # Condtions are empty board or board with jewels already in it

    #Initialize class with game logic
    columns = Columns(rows, cols, display_condition)

    #Loop until reach an ending condition
    while not columns.game_over:
        #display board and get uder input
        columns.display_board()

        """
        Get user input for
        1) Creating faller
        2) Move faller to right
        3) Move faller to left
        4) Quit game
        5) move time
        6) Rotate Faller
        """

        user_input = input()

        if user_input == "Q":
            columns.is_game_over(True)
        elif user_input == "<":
            columns.move_faller_left()
        elif user_input == ">":
            columns.move_faller_right()
        elif user_input == "R":
            columns.rotate_faller()
        elif user_input == "":
            columns.move_time()
        else:
            #create faller
            faller_data = user_input.split()
            columns.create_faller(faller_data)