import enum
import game_board

class Players(enum.Enum):
    PLAYER_1 = enum.auto(),
    PLAYER_2 = enum.auto()

dict_events = {
    Players.PLAYER_1: [game_board.state.O, ''],
    Players.PLAYER_2: [game_board.state.X, '']
}

def print_GB_matrix(matrix_val: list) -> None:
    for item in matrix_val:
        for item_cell in item:
            print(item_cell, end='')
        print("\n")

def main() -> None:
    GB = game_board.game_board(3)
    matrix = GB.matrix
    queue = Players.PLAYER_1
    end = False
    dict_events[Players.PLAYER_1][1] = input("first player name: ")
    dict_events[Players.PLAYER_2][1] = input("second player name: ")
    print(GB.size)
    while not end:
        print("Player name:", dict_events[queue][1])
        print_GB_matrix(matrix)
        print(f"Player_1: {dict_events[Players.PLAYER_1][1]}, cell_type: {dict_events[Players.PLAYER_1][0]}")
        print(f"Player_2: {dict_events[Players.PLAYER_2][1]}, cell_type: {dict_events[Players.PLAYER_2][0]}")
        x = input("x: ")
        while not (x.isnumeric() and 1 <= int(x) <= GB.size):
            print("Errooooooor!!!")
            x = input("x: ")
        y = input("y: ")
        while not (y.isnumeric() and 1 <= int(y) <= GB.size):
            print("Errooooooor!!!")
            y = input("y: ")
        x = int(x)
        y = int(y)
        while matrix[y - 1][x - 1].state != game_board.state.NEUTRAL:
            print('have already played here!!')
            x = input("x: ")
            while not (x.isnumeric() and 1 <= int(x) <= GB.size):
                print("Errooooooor!!!")
                x = input("x: ")
            y = input("y: ")
            while not (y.isnumeric() and 1 <= int(y) <= GB.size):
                print("Errooooooor!!!")
                y = input("y: ")
            x = int(x)
            y = int(y)

        matrix[y - 1][x - 1].state = dict_events[queue][0]

        #wherever the given cell is located, we check those rows and columns

        #1 vert

        flag = True
        for i in range(GB.size) :
            if matrix[i][x - 1].state != dict_events[queue][0]:
                flag = False
                break
        if flag:
            print(f"won {dict_events[queue][1]}!!!")
            break

        #2 horizontal
        flag = True
        for i in range(GB.size) :
            if matrix[y - 1][i].state != dict_events[queue][0]:
                flag = False
                break
        if flag:
            print(f"won {dict_events[queue][1]}!!!")
            break

        if x == y:
            flag = True
            for i in range(GB.size):
                if matrix[i][i].state != dict_events[queue][0]:
                    flag = False
                    break
            if flag:
                print(f"won {dict_events[queue][1]}!!!")
                break

        if x + y == GB.size + 1:
            flag = True
            for i in range(GB.size):
                if matrix[i][GB.size - i - 1].state != dict_events[queue][0]:
                    flag = False
                    break
            if flag:
                print(f"won {dict_events[queue][1]}!!!")
                break


        if queue == Players.PLAYER_1:
            queue = Players.PLAYER_2
        else:
            queue = Players.PLAYER_1
if __name__ == "__main__":
    main()


