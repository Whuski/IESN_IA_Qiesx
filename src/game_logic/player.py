class player:

    def __init__(self, id, game):
        if id < 1:
             raise("Player creation error, cannot have id < 1")
        self._id = id
        self.case_claimed = 0
        self._game = game
        if (id == 0):
            self._x = 0
            self._y = 0
        else:
            self._x = 7
            self._y = 7


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        self._y = new_y

    def move(self, direction):
        if direction == "up":
            new_x = self.x - 1
            new_y = self.y
        elif direction == "down":
            new_x = self.x + 1
            new_y = self.y
        elif direction == "left":
            new_x = self.x
            new_y = self.y - 1
        elif direction == "right":
            new_x = self.x
            new_y = self.y + 1
        case = self._game.get_case((new_x, new_y))
        if case == 0:
            self._game.update_case((new_x, new_y), self._id)
            self.case_claimed += 1
        if case == self._id or case == 0:
            self.x = new_x
            self.y = new_y