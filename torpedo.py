import math
import copy

class Torpedo:
    """
    A class representing a torpedo shot by a space ship.
    A torpedo moves and accelerate constantly based on the speed and direction
    of the space ship, at the time the torpedo was shot.
    A torpedo can continue flight beyond the board lines of the board,
    so that it continues from the exact opposite spot on the board.
    Furthermore, a torpedo's life span is 200 game loops. But if it hits an
    asteroid, it will disappear (and injure the asteroid, of course).
    """
    ACCEL_FACT = 2
    MAX_X = 0
    MAX_Y = 1
    MIN_X = 2
    MIN_Y = 3
    RADIUS = 4
    START_LIFE_TIME = 200

    def __init__(self, ship):
        """
        a constructor for a ship object
        :param ship: a space ship the type of class Ship.
        """
        self.__x_pos = ship.get_x_pos()
        self.__y_pos = ship.get_y_pos()
        self.__board_size = ship.get_board_size()
        self.__direction = ship.get_direction()
        self.__x_speed = ship.get_x_speed() + self.ACCEL_FACT * math.cos(
            math.radians(self.__direction))
        self.__y_speed = ship.get_y_speed() + self.ACCEL_FACT * math.sin(
            math.radians(self.__direction))
        self.__life_time = self.START_LIFE_TIME

    def move(self):
        """
        This function receives no external parameters.
        The function updates the position of the ship on both horizontal and
        vertical scales. If the ship reaches the edge of the board, it will
        continue its flight on the exact opposite position of the board.
        :return: None
        """
        delta_x = self.__board_size[self.MAX_X] - self.__board_size[self.MIN_X]
        self.__x_pos = (self.__x_speed + self.__x_pos - self.__board_size[
            self.MIN_X]) % delta_x + self.__board_size[self.MIN_X]

        delta_y = self.__board_size[self.MAX_Y] - self.__board_size[self.MIN_Y]
        self.__y_pos = (self.__y_speed + self.__y_pos - self.__board_size[
            self.MIN_Y]) % delta_y + self.__board_size[self.MIN_Y]

        self.__life_time -= 1

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

    def get_direction(self):
        """
        This function receives no external parameters.
        :return: An integer number representing the direction in degrees,
        in comparison to the vertical scale, as accepted within the
        mathematical world.
        """
        return copy.copy(self.__direction)

    def get_radius(self):
        """
        This function receives no external parameters.
        :return: An integer number representing the radius of the torpedo.
        """
        return self.RADIUS

    def get_life_time(self):
        """
        This function receives no external parameters.
        :return: An integer number representing the remaining life time of the
        torpedo.
        """
        return copy.copy(self.__life_time)





