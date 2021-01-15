import random
import copy

class Asteroid:
    """
    A class representing an asteroid used in an Asteroids game.
    An asteroid is a 2D object that can move both horizontally and
    vertically. The asteroid floats around the board maintaining the same
    direction and speed. It can also check weather or not any other object
    stumbled upon it.
    """
    MIN_SPEED = 1
    MAX_SPEED = 10
    DEFAULT_SIZE = 3
    MAX_X = 0
    MAX_Y = 1
    MIN_X = 2
    MIN_Y = 3
    SIZE_COEFFICIENT = 10
    NORMALIZER = -5

    def __init__(self, board_size, size = DEFAULT_SIZE):
        """
        A constructor for an Asteroid object
        :param board_size: Board size is a tuple of edges both on 
                           the vertical and horizontal scale of the board in
                           which the asteroid floats.
        :param size: An integer number representing the size of the asteroid.
        """
        self.__board_size = board_size
        self.__size = size
        self.__x_pos = random.randint(board_size[self.MIN_X],
                           board_size[self.MAX_X])
        self.__x_speed = random.randint(self.MIN_SPEED, self.MAX_SPEED)
        self.__y_pos = random.randint(board_size[self.MIN_Y],
                            board_size[self.MAX_Y])
        self.__y_speed = random.randint(self.MIN_SPEED, self.MAX_SPEED)
        self.__is_register = True

    def move(self):
        """
        This function receives no external parameters.
        The function updates the position of the object on both vertical and 
        horizontal scale.
        if the object reaches the edge of the board, it will continue its 
        flight on the exact opposite position of the board.
        :return: None
        """
        delta_x = self.__board_size[self.MAX_X] - self.__board_size[
                            self.MIN_X]
        self.__x_pos = (self.__x_speed + self.__x_pos - self.__board_size[
            self.MIN_X]) % delta_x + self.__board_size[self.MIN_X]

        delta_y = self.__board_size[self.MAX_Y] - self.__board_size[
                self.MIN_Y]
        self.__y_pos = (self.__y_speed + self.__y_pos - self.__board_size[
            self.MIN_Y]) % delta_y + self.__board_size[self.MIN_Y]

    def get_size(self):
        """
        This function receives no external parameters.
        :return: (int) representing the size of the asteroid.
        """
        return copy.copy(self.__size)

    def get_x_pos(self):
        """
        This function receives no external parameters.
        :return: an integer number representing the object's position on the
        vertical scale.
        """
        return copy.copy(self.__x_pos)

    def set_x_pos(self, new_x_pos):
        """
        function sets a new place to the object on the horizontal scale.
        :param new_x_pos: an integer number representing the object's new
        position on the horizontal scale.
        :return: None
        """
        self.__x_pos = new_x_pos

    def get_y_pos(self):
        """
        This function receives no external parameters.
        :return: an integer number representing the object's position on the
        vertical scale.
        """
        return copy.copy(self.__y_pos)

    def set_y_pos(self, new_y_pos):
        """
        This function sets a new position for the object on the vertical scale.
        :param new_y_pos: an integer number representing the object's new
        position on the vertical scale.
        :return: None
        """
        self.__y_pos = new_y_pos


    def get_x_speed(self):
        """
        This function receives no external parameters.
        :return: the object's speed on the horizontal scale (float)
        """
        return copy.copy(self.__x_speed)

    def set_x_speed(self, new_x_speed):
        """
        This function will set a new speed to the object on the horizontal
        scale.
        :param new_x_speed (float): the new speed of the object on the
        vertical scale.
        :return: None
        """
        self.__x_speed = new_x_speed

    def get_y_speed(self):
        """
        This function receives no external parameters.
        :return: the object's speed on the vertical scale (float)
        """
        return copy.copy(self.__y_speed)

    def set_y_speed(self, new_y_speed):
        """
        This function will set a new speed to the object on the vertical scale.
        :param new_y_speed (float): the new speed of the object on the
        vertical scale.
        :return: None
        """
        self.__y_speed = new_y_speed


    def get_radius(self):
        """
        This function receives no external parameters.
        :return: the return the radius of the object
                 the radius is with proportion to the size
        """
        return self.__size * self.SIZE_COEFFICIENT + self.NORMALIZER

    def has_intersection(self, obj):
        """
        This function will check if any other object, besides an asteroid,
        is within a distance that's too close for comfort with an asteroid,
        which will be counted as an clashing intersection.
        :param obj: any object that have function get_radius(self) , 
        get_x_pos(self), get_y_pos(self), meaning a ship or a torpedo.
        :return: True/False
        """
        distance = ((obj.get_x_pos() - self.__x_pos) ** 2 + (obj.get_y_pos() - 
                           self.__y_pos) ** 2) ** 0.5
        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False
            
    def is_register(self):
        """
        This function receives no external parameters.
        :return: self.__is_register (bool)
        """
        return self.__is_register

    def un_register(self):
        """
        This function will set the __is_register value to be False.
        This function receives no external parameters.
        :return: None
        """
        self.__is_register = False
