from screen import Screen
import sys
import ship
import asteroid
import torpedo

DEFAULT_ASTEROIDS_NUM = 3
TURN_RIGHT = -7
TURN_LEFT = 7
NEW_TORP_PLACE_IN_LIST = -1
STARTING_SCORE = 0
BIG_ASTEROID = 3
MED_ASTEROID = 2
SMALL_ASTEROID = 1
BIG_POINTS = 20
MED_POINTS = 30
SMALL_POINTS = 50
MAX_TORPEDOS = 15
HIT_TITLE = "WARNING!"
HIT_MESSAGE = "You've been hit and a lost a life. You have %s lives left."
QUIT_MSG = "You decided to quit? OK you spineless fool."
LOSER_MSG = "Hahaha LOSER! Better luck next time!"
WIN_MSG = '''Horray ou won the game! You're so awesome you might even get 100
                   in Infi_1.'''

class GameRunner:
    """
    A class representing a single game of Asteroids.
    A game is composed of a space ship, asteroids and torpedos, which all move
    within a 2D square board.
    The objective of the game is for the ship to destroy all the asteroids by shooting
    torpedos at them, without being hit by the asteroids. And of course,
    having a blast while doing it.
    """
    def __init__(self, asteroids_amnt):
        """
        Initialize a new Game object.
        :param asteroids_amnt (int): the amount of asteroids in the start of  
                        the game.
        The function will set a new screen object.
        The function will set a new ship object.
        The function will create asrteroids and will make sure that the
                     starting point is different that the ship's.
        :return: A new Game object.
        """
        self._screen = Screen()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        board_size = (self.screen_max_x, self.screen_max_y, self.screen_min_x,
                      self.screen_min_y)
        self.board_size = board_size
        self.ship = ship.Ship(board_size)
        self.score = STARTING_SCORE
        self.torpedos = []
        self.asteroids = []
        for i in range(asteroids_amnt):
            new_asteroid = asteroid.Asteroid(board_size)
            #making sure asteroids aren't created on the ship
            while new_asteroid.get_x_pos() == self.ship.get_x_pos() and \
                            new_asteroid.get_y_pos() == self.ship.get_y_pos():
                new_asteroid = asteroid.Asteroid(board_size)
            self.asteroids.append(new_asteroid)
            self._screen.register_asteroid(self.asteroids[i], 
                               self.asteroids[i].get_size())
            
            
    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def new_astr_speed(self, astr, torp):
        """
        This function will calculate the new speed of the new smaller asteroids
        after an encounter with a torpedo.
        :param astr: an Astroid object
        :param torp: an Torpeo object 
        :return: a tuple of the new speed (int) on the horizontal and vertical
                  scale
        """
        new_x_speed = (torp.get_x_speed() + astr.get_x_speed()) / (
        ((astr.get_x_speed()) ** 2 + (astr.get_y_speed()) ** 2) ** 0.5)
        new_y_speed = (torp.get_y_speed() + astr.get_y_speed()) / (
        ((astr.get_x_speed()) ** 2 + (astr.get_y_speed()) ** 2) ** 0.5)
        return (new_x_speed, new_y_speed)

    def split_asteroid(self, astr, torp):
        """
        This function will split a given asteroid after an encounter with a
        torpedo. it will register both new smaller asteroids to the screen and
        unregister the old one which go hit.
        :param astr: an Astroid object
        :param torp: an Torpeo object 
        :return: a tuple of two new asteroid type objects.
        """
        # makes sure the new asteroid are smaller
        new_size = astr.get_size() - 1
        new_x_speed, new_y_speed = self.new_astr_speed(astr, torp)
        new_astr1 = asteroid.Asteroid(self.board_size, new_size)
        new_astr2 = asteroid.Asteroid(self.board_size, new_size)
        # set the new asteroid position
        new_astr1.set_x_pos(astr.get_x_pos())
        new_astr1.set_y_pos(astr.get_y_pos())
        new_astr2.set_x_pos(astr.get_x_pos())
        new_astr2.set_y_pos(astr.get_y_pos())
        # set the new asteroid speed
        new_astr1.set_x_speed(new_x_speed)
        new_astr1.set_y_speed(new_y_speed)
        new_astr2.set_x_speed(new_x_speed*(-1))
        new_astr2.set_y_speed(new_y_speed * (-1))
        # register and un register to the Screen object
        self._screen.register_asteroid(new_astr1, new_size)
        self._screen.register_asteroid(new_astr2, new_size)
        if astr.is_register():
            self._screen.unregister_asteroid(astr)
            astr.un_register()
        
        return new_astr1, new_astr2

    def exit_game(self):
        """
        This function will close the game window and end the game.
        This function receives no external parameters.
        :return: None
        """
        self._screen.end_game()
        sys.exit()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def _game_loop(self):
        """
        This function receives no external parameters.
        Checks whether the game ended.
        If not, the function will go over one more  game loop, moving all the
        objects on the board and checking for encounters between asteroids 
        and any other objects.
        :return: None
        """
        hit_asteroids = []
        intact_asteroids = []
        hit_torpedos = []
        intact_torpedos = []
        # checking whether the game should end
        if self._screen.should_end():
            print(QUIT_MSG)
            self.exit_game()
        if self.ship.get_life() == 0:
            print(LOSER_MSG)
            self.exit_game()
        if not self.asteroids:
            print(WIN_MSG)
            self.exit_game()
        
        self._screen.draw_ship(self.ship.get_x_pos(), self.ship.get_y_pos(),
                           self.ship.get_direction())
        # checking for user input
        if self._screen.is_left_pressed():
            self.ship.turn(TURN_LEFT)
        elif self._screen.is_right_pressed():
            self.ship.turn(TURN_RIGHT)
        elif self._screen.is_up_pressed():
            self.ship.accelerate()
        elif self._screen.is_space_pressed() and \
                        len(self.torpedos) < MAX_TORPEDOS:
            self.torpedos.append(torpedo.Torpedo(self.ship))
            self._screen.register_torpedo(self.torpedos[
                                 NEW_TORP_PLACE_IN_LIST])
        # start moving objects
        self.ship.move()

        for torp in self.torpedos:
            self._screen.draw_torpedo(torp,torp.get_x_pos(), torp.get_y_pos(),
                              torp.get_direction())
            torp.move()
            # checking for torpedos that are outdated
            if torp.get_life_time() == 0:
                self._screen.unregister_torpedo(torp)
                hit_torpedos.append(torp)
        # removing outdated torpedos
        for torp in self.torpedos:
            if torp not in hit_torpedos:
                intact_torpedos.append(torp)
        self.torpedos = intact_torpedos
        intact_torpedos = []
       
        for asteroid in self.asteroids:
            self._screen.draw_asteroid(asteroid, asteroid.get_x_pos(), 
                                       asteroid.get_y_pos())
            asteroid.move()
            # checking for encounters with ship
            if asteroid.has_intersection(self.ship):
                self.ship.reduce_life()
                self._screen.remove_life()
                self._screen.show_message(HIT_TITLE, 
                               HIT_MESSAGE%self.ship.get_life())
                self._screen.unregister_asteroid(asteroid)
                hit_asteroids.append(asteroid)
            else:
                for torp in self.torpedos:
                    # checking for encounters with torpedos 
                    if asteroid.has_intersection(torp):
                        # adding points and removing\splitting asteroids
                        if asteroid.get_size() == BIG_ASTEROID:
                            self.score += BIG_POINTS
                            new_astr1, new_astr2 = self.split_asteroid(
                                                  asteroid, torp)
                            intact_asteroids.append(new_astr1)
                            intact_asteroids.append(new_astr2)
                        elif asteroid.get_size() == MED_ASTEROID:
                            self.score += MED_POINTS
                            new_astr1, new_astr2 = self.split_asteroid(
                                asteroid, torp)
                            intact_asteroids.append(new_astr1)
                            intact_asteroids.append(new_astr2)
                        elif asteroid.get_size() == SMALL_ASTEROID:
                            self.score += SMALL_POINTS
                            if asteroid.is_register():
                                self._screen.unregister_asteroid(asteroid)
                                asteroid.un_register()
                        self._screen.set_score(self.score)
                        hit_asteroids.append(asteroid)
                        hit_torpedos.append(torp)
                        self._screen.unregister_torpedo(torp)
                # removing torpedos which hit asteroids
                for torp in self.torpedos:
                    if torp not in hit_torpedos:
                        intact_torpedos.append(torp)
                self.torpedos = intact_torpedos
                intact_torpedos = []
        # removing demolished asteroids
        for asteroid in self.asteroids:
            if asteroid not in hit_asteroids:
                intact_asteroids.append(asteroid)
        self.asteroids = intact_asteroids


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )
