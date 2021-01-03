# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, start_row, start_col):
        """(Rat, str, int, int) -> NoneType​
        
        a Rat with symbol, row position, column position
        """
        self.symbol = symbol
        self.row = start_row
        self.col = start_col
        self.num_sprouts_eaten = 0

    def set_location(self, new_row, new_col):
        """(Rat, int, int) -> NoneType​
        
        update new position for Rat
        """
        self.row = new_row
        self.col = new_col

    def eat_sprout(self):
        """(Rat) -> NoneType​
        
        add one to number of sprout eaten
        >>> aaa = Rat('P', 1, 4)
        >>> aaa.num_sprouts_eaten
        0
        >>> aaa.eat_sprout()
        >>> aaa.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """(Rat) -> str
        
        return a string representation of Rat
        >>> rat1 = Rat(J, 4, 3)
        >>> rat2.__str__()
        ’J at (4, 3) ate 0 sprouts.’
        ​"""
        return "{0} at ({1}, {2}) ate {3} sprouts.".format(self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    def __init__(self, maze, firstRat, secondRat):
        """(Maze, list of list of str, Rat, Rat) -> NoneType​

        initialise the Maze
        >>> bbb = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                        ['#', '.', '.', '.', '.', '.', '#'],\
                        ['#', '.', '#', '#', '#', '.', '#'],\
                        ['#', '.', '.', '@', '#', '.', '#'],\
                        ['#', '@', '#', '.', '@', '.', '#'],\
                        ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> print(bbb.rat_1)
        J at (1, 1) ate 0 sprouts.
        >>> print(bbb.rat_2)
        P at (1, 4) ate 0 sprouts.
        >>> bbb.num_sprouts_left
        3
        """
        self.maze = maze
        self.rat_1 = firstRat
        self.rat_2 = secondRat
        self.num_sprouts_left = sum(r.count(SPROUT) for r in self.maze)

    def is_wall(self, row, col):
        """(Maze, int, int) -> bool​

        boolean whether a position is a wall or not
        """

        return self.maze[row][col] == WALL
            
    def get_character(self, row, col):
        """(Maze, int, int) -> str​
        
        return character at given row and column
        >>> bbb = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                        ['#', '.', '.', '.', '.', '.', '#'],\
                        ['#', '.', '#', '#', '#', '.', '#'],\
                        ['#', '.', '.', '@', '#', '.', '#'],\
                        ['#', '@', '#', '.', '@', '.', '#'],\
                        ['#', '#', '#', '#', '#', '#', '#']],\
                        Rat('J', 1, 1),\
                        Rat('P', 1, 4))
        >>> bbb.get_character(0, 0)
        '#'
        >>> bbb.get_character(1, 2)
        '.'
        >>> bbb.get_character(1, 1)
        'J'
        >>> bbb.get_character(3, 3)
        '@'
        """

        return self.maze[row][col]

    def move(self, givenRat, up_down, left_right):
        """(Maze, Rat, int, int) ->bool​

        Preconditions: row_move is UP, NO_CHANGE, or DOWN. col_move is LEFT, NO_CHANGE, or RIGHT.

        - move the given Rat in given direction. 
        - if there is sprout at the new location, make the location of the maze a HALL(.). Decrease value of num_spourts_left by 1. 
        - return True if the location is not a wall --> True means movable
        
        >>> maze_1.move("J",DOWN,NO_CHANGE)
        >>> maze_1.move("P",NO_CHANGE,RIGHT)
        """
        # unable to move if the proposed position is wall. Use is_wall method of maze class 
        if self.is_wall(givenRat.row + up_down, givenRat.col + left_right):
            return False
        # able to move. If the proposed position is sprout, then call rat's eat_sprout() method to add 1 to its num_sprouts_eaten; reduce number of sprout left, change the position of the maze from sprout to hall
        if self.get_character(givenRat.row + up_down, givenRat.col + left_right) == SPROUT:
            givenRat.eat_sprout()
            self.num_sprouts_left -= 1
            self.maze[givenRat.row + up_down][givenRat.col + left_right] = HALL
            givenRat.set_location(givenRat.row + up_down, givenRat.col + left_right)
            return True

    def __str__(self):
        """(Maze) -> str​

        output representation of the maze + rat_1 position and how many it has eaten + rat_2 position and how many it has eaten.
        """

        return "\n".join(["".join(r)  for r in self.maze]) + ('\n') + "{0} at ({1}, {2}) ate {3} sprouts.".format(self.rat_1.symbol, self.rat_1.row, self.rat_1.col, self.rat_1.num_sprouts_eaten) + ('\n') + "{0} at ({1}, {2}) ate {3} sprouts.".format(self.rat_2.symbol, self.rat_2.row, self.rat_2.col, self.rat_2.num_sprouts_eaten)