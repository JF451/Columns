class Columns():
    def __init__(self, row, col, condition):
        self.board[row][col]
        self.faller = []

    def display_board(self):
        """Displays board with current faller and/or jewels on board"""
        pass

    def is_game_over(self, value):
        """Checks if losing condition is true"""
        return value

    def move_faller_left(self):
        """For current faller on board move left if possible"""
        pass

    def move_faller_right(self):
        """For current faller on board move to right if possible"""
        pass

    def rotate_faller(self):
        """For current faller on board rotate the jewels"""
        pass

    def move_time(self):
        """For current faller on board move down position"""
        pass

    def create_faller(self, data):
        """Creates a faller from user input"""
        #get faller from input from user
        self.faller = data[:]
        pass



