import random
import math
import copy

class Ship:
    """
    A class representing a space ship in a 2D world.
    A ship can shift its direction and change direction in differences of 7
    degrees per move in an entire 360 degree range, so that -> will add 7
    degrees to it's current direction, and <- will reduce 7 degrees,
    accordingly.
    A ship can move forward in whichever direction it is facing, and
    accelerate, based on the mathematical functions of 'sin' and 'cos' and its
    current speed and direction.
    A ship can continue flight beyond the board lines of the board,
    so that it continues from the exact opposite spot on the board.
    Furthermore, a ship's life span is 3 and if hit by an asteroid, loses 1
    life. If a ship loses all of it's lives, it is destroyed.
    """
    SHIP_LIFE = 3
    STARTING_DIRECTION = 0
    STARTING_SPEED = 0
    MAX_X = 0
    MAX_Y = 1
    MIN_X = 2
    MIN_Y = 3
    POS = 0
    RADIUS = 1

    def __init__(self, board_size):
        """
        a constructor for a ship object
        :param board_size: The 2D board size in which the ship is flying around
        """
        self.__board_size = board_size
        self.__life = self.SHIP_LIFE
        self.__x_pos = random.randint(board_size[self.MIN_X],
                                      board_size[self.MAX_X])
        self.__x_speed = self.STARTING_SPEED
        self.__y_pos = random.randint(board_size[self.MIN_Y],
                                      board_size[self.MAX_Y])
        self.__y_speed = self.STARTING_SPEED
        self.__direction = self.STARTING_DIRECTION

    def get_x_pos(self):
        """
        This function receives no external parameters.
        :return: An integer number representing the ship's placing on the
        horizontal scale.
        """
        return copy.copy(self.__x_pos)

    def get_y_pos(self):
        """
        This function receives no external parameters.
        :return: An integer number representing the ship's placing on the
        vertical scale.
        """
        return copy.copy(self.__y_pos)

    def get_direction(self):
        """
        This function receives no external parameters.
        :return: An integer number representing the ship's direction in degrees
        in comparison to the vertical scale, as accepted within the
        mathematical world.
        """
        return copy.copy(self.__direction)

    def get_radius(self):
        """
        This function receives no external parameters.
        :return: An integer number representing the radius of the ship.
        """
        return self.RADIUS

    def get_x_speed(self):
        """
        This function receives no external parameters.
        :return: A float number representing the speed of the ship in
        comparison to the horizontal scale.
        """
        return copy.copy(self.__x_speed)

    def get_y_speed(self):
        """
        This function receives no external parameters.
        :return: A float number representing the speed of the ship in
        comparison to the vertical scale.
        """
        return copy.copy(self.__y_speed)

    def get_board_size(self):
        """
        This function receives no external parameters.
        :return: A tuple of integer objects, representing the min and
        max values of the board on each scale.
        """
        return copy.copy(self.__board_size)

    def turn(self,angle):
        """
        Updates the direction of the ship by adding the amount of the
        given angle.
        :param: angle: an integer number of either 7 ot -7
        :return: None.
        """
        self.__direction += angle

    def move(self):
        """
        This function receives no external parameters.
        The function updates the position of the ship on both horizontal and
        vertical scales. If the ship reaches the edge of the board, it will
        continue its flight on the exact opposite position of the board.
        :return: None
        """
        delta_x = self.__board_size[self.MAX_X]-self.__board_size[self.MIN_X]
        self.__x_pos = (self.__x_speed + self.__x_pos -
                        self.__board_size[self.MIN_X]) % delta_x + \
                       self.__board_size[self.MIN_X]

        delta_y = self.__board_size[self.MAX_Y]-self.__board_size[self.MIN_Y]
        self.__y_pos = (self.__y_speed + self.__y_pos -
                        self.__board_size[self.MIN_Y]) % delta_y + \
                       self.__board_size[self.MIN_Y]

    def accelerate(self):
        """
        Updates the ship's speed on each scale.
        This function receives no external parameters.
        :return: None.
        """
        self.__x_speed += math.cos(math.radians(self.__direction))
        self.__y_speed += math.sin(math.radians(self.__direction))

    def reduce_life(self):
        """
        Reduces the remaining life of a ship by 1.
        This function receives no external parameters.
        :return: None
        """
        new_life = self.__life -1
        self.__life = new_life

    def get_life(self):
        """
        This function receives no external parameters.
        :return: An integer number representing remaining life of a ship.
        """
        return copy.copy(self.__life)


