import numpy as np


class Columns():
    def __init__(self, row, col, condition):
        self.row = row
        self.col = col
        self.faller = []
        self.board = np.zeros((self.row, self.col))
        self.game_over = False

        if condition == "EMPTY":
            pass
        elif condition == "CONTENTS":
            pass

    def display_board(self):
        """Displays board with current faller and/or jewels on board"""
        for r in range(self.row):
            for c in range(self.col):
                if self.board[r][c] == 0:
                    print(".", end=" ")
            print()

    def is_game_over(self, value):
        """Checks if losing condition is true"""
        self.game_over = value

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



