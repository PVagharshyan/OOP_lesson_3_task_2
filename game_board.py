import enum

class state(enum.Enum):
    NEUTRAL = enum.auto(),
    X = enum.auto(),
    O = enum.auto()

class game_board:
    _max: int = 100
    _min: int = 3

    def __init__(self, size_val: int) -> None:
        if self._min <= size_val <= self._max:
            self._size = size_val
            self._matrix = [[cell(j, i) for j in range(1, self._size + 1)] for i in range(1, self._size + 1)]
        else:
            raise ValueError("Value error")

    @classmethod
    def max(cls):
        return cls._max

    @classmethod
    def min(cls):
        return cls._min

    @property
    def size(self) -> int:
        return self._size

    @property
    def matrix(self) -> list:
        return self._matrix

class cell:
    _max_c: int = game_board.max()
    _min_c: int = 1

    def __init__(self, x_val: int, y_val: int) -> None:
        self._state = state.NEUTRAL
        if self._check_c(x_val) and self._check_c(y_val):
            self._x = x_val
            self._y = y_val
        else:
            raise ValueError("Value Error")

    def __str__(self) -> str:
        return f"({self.x}, {self.y}) : {self.state}"

    @classmethod
    def max(cls) -> int:
        return cls._max_c

    @classmethod
    def min(cls) -> int:
        return cls._min_c

    @property
    def state(self) -> state:
        return self._state

    @state.setter
    def state(self, state_val: state) -> None:
        self._state = state_val

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @classmethod
    def _check_c(cls, val: int) -> bool:
        if cls._min_c <= val <= cls._max_c:
            return True
        return False





